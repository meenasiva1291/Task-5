from functools import reduce
list_ = [10,20,30,40,50,60]
#reduce() performs a repetitive operation over the pairs of the iterable
mul_num = reduce(lambda x,y:x*y,list_)
print(mul_num)
