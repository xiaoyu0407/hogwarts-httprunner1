import os
import unittest

from hogwarts_httprunner1.loader import load_yaml
from hogwarts_httprunner1.runner import run_yaml


class TestSingleAPI(unittest.TestCase):

    def test_loader_single_api(self):
        """
        加载出的接口请求参数与原始信息一样
        :return:
        """
        single_api_yaml = os.path.join(os.path.dirname(__file__),"api","get_homepage.yml")
        loaded_json = load_yaml(single_api_yaml)
        self.assertIn("request",loaded_json)
        self.assertEqual(loaded_json["request"]["url"],"https://mubu.com/")

    def test_run_single_api(self):
        single_api_yaml = os.path.join(os.path.dirname(__file__), "api", "get_homepage.yml")
        result = run_yaml(single_api_yaml)
        self.assertEqual(result,True)

        single_api_yaml = os.path.join(os.path.dirname(__file__), "api", "api_login_submit.yml")
        result = run_yaml(single_api_yaml)
        self.assertEqual(result, True)

        single_api_yaml = os.path.join(os.path.dirname(__file__), "api", "get_login.yml")
        result = run_yaml(single_api_yaml)
        self.assertEqual(result, True)
