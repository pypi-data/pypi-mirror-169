from setuptools import setup
import PyTistory



setup(
    name='Python-Tistory',
    version=PyTistory.__version__,
    description='Tistory Open API Python Wrapper',
    author=PyTistory.__author__,
    author_email='t3nderex@gmail.com',
    packages=['PyTistory'],
    install_requires=['webdriver-manager==3.8.3',
                    'requests==2.28.1',
                    'selenium==4.4.3'
                    ])
