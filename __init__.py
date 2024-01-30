#!/usr/bin/env python
# -*- coding: utf-8 -*-

from binaryninja import PluginCommand, Architecture
from binaryninja import binaryview
from .eravm import EraVM, EraVMView

def is_valid_eravm(view, function=None):
    file_length = view.end
    return file_length % 16 == 0

# PluginCommand.register(
#     'EraVM disassemble',
#     'Zksync era disassemble',

# )

EraVM.register()
EraVMView.register()