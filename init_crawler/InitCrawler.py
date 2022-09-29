from container import Container
from dependency_injector import providers

from wrapper import Crawler


class InitCrawler:

    @staticmethod
    def init_crawler_by_path_str(chk_pre_con_path: str, get_url_list_path: str, get_html_path: str,
                                 parse_html_path: str, save_data_path: str) -> Crawler:
        container = Container()

        container.chk_pre_con_factory.override(providers.Factory(chk_pre_con_path))
        container.get_url_list_factory.override(providers.Factory(get_url_list_path))
        container.get_html_factory.override(providers.Factory(get_html_path))
        container.parse_html_factory.override(providers.Factory(parse_html_path))
        container.save_data_factory.override(providers.Factory(save_data_path))

        return container.crawler_factory()
