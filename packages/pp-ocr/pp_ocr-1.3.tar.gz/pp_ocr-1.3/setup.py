import pathlib
from setuptools import setup, find_packages


APPNAME = "pp_ocr"
VERSION = "1.3"

with open("requirements.txt") as fin:
    REQUIRED_PACKAGES = fin.read()

setup(
    name = APPNAME,
    version = VERSION,
    description="ocr识别",                                          # 长描述，用于在Pypi上面显示
    author="xdg",
    license="Apache Software License",
    packages=find_packages(),                                       # 包模块
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
   )
