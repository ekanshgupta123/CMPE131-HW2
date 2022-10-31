import time
def timeme(func):
	def wrapper():
		first = time.time()
		func()
		last = time.time()
		print("Total time ", last - first)
	return wrapper

