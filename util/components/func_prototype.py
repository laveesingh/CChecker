class func_prototype:

	def __init__(self, text, lines):
		self.text = '\n'.join(text)
		self.start = lines[0]
		self.end = lines[1]