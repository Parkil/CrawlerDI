
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

"""
    파아썬 소스 코드를 패키징 하기 위한 설정 파일
    py_module : 파이썬의 모듈을 하나하나씩 열거
    packages : 여기에 지정된 폴더안의 모든 모듈을 자동으로 인식
    
    python -m pip install /Users/ilpark/PycharmProjects/CrawlerDI/dist/di_crawler-0.1-py3-none-any.whl
"""
setup(
    name='init_crawler crawler',
    version='0.1',
    description='init_crawler crawler',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='alkain77',
    author_email='alkain77@gmail.com',
    license='MIT',
    python_requires='>=3.8',
    packages=find_packages(),  # where를 정의하지 않으면 최상위 부터 package를 전부 검색한다
    install_requires=['dependency-injector==4.40.0']
)

