import gdb


class HelloPy(gdb.Command):
    def __init__(self):
        super(HelloPy, self).__init__('hello_py', gdb.COMMAND_USER)

    def invoke(self, _unicode_args, _from_tty):

      test = 'abcdefghijklmnopqrstuvwxyz0123456789'

      with open('code_asm.txt', 'a') as f:

         gdb.execute('b *0x0000555555555400')
         gdb.execute('b *0x000055555555553a')
         gdb.execute('b *0x00005555555555b7')
         gdb.execute('b *0x0000555555555649')
         gdb.execute('b *0x00005555555556c7')
         gdb.execute('b *0x0000555555555727')
         gdb.execute('b *0x0000555555555282')

         gdb.execute(f'r <<< {test}')

         while True:

            gdb.execute('ni')

            try:
               rip = int(gdb.parse_and_eval("$rip"))
            except gdb.error:
               f.write(f'RIP not available {hex(rip)}\n')
               continue

            if rip == 0x5555555551e9 or rip == 0x0000555555555381 or rip == 0x0000555555555401 or rip == 0x55555555553b or \
               rip == 0x5555555555b8 or rip == 0x55555555564a or rip == 0x5555555556c8:
               gdb.execute('c')
               continue

            w = gdb.execute('disassemble $pc, +1', from_tty=True, to_string=True)

            if '(bad)' in w:
               continue

            if 0x555555555310 <= rip <= 0x555555555350:

               try:
                  ww = w.split('\n')[1].strip()
                  f.write(ww + '\n')
            
                  if ',al' in w:
                     try:
                        rax_val = int(gdb.parse_and_eval("$rax"))
                        ch = chr(rax_val)
                        idx = test.index(ch)
                        ss = f'al {ch} -> {idx} (position in string)'
                     except (ValueError, gdb.error):
                        ss = f'al ? (invalid)'
                     f.write(ss + '\n')

                  if 'cmp' in w:
                     ww = w.split('\n')[1].strip().replace(':','').split()
                     ss = f'cmp {ww[-1]}'

                     if 'eax,0xffffffa0' in ww[-1]:
                        break

               except Exception as e:
                     continue

HelloPy()