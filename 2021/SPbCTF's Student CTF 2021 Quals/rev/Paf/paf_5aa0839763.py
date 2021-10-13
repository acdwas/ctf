
from unicorn import *
from unicorn.x86_const import *
from capstone import *
from capstone.x86 import *

import struct

def read(name):
    with open(name, 'rb') as f:
        return f.read()
        
def u64(data):
    return struct.unpack("<Q", data)[0]
    
def p64(num):
    return struct.pack("<Q", num)


mu = Uc(UC_ARCH_X86, UC_MODE_64)
cs = Cs(CS_ARCH_X86, CS_MODE_64)

BASE = 0x400000
STACK_ADDR = 0x0
STACK_SIZE = 1024*1024*2

mu.mem_map(BASE, 1024*1024*2)
mu.mem_map(STACK_ADDR, STACK_SIZE)

mu.mem_write(BASE, read("./paf_5aa0839763.elf"))
mu.reg_write(UC_X86_REG_RSP, STACK_ADDR)

FLAG = ''

def hook_code(mu, address, size, user_data):  
    code = mu.mem_read(address, size)
    global FLAG
    # for i in cs.disasm(code, size):
        # print("0x%x 0x%x:\t%s\t%s" %(address,i.address, i.mnemonic, i.op_str))
    if address == 0x401d6a:
        mu.reg_write(UC_X86_REG_R8,2)
        r_8 = mu.reg_read(UC_X86_REG_R8)
    if address == 0x401d7e:
        r_rax = mu.reg_read(UC_X86_REG_RAX)
        FLAG += bytes.fromhex(hex(r_rax)[2:])[::-1].decode()
        mu.reg_write(UC_X86_REG_R10, STACK_ADDR)
        mu.mem_write(STACK_ADDR, p64(r_rax))
    if address == 0x401d8d:
        r_rax = mu.reg_read(UC_X86_REG_RAX)
        FLAG += bytes.fromhex(hex(r_rax)[2:])[::-1].decode()
        mu.reg_write(UC_X86_REG_R10, STACK_ADDR)
        mu.mem_write(STACK_ADDR + 8, p64(r_rax))

mu.hook_add(UC_HOOK_CODE, hook_code)

mu.emu_start(0x400080, 0x401dab)

print(FLAG)

