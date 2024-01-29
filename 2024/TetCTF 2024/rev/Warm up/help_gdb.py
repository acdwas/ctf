
import gdb


class HelloPy(gdb.Command):
    def __init__(self):
        super(HelloPy, self).__init__('hello_py', gdb.COMMAND_USER)

    def invoke(self, _unicode_args, _from_tty):

        gdb.execute('b *0x55555555542A')
        gdb.execute('r <<< ' + 'a' * 84)

        l = []

        for i in range(441):
            l.append(gdb.execute("p/x $rax", to_string=True).split()[-1])
            gdb.execute('c')

        print(l)
        
HelloPy()