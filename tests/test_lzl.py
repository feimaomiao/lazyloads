import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from lzl import lzlist, lzdict, lzstr, lzint, lzfloat
import random

OUTPUTFILE= 'test_output.out'
# Allows reproduction
random.seed(1234)
class test_lzlist(unittest.TestCase):

	def test_basic(self):
		var = [1,2,3,4,'a','b','c','d',['a','b'],{'a','b'}]
		test = lzlist(var)
		self.assertEqual(test, var)


	def test_includetype(self):
		var= [1,2,3,4,'b','c']
		test = lzlist(var)
		self.assertTrue(test.includes_type(int))
		self.assertTrue(test.includes_type(str))
		self.assertFalse(test.includes_type(list))
		self.assertFalse(test.includes_type(lzdict))

	def test_revert(self):
		var= [1,2,3,4,'b','c']
		test= lzlist(var)
		test.clear()
		self.assertEqual(test.revert(), var)
		self.assertEqual(test, var)

	def test_listtypes(self):
		var=[1,2,3,[1,2],'a','b','c']
		test=lzlist(var)
		self.assertEqual(test.list_types, [list,int,str])

	def test_all_index(self):
		var= [1,2,1,2,3,4,3,43,5,4,3,3,2,22,1,3]
		test = lzlist(var)
		self.assertEqual(test.all_index(1),[0,2,14])

	def test_unique(self):
		var=[1,2,1,1,2,1,3,1,4,15,1,2,13,[1,2,3,9]]
		test= lzlist(var)
		self.assertEqual(test.unique,[1,2,3,4,9,13,15])

	def test_split_by(self):
		var=[1,2,3,4,5,6,7,8,9]
		test=lzlist(var)
		self.assertEqual(test.split_by(3),[[1,2,3],[4,5,6],[7,8,9]])
		# split_by function replaces original string
		test.revert()
		self.assertEqual(test.split_by(4),[[1,2,3,4],[5,6,7,8],[9]])

	def test_join_all(self):
		var= [1,[2,[3,[4,[5,[6,[7,[8,[9,10],11],12],13],14],15],16],17],18]
		test=lzlist(var)
		self.assertEqual(test.join_all(),[i for i in range(1,19)])
		# joinall function replaces original string
		self.assertEqual(test,[i for i in range(1,19)])

	def test_similar_to(self):
		var = ['apple','apes','ape','app','application','bape','bang','bong']
		test=lzlist(var)
		self.assertEqual(test.similar_to('ap'),['apple','apes','ape','app','application','bape'])
		self.assertEqual(test.similar_to('^app'),['apple','app','application'])
		self.assertEqual(test.similar_to('b..g'),['bang','bong'])
		self.assertEqual(test.similar_to('^c'),[])

	def test_split_mod(self):
		var=[1,4,7,2,5,8,3,6,9]
		test=lzlist(var)
		self.assertEqual(test.split_mod(3),[[1,2,3],[4,5,6],[7,8,9]])

	def test_split_to(self):
		var=[1,2,3,4,5,6,7,8]
		test=lzlist(var)
		self.assertEqual(test.split_to(2),[[1,2,3,4],[5,6,7,8]])
		test.revert()
		self.assertEqual(test.split_to(3),[[1,2,3],[4,5,6],[7,8]])

	def test_deepshuffle(self):
		var = [1,2,3,4,5,6,[7,8,9,[1,2,3,4]]]
		test=lzlist(var)
		# All values should be the same
		MSGSTRING=f'''\

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For test lzl.deeppshuffle:
Before shuffle: {test}
After shuffle:  {test.deepshuffle()}
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'''
		with open(OUTPUTFILE,'a') as file:
			print(MSGSTRING,file=file)
		self.assertTrue(all([i in var for i in test.deepshuffle()]))

	def test_shuffle(self):
		var=[1,2,3,4,5,6,7,8,9]
		test=lzlist(var)
		MSGSTRING=f'''\

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For test lzlist.shuffle:
Before shuffle: {test}
After shuffle:  {test.shuffle(rp=True)}
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'''
		with open(OUTPUTFILE,'a') as file:
			print(MSGSTRING, file=file)
		self.assertTrue(all([i in test for i in var]))

	def test_choice(self):
		var=[1,2,3,4,5,6,7,8,9,0]
		test=lzlist(var)
		random.seed(1234)
		# self.assertEqual(test.choice(random.randrange(1,10)),_k)
		self.assertTrue(all([i in var for i in test.choice(10)]))
		self.assertTrue(len(test.choice(1010)), 1010)

	def test_type_is_all(self):
		var=[1,2,3,4,5,6,7]
		test=lzlist(var)
		# if value have the same type
		self.assertTrue(test.type_is_all(int))
		self.assertFalse(test.type_is_all(str))
		# if value have different types
		var= [1,2,'3',4,5,6,7]
		test=lzlist(var)
		self.assertFalse(test.type_is_all(int))
		self.assertFalse(test.type_is_all(str))

	def test_type_includes(self):
		var=  [1,2,3,4,5,6,[1,2,3,{4:5},{7}],'4']
		test=lzlist(var)
		# type_includes only checks first layer of lists
		self.assertTrue(test.type_includes(int))
		self.assertTrue(test.type_includes(str))
		self.assertTrue(test.type_includes(list))
		self.assertFalse(test.type_includes(set))
		self.assertFalse(test.type_includes(dict))
		# test for different data types
		var = [{1,2},[3,4]]
		test=lzlist(var)
		self.assertTrue(test.type_includes(set))
		self.assertTrue(test.type_includes(list))
		self.assertFalse(test.type_includes(str))
		self.assertFalse(test.type_includes(int))

	def test_includes(self):
		var= [1,'2',3,[4,5]]
		test=lzlist(var)
		# test for include
		self.assertTrue(test.includes(1))
		self.assertTrue(test.includes('2'))
		self.assertTrue(test.includes(3))
		self.assertTrue(test.includes([4,5]))
		# test for not include
		self.assertFalse(test.includes('1'))
		self.assertFalse(test.includes([4]))
		self.assertFalse(test.includes([4,'5']))

	def test_all_with_type(self):
		var=[1,'2',3,[1,2,3],{1:2},{5},'4',5]
		test=lzlist(var)
		self.assertEqual(test.all_with_type(int),[1,3,5])
		self.assertEqual(test.all_with_type(str),['2','4'])
		self.assertEqual(test.all_with_type(list),[[1,2,3]])
		self.assertEqual(test.all_with_type(dict),[{1:2}])
		self.assertEqual(test.all_with_type(set),[{5}])
		# test for >1 types
		self.assertEqual(test.all_with_type((int,str,list,dict,set)),var)

	def test_all_without_type(self):
		var=[1,'2',3,[1,2,3],{1:2},{5},'4',5]
		test=lzlist(var)
		self.assertEqual(test.all_without_type(int),['2',[1,2,3],{1:2},{5},'4'])
		self.assertEqual(test.all_without_type(list),[1,'2',3,{1:2},{5},'4',5])
		# test for >1 types
		self.assertEqual(test.all_without_type((int,str,list)),[{1:2},{5}])
		self.assertEqual(test.all_without_type((int,str,list,dict,set)),[])

	def test_count_type(self):
		var = [1,'2',[3],{4:'4'},{5},range(6),7,8,'9',{10}]
		test=lzlist(var)
		self.assertEqual(test.count_type(int),3)
		self.assertEqual(test.count_type(str),2)
		self.assertEqual(test.count_type((int,str)),5)

	def test_forall(self):
		import itertools
		var=[1,2,3,4]
		test=lzlist(var)
		# return type is list for function forall instead of tuple
		self.assertEqual(test.forall('pro'),[list(i) for i in itertools.product(var,repeat=2)])
		self.assertEqual(test.forall('product'),[list(i) for i in itertools.product(var,repeat=2)])
		self.assertEqual(test.forall('per'),[list(i) for i in itertools.permutations(var,2)])
		self.assertEqual(test.forall('permuutations'),[list(i) for i in itertools.permutations(var,2)])
		self.assertEqual(test.forall('combinations'), [list(i) for i in itertools.combinations(var,2)])
		self.assertEqual(test.forall('combinations'), [list(i) for i in itertools.combinations(var,2)])
		self.assertEqual(test.forall('combinations_with_replacement'), [list(i) for i in itertools.combinations_with_replacement(var,2)])
		self.assertEqual(test.forall('random words that does not make sense'),[list(i) for i in itertools.combinations_with_replacement(var,2)])
		del itertools

	def test_tostr(self):
		var= [97,98,99]
		test=lzlist(var)
		self.assertEqual(test.tostr,'abc')

		var= [102, 101, 105, 109, 97, 111, 109, 105, 97, 111]
		test=lzlist(var)
		self.assertEqual(test.tostr,'feimaomiao')

		var=[77, 97, 116, 116, 104, 101, 119, 32, 76, 97, 109]
		test=lzlist(var)
		self.assertEqual(test.tostr,'Matthew Lam')

		# test for other languages
		var=[49324, 46993, 54644]
		test=lzlist(var)
		self.assertEqual(test.tostr,'사랑해')

	def test_next(self):
		var=[0,1,2,3,4,5,6,7,8,9]	
		test=lzlist(var)
		self.assertEqual(test.next(0),[1])
		self.assertEqual(test.next(5),[6])

		# Final unit
		self.assertEqual(test.next(9),[0])

		# Default case
		self.assertEqual(test.next() ,[1])

		# Non existense case
		self.assertEqual(test.next('a'),[])

	def test_run_all(self):
		# test function that will be called
		def _t(v=1):
			return lzint(v).iseven

		var = [_t, _t, _t, _t, _t, print, _t, _t]
		test= lzlist(var)
		self.assertEqual(test.run_all([1,3,6],2), [False, True, False, True,False,None, True,False])
		self.assertEqual(test.run_all([0,1,2],v=2),[True,True,True,False,False,None,False,False])

	def test_makerandlist(self):
		test = lzlist.mkrandlist(359,
			# start
			100,
			# end
			300,
			#seed
			1234)
		self.assertTrue(len(test)==359)
		self.assertTrue(all([i in range(100,300) for i in test]))


