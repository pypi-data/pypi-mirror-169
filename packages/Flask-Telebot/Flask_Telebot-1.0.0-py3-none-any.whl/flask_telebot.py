# !/usr/bin/env python3
# encoding: utf-8
import logging
import os
import sys
import time
import telebot
from flask import current_app, request, abort, Blueprint
from pyngrok import ngrok

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack
logger = logging.getLogger(__name__)
telebot.apihelper.ENABLE_MIDDLEWARE = True
prefix = os.path.basename(__file__)[:-3].lower()
blueprint = Blueprint(prefix, prefix, url_prefix='/{}'.format(prefix))


class FlaskTelebot(object):
    _public_url = None
    _bot = None
    _bot_info = None
    _message_handler = []

    def __init__(self, token, app=None):
        self._bot = telebot.TeleBot(token=token, threaded=False, skip_pending=True)
        self.app = app
        if app is not None:
            self.init_app(app)

    def _init_route(self):
        @blueprint.route('/', methods=['GET'])
        def debug():
            return self.bot_info.to_dict(), 200

        @blueprint.route('/webhook', methods=['POST'])
        def webhook():
            if request.headers.get('content-type') == 'application/json':
                json_string = request.get_data().decode('utf-8')
                update = telebot.types.Update.de_json(json_string)
                self.bot.process_new_updates([update])
                return ''
            else:
                abort(403)

    @property
    def public_url(self) -> str:
        return self._public_url

    def init_app(self, app):
        app.extensions[prefix] = self
        if app.config.get('NGROK_TOKEN'):
            ngrok.set_auth_token(current_app.config.get('NGROK_TOKEN'))
        command_line = ' '.join(sys.argv)
        is_running_server = ('flask run' in command_line) or ('wsgi' in command_line)
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)
        if not is_running_server:
            return
        elif self.public_url:
            return
        self._init_route()
        app.register_blueprint(blueprint)
        port = os.getenv('FLASK_RUN_PORT', 9000)
        if not port.__str__().isdigit():
            raise KeyError('Error: Invalid Port')
        try:
            ngrok.kill()
            self._public_url = ngrok.connect(port).public_url
        except Exception as error:
            logging.error(error.__str__())
        finally:
            if self.public_url:
                self.bot.remove_webhook()
                time.sleep(1.2)
                webhook = '{}/{}/webhook'.format(self.public_url.replace('http://', 'https://'), prefix)
                print(
                    ' * ngrok tunnel "{}" -> "http://127.0.0.1:{}/"'.format(
                        self.public_url, port
                    )
                )
                print(
                    ' * bot webhook "{}"'.format(webhook)
                )
                self.bot.set_webhook(url=webhook)

    def teardown(self, exception):
        ctx = stack.top

    def connect(self):
        return self.bot

    @property
    def bot(self):
        return self._bot

    @property
    def bot_info(self):
        if not self._bot_info:
            self._bot_info = self.bot.get_me()
        return self._bot_info

    @property
    def telebot(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'telebot'):
                ctx.telebot = self.bot
            return ctx.telebot
