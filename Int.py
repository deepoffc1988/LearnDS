class Float:
	value = 7.8
	
	def __float__(self):
		return self.value

data = Float()
print("number =", float(data))


class Number:
	value = 7
	
	def __index__(self):
		return self.value

data = Number()
print("number =", int(data))





