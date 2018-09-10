import unittest
from prime import *


sieve_50 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
class TestPrimeNumbers(unittest.TestCase):
	""" Test Cases For Prime Numbers"""

       
	def test_10(self):
		""" Computing the first 10 prime numbers"""
		self.assertEqual(PrimeNumber(50),sieve_50)

	def test_zero(self):
		""" Computing the zero prime numbers"""
        	with self.assertRaises(Exception):
			PrimeNumber(0)
	
	def test_one(self):
		""" Computing one """
        	with self.assertRaises(Exception):
			PrimeNumber(1)

	def test_negative(self):
		"""Testing a negative number"""
		with self.assertRaises(Exception):
			PrimeNumber(-10)

	def test_string(self):
		"""Testing a string"""
		with self.assertRaises(TypeError):
			PrimeNumber("hsdfskjnd")
	
	def test_null(self):
		"""Testing a string"""
		with self.assertRaises(TypeError):
			PrimeNumber(None)
        	
if __name__ == '__main__':
    unittest.main()
