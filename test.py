"""
测试函数
wang daka
"""

import unittest
from name_function import get_formatted_name


#测试函数

class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('jains','joplin')
        self.assertEqual(formatted_name,'Jains Joplin')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('jains','joplin','willen')
        self.assertEqual(formatted_name,'Jains Willen Joplin')

unittest.main()
unittest.main()

