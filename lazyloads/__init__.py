class lzlist(list):
	def __init__(self, ip):
		super().__init__(ip)

	def find_type(self,tp):
		try:
			return [i for i in self if type(i) == tp]
		except NameError:
			return None

	def list_types(self):
		return list(set([type(i) for i in self]))

	def all_index(self,val):
		for count,value in enumerate(self):
			if value == val:
				yield count
		return None

	def unique(self):
		return list(set(self))

	def split_by(self,val):
		self = [self[i:i+val] for i in range(0,len(self),val)]
		return self

	def join_all(self):
		_o = []
		for i in self:
			_o += list(i)
		self = lzlist(_o)
		del _o
		return self



		


