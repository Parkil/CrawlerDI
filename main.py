from config.log import config_logging
from container import Container
from dependency_injector import providers

from wrapper import Crawler

config_logging()

"""
    impl 패키지는 외부 구현체로 언제든지 변경될 수 있는 부분
"""


def init_crawler(chk_pre_con_path: str, get_url_list_path: str, get_html_path: str,
                 parse_html_path: str, save_data_path: str) -> Crawler:
    container = Container()

    container.chk_pre_con_factory.override(providers.Factory(chk_pre_con_path))
    container.get_url_list_factory.override(providers.Factory(get_url_list_path))
    container.get_html_factory.override(providers.Factory(get_html_path))
    container.parse_html_factory.override(providers.Factory(parse_html_path))
    container.save_data_factory.override(providers.Factory(save_data_path))

    return container.crawler_factory()


if __name__ == "__main__":
    crawler_factory: Crawler = init_crawler("impl.ChkPreConImpl", "impl.GetUrlListImpl",
                                            "impl.GetHtmlImpl", "impl.ParseHtmlImpl",
                                            "impl.SaveDataImpl")
    crawler_factory.run_crawler()
