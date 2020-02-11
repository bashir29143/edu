class Container:
	def __init__(self):
		self.keys = list()
		self.items = list()

	def __getitem__(self, key):
		for i in range(len(self.keys)):
			if self.keys[i] == key:
				return self.items[i]
		print('There is no key: {}'.format(key))		

	def __setitem__(self, key, item):
		for i in range(len(self.keys)):
			if self.keys[i] == key:
				self.items[i] = item
				return
		self.keys.append(key)
		self.items.append(item)



obj = Container()

obj['yoel'] = 'romero'

print(obj['yoel'])
print(obj['robert'])

obj['yoel'] = 'soldier'

print(obj['yoel'])
