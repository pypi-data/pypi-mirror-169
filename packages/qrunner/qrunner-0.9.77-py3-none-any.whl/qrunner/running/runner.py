import pytest
from qrunner.utils.log import logger
from qrunner.utils.config import conf


class TestMain(object):
    """
    Support for app and web
    """
    def __init__(self,
                 android_device_id: str = None,
                 android_pkg_name: str = None,
                 ios_device_id: str = None,
                 ios_pkg_name: str = None,
                 browser_name: str = 'chrome',
                 case_path: str = '.',
                 rerun: int = 0,
                 concurrent: bool = False,
                 base_url: str = None,
                 executable_path: str = None,
                 headers: dict = None,
                 timeout: int = 10,
                 headless: bool = False
                 ):
        """
        :param serial_no str: 设备id，如UJK0220521066836、00008020-00086434116A002E
        :param pkg_name str: 应用包名，如com.qizhidao.clientapp、com.qizhidao.company
        :param browser str: 浏览器类型，如chrome、firefox、edge、safari
        :param case_path str: 用例路径
        :param rerun int: 失败重试次数
        :param concurrent bool: 是否需要并发执行
        :@param base_url str: 接口host
        "@param headers dict: 额外的请求头，{
            'login_headers': {
                "accessToken": "xxxx",
                "signature": "xxxx"
            }, # 非必填
            'visit_headers': {} # 非必填
        }
        :@param timeout int: 接口请求超时时间
        """

        # 将数据写入全局变量
        conf.set_item('android', 'serial_no', android_device_id)
        conf.set_item('android', 'pkg_name', android_pkg_name)
        conf.set_item('ios', 'serial_no', ios_device_id)
        conf.set_item('ios', 'pkg_name', ios_pkg_name)
        conf.set_item('web', 'browser_name', browser_name)
        conf.set_item('common', 'base_url', base_url)
        conf.set_item('web', 'executable_path', executable_path)
        if headers is not None:
            login_headers = headers.pop('login_headers', {})
            conf.set_item('common', 'login_headers', login_headers)
            visit_headers = headers.pop('visit_headers', {})
            conf.set_item('common', 'visit_headers', visit_headers)
        conf.set_item('common', 'timeout', timeout)
        conf.set_item('web', 'headless', headless)

        # 执行用例
        logger.info('执行用例')
        logger.info(f'用例路径: {case_path}')
        cmd_list = [
            '-sv',
            '--reruns', rerun,
            '--alluredir', 'allure-results', '--clean-alluredir'
        ]
        if case_path:
            cmd_list.insert(0, case_path)
        if concurrent:
            cmd_list.insert(1, '-n')
            cmd_list.insert(2, 'auto')
            cmd_list.insert(3, '--dist=loadscope')
        logger.info(cmd_list)
        pytest.main(cmd_list)


main = TestMain


if __name__ == '__main__':
    main()