class test_lzstr(unittest.TestCase):
	def test_toord(self):
		var= 'abcde'
		test=lzstr(var)
		self.assertEqual(test.toord(),[97,98,99,100,101])


		var='feimaomiao'
		test=lzstr(var)
		self.assertEqual(test.toord(),[102, 101, 105, 109, 97, 111, 109, 105, 97, 111])

		var='Matthew Lam'
		test=lzstr(var)
		self.assertEqual(test.toord(),[77, 97, 116, 116, 104, 101, 119, 32, 76, 97, 109])

	def test_rot13(self):
		var='AbCdE'
		test=lzstr(var)
		self.assertEqual(test.rot13,'NoPqR')

		var='1A2b3C'
		test= lzstr(var)
		self.assertEqual(test.rot13, '1N2o3P')

	def test_reversed(self):
		var='abcde'
		test=lzstr(var)
		self.assertEqual(test.reversed, 'edcba')

		var='maL wehttaM'
		test=lzstr(var)
		self.assertEqual(test.reversed, 'Matthew Lam')

	def test_remove(self):
		var='aabbccddeeddffeeccaba'
		test=lzstr(var)
		self.assertEqual(test.remove('aba'),'aabbccddeeddffeecc')
		self.assertEqual(test.remove('dee'),'aabbccdddffeeccaba')
		self.assertEqual(test.remove('^a.+a$'),'')
		self.assertEqual(test.remove('cde'), 'aabbccddeeddffeeccaba')

	def test_sorted(self):
		var='igdedbfcha'
		test=lzstr(var)
		self.assertEqual(test.sorted,'abcddefghi')

	def test_split_by(self):
		var='aaabbbcccdddeeefffggg'
		test=lzstr(var)
		self.assertEqual(test.split_by(3),['aaa','bbb','ccc','ddd','eee','fff','ggg'])
		self.assertEqual(test.split_by(6),['aaabbb','cccddd','eeefff','ggg'])

	def test_fillwith(self):
		var = '111'
		test= lzstr(var)
		self.assertEqual(test.fill(5,'0'), '11100')
		self.assertEqual(test.fill(10,'a'),'111aaaaaaa')

	def test_shuffle(self):
		random.seed(1234)
		var = 'abcdefg'
		test= lzstr(var) 
		MSGSTRING=f'''\

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For test lzstr.shuffle:
Before shuffle: {test}
After shuffle:  {test.shuffle()}
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'''
		random.seed(1234)
		with open(OUTPUTFILE,'a') as file:
			print(MSGSTRING,file=file)
		self.assertTrue(all([i in var for i in test.shuffle()]))

	def test_join_all_ints(self):
		var = 'basdf133.,a/s.dfqwer234ergs你好2qwr8euofidjkls'
		test= lzstr(var)
		self.assertEqual(test.join_all_ints(),13323428)

	def test_sum_of_ints(self):
		var = '阿塞12德法鼓山；1as2;ldkf4jqow12e4ijksf6ba4ksklkf'
		test=lzstr(var)
		# 1+2+1+2+4+1+2+4+6+4 = 27
		self.assertEqual(test.sum_of_ints(),27)


