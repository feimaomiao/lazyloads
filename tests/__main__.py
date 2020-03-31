import sys
import unittest
import test_lzl as testfile
import os


if __name__ == '__main__':
	if not os.path.isdir('tests'):
		os.mkdir('tests')
	test_suite = unittest.TestLoader().loadTestsFromModule(testfile)
	try:
		os.remove('test_output.out')
	except FileNotFoundError:
		pass
	sys.stdout = None 
	unittest.TextTestRunner(open('test_output.out','a+'),verbosity=2).run(test_suite)
	sys.stdout = sys.__stdout__