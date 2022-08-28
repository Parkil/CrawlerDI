from dependency_interface.ChkPreCon import ChkPreCon


class ChkPreConImpl(ChkPreCon):

    def __init__(self, add_param: str):
        print('ChkPreConImpl init', add_param)

    def chk_pre_con(self) -> bool:
        return True