class test_lzdict(unittest.TestCase):

	def test_swap(self):
		var= {1:2,2:3,3:4,4:5}
		test=lzdict(var)
		self.assertEqual(test.swap,{2:1,3:2,4:3,5:4})
		var = {1:'a',2:'b',3:'c'}
		test= lzdict(var)
		self.assertEqual(test.swap,{'a':1,'b':2,'c': 3})

	def test_get_fromvalue(self):
		var= {1:'a',2:'b',3:'c'}
		test=lzdict(var)
		self.assertEqual(test.get_fromvalue('a'),[1])
		var = {1:'a',2:'b',3:'a','a':'a'}
		test= lzdict(var)
		self.assertEqual(test.get_fromvalue('a'),[1,3,'a'])

	def test_lists(self):
		var = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i'}
		test=lzdict(var)
		self.assertEqual(test.lists,[[1,2,3,4,5,6,7,8,9],['a','b','c','d','e','f','g','h','i']])
		self.assertTrue(isinstance(test.lists,(lzlist)))

	def test_listkeys(self):
		var = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i'}
		test=lzdict(var)
		self.assertEqual(test.listkeys, [1,2,3,4,5,6,7,8,9])
		self.assertTrue(isinstance(test.listkeys,(lzlist)))

	def test_listvalues(self):
		var = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i'}
		test=lzdict(var)
		self.assertEqual(test.listvalues,['a','b','c','d','e','f','g','h','i'])
		self.assertTrue(isinstance(test.listvalues,(lzlist)))

	def test_randitems(self):
		var = {1:'a',2:'b',3:'c',4:'d'}
		test=lzdict(var)
		_l = random.randrange(1,10)
		MSGSTRING=f'''\

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For test lzdict.randitems:
Random items will not duplicate therefore the length will not be equal
Full dict: {test}
Random item amount: {_l}
Random items: {test.randitems(_l)}
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'''
		with open(OUTPUTFILE,'a') as file:
			print(MSGSTRING,file=file)
		self.assertTrue(all([i in var for i in test.randitems(_l)]))

	def test_find_inkeys(self):
		var = {'abcde':'true1','apple':'false1','aberaham':'true2','amplitude':'false2'}
		test= lzdict(var)
		self.assertEqual(test.find_inkeys('^ab'),{'abcde':'true1','aberaham':'true2'})
		self.assertEqual(test.find_inkeys('^a.+e$').listvalues,['true1','false1','false2'])

	def test_find_invalues(self):
		var= {'true1':'text1','false1':'text2','true2':'case1','false2':'case2'}
		test=lzdict(var)
		self.assertEqual(test.find_invalues('1$'),{'true1':'text1','true2':'case1'})
		self.assertEqual(test.find_invalues('^case').listkeys,['true2','false2'])

