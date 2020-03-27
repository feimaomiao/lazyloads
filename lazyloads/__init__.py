from copy import deepcopy as dc
import time
from random import seed as randomseed, randrange as rrange
randomseed(time.time()*rrange(1234,123456789))
del randomseed, time,rrange


class lzlist(list):
	def __init__(self, ip):
		super().__init__(ip)
		self.__copy = ip

	def __hash__(self):
		from hashlib import sha512
		_h = sha512()
		[_h.update(str(i).encode('utf-32')) for i in self]
		del sha512
		return _h.hexdigest()

	def includes_type(self,tp):
		try:
			return lzlist([i for i in self if type(i) == tp])
		except NameError:
			return None

	def revert(self):
		super().__init__(dc(self.__copy))
		return self 
	

	@property
	def list_types(self):
		return list(set([type(i) for i in self]))

	def all_index(self,val):
		return lzlist([count for count, value in enumerate(self) if value==val])

	@property
	def unique(self):
		_tmp = dc(self)
		_tmp.join_all()
		return lzlist(set(_tmp))

	def split_by(self,val):
		super().__init__([self[i:i+val] for i in range(0,len(self),val)])
		return self

	def join_all(self):
		def _check():
			return any([isinstance(i,list) for i in self])

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

	def similar_to(self, sstr):
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
		return lzlist(_r)

	def split_mod(self, grps):
		_gp = [[] for i in range(grps)]
		_l = dc(self)
		for count, i in enumerate(_l):
			_gp[count%grps].append(i)
		del _l
		super().__init__(_gp)
		return self

	def split_to(self, grps):
		from math import ceil as mceil
		_g = mceil(len(self)/grps)
		del mceil
		super().__init__([self[i:i+_g] for i in range(0,len(self),_g)])
		return self

	def deepshuffle(self,replace=True):
		from random import shuffle
		def _s(l):
			shuffle(l)
			for i in l:
				if isinstance(i, list):
					shuffle(i)
					_s(i)
			return l

		if replace:
			_k = _s(self)
		else:
			_k = dc(self)
			_k = _s(_k)

		del shuffle
		return lzlist(_k)

	def shuffle(self,rp=False):
		from random import shuffle
		k = dc(self)
		shuffle(k)
		shuffle(k)
		if rp:
			super().__init__(dc(k))
		del shuffle
		return lzlist(k)

	def choice(self,amount):
		from random import choices
		_p =  choices(self, k=amount)
		del choices
		return lzlist(_p)

	def type_is_all(self, t):
		return all([isinstance(i,t) for i in self])

	def type_includes(self, t):
		return any([isinstance(i,t) for i in self])

	def includes(self ,t):
		return any([i==t for i in self])

	def all_with_type(self, t):
		return lzlist([i for i in self if isinstance(i,t)])

	def all_without_type(self,t):
		return lzlist([i for i in self if not isinstance(i,t)])

	def count_type(self, t):
		return len(self.all_with_type(t))

	def forall(self,t='product'):
		from itertools import product,permutations,combinations, combinations_with_replacement
		if t.startswith('pr'):
			_k = list([list(i) for i in product(self,repeat=2)])
		elif t.startswith('pe'):
			_k = list([list(i) for i in permutations(self,2)])
		elif t.startswith('c') and t.endswith('s'):
			_k = list([list(i) for i in combinations(self,2)])
		else:
			_k = list([list(i) for i in combinations_with_replacement(self,2)])
		del product, permutations, combinations, combinations_with_replacement
		return lzlist(_k)

	@property
	def tostr(self):
		return lzstr('').join([chr(round(i)) for i in self]) if self.type_is_all((int, float)) else None

	def next(self, askval=None, rt=False):
		if not askval:
			askval=self[0]
		def _g(self,askval):
			_s = self.all_index(askval)
			if len(_s) ==0:
				return
			else:
				try:
					for i in self.all_index(askval):
						yield self[i+1]
				except IndexError:
					yield self[0]
		return _g(self, askval) if rt else lzlist(_g(self,askval))


	def sort(self):
		return sorted(self,key=lambda x: hash(x))



	@staticmethod
	def mkrandlist(length,start=None,end=None,sd=None):
		from random import seed, randrange
		if sd:
			seed(sd)
		if not start and end:
			start=end
			end= None
		if not start:
			start=100
		_k=lzlist([])
		for i in lzint(length):
			seed(randrange(0,randrange(10000000000)))
			if start and end:
				_k.append(randrange(start,end))
			else:
				_k.append(randrange(start))
		del seed, randrange
		return _k

class lzstr(str):

	def toord(self, gen=True):
		def _s(l):
			for i in l:
				yield ord(i)

		return _s(self) if not gen else lzlist(_s(self))

	@property
	def rot13(self):
		from codecs import encode
		_k = encode(self, 'rot_13')
		del encode
		return lzstr(_k)

	@property
	def reversed(self):
		return lzstr(dc(lzstr(''.join(reversed(list(self))))))

	def remove(self,n):
		from re import sub
		_k = lzstr(sub(str(n), '',self))
		del sub
		return _k

	@property
	def sorted(self):
		return lzstr(''.join(sorted(self)))

	def split_by(self, end):
		return [self[i:i+end] for i in range(0,len(self),end)]

	def fillwith(self,tl,ends='0'):
		return self+ends*(tl-len(self))


class lzdict(dict):
	def __init__(self,ip):
		super().__init__(ip)

	@property
	def swap(self):
		_k = {v:k for k,v in self.items()}
		self.clear()
		super().__init__(_k)
		del _k
		return self

	def get_fromvalue(self,val=None,gen=False):
		if not val:
			val= self.listvalues[0]

		def _s(self,val):
			for count, i in enumerate(self.values()):
				if i==val:
					yield lzlist(self.keys())[count]
			return None

		return _s(self,val) if gen else lzlist(_s(self,val))

	@property
	def lists(self):
		return lzlist([lzlist(self.keys()),lzlist(self.values())])

	@property
	def listkeys(self):
		return lzlist(self.lists[0])

	@property	
	def listvalues(self):
		return lzlist(self.lists[1])

	def randitems(self,i):
		return lzdict({k: v for k, v in lzlist(self.items()).choice(i)})


class lzint(int):
	def __iter__(self):
		return iter(range(self))

	def __len__(self):
		return len(str(self))

	@property
	def isodd(self):
		return self%2==1

	@property
	def iseven(self):
		return self%2==0

	def divisible_by(self,r):
		return self % r==0

	@property
	def percentage(self):
		return str(100*self)+str('%')

	def round_sf(self,l):
		return lzint(lzstr(str(self)[:l]).fillwith(len(self), 0))

	@property
	def reciprocal(self):
		return 1/self

class lzfloat(float):
	def __iter__(self):
		return iter(range(round(self)))

	def __len__(self):
		return len(''.join(str(self).split('.')))

	@property
	def digits_afterzero(self):
		return len(str(self).split('.')[1])

	@property
	def digits_beforezero(self):
		return len(str(self).split('.')[0])

	def significant_figures(self):
		return len(str(self))

	def round_sf(self, l):
		if l>self.digits_beforezero:
			return round(self,l-self.digits_beforezero)
		return lzint(lzstr(str(self)[:l]).fillwith(self.digits_beforezero))
	







