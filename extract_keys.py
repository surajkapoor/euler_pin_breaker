import re
from collections import Counter
import pdb
from itertools import permutations

class KeyLogs(object):

	def __init__(self):
		self.keylogs = []
		self.bucket_a = []
		self.bucket_b = []
		self.bucket_c = []
		self.code = []

	def extract_numbers(self):
		with open("keylog.txt", "r") as k:
			keylogs = k.read()
			keylogs = keylogs[0:-1]
			start = 0
			end = 4
			while start < len(keylogs):
				self.keylogs.append(int(keylogs[start:end]))
				start = end
				end += 4	
		return self.keylogs

k = KeyLogs()
print k.extract_numbers()