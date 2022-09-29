import dataclasses
from typing import List

from wrapper import Crawler


@dataclasses.dataclass
class CrawlerChain:
    crawler_list: List[Crawler]

    def run_crawler_chain(self):
        for crawler in self.crawler_list:
            crawler.run_crawler()
