
import angr
import claripy
import binascii

p = angr.Project("./solver.bin", load_options={"auto_load_libs": False})

input = claripy.BVS("input", 8*15)

state = p.factory.blank_state(addr=0x04011C9, add_options={
                              angr.options.LAZY_SOLVES})

state.memory.store(0x04040A0, input)

for i in range(15):
    state.add_constraints(input.get_byte(i) != 0)
    state.add_constraints(input.get_byte(i) >= 0x20)
    state.add_constraints(input.get_byte(i) <= 0x7f)

state.add_constraints(state.memory.load(0x04040A0, 4) ==
                      int(binascii.hexlify(b"CTF{"), 16))

sm = p.factory.simulation_manager(state)

sm.explore(find=0x040130E, avoid=(0x040131C))
found = sm.found[0]

flag_str = found.solver.eval(input, cast_to=bytes)
print('FLAG: ' + flag_str.decode())

# FLAG: CTF{S1MDf0rM3!}
