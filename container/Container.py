from dependency_injector import containers, providers

from abstract import ChkPreCon, GetUrlList, GetHtml, ParseHtml, SaveData
from wrapper import Crawler


class Container(containers.DeclarativeContainer):

    chk_pre_con_factory = providers.AbstractFactory(ChkPreCon)
    get_url_list_factory = providers.AbstractFactory(GetUrlList)
    get_html_factory = providers.AbstractFactory(GetHtml)
    parse_html_factory = providers.AbstractFactory(ParseHtml)
    save_data_factory = providers.AbstractFactory(SaveData)

    crawler_factory = providers.Factory(
        Crawler,
        chk_pre_con=chk_pre_con_factory,
        get_url_list=get_url_list_factory,
        get_html=get_html_factory,
        parse_html=parse_html_factory,
        save_data=save_data_factory
    )


