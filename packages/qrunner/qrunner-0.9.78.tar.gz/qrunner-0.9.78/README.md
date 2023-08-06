[Gitee](https://gitee.com/bluepang2021/qrunner_new)

![](Qrunner_logo.jpg)

[![PyPI version](https://badge.fury.io/py/qrunner.svg)](https://badge.fury.io/py/qrunner) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/qrunner)
![visitors](https://visitor-badge.glitch.me/badge?page_id=qrunner_new.qrunner)

AppUI/WebUI/HTTP automation testing framework based on pytest.

> 基于pytest 的 App UI/Web UI/HTTP自动化测试框架。

### 特点

* 集成`facebook-wda`/`uiautomator2`/`selenium`/`requests`，支持Web UI/HTTP测试。
* 集成`allure`, 支持HTML格式的测试报告。
* 提供脚手架，快速生成自动化测试项目。
* 提供强大的`数据驱动`。
* 提供丰富的断言。
* 支持生成随机测试数据。
* 支持设置用例依赖。

### Install

```shell
> pip install qrunner
```

### 🤖 Quick Start

1、查看帮助：
```shell
usage: qrunner [-h] [-V] {start} ...

全栈自动化测试框架

positional arguments:
  {start}        sub-command help
    start        Create a new project with template structure.

optional arguments:
  -h, --help     show this help message and exit
  -V, --version  show version
```

2、创建项目：
```shell
> qrunner start mypro
```
目录结构如下：
```shell
mypro/
├── test_dir/
│   ├── __init__.py
│   ├── test_android.py
│   ├── test_ios.py
│   ├── test_web.py
│   ├── test_api.py
├── test_data/
│   ├── data.json
├── .gitignore
├── requiremets.txt
└── run.py
```

