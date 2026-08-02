from bot import app
from bot.handlers import *

from bot.utils.logger import LOGGER


def main():

    LOGGER.info("=" * 50)
    LOGGER.info("Starting DG Defender...")
    LOGGER.info("=" * 50)

    app.run()


if __name__ == "__main__":
    main()
