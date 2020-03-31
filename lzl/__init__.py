from copy import deepcopy as _dc
import time
from random import seed as _seed ,randrange as _randrange ,sample as _sample
from random import shuffle as _shuffle, choice as _choice
from itertools import product as _product, permutations as _permutations
from itertools import combinations as _combinations,combinations_with_replacement as _combinations_with_replacement
from hashlib import sha512 as _sha512
from math import ceil as _mceil
from string import ascii_letters as _ascii_chars, digits as _digs
from re import search as _se
_seed(time.time()*_randrange(1234,123456789))
del time

__all__ = ['lzlist','lzstr','lzdict','lzint','lzfloat']
__author__  = 'Matthew Lam'
__email__   = 'lcpmatthew@gmail.com'
__version__ = '0.0.1'   
__license__ = 'MIT'

class lzlist(list):
	def __init__(self, ip=[]):
		super().__init__(ip)
		self.__copy = ip

	def __hash__(self):
		_h = _sha512()
		[_h.update(str(i).encode('utf-32')) for i in self]
		return _h.hexdigest()

	def includes_type(self,tp):
		try:
			return lzlist([i for i in self if type(i) == tp])
		except NameError:
			return None

	def revert(self):
		super().__init__(_dc(self.__copy))
		return self 
	

	@property
	def list_types(self):
		return list(set([type(i) for i in self]))

	def all_index(self,val):
		return lzlist([count for count, value in enumerate(self) if value==val])

	@property
	def unique(self):
		_tmp = _dc(self)
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
				if issubclass(type(i), list):
					_o += i 
				else:
					_o.append(i)
			super().__init__(_dc(_o))
		return self

	def similar_to(self, sstr):
		_r = []
		for i in self:
			_t = type(i)
			if _t == list:
				continue
			try:
				_r.append(_t(_se(f'^.*{str(sstr)}.*$', str(i)).group(0)))
			except AttributeError:
				continue
		return lzlist(_r)

	def split_mod(self, grps):
		_gp = [[] for i in range(grps)]
		_l = _dc(self)
		for count, i in enumerate(_l):
			_gp[count%grps].append(i)
		del _l
		super().__init__(_gp)
		return self

	def split_to(self, grps):
		_g = _mceil(len(self)/grps)
		super().__init__([self[i:i+_g] for i in range(0,len(self),_g)])
		return self

	def deepshuffle(self,replace=True):
		def _s(l):
			_shuffle(l)
			for i in l:
				_shuffle(l)
				if isinstance(i, list):
					_shuffle(i)
					_s(i)
			_shuffle(l)
			return l

		if replace:
			_k = _s(_s(self))
		else:
			_k = _dc(self)
			_k = _s(_s(_k))
		return lzlist(_k)

	def shuffle(self,rp=False):
		k = _dc(self)
		[_shuffle(k) for i in lzint(_randrange(100))]
		if rp:
			super().__init__(_dc(k))
		return lzlist(k)

	def choice(self,amount):
		return lzlist(_sample((lzlist(self* (amount if amount>len(self) else 1)).join_all().shuffle()),amount))

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
		if t.startswith('pr'):
			_k = list([list(i) for i in _product(self,repeat=2)])
		elif t.startswith('pe'):
			_k = list([list(i) for i in _permutations(self,2)])
		elif t.startswith('c') and t.endswith('s'):
			_k = list([list(i) for i in _combinations(self,2)])
		else:
			_k = list([list(i) for i in _combinations_with_replacement(self,2)])
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

	def run_all(self,*args,**kwargs):
		try:
			margs = list(args)[0]
		except IndexError:
			margs = []
		try:
			others= tuple(args[1:]) if len(args) > 1 else ()
		except IndexError:
			others= ()
		if any([not callable(i) for i in self]):
			return
		return [self[i](*others, **kwargs) if i in margs else self[i]() for i in range(len(self))]

	@staticmethod
	def mkrandlist(length,start=None,end=None,sd=None):
		if sd:
			_seed(sd)
		if not start and end:
			start=end
			end= None
		if not start:
			start=100
		_k=lzlist([])
		for i in lzint(length):
			_seed(_randrange(0,_randrange(10000000000)))
			if start and end:
				_k.append(_randrange(start,end))
			else:
				_k.append(_randrange(start))
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
		return lzstr(_dc(lzstr(''.join(reversed(list(self))))))

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

	def fill(self,tl,ends='0'):
		return self+str(ends)*(tl-len(self))

	def shuffle(self):
		_k=lzlist(self)
		_k.shuffle(rp=True)
		return ''.join(_k)

	@staticmethod
	def randstring(l):
		return ''.join([_choice(_ascii_chars+_digs) for i in lzint(l)])


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

	def get_fromvalue(self,val=None):
		if not val:
			val= self.listvalues[0]

		def _s(self,val):
			for count, i in enumerate(self.values()):
				if i==val:
					yield lzlist(self.keys())[count]
			return None

		return lzlist(_s(self,val))

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
		if i>len(self):
			return self
		return lzdict({k: v for k, v in lzlist(self.items()).choice(i)})

	def find_inkeys(self,searchstring):
		_r = lzlist()
		for i in self.listkeys:
			_t = type(i)
			try:
				_r.append(_t(_se(f'^.*{str(searchstring)}.*$',str(i)).group(0)))
			except AttributeError:
				continue
		return lzdict({i:self[i] for i in _r})

	def find_invalues(self,searchstring):
		_r = lzlist()
		for i in self.listvalues:
			_t = type(i)
			try:
				_r.append(_t(_se(f'^.*{str(searchstring)}.*$',str(i)).group(0)))
			except AttributeError:
				continue
		return {i:self[i] for i in lzlist([self.get_fromvalue(i) for i in _r]).join_all()}

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
		print(10**(self.digits_beforezero-l))
	






