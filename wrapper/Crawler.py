import dataclasses
import logging
from typing import List

from abstract import ChkPreCon, GetUrlList, GetHtml, ParseHtml, SaveData
from abstract.vo import HtmlInfo, ParseHtmlInfo
from config.exception import CrawlerException

logger = logging.getLogger('detail')


@dataclasses.dataclass
class Crawler:
    chk_pre_con: ChkPreCon
    get_url_list: GetUrlList
    get_html: GetHtml
    parse_html: ParseHtml
    save_data: SaveData

    def run_crawler(self):
        __chk_result: bool = self.chk_pre_con.chk_pre_con()

        if __chk_result is False:
            raise CrawlerException('chk pre condition is False', None)

        __url_list: List[str] = self.get_url_list.get_url_list()
        logger.info('url_list : %s', __url_list)

        __html_list: List[HtmlInfo] = self.get_html.get_htmls(__url_list)

        __parse_html_info_list: List[ParseHtmlInfo] = self.parse_html.parse_htmls(__html_list)
        logger.info('parse_result_dict : %s', __parse_html_info_list)

        self.save_data.save(__parse_html_info_list)
