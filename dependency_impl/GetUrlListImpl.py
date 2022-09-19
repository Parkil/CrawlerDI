import logging
from typing import List

from dependency_interface import GetUrlList


class GetUrlListImpl(GetUrlList):

    logger = logging.getLogger('detail')

    def __init__(self):
        self.logger.info('GetUrlListImpl Init')

    def get_url_list(self) -> List[str]:
        return ['https://novel.munpia.com/page/novelous/group/nv.regular/order/create/gpage/1']

