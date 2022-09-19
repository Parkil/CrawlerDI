from dependency_injector import containers, providers

from dependency_impl import ChkPreConImpl, GetHtmlImpl, ParseHtmlImpl, GetUrlListImpl, SaveDataImpl


class Container(containers.DeclarativeContainer):

    # 해당 로직이 정상 작동 하지 않으면 @inject 에서 나오는 type 이 <class 'dependency_injector.wiring.Provide'> 로 고정된다
    wiring_config = containers.WiringConfiguration(packages=["di_handler"])

    """
    chk_pre_con : 크롤러 작동 사전 조건 체크
    get_url_list : url 리스트 반환
    get_html : url 에서 html 문자열 을 가져 온다
    parse_html : html 문자열 을 parsing 하여 원하는 정보를 추출 한다
    save_data : parse_html 에서 추출한 정보를 저장 한다
    """

    chk_pre_con = providers.Factory(
        ChkPreConImpl
    )

    get_url_list = providers.Factory(
        GetUrlListImpl
    )

    get_html = providers.Factory(
        GetHtmlImpl
    )

    parse_html = providers.Factory(
        ParseHtmlImpl
    )

    save_data = providers.Factory(
        SaveDataImpl
    )
