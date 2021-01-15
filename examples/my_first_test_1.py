from seleniumbase import BaseCase
from pytest_steps import test_steps
import pytest_steps

class MyTestClass(BaseCase):

    # pytest_steps.test_steps('step_a', 'step_b', 'step_c')
    # @test_steps('step_a', 'step_b', 'step_c')
    # def test_basic(self):
    def basic(self):
        self.open("https://store.xkcd.com/search")
        self.type('input[name="q"]', "xkcd book")
        self.click('input[value="Search"]')
        self.assert_text("xkcd: volume 0", "h3")
        self.open("https://xkcd.com/353/")
        self.assert_title("xkcd: Python")
        self.assert_element('img[alt="Python"]')
        self.click('a[rel="license"]')
        self.assert_text("free to copy and reuse")
        self.go_back()
        self.click_link_text("About")
        self.assert_exact_text("xkcd.com", "h2")
        self.click_link_text("geohashing")
        self.assert_element("#comic img")

        # print("step a")
        # assert not False  # replace with your logic
        # intermediate_a = 'hello'
        # yield
        #
        # # Step B
        # print("step b")
        # assert not False  # replace with your logic
        # yield
        #
        # # Step C
        # print("step c")
        # new_text = intermediate_a + " ... augmented"
        # print(new_text)
        # assert len(new_text) == 56
        # yield



@test_steps('step_a', 'step_b', 'step_c')
def test_ppp():
    ppp = MyTestClass()
    ppp.basic()
    print("step a")
    assert not False  # replace with your logic
    intermediate_a = 'hello'
    yield

    # Step B
    print("step b")
    assert not False  # replace with your logic
    yield

    # Step C
    print("step c")
    new_text = intermediate_a + " ... augmented"
    print(new_text)
    assert len(new_text) == 56
    yield


