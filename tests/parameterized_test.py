from parameterized import parameterized
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class GoogleTests(BaseCase):
    @parameterized.expand(
        [
            ["Download Python", "Download Python"],
            ["wikipedia", "www.wikipedia.org"],
            ["SeleniumBase.io Docs", "SeleniumBase"],
        ]
    )
    def test_parameterized_google_search(self, search_term, expected_text):
        self.open("https://google.com/ncr")
        self.type('input[title="Search"]', search_term + "\n")
        self.assert_text(expected_text, "#search")
