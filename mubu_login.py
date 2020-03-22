import requests
import unittest

class TestMubuLogin(unittest.TestCase):
    def test_get_homepage(self):
        url = "https://mubu.com/"
        method = "GET"
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2)"
                          "AppleWebKit/537.36(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        }
        kwargs = {
            "headers": headers,
            "verify": False
        }
        resp = requests.request(method,url, **kwargs)
        # print(resp.text)
        assert resp.status_code ==200

    def test_get_login(self):
        url = "https://mubu.com/login"
        method = "GET"
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2)"
                          "AppleWebKit/537.36(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        }
        kwargs = {
            "headers": headers,
            "verify": False
        }
        resp = requests.request(method, url, **kwargs)
        # print(resp.text)
        assert resp.status_code == 200

    def test_get_login_password(self):
        url = "https://mubu.com/login/password"
        method = "GET"
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2)"
                          "AppleWebKit/537.36(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        }
        kwargs = {
            "headers": headers,
            "verify": False
        }
        resp = requests.request(method, url, **kwargs)
        # print(resp.text)
        assert resp.status_code == 200


    def test_post_login(self):
        url = "https://mubu.com/api/login/submit"
        method = "post"
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2)"
                          "AppleWebKit/537.36(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        data = "phone=18616708947&password=wodemima0407&remember=true"
        kwargs = {
            "headers": headers,
            "data": data,
            "verify": False
        }

        resp = requests.request(method,url, **kwargs)
        # print(resp.text)
        assert resp.status_code ==200

# if __name__=='__main__':
#     test_get_homepage()
#     test_get_login()
#     test_get_login_password()
#     test_post_login()