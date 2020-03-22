import os
import unittest

from hogwarts_httprunner1.loader import load_yaml

class TestSingleAPI(unittest.TestCase):

    def test_loader_single_api(self):
        """
        加载出的接口请求参数与原始信息一样
        :return:
        """
        single_api_yaml = os.path.join(os.path.dirname(__file__),"api","get_homepage.yml")
        loaded_json = load_yaml(single_api_yaml)
        self.assertEqual(loaded_json["url"],"https://mubu.com/")

    def test_run_single_api(self):
        single_api_yaml = os.path.join(os.getcwd(), "api", "get_homepage.yml")
        resp = run_yml(single_api_yaml)
        self.assertEqual(resp.status_code,200)
