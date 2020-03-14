from copy import deepcopy as dc
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
		super().__init__([self[i:i+val] for i in range(0,len(self),val)])
		return self

	def join_all(self):
		def _check():
			for i in self:
				if type(i)==list:
					return True
			return False

		while _check():
			_o = []
			for i in self:
				print(i,_o)
				if type(i) == list:
					_o += i 
				else:
					_o.append(i)
			super().__init__(dc(_o))
			print(self)
			del _o
		return self
