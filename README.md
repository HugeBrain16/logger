# logger

[![GitPack](https://img.shields.io/badge/-GitPack-yellow)](https://github.com/HugeBrain16/logger)  

A logger for logging :/

### Installation
  
from source: `python setup.py install`  
using [GitPack](https://github.com/HugeBrain16/GitPack): `python -m gitpack install HugeBrain16 logger`  

### Example
```py
from logger import Logger

x = Logger('test.log')
x.print(0,'Hello World') # print hello world with `INFO` log code
log_info = x.get(0) # get INFO logs
print(log_info)
```
