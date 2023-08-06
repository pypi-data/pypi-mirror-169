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


### 三方依赖

* Allure：https://github.com/allure-framework/allure2
* WebDriverAgent：https://github.com/appium/WebDriverAgent

### Install

```shell
> pip install -i https://pypi.tuna.tsinghua.edu.cn/simple qrunner
```

### 🤖 Quick Start

1、查看帮助：
```shell
usage: qrunner [-h] [-v] [-p PROJECT]

全平台自动化测试框架

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show version
  -p PROJECT, --project PROJECT
                        create demo project
```

2、创建项目：
```shell
> qrunner -p mypro
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
└── run.py
```

3、运行项目：

* ✔️ 在`pyCharm`中右键执行。

* ✔️ 通过命令行工具执行。

```shell
> python run.py

2022-09-29 11:02:40,206 - root - INFO - 执行用例
2022-09-29 11:02:40,206 - root - INFO - 用例路径: test_adr.py
2022-09-29 11:02:40,206 - root - INFO - ['test_adr.py', '-sv', '--reruns', '0', '--alluredir', 'allure-results', '--clean-alluredir']
================================================================================================================================================= test session starts ==================================================================================================================================================
platform darwin -- Python 3.9.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /Users/UI/PycharmProjects/qrunner_new_gitee/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/UI/PycharmProjects/qrunner_new_gitee
plugins: xdist-2.5.0, forked-1.4.0, allure-pytest-2.9.45, rerunfailures-10.2, dependency-0.5.1, ordering-0.6
collecting ... 2022-09-29 11:02:40,294 - root - INFO - [UJK0220521066836] Create android driver singleton
2022-09-29 11:02:40,303 - root - INFO - 启动 android driver for UJK0220521066836
2022-09-29 11:02:40,309 - urllib3.connectionpool - DEBUG - Starting new HTTP connection (1): ujk0220521066836:7912
2022-09-29 11:02:40,357 - urllib3.connectionpool - DEBUG - Starting new HTTP connection (1): 127.0.0.1:62522
2022-09-29 11:02:40,377 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "GET /wlan/ip HTTP/1.1" 200 11
collected 1 item                                                                                                                                                                                                                                                                                                       

test_adr.py::TestLogin::test_login 2022-09-29 11:02:40,381 - root - DEBUG - [start_time]: 2022-09-29 11:02:40
2022-09-29 11:02:40,381 - root - INFO - 强制启动应用: com.qizhidao.clientapp
2022-09-29 11:02:40,496 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /shell HTTP/1.1" 200 39
2022-09-29 11:02:40,792 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "GET /packages/com.qizhidao.clientapp/info HTTP/1.1" 200 221
2022-09-29 11:02:40,893 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /shell HTTP/1.1" 200 184
2022-09-29 11:02:40,895 - root - INFO - 存在才点击元素: {'resourceId': 'com.qizhidao.clientapp:id/bottom_btn'},0
2022-09-29 11:02:40,895 - root - INFO - 判断元素是否存在: {'resourceId': 'com.qizhidao.clientapp:id/bottom_btn'},0
2022-09-29 11:02:40,895 - root - INFO - 查找元素: {'resourceId': 'com.qizhidao.clientapp:id/bottom_btn'},0
2022-09-29 11:02:54,106 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /jsonrpc/0 HTTP/1.1" 200 90
2022-09-29 11:02:54,179 - root - WARNING - 【exists:257】未找到元素 {'resourceId': 'com.qizhidao.clientapp:id/bottom_btn'}
2022-09-29 11:02:54,179 - root - INFO - 点击元素: {'resourceId': 'com.qizhidao.clientapp:id/bottom_view'},3
2022-09-29 11:02:54,179 - root - INFO - 查找元素: {'resourceId': 'com.qizhidao.clientapp:id/bottom_view'},3
2022-09-29 11:02:54,332 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /jsonrpc/0 HTTP/1.1" 200 89
2022-09-29 11:02:54,685 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "GET /screenshot/0 HTTP/1.1" 200 236334
2022-09-29 11:02:55,619 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /jsonrpc/0 HTTP/1.1" 200 290
2022-09-29 11:02:55,822 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /jsonrpc/0 HTTP/1.1" 200 89
2022-09-29 11:02:55,822 - root - DEBUG - 点击成功
2022-09-29 11:02:55,822 - root - INFO - 判断元素是否存在: {'text': '登录/注册'},0
2022-09-29 11:02:55,823 - root - INFO - 查找元素: {'text': '登录/注册'},0
2022-09-29 11:03:00,253 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /jsonrpc/0 HTTP/1.1" 200 90
2022-09-29 11:03:00,254 - root - WARNING - 【exists:257】未找到元素 {'text': '登录/注册'}
2022-09-29 11:03:00,254 - root - INFO - 已登录成功
2022-09-29 11:03:00,255 - root - DEBUG - 等待: 3s
PASSED2022-09-29 11:03:03,621 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "GET /screenshot/0 HTTP/1.1" 200 175495
2022-09-29 11:03:03,624 - root - INFO - 退出应用: com.qizhidao.clientapp
2022-09-29 11:03:03,782 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /shell HTTP/1.1" 200 39
2022-09-29 11:03:03,783 - root - DEBUG - [end_time]: 2022-09-29 11:03:03
2022-09-29 11:03:03,783 - root - DEBUG - [run_time]: 23.40 s
```

4、查看报告

