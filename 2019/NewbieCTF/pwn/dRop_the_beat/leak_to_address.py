
from pwn import u32, u64, p32, p64


class Leak_address():
    def __init__(self, leak, bits, lenght=0):
        self.leak = leak
        self.lenght = lenght
        self.xxx = []
        if bits == 64:
            self.leak64()
        else:
            self.leak32()

    def leak64(self):
        if len(self.leak[self.lenght:]) > 0:
            s = self.leak[self.lenght:]
            if len(s) % 8 == 0:
                l = []
                for x in range(0, len(s), 8):
                    pp = hex(u64(s[x:x + 8]))
                    if len(pp[2:]) % 8 == 0:
                        if len(pp[2:]) == 16:
                            l.append(pp)
                        else:
                            l.append('0x00000000' + pp[2:])
                    else:
                        if len(pp[2:]) < 8:
                            pp = '0x00000000' + '0' * (8 - (len(pp[2:]) % 8)) + pp[2:]
                            l.append(pp)
                        else:
                            pp = '0x' + '0' * (8 - (len(pp[2:]) % 8)) + pp[2:]
                            l.append(pp)
                self.xxx = l
            else:
                s = s + '\x00' * (8 - (len(s) % 8))
                l = []
                for x in range(0, len(s), 8):
                    pp = hex(u64(s[x:x + 8]))
                    if len(pp[2:]) % 8 == 0:
                        if len(pp[2:]) == 16:
                            l.append(pp)
                        else:
                            l.append('0x00000000' + pp[2:])
                    else:
                        if len(pp[2:]) < 8:
                            pp = '0x00000000' + '0' * (8 - (len(pp[2:]) % 8)) + pp[2:]
                            l.append(pp)
                        else:
                            pp = '0x' + '0' * (8 - (len(pp[2:]) % 8)) + pp[2:]
                            l.append(pp)
                self.xxx = l
        return self.xxx

    def leak32(self):
        if len(self.leak[self.lenght:]) > 0:
            s = self.leak[self.lenght:]
            if len(s) % 4 == 0:
                l = []
                for x in range(0, len(s), 4):
                    pp = hex(u32(s[x:x + 4]))
                    if len(pp[2:]) % 4 == 0:
                        if len(pp[2:]) == 8:
                            l.append(pp)
                        else:
                            l.append('0x0000' + pp[2:])
                    else:
                        if len(pp[2:]) < 4:
                            pp = '0x0000' + '0' * (4 - (len(pp[2:]) % 4)) + pp[2:]
                            l.append(pp)
                        else:
                            pp = '0x' + '0' * (4 - (len(pp[2:]) % 4)) + pp[2:]
                            l.append(pp)
                self.xxx = l
            else:
                s = s + '\x00' * (4 - (len(s) % 4))
                l = []
                for x in range(0, len(s), 4):
                    pp = hex(u32(s[x:x + 4]))
                    if len(pp[2:]) % 4 == 0:
                        if len(pp[2:]) == 8:
                            l.append(pp)
                        else:
                            l.append('0x0000' + pp[2:])
                    else:
                        if len(pp[2:]) < 4:
                            pp = '0x0000' + '0' * (4 - (len(pp[2:]) % 4)) + pp[2:]
                            l.append(pp)
                        else:
                            pp = '0x' + '0' * (4 - (len(pp[2:]) % 4)) + pp[2:]
                            l.append(pp)
                self.xxx = l
        return self.xxx

    def print_leak(self):
        return self.xxx

    def leak_to64(self, i):
        return p64(int(self.xxx[i][2:], 16))

    def leak_to32(self, i):
        return p32(int(self.xxx[i][2:], 16))

    def leak_to_32_int(self, i):
        return int(self.xxx[i][2:], 16)

    def leak_to_64_int(self, i):
        return int(self.xxx[i][2:], 16)
