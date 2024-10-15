'''测试文件'''
import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    '''测试name_function.py'''
    def  test_first_last_name(self):
        '''能够正确处理Janis 这样的姓名'''
        formatted_name=get_formatted_name("janis","jenny")
        self.assertEqual(formatted_name,'Janis Jenny')
    def test_first_middle_name(self):
        formatted_name=get_formatted_name('dad','dad','dad')
        self.assertEqual(formatted_name,'Dad Dad Dad')
if __name__ == '__main__':
    unittest.main()