#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform
from ctypes import cdll, c_char_p, c_ulonglong

current_file_path = os.path.abspath(__file__)
current_dir_path = os.path.dirname(current_file_path)

os_name = platform.system()

lib_name = 'liberavm.dylib'

if os_name == 'Darwin':
    lib_name = 'liberavm.dylib'
elif os_name == 'Linux':
    lib_name = 'liberavm.so'
elif os_name == 'Windows':
    lib_name = 'liberavm.dll'

lib_path = os.path.join(current_dir_path, lib_name)

lib = cdll.LoadLibrary(lib_path)
lib.disassemble_one.argtypes = [c_ulonglong]
lib.disassemble_one.restype = c_char_p

def disassemble_one(addr):
    return lib.disassemble_one(addr).decode('utf-8')

# x = disassemble_one(0x0000008003000039)
# print(x)