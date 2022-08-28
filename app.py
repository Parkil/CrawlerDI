from di import Container
from di_handler.handler import chk_pre_con, get_html


def run_crawler():
    Container()
    chk_result: bool = chk_pre_con()
    print('chk_result : ', chk_result)

    result_dict: dict = get_html('http://python.org')
    print('result_dict : ', result_dict)


if __name__ == "__main__":
    run_crawler()

