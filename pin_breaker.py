import random

class Keys(object):

	def __init__(self):
		self.keys = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716]
		print len(self.keys)
		self.splitkeys = [[int(k) for k in (list(str(key)))] for key in self.keys]
		self.pin = []


	def missing_digit(self, key):
		a, b, c = key	
		if a not in self.pin:
			self.pin.append(a)
		if b not in self.pin:
			self.pin.append(b)
		if c not in self.pin:
			self.pin.append(c)	
		return self.pin


	def find_pin_digits(self):
		for key in self.splitkeys:
			a, b, c = key
			try:
				key_pin_match = self.pin.index(a) < self.pin.index(b) < self.pin.index(c)
			except ValueError:
				self.missing_digit(key)	
		return self.pin


	def rearrange_pin(self, a, a_index, b, b_index, c, c_index):
		if b_index < a_index < c_index:
			self.pin.remove(b)
			self.pin.insert(a_index + 1, b)
		elif c_index < a_index < b_index:
			self.pin.remove(c)
			self.pin.insert(b_index + 1, c)
		elif a_index < c_index < b_index:
			self.pin.remove(b)
			self.pin.insert(a_index + 1, b)
		elif b_index < a_index < c_index:
			self.pin.remove(b)
			self.pin.insert(a_index + 1, b)
		elif b_index < c_index < a_index:
			self.pin.remove(b)
			self.pin.insert(a_index + 1, b)
			self.pin.remove(c)
			self.pin.insert(a_index + 2, c)
		elif c_index < b_index < a_index:
			self.pin.remove(b)
			self.pin.insert(a_index + 1, b)
			self.pin.remove(c)
			self.pin.insert(a_index + 2, c)
		return	

	def sort_code(self):
		self.find_pin_digits()
		counter = 0
		while counter < len(self.splitkeys): 
			key = self.splitkeys[counter]
			a, b, c = key
			a_index = self.pin.index(a)
			b_index = self.pin.index(b)
			c_index = self.pin.index(c)
			if a_index < b_index < c_index:
				pass
				counter += 1
			else:	
				self.rearrange_pin(a, a_index, b, b_index, c, c_index)
				counter = 0
			print self.pin	
		return self.pin		

	
if __name__ == "__main__":
	k = Keys()
	k.sort_code()


