import asyncio

from loguru import logger

from boil.bot import BoilerBot
from boil.logging import init_logging


async def main():
    bot = BoilerBot()
    bot_loop = asyncio.create_task(bot.loop())
    await asyncio.wait([bot_loop, ])


def run():
    init_logging()
    logger.info('Running boilerbot service')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info('Shutting down..')


if __name__ == '__main__':
    run()
