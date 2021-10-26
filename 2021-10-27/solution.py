import bisect
class Autocomplete:
	def build(self, w=[]):
		self.words = sorted(w)

	def autocomplete(self, word):
		i=bisect.bisect_left(self.words, word)
		word += "}"
		j=bisect.bisect_left(self.words, word)
		return self.words[i:j]

a = Autocomplete()
a.build(['dog', 'dark', 'cat', 'door', 'dodge'])
print(a.autocomplete('do'))