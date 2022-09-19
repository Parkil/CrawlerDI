from dependency_interface.ChkPreCon import ChkPreCon


class ChkPreConImpl(ChkPreCon):

    def __init__(self):
        print('ChkPreConImpl init')

    def chk_pre_con(self) -> bool:
        return True
