from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class BaseTestCase(BaseCase):
    def set_up(self):
        super().set_up()
        # <<< Run custom code AFTER the super() line >>>

    def tear_down(self):
        self.save_tear_down_screenshot()
        if self.has_exception():
            # <<< Run custom code if the test failed. >>>
            pass
        else:
            # <<< Run custom code if the test passed. >>>
            pass
        # (Wrap unreliable code in a try/except block.)
        # <<< Run custom code BEFORE the super() line >>>
        super().tear_down()

    def login(self):
        # <<< Placeholder. Add your code here. >>>
        pass

    def example_method(self):
        # <<< Placeholder. Add your code here. >>>
        pass
