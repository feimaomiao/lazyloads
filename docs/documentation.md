# Welcome to the documentation
## Usage  
The prerequisite for all code down below is like this
```python  
from lzl import *  
from random import shuffle, seed
>>[.......'lzdict', 'lzfloat', 'lzint', 'lzlist', 'lzstr', 'shuffle','seed']  
```    
##Some important ideas to clarify  
- property
> A property in a class in python is like a value in class. 
> It works like a value instead of a function.
- replace
> Some of the functions have specifications that it *replaces* itself
> These would only happen in *mutable* types like lzdict and lzlist
> It converts the object itself to the new values.

## Here are the objects down below

### lzlist object  
```python  
llist = lzlist([1,2,3])  
# Because lzlist is a subclass of list, lzlist and list objects are comparable.  
llist == [1,2,3]  
>>True  
# All functions that work on list will also work on lzlist object  
llist.append(4)  
print(llist)  
>>[1,2,3,4]  
```  
- includes_type(type)  
> Checks if the lzlist object includes a type  
```python  
lzlist([1,2,3,'a','b']).includes_type(int)  
>> True  
# Multiple values can be passed with a tuple  
lzlist([1,2,3,'a','b']).includes_type((int,str))  
>> True  
lzlist([1,2,3,'a','b']).includes_type(bool)  
>> False  
```  
- revert()  
>Reverses the list to the original form when you inputted it.  
>*replaces the list*  
```python  
llist = lzlist([1,2,3,4,5,6,7,8,9])  
seed(1234)  
shuffle(llist)  
llist.append([1,2,3])  
print(llist)  
>>[9, 4, 3, 6, 5, 7, 1, 2, 8, [1, 2, 3]]  
llist.revert()  
>>[1,2,3,4,5,6,7,8,9]  
print(llist)  
>>[1,2,3,4,5,6,7,8,9]  
```  
- listtypes   
> lists all __unique__ types that occurs in the list  
 >is a *property*  
