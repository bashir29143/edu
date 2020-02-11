l = [123, 245, 366, 477, 588, 666]

def f(l):
	return list(map(lambda x: str(x), l))

for i in f(l):
	print(type(i))
