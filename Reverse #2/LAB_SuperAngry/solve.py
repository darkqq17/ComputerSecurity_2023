import angr
import claripy
import logging

logging.getLogger('angr').setLevel('ERROR')

proj = angr.Project('./super_angry', load_options={'auto_load_libs': False}) # auto_load_libs=False is important, let angr know not to load the library

# Create a symbolic bit vector of 32 bytes (8 bits * 32 = 256 bits)
sym_argv = claripy.BVS('sym_argv', 8 * 0x20)

# Create an initial state starting from the beginning of the main function
state = proj.factory.entry_state(args=['./super_angry', sym_argv]) 

# Create a simulation manager initialized with the starting state
simgr = proj.factory.simulation_manager(state)

# Explore the binary until we reach the "Good Job" message
simgr.explore(find = lambda s: b"Correct!" in s.posix.dumps(1))

# Get the first found solution
if len(simgr.found) > 0:
    found = simgr.found[0]
    print(found.solver.eval(sym_argv, cast_to=bytes))
else:
    print("No solution found")