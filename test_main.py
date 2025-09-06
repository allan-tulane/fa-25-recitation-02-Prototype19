from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650

	assert simple_work_calc(81, 2, 3) == 211
	assert simple_work_calc(50, 10, 3) == 1710
	assert simple_work_calc(10, 3,2) == 70



def test_work():
	assert work_calc(10, 2, 2, lambda x: x) == 36
	assert work_calc(10, 2, 2, lambda x: 1) == 15
	assert work_calc(16, 2, 2, lambda x: x * x) == 496

	assert work_calc(8, 3, 2, lambda x: x) == 65
	assert work_calc(27, 3, 3, lambda x: 1) == 40
	assert work_calc(16, 4, 2, lambda x: x * x) == 1280


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	work_fn1 = lambda n: work_calc(n, 2, 2, lambda x: 1)  # f(n) = 1
	work_fn2 = lambda n: work_calc(n, 2, 2, lambda x: x)  # f(n) = n
	res = compare_work(work_fn1, work_fn2)

	print(res)

	
def test_compare_span():
	work_fn1 = lambda n: span_calc(n, 2, 2, lambda x: 1)  # f(n) = 1
	work_fn2 = lambda n: span_calc(n, 2, 2, lambda x: x)  # f(n) = n
	res = compare_span(work_fn1, work_fn2)

	print(res)

