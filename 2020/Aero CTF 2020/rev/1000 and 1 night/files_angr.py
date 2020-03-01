
import angr
import os

l = os.listdir('files')

sw = {}

for i in l:
    proj = angr.Project('files/'+i)
    simgr = proj.factory.simgr()
    simgr.explore(find=lambda s: b"This is a valid token" in s.posix.dumps(1))
    s = simgr.found[0]
    flag = s.posix.dumps(0)
    sw[i] = flag.decode()[:32]

with open('file.txt', 'w') as f:
    f.write(str(sw))
