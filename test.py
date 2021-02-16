from logger import *

f = 'test.log'
x = Logger(f)

if not Logger_UTILS.fexist(f): x.create()

x.print(0,'Logger initialized')

y = x.get(0)
print(y)

#x.flush()
