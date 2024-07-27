import unittest
from app import power_set

class TestPowerSet(unittest.TestCase):
    def test_normal_case_1(self):
        input_set = ['a', 'b', 'c']
        expected_output = [[], ['a'], ['b'], ['c'], ['a', 'b'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
        self.assertCountEqual(power_set(input_set), expected_output)
    
    def test_normal_case_2(self):
        input_set = ['1', '2']
        expected_output = [[], ['1'], ['2'], ['1', '2']]
        self.assertCountEqual(power_set(input_set), expected_output)
    
    def test_normal_case_3(self):
        input_set = ['x', 'y', 'z']
        expected_output = [[], ['x'], ['y'], ['z'], ['x', 'y'], ['x', 'z'], ['y', 'z'], ['x', 'y', 'z']]
        self.assertCountEqual(power_set(input_set), expected_output)

    def test_edge_case_empty_set(self):
        input_set = []
        expected_output = [[]]
        self.assertCountEqual(power_set(input_set), expected_output)

    def test_edge_case_single_element(self):
        input_set = ['a']
        expected_output = [[], ['a']]
        self.assertCountEqual(power_set(input_set), expected_output)
    
    def test_edge_case_duplicate_elements(self):
        input_set = ['a', 'a']
        expected_output = [[], ['a'], ['a'], ['a', 'a']]
        self.assertCountEqual(power_set(input_set), expected_output)

if __name__ == '__main__':
    unittest.main()
