from copy import deepcopy as dc
import time
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
			return any([type(i)==list for i in self])

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
		from re import search
		_r = []
		for i in self:
			_t = type(i)
			if _t == list:
				continue
			try:
				_r.append(_t(search(f'^.*{str(sstr)}.*$', str(i)).group(0)))
			except AttributeError:
				continue
		del search
		return _r

	def split_mod(self, grps, rtt=list):
		_gp = [[] for i in range(grps)]
		_l = dc(self)
		for count, i in enumerate(_l):
			_gp[count%grps].append(i)
		del _l
		return rtt(_gp)

	def split_to(self, grps):
		from math import ceil as mceil
		_g = mceil(len(self)/grps)
		return [self[i:i+_g] for i in range(0,len(self),_g)]

	def deepshuffle(self,replace=True):
		import time
		import random
		def _s(l):
			random.seed(random.randrange(1,random.randrange(1000,10000000)))
			random.shuffle(l)
			for i in l:
				if isinstance(i, list):
					random.seed(random.randrange(1,random.randrange(1000,10000000)))
					random.shuffle(i)
					_s(i)
			return l

		if replace:
			_k = _s(self)
		else:
			_k = dc(self)
			_k = _s(_k)

		del time, random
		return _k

	def shuffle(self, s=time.time(),rp=False):
		from random import shuffle, seed
		seed(s)
		k = dc(self)
		shuffle(k)
		if rp:
			self=dc(k)
		return k








