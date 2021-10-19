import unittest
import doubles

import sum


class MyTestCase(unittest.TestCase):
    def test_a_value(self):
        self.lines = open("sample.txt").readlines()
        self.total = 0
        for l in self.lines:
            self.total += int(l)
        self.assertEqual(self.total, 155)  # add assertion here

    def test_b_string(self):
        open("sample.txt", "a").write("\nfire")
        self.lines = open("sample.txt").readlines()
        self.assertRaises(ValueError, sum.summing())


if __name__ == '__main__':
    unittest.main()

