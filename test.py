from multipledispatch import dispatch


class AAA:
    @dispatch(str)
    def test(self, a: str):
        print('org : ', a)

    @dispatch(str, str)
    def test(self, a: str, b: str):
        print('overloading : ', a, b)

    @dispatch(str, str, str)
    def test(self,a, b, c):
        print('overloading : ', a, b, c)


aaa = AAA()

aaa.test('1111')

aaa.test('1111', '2222')

aaa.test('3333', '44444', '55555')

