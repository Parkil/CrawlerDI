import logging
from typing import List

from config.log import config_logging
from di import Container
from di_handler.handler import run_crawler

config_logging()

logger = logging.getLogger('detail')

if __name__ == "__main__":
    # 여기 에서 wire 설정을 할 수 도 있다
    container = Container()
    container.wire(packages=["di_handler"])
    run_crawler()