class test_lzint(unittest.TestCase):

	def test_iter(self):
		var = 10
		test = lzint(var)
		val = 0
		for i in test:
			val += 1
		self.assertEqual(val,10)
		self.assertTrue(1 in test)

	def test_len(self):
		var = 101010
		test= lzint(var)
		self.assertEqual(len(test),6)

	def test_isodd(self):
		var = 101010
		test=lzint(var)
		self.assertFalse(test.isodd)
		test += 1
		self.assertTrue(lzint(test).isodd)

	def test_iseven(self):
		var = 101011
		test = lzint(var)
		self.assertFalse(test.iseven)
		test = lzint(test + 1)
		self.assertTrue(test.iseven)

	def test_divisible_by(self):
		var = 12
		test= lzint(var)
		self.assertTrue(test.divisible_by(3))
		self.assertTrue(test.divisible_by(4))
		self.assertFalse(test.divisible_by(5))

	def test_round_sf(self):
		var = 1555155
		test= lzint(var)
		self.assertEqual(test.round_sf(1),2000000)
		self.assertEqual(test.round_sf(2),1600000)
		self.assertEqual(test.round_sf(4),1555000)

	def test_reciprocal(self):
		var = 100
		test=lzint(var)
		self.assertEqual(test.reciprocal,0.01)

class test_lzfloat(unittest.TestCase):
	def test_len(self):
		var = 10.1002
		test=lzfloat(var)
		self.assertEqual(len(test),6)
		test= lzfloat(1234.123123)
		self.assertEqual(len(test),10)

	def test_digits_beforezero(self):
		var = 12345.6789
		test=lzfloat(var)
		self.assertEqual(test.digits_beforezero,5)

	def test_digits_afterzero(self):
		var = 12345.678912345
		test=lzfloat(var)
		self.assertEqual(test.digits_afterzero,9)

	def test_significant_figures(self):
		var= 00000.0123000
		test=lzfloat(var)
		self.assertEqual(test.significant_figures,3)

	def test_round_sf(self):
		var = 151515.151515
		test=lzfloat(var)
		self.assertEqual(test.round_sf(1),200000.0)
		self.assertEqual(test.round_sf(2),150000.0)
		self.assertEqual(test.round_sf(7),151515.2)
		self.assertEqual(test.round_sf(8),151515.15)



		