from pytest_steps import test_steps
import allure
from seleniumbase import BaseCase

class MMMM(BaseCase):

    @test_steps('step_a', 'step_b', 'step_c')
    def test_suite(self):
        # Step A
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

    def test_my_12345(self):
        with allure.step('Моя перша алюра'):
            assert True

        with allure.step('Моя second алюра'):
            assert False




