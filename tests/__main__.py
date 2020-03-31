import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from lazyloads import lzlist, lzdict, lzstr, lzint, lzfloat
import random

# Allows reproduction
random.seed(1234)
class test_lazyloads(unittest.TestCase):

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
		print('\nFor test DEEPSHUFFLE')
		print('Before shuffle:', test)
		print(f'After shuffle: ', test.deepshuffle())
		self.assertTrue(all([i in var for i in test.deepshuffle()]))

	def test_shuffle(self):
		var=[1,2,3,4,5,6,7,8,9]
		test=lzlist(var)
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
		k = lzlist.mkrandlist(359,
			# start
			100,
			# end
			300,
			#seed
			1234)
		self.assertTrue(len(k)==359)
		self.assertTrue(all([i in range(100,300) for i in k]))


class test_lazystring(unittest.TestCase):
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


class tes_lazydict(unittest.TestCase):
	def test_swap(self):
		var= {1:2,2:3,3:4,4:5}
		test=lzdict(var)
		self.assertEqual(test.swap,{2:1,3:2,4:3,5:4})
		var = {1:'a',2:'b',3:'c'}
		test= lzdict(var)
		self.assertEqual(test.swap,{'a':1,'b':2,'c': 3})

	



if __name__ == '__main__':
	unittest.main()