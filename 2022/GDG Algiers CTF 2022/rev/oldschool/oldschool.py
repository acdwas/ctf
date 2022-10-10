
import angr
import claripy

FLAG_LEN = 8
STDIN_FD = 0

base_addr = 0x400000

proj = angr.Project("./oldschool", main_opts={'base_addr': base_addr}) 

flag_chars = [claripy.BVS('flag_%d' % i, 8) for i in range(FLAG_LEN)]
flag = claripy.Concat( *flag_chars + [claripy.BVV(b'\n')]) # Add \n for scanf() to accept the input

state = proj.factory.full_init_state(
        args=['./oldschool'],
        stdin=angr.SimFileStream(name='stdin', content=flag, has_end=False)
)


for k in flag_chars:
    state.solver.add(k >= ord('!'))
    state.solver.add(k <= ord('~'))

simgr = proj.factory.simulation_manager(state)
find_addr  = 0x401290 # SUCCESS
avoid_addr = 0x40123F # FAILURE
simgr.explore(find=find_addr, avoid=avoid_addr)

if (len(simgr.found) > 0):
    for found in simgr.found:
        print(found.posix.dumps(STDIN_FD))