
import angr
import claripy
import binascii

p = angr.Project("./runofthemill", load_options={"auto_load_libs": False})

input = claripy.BVS("input", 8*34)

state = p.factory.blank_state(addr=0x40104d, add_options={angr.options.LAZY_SOLVES})

state.memory.store(0x412000, input)
state.regs.rdi = 0x412000

for i in range(34):
    state.add_constraints(input.get_byte(i) != 0)
    state.add_constraints(input.get_byte(i) >= 0x20)
    state.add_constraints(input.get_byte(i) <= 0x7f)

state.add_constraints(state.memory.load(0x412000, 6) == int(binascii.hexlify(b"DrgnS{"), 16))

sm = p.factory.simulation_manager(state)

sm.explore(find=0x411833, avoid=(0x411822))
found = sm.found[0]

flag_str = found.solver.eval(input, cast_to=bytes)
print('Password: ' + flag_str.decode(errors='ignore'))

# DrgnS{SoManyInstructionsYetSoWeak}
