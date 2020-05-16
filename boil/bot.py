from aiotg import Bot

from boil import conf
from boil.model import db
from boil.model.magic.helpers import ThreadSwitcherWithDB, db_in_thread
from boil.model.tables import Chat


async def get_chat_id(chat, match):
    await chat.send_text(f'Chat id: {chat.id}')


@ThreadSwitcherWithDB.optimized
async def save_chat_id(chat, match):
    await chat.send_text(f'saving chat id: {chat.id} to db')
    async with db_in_thread():
        admin = Chat(chat_id=chat.id)
        db.add(admin)
        db.commit()
    await chat.send_text('Done!')


class BoilerBot:
    def __init__(self):
        self._bot = Bot(conf.bot_token, proxy=conf.tele_proxy)
        self.session = self._bot.session
        self.loop = self._bot.loop
        self.init_handlers()

    def init_handlers(self):
        self._bot.add_command(r'/ch', get_chat_id)
        self._bot.add_command(r'/save_ch', save_chat_id)
