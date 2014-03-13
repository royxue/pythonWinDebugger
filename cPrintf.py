from ctypes import *
#run c printf
msvcrt=cdll.msvcrt
message="Hello World \n"
msvcrt.printf("I Say %s",message)

#
seize=c_char_p("hello")
print seize
print seize.value

class struc(Structure):
	_fields_=[
	('a',c_int),
	('b',c_int)
	]
str_test=struc(2,4)
print str_test.a,str_test.b

class unio(Union):
	_fields_=[
	("c",c_long),
	("a", c_int),
	("b", c_char*4)
	]
value=raw_input('Input a value:')
my_unio=unio(int(value))
print "Union test Output %d"%my_unio.a 
print "Union test Output %s"%my_unio.b