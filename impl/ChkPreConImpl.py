import logging

from abstract.ChkPreCon import ChkPreCon


class ChkPreConImpl(ChkPreCon):
    logger = logging.getLogger('detail')

    def __init__(self):
        self.logger.info('ChkPreConImpl init')

    def chk_pre_con(self) -> bool:
        return True
