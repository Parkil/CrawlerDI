from config.log import config_logging
from init_crawler import InitCrawler

from wrapper import Crawler, CrawlerChain

config_logging()

if __name__ == "__main__":
    """
    crawler1: Crawler = InitCrawler.init_crawler_by_path_str("impl.ChkPreConImpl", "impl.GetUrlListImpl",
                                                             "impl.GetHtmlImpl", "impl.ParseHtmlImpl",
                                                             "impl.SaveDataImpl")

    crawler2: Crawler = InitCrawler.init_crawler_by_path_str("impl2.ChkPreConImpl", "impl2.GetUrlListImpl",
                                                             "impl.GetHtmlImpl", "impl2.ParseHtmlImpl",
                                                             "impl2.SaveDataImpl")

    crawler_chain = CrawlerChain([crawler1, crawler2])
    crawler_chain.run_crawler_chain()
    """
    crawler1: Crawler = InitCrawler.init_crawler_by_path_str("impl.ChkPreConImpl", "impl.GetUrlListImpl",
                                                             "impl.GetHtmlImpl", "impl.ParseHtmlImpl",
                                                             "impl.SaveDataImpl")

    crawler1.run_crawler()