运行`allure server allure-results`浏览器会自动调起报告（需先安装配置allure）

![test report](./test_report.jpg)

## 🔬 Demo

[demo](/demo) 提供了丰富实例，帮你快速了解qrunner的用法。

### 安卓APP 测试

```shell
import qrunner
from qrunner import AndroidElement, story, title


class HomePage:
    ad_close_btn = AndroidElement(rid='id/bottom_btn', desc='首页广告关闭按钮')
    bottom_my = AndroidElement(rid='id/bottom_view', index=3, desc='首页底部我的入口')


@story('首页')
class TestClass(qrunner.AndroidTestCase):
    
    def start(self):
        self.hp = HomePage()
    
    @title('从首页进入我的页')
    def testcase(self):
        self.hp.ad_close_btn.click()
        self.hp.bottom_my.click()
        self.assertText('我的订单')


if __name__ == '__main__':
    qrunner.main(
        android_device_id='UJK0220521066836',
        android_pkg_name='com.qizhidao.clientapp'
    )
```

__说明：__

* 创建测试类必须继承 `qrunner.AndroidTestCase`。
* 测试用例文件命名必须以 `test` 开头。
* qrunner的封装了`assertText`、`assertElement` 等断言方法。
* 建议优先使用PageObject模式，方便后期代码维护
* 如需在自定义的Page类中使用driver则需要继承Page类，否则无需继承
    * 如继承Page类，实例化时需要传入driver参数

### IOS APP 测试

```shell
import qrunner
from qrunner import IosElement, story, title


class HomePage:
    ad_close_btn = IosElement(label='close white big', desc='首页广告关闭按钮')
    bottom_my = IosElement(label='我的', desc='首页底部我的入口')


@story('首页')
class TestClass(qrunner.IosTestCase):

    def start(self):
        self.hp = HomePage()

    @title('从首页进入我的页')
    def testcase(self):
        self.hp.ad_close_btn.click()
        self.hp.bottom_my.click()
        self.assertText('我的订单')


if __name__ == '__main__':
    qrunner.main(
        ios_device_id='00008101-000E646A3C29003A',
        ios_pkg_name='com.qizhidao.company'
    )
```

__说明：__

* 创建测试类必须继承 `qrunner.IosTestCase`。
* 测试用例文件命名必须以 `test` 开头。
* qrunner的封装了`assertText`、`assertElement` 等断言方法。
* 建议优先使用PageObject模式，方便后期代码维护
* 如需在自定义的Page类中使用driver则需要继承Page类，否则无需继承
    * 如继承Page类，实例化时需要传入driver参数

### Web 测试

```shell
import qrunner
from qrunner import WebElement, story, title, Page


class PatentPage(Page):
    search_input = WebElement(tid='driver-home-step1', desc='查专利首页输入框')
    search_submit = WebElement(tid='driver-home-step2', desc='查专利首页搜索确认按钮')

    def open(self):
        self.driver.open_url()


@story('专利检索')
class TestClass(qrunner.WebTestCase):
    
    def start(self):
        self.pp = PatentPage(self.driver)
    
    @title('专利简单检索')
    def testcase(self):
        self.pp.open()
        self.pp.search_input.set_text('无人机')
        self.pp.search_submit.click()
        self.assertTitle('无人机专利检索-企知道')


if __name__ == '__main__':
    qrunner.main(
        base_url='https://www-pre.qizhidao.com',
        executable_path='/Users/UI/Documents/chromedriver'
    )
```

__说明：__

* 创建测试类必须继承 `qrunner.WebTestCase`。
* 测试用例文件命名必须以 `test` 开头。
* qrunner的封装了`assertTitle`、`assertUrl` 和 `assertText`等断言方法。
* 建议优先使用PageObject模式，方便后期代码维护
* 如需在自定义的Page类中使用driver则需要继承Page类，否则无需继承
    * 如继承Page类，实例化时需要传入driver参数

### HTTP 测试

```python
import qrunner
from qrunner import title, file_data, story


@story('PC站首页')
class TestClass(qrunner.TestCase):

    @title('查询PC站首页banner列表')
    @file_data('card_type', 'data.json')
    def test_getToolCardListForPc(self, card_type):
        path = '/api/qzd-bff-app/qzd/v1/home/getToolCardListForPc'
        payload = {"type": card_type}
        self.post(path, json=payload)
        self.assertEq('code', 0)


if __name__ == '__main__':
    qrunner.main(
        base_url='https://www-pre.qizhidao.com'
    )
```

__说明：__

* 创建测试类必须继承 `qrunner.TestCase`。
* 测试用例文件命名必须以 `test` 开头。
* qrunner的封装了`assertEq`、`assertLenEq` 和 `assertLenGt`等断言方法。

### Run the test

```python
import qrunner

qrunner.main()  # 默认运行当前测试文件
qrunner.main(case_path="./")  # 当前目录下的所有测试文件
qrunner.main(case_path="./test_dir/")  # 指定目录下的所有测试文件
qrunner.main(case_path="./test_dir/test_api.py")  # 指定目录下的测试文件
```

## 感谢

感谢从以下项目中得到思路和帮助。

* [seldom](https://github.com/SeldomQA/seldom)

* [selenium](https://www.selenium.dev/)

* [uiautomator2](https://github.com/openatx/uiautomator2)
  
* [facebook-wda](https://github.com/openatx/facebook-wda)

* [requests](https://github.com/psf/requests)



