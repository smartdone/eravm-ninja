#!/usr/bin/env python
# -*- coding: utf-8 -*-

from binaryninja import (LLIL_TEMP, Architecture, BinaryDataNotification,
                         BinaryView, BranchType, Endianness, InstructionInfo,
                         InstructionTextToken, InstructionTextTokenType, Function,
                         LowLevelILLabel, LowLevelILOperation, RegisterInfo, log_info,
                         SegmentFlag, Symbol, SymbolType, log_debug, Settings, SettingsScope, log)

from .eravmlib import disassemble_one, data_offset

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
        instruction = disassemble_one(addr)
        print(instruction)
        result = InstructionInfo()
        result.length = 4

        return result

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
        log.log_info(f'is_valid_for_data')
        return data.file.original_filename.endswith('.eravm')
    
    def is_executable(self):
        log.log_info(f'is_executable')
        return True
    
    def read_content(self):
        file_size = len(self.raw)
        content_bytes = self.read(0, file_size)
        log.log_info(f'content_bytes={content_bytes}')
        log.log_info(f'byte type={type(content_bytes)}')

    def init(self):
        self.arch = Architecture['EraVM']
        self.platform = Architecture['EraVM'].standalone_platform
        self.max_function_size_for_analysis = 0

        log.log_info(f'arch = {self.arch}')
        log.log_info(f'platform = {self.platform}')

        file_size = len(self.raw)

        log.log_info(f'file_size={file_size}')

        self.read_content()
        
        content_bytes = self.raw.read(0, file_size)

        # add segment
        df = data_offset(content_bytes, file_size)
        df = df * 4
        log.log_info(f'df={df}')
        self.add_auto_segment(0, df, df, file_size-df, SegmentFlag.SegmentReadable | SegmentFlag.SegmentWritable | SegmentFlag.SegmentExecutable)


    def get_entry_point(self):
        log.log_info(f'get_entry_point')
        return 0
    
    def perform_is_executable(self):
        log.log_info(f'perform_is_executable')
        return True
    
    def perform_get_entry_point(self):
        log.log_info(f'perform_get_entry_point')
        return 0