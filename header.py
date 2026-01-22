from gc import disable
disable()
del disable
from sys import stdout, dont_write_bytecode
stdout.reconfigure(encoding="utf-8")
dont_write_bytecode = True
del dont_write_bytecode
del stdout
del print