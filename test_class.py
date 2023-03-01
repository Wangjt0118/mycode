# class A:
# 	def test_a(self):
# 		self.test_a_a()
# 		print('123AAAA')

# 	def test_a_a(self):
# 		print('123A_a_A_A_A_A_A_')

# 	def send(self):
# 		self.test_a()


# class B(A):
# 	def test_a(self):
# 		super(B, self).test_a()
# 		print('456BBBB')

# 	def test_a_a(self):
# 		print('456A_a_A_A_A_A_A_')



# b = B()
# b.test_a()


# def func1_1(name):
# 	print(name)
# 	def func1(func):
# 		print('func1_inner')
# 		def func1_inner(*args, **kwargs):
# 			print('func1_inner_inner_inner:start')
# 			a =func(*args, **kwargs)
# 			print('func1_inner_inner_inner:end')
# 			return a
# 		return func1_inner
# 	return func1


# def func2_2(name):
# 	print(name)
# 	def func2(func):
# 		print('func2_inner')
# 		def func2_inner(*args, **kwargs):
# 			print('func2_inner_inner_inner:start')
# 			a = 1
# 			if 5 > 2:
# 				a = func(*args, **kwargs)
# 			print('func2_inner_inner_inner:end')
# 			return a
# 		return func2_inner
# 	return func2


# @func1_1('1')
# @func2_2('2')
# def test(a):
# 	print('a: %s' % a)

# test(2)
import gevent
from gevent import monkey
import time

monkey.patch_all()

def test1():
    for i in range(10):
        time.sleep(0.2)
        print('1:%s' % i)


def test2():
    for i in range(10):
        time.sleep(0.1)
        print('2:%s' % i)


def test3():
    for i in range(10):
        time.sleep(0.1)
        print('3:%s' % i)

j1 = gevent.spawn(test1)
j2 = gevent.spawn(test2)
j3 = gevent.spawn(test3)
j1.join()
j3.join()
j2.join()

