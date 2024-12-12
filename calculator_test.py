import unittest
from calculator import Calculator
 
class TestSum(unittest.TestCase):
 
  def test_sum(self):
    calculator = Calculator()
    self.assertEqual(calculator.add(1, 2), 3)
 
  def test_sum2(self):
    calculator = Calculator()
    self.assertEqual(calculator.add(1, 3), 3)

  if __name__ =="__main__":
    unittest.main()