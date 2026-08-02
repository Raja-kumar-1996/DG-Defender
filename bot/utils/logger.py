import logging
import sys

LOGGER = logging.getLogger("DG-Defender")

LOGGER.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

handler.setFormatter(formatter)

if not LOGGER.handlers:
    LOGGER.addHandler(handler)
