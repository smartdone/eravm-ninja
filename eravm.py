#!/usr/bin/env python
# -*- coding: utf-8 -*-

from binaryninja import (LLIL_TEMP, Architecture, BinaryDataNotification,
                         BinaryView, BranchType, Endianness, InstructionInfo,
                         InstructionTextToken, InstructionTextTokenType, Function,
                         LowLevelILLabel, LowLevelILOperation, RegisterInfo, log_info,
                         SegmentFlag, Symbol, SymbolType, log_debug, Settings, SettingsScope, log)

class EraVM(Architecture):
    name = "EraVM"

    address_size = 32
    default_int_size = 32
    instr_alignment = 1
    max_instr_length = 33

    endianness = Endianness.BigEndian

    regs = {
        "sp": RegisterInfo("sp", 32),
    }

    stack_pointer = "sp"

    def get_instruction_info(self, data, addr):
        log.log_info(f'get_instruction_info data={data}, addr={addr}')
        print(data, addr)

    def get_instruction_text(self, data, addr):
        log.log_info(f'get_instruction_text data={data}, addr={addr}')
        print(data, addr)

    def get_instruction_low_level_il(self, data, addr, il):
        log.log_info(f'get_instruction_low_level_il data={data}, addr={addr}')
        print(data, addr)

class EraVMView(BinaryView):
    name = "EraVM"
    long_name = "Zksync era Bytecode"

    def __init__(self, data):
        BinaryView.__init__(self, parent_view=data, file_metadata=data.file)
        self.raw = data

    @staticmethod
    def is_valid_for_data(data):
        return data.file.original_filename.endswith('.eravm')
    
    def is_executable(self):
        return True
    
    def init(self):
        self.arch = Architecture['EraVM']
        self.platform = Architecture['EraVM'].standalone_platform
        self.max_function_size_for_analysis = 0

        file_size = len(self.raw)

        log.log_info(f'file_size={file_size}')

    def get_entry_point(self):
        return 0