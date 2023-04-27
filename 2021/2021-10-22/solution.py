class LRUCache:
	def __init__(self, size):
		self.size = size if size>0 else 10
		self.pages = dict()

	def get(self, key):
		if key in self.pages:
			value = self.pages[key]
			self.pages.pop(key)
			self.pages[key] = value
			return value
		return None

	def put(self, key, value):
		if key in self.pages:
			self.pages.pop(key)
		elif len(self.pages) == self.size:
			self.pages.pop(next(iter(self.pages)))
		self.pages[key] = value

cache = LRUCache(2)

cache.put(3, 3)
cache.put(4, 4)
print(cache.get(3))
print(cache.get(2))
cache.put(2, 2)
print(cache.get(4))
print(cache.get(3))