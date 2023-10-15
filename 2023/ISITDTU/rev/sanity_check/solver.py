
import gdb


class HelloPy(gdb.Command):
    def __init__(self):
        super(HelloPy, self).__init__('hello_py', gdb.COMMAND_USER)

    def invoke(self, _unicode_args, _from_tty):

        x = '0' * 23
        for _ in range(35):
            x = int(gdb.execute('x/gx $rsp+$rbx*8+0x58',
                    to_string=True).split()[-1], 16)
            y = int(gdb.parse_and_eval("$rax"))
            gdb.execute(f'set $rdx={x^y}')
            gdb.execute('c')


HelloPy()
