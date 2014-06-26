from setuptools import setup

setup(
    name="zend",
    version="0.0.1-dev",
    packages=["zend"],
    entry_points={
        'console_scripts': [
            'zend = zend.__main__:main'
        ]
    }
)