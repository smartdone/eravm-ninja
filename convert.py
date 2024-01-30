#!/usr/bin/env python
# -*- coding: utf-8 -*-

import binascii
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python convert_hex.py input.hex output.bin")
        exit(0)

    filename_input = sys.argv[1]
    filename_output = sys.argv[2]

    # 读取hex编码的字符串
    with open(filename_input, 'r') as f:
        hex_data = f.read().replace('\n', '')

    # 移除非十六进制的字符
    hex_data = hex_data.replace('0x', '')

    # 将hex编码的字符串解码为二进制数据
    bin_data = binascii.unhexlify(hex_data)

    # 将二进制数据写入文件
    with open(filename_output, 'wb') as f:
        f.write(bin_data)