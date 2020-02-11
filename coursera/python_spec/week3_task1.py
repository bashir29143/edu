class FileReader:
	def __init__(self, path):
		self.path = path
	def read(self):
		try:
			file = open(self.path, 'r')
			string = file.read()
			file.close()
		except IOError:
			return ""
		return string

