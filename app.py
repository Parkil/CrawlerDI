from di import Container
from di_handler.handler import chk_pre_con, get_htmls, parse_html


def run_crawler():
    Container()
    chk_result: bool = chk_pre_con()
    print('chk_result : ', chk_result)

    result_dict: dict = get_htmls(['http://python.org', 'https://en.wiktionary.org/wiki/bigle'])
    print('result_dict : ', result_dict)

    parse_result_dict: dict = parse_html(result_dict)
    print(parse_result_dict)


if __name__ == "__main__":
    run_crawler()

