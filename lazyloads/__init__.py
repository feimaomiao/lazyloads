from copy import deepcopy as dc
from re import search
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
		return [count for count, value in enumerate(self) if value==val]

	def unique(self):
		_tmp = dc(self)
		_tmp.join_all()
		return list(set(_tmp))

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
				if type(i) == list:
					_o += i 
				else:
					_o.append(i)
			super().__init__(dc(_o))
			del _o
		return self

	def similarto(self, sstr):
		_r = []
		for i in self:
			_t = type(i)
			if _t == list:
				continue
			try:
				_r.append(_t(search(f'^.*{str(sstr)}.*$', str(i)).group(0)))
			except AttributeError:
				continue
		return _r