```python  
llist = lzlist([1,2,'a'])  
llist.list_types  
>> [int, str]  
```  
- all_index(val)  
> returns all indexes that  have the exact value as value  
> works like `list.index(val)` but returns a list instead of one value only.  
> returns a *list*  
```python  
llist = lzlist([1,2,1,'1',1])  
llist.all_index(1)  
>>[0,2,4]  
llist.all_index('1')  
>>[3]  
```  
- unique  
> returns all unique items in the list  
> is a *property*  
```python  
llist = lzlist([1,2,1,2,1,3,1,4,1,5,1,6,'1'])  
llist.unique  
>> [1,2,3,4,5,6,'1']  
```  
- split_by(val)  
> splits the values in the list by the `val` argument  
```python  
llist = lzlist([1,2,3,4,5,6,7,8,9])  
llist.split_by(3)  
>> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
```  
- join_all()  
>  turns 2-D or 3-D array into a list  
>  *replaces the list*  
```python  
llist = lzlist([[1,2],[3,4],[5,6],7,8,9,[10,11,[12,13],14]])  
llist.join_all()  
>>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  
llist  
>>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  
```  
- similar_to(sstr)  
> searchs for anything that is similar to the search string  
> Can use regex searches for sstr  
> searches for multiple data types  
> returns a *list*  
```python  
llist = lzlist(['12345',12535,'15542',177345,'10987657'])  
# regex search  
llist.similar_to('^12.+5$')  
>> ['12345', 12535]  
```  
- split_mod(groups)  
> returns a 2-D array, the first item in the original list goes to the first slot, the second item goes to the second one.  
> *replaces the original list*  
```python  
llist = lzlist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])  
llist.split_mod(7)  
>> [[1, 8], [2, 9], [3, 10], [4, 11], [5, 12], [6, 13], [7, 14]]  
llist.revert()  
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  
llist.split_to(2)  
>> [[1, 3, 5, 7, 9, 11, 13], [2, 4, 6, 8, 10, 12, 14]]  
```  
- split_to(grps)  
> splits the list into given amount of groups  
> It follows the order  
> *replaces the original list*  
```python  
llist = lzlist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])  
llist.split_to(grps=2)  
>> [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]]  
llist  
>> [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]]  
```  
- deepshuffle(replace=True)  
> shuffles the list and every inner list inside  
> replaces the original list if `replace` is set to True  
```python  
seed(1235)  
llist = lzlist([[1,2,3],[4,5,6],[7,8,9]])  
llist.deepshuffle(False)  
>>[[8, 9, 7], [1, 2, 3], [5, 6, 4]]  
llist  
>> [[1,2,3],[4,5,6],[7,8,9]]  
llist.deepshuffle()  
>> [[6, 4, 5], [1, 2, 3], [7, 9, 8]]  
llist  
>> [[6, 4, 5], [1, 2, 3], [7, 9, 8]]  
# The deepshuffle also works for deeper lists  
seed(1999)  
llist = lzlist([[1,[2,3],4,[5,6]],[[4,5],6,7,[8,9]],[7,[8,9],1,[2,3]]])  
llist.deepshuffle()  
>> [[[8, 9], 1, 7, [3, 2]], [[8, 9], 7, [5, 4], 6], [1, [6, 5], [2, 3], 4]]  
```  
- shuffle(rp=False)  
> works like random.shuffle()  
> Replaces the original list if `rp` is set to true.  
> Does not work in deeper lists  
```python  
seed(123)  
llist = lzlist([[1,2,3],[4,5,6],[7,8,9]])  
llist.shuffle()  
 >> [[4, 5, 6], [7, 8, 9], [1, 2, 3]]  
llist  
 >> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
llist.shuffle(True)  
 >> [[4, 5, 6], [1, 2, 3], [7, 8, 9]]  
llist  
 >> [[4, 5, 6], [1, 2, 3], [7, 8, 9]]  
```  
- choice(amount)  
> works like random.choice with different amount  
```python  
seed(1234)  
llist = lzlist([1,2,3])  
llist.choice(2)  
>> [3, 2]  
llist.choice(30)  
>> [1, 3, 3, 2, 3, 1, 3, 1, 1, 3, 2, 2, 2, 1, 1, 1, 1, 2, 3, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2]  
```  
- type_is_all(t)  
> Checks if all values in the list is t  
```python  
llist = lzlist([1,2,3])  
llist.type_is_all(int)  
>> True  
llist = lzlist([1,2,'3'])  
llist.type_is_all(str)  
>> False  
# However, there is a workaround for this function  
llist.type_is_all((str,int))  
```  
- type_includes(t)  
> Checks if any of the values is type t  
```python  
llist = lzlist([1,2,'3'])  
llist.type_includes(str)  
>> True  
llist.type_includes(float)  
>> False  
llist.type_includes((str,int))  
>> True  
```  
- includes(t)  
> Checks if t is in list  
```python  
llist = lzlist([1,2,'3'])  
llist.includes('3')  
>> True  
llist.includes(3)  
>> False  
```  
- all_with_type(t)  
> returns a list with only the type of t  
```python  
llist = lzlist([1,2,'3',4,5,6,'7','8','9'])  
llist.all_with_type(int)  
>> [1, 2, 4, 5, 6]  
llist.all_with_type(str)  
>> ['3', '7', '8', '9']  
llist.all_with_type(list)  
>> []  
llist.all_with_type((int,str))  
>> [1, 2, '3', 4, 5, 6, '7', '8', '9']  
```  
- all_without_type(t)  
> returns a list without type t  
```python  
llist = lzlist(['a','b',1,2,3,[1,2]])  
llist.all_without_type(str)  
>>[1, 2, 3, [1, 2]]  
llist.all_without_type(float)  
>>['a', 'b', 1, 2, 3, [1, 2]]  
llist.all_without_type((str,list))  
>>[1, 2, 3]  
```  
- count_type(t)  
> Counts how many  values in list is type t  
```python  
llist = lzlist(['a','b',1,2,3,[1,2]])  
llist.count_type(int)  
>> 3  
llist.count_type(str)  
>> 2  
llist.count_type(float)  
>> 0  
llist.count_type((int,str))  
>> 5  
```  
- forall(t='product')  
> building itertools into lzlist by itself.  
> for more docs go visit the [website](https://docs.python.org/2/library/itertools.html#itertools.product)  
```python  
llist = lzlist([1,2,3])  
llist.forall('product')# Or anything that starts with 'pr'  
>> [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]  
llist.forall('permutations')# or anything that starts with 'pe'  
>> [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]  
llist.forall('combinations') # Or anything that starts with 'c' and ends with 's'  
>> [[1, 2], [1, 3], [2, 3]]  
llist.forall('combinations_with_replacements') # Or anything else  
>> [[1, 2], [1, 3], [2, 3]]  
```  
- tostr  
> Function that changes all the int or float object in the list into a string  
> Uses the function chr()  
> Is a  *property*  
```python  
llist= lzlist([97,98,99,100])  
llist.tostr  
>> 'abcd'  
llist = lzlist(['a','b','c'])  
llist.tostr  
>> ''  
```  
- next(askval=None)  
> Returns a list of items where it is the next value of `askval`  
```python  
llist = lzlist(['a','b','c','a','c','b'])  
llist.next('a')  
>> ['b', 'c']  
llist.next('b')  
>> ['c', 'a']  
llist.next()  
# Searchs for the first item in list  
>> ['b', 'c']  
```  
- before(askval=None)  
> Returns a list of items where it is the item before `askval`  
```python  
llist = lzlist([1,2,3,1,3,2])  
llist.before(1)  
>>[2, 3]  
llist.before(2)  
>>[1, 3]  
```  
- run_all(*args, **kwargs)  
> Runs all functions that is in the list  
```python   
llist = lzlist([print, print])  
llist.run_all(  
# arg 1 must be the index where args are provided  
[0],  
# after that could be the args that is just provided  
'hello',  
# positional arguments could be provided too  
end='///'  
)  
# Hello from the print in index position 0  
>> 'hello///'  
>>   
# The empty line is because of the print in index position 1  
```  
- mkrandlist(length, start=None,end=None,sd=None)  
> Generates a list with random numbers  
> Length is the length of the random list generated  
> Start and end is the randrange of numbers  
> Default values is 100  
> If you put in one number it would be the randrange() number  
```python  
seed(123)  
lzlist().mkrandlist(10,  
#start  
20,  
# end  
100)  
[61, 33, 57, 94, 46, 99, 20, 47, 92, 77]  
```  
- \_\_hash__()  
> lzlist object is hashable.  
```python  
hash(lzlist([1,2,3]))  
>> 661977612421174894  
```  
### lzstr object  
Because str is an immutable type in python, there could be no function that changes the basis of lzstr object.  
```python  
lstr = lzstr('abcde')  
# Normal functions can still be used  
lstr.find('a')  
>> 0   
```  
- toord()  
> Returns a lzlist object which is an array of the ascii code of each character  
```python  
lstr = lzstr('abcdefg')  
lstr.toord()  
[97, 98, 99, 100, 101, 102, 103]  
```  
- rot13  
> rot-13 shifts the character by 13 units.   
> Case is preserved  
> Is a *property*  
```python  
lstr = lzstr('ABCdenoPQ')  
lstr.rot13  
>> 'NOPqrabCD'  
```  
- reversed  
> reversed returns a reversed string of self  
> is a *property*  
```python  
lstr = lzstr('abcdefg')  
lstr.reversed  
>> 'gfedcba'  
```  
- remove(n)  
> return a string without the character or character set n  
> n can be a regex search case  
```python  
lstr=lzstr('this is an actual thing')  
lstr.remove('i(s|n)')  
>> 'th  an actual thg'  
lstr.remove('a(n|c)')  
>> 'this is  tual thing'  
```  
- sorted  
> sorts the string and returns the string  
> this is a *property*  
```python  
lstr = lzstr('this is an actual thing')  
lstr.sorted  
>> '    aaacghhiiilnnsstttu'  
```  
- split_by(end)  
> splits the string into 2-d arrays  
```python  
lstr = lzstr('aaabbbcccdddeee')  
lstr.split_by(3)  
>> ['aaa', 'bbb', 'ccc', 'ddd', 'eee']  
```  
- fill(tl,ends='0')  
> fills the string at the end.  
> `ends` does not have to be a string  
> Like zfill() function but ends at the end  
```python  
lstr= lzstr('11100')  
lstr.zfill(8)  
>> '00011100'  
lstr.fill(8)  
>> '11100000'  
lstr.fill(8,1)  
>> '11100111'  
```  
- shuffle()  
> shuffles the string and returns a shuffled string  
```python  
seed(123)  
lstr = lzstr('abcde')  
lstr.shuffle()  
>> 'ecadb'  
```  
- join_all_ints()  
> joins all the integers in the string and return an int  
```python  
lstr = lzstr('abc12wwerdfffhu7654efbhrfg4')  
lstr.join_all_ints()  
>> 1276544  
```  
- sum_of_ints()  
> finds the sum of all integers in the string  
```python  
lstr= lzstr('123rewdfsfdfg43wdffr3e')  
lstr.sum_of_ints()  
>> 16  
```  
- randstring(l)  
> creates a random string with numbers and characters  
> l is the length of the string  
>*static method*  
```python  
seed(1234)  
lzstr().randstring(100)  
>> '9XChaf688ZLcQSfgXwpbbYbwPNENDjflTh2aGF49peQI6DeMRfGLcr0JePtE2wrpP7mD4HQb8GeavjTEQykdeLFkeJnjb7wXh9Hj'  
lzstr().randstring(15)  
>> 'QtDcArQZclrjt92'  
```  
### lzdict object  
`dicts` are mutable objects. A lot more functionalities are allowed.  
```python  
ldict = lzdict({1:'a'})  
ldict.get(1)  
>> 'a'  
```  
- swap  
> returns a dictionary that the keys is swapped from the value  
> dict keys must be unique. Therefore, any duplicated values would lead to a corrupted dictionary  
> swap is a *property*  
```python  
ldict = lzdict({1:'a',2:'b',3:'c'})  
ldict.swap  
>> {'a': 1, 'b': 2, 'c': 3}  
ldict = lzdict({1:'a',2:'a',3:'a'})  
ldict.swap  
>> {'a': 3}  
```  
- get_fromvalue(val=None)  
> returns the key(s) where the value paird is val  
> if val is not provided it will be changed to the first value of the dictionary.  
```python  
ldict = lzdict({1:2,3:4,5:2,6:4,7:8})  
ldict.get_fromvalue(2)  
>> [1, 5]  
ldict.get_fromvalue(8)  
>> [7]  
ldict.get_fromvalue(7)  
>> []  
```  
- lists, listkeys, listvalues  
> as the keys() and values() both return non-iterable object, lists converts it to an iterable list object  
> all of them are *properties*  
```python  
ldict = lzdict({1:2,3:4,5:2,6:4,7:8})  
ldict.lists  
>> [[1, 3, 5, 6, 7], [2, 4, 2, 4, 8]]  
ldict.listkeys  
>> [1, 3, 5, 6, 7]  
ldict.listvalues  
>> [2, 4, 2, 4, 8]  
```  
- randitems(i)  
> returns a dictionary filled with random items from the dictionary  
> The length could be not matching argument `i` as dicts cannot repeat its values.  
```python  
ldict = lzdict({1:2,3:4,5:2,6:4,7:8})  
ldict.randitems(2)  
>> {1: 2, 7: 8}  
ldict.randitems(3)  
>> {1: 2, 3: 4}  
```  
- find_inkeys(searchstring)  
> Searches in the dictionary keys with regex search   
>  returns a dict which fits the regex search  
```python  
ldict = lzdict({'alabama':10000000,'california':15234200,'new york':152349203, 'washington': 152342410,'alaska':12412424,'Arizona':1252131123})  
ldict.find_inkeys('^[a|A]la.{3}$')  
>> {'alaska': 12412424}  
ldict.find_inkeys('^[a|A]la.{3}$')  
>> {'alabama': 10000000, 'alaska': 12412424}  
ldict.find_inkeys('al')  
>> {'alabama': 10000000, 'california': 15234200, 'alaska': 12412424}  
```  
- find_invalues(searchstring)  
> Searches in the dictionary values with regex search  
> returns a dict which fits the regex search  
```python  
ldict = lzdict({'matthew': 'golden membership', 'Lucinda Cope': 'silver membership', 'Kavita Mcpherson': 'normal player'})  
ldict.find_invalues('membership$')  
>> {'matthew': 'golden membership', 'Lucinda Cope': 'silver membership'}  
ldict.find_invalues('er')  
>> {'matthew': 'golden membership', 'Lucinda Cope': 'silver membership', 'Kavita Mcpherson': 'normal player'}  
```  
- \_\_hash__()  
> hash is implemented in the lzdict object  
```python  
ldict = lzdict({'alabama':10000000,'california':15234200,'new york':152349203, 'washington': 152342410,'alaska':12412424,'Arizona':1252131123})  
hash(ldict)  
>> 2152418949226078860  
```  
### lzint object  
int is not a mutable object. Not many funcitonalities could be implemented.  
- \_\_iter__()  
> Even though `int` is not iterable, lzint is iterable.  
> It yields the range from 0 to itself.  
> Works for negative numbers  
```python  
for i in lzint(3):  
	print(i)  
  
>> 0  
>> 1  
>> 2  
  
for i in lzint(-3):  
	print(i)  
  
>> 0  
>> -1  
>> -2  
```  
- \_\_len__()  
> returns the length of the int  
```python  
len(lzint(12345))  
>> 5  
len(lzint(144))  
>> 3  
```  
- ispositive  
> *property* to check if the integer is positive  
```python  
lzint(12345).ispositive  
>> True  
lzint(-1234).ispoitive  
>> False  
lsint(1).ispostive  
>> True  
```  
- iseven  
> Checks if the number is even.   
> is a *property*  
```python  
lzint(124).iseven  
>> True  
lzint(121).iseven  
>> False  
```  
- isodd  
> Checks if the number is odd  
> is a *property*  
```python  
lzint(124).isodd  
>> False  
lzint(121).isodd  
>> True  
```  
- divisible_by(other)  
> check if self could be divided by `other` without remainders  
```python  
lzint(12).divisible_by(3)  
>> True  
lzint(12).divisible_by(10)  
>> False  
```  
- round_sf(l)  
> rounds the integer to a certain significant figures  
```python  
lzint(1551).round_sf(2)  
>> 1600  
lzint(1551).round_sf(3)  
>> 1550  
```  
- reciprocal  
> *property* that returns the reciprocal of self  
```python  
lzint(100).reciprocal  
>> 0.01  
lzint(123).reciprocal  
>> 0.008130081300813009  
```  
### lzfloat object  
float is another immutable object and many functions couldn't be worked.   
- \_\_iter__()  
> rounds the range of closest number  
```python  
for i in lzfloat(2.4):  
	print(i)  
>> 0  
>> 1  
for i in lzfloat(2.6):  
	print(i)  
>> 0  
>> 1  
>> 2  
```  
- \_\_len__()  
> returns the length of the float number  
```python  
len(lzfloat(1.234))  
>> 4  
len(lzfloat(123.234))  
>> 6  
```  
- digits_beforezero  
> returns the length of the integer before decimal point  
> is a *property*  
```python  
lzfloat(142.1234).digits_beforezero  
>> 3  
lzfloat(0.12351).digits_beforezero  
>> 0  
```  
- digits_afterzero  
> returns the length of the integer after the decimal point  
> is a *property*  
```python  
lzfloat(142.1234).digits_afterzero  
>> 4  
lzfloat(0.12351).digits_afterzero  
>> 5  
```  
- significant_figures  
> returns the significant figure of such float   
> is a *property*  
```python  
lzfloat(123.1234).significant_figures  
>> 7  
lzfloat(0.0123).significant_figures  
>> 3  
```  
- round_sf(l)  
> rounds the float to `l`, the given significant figure  
```python  
lzfloat(155.1236).round_sf(6)  
>> 155.124  
lzfloat(155.1236).round_sf(2)  
>> 160.0  
# when you round a float it returns a float   
lzfloat(0.153337).round_sf(1)  
>> 0.2  
lzfloat(0.153337).round_sf(0)  
>> 0.0  
```  
###### lazyloads, a python module to make your life easier  
###### © 2020 Matthew Lam