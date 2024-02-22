import angr
import claripy
import logging

logging.getLogger('angr').setLevel('ERROR')

proj = angr.Project('./stateful.exe', load_options={'auto_load_libs': False}) # auto_load_libs=False is important, let angr know not to load the library

# Create a symbolic bit vector of 43 bytes (8 bits * 43)
sym_argv = claripy.BVS('sym_argv', 8 * 0x2b)

# Create an initial state starting from the beginning of the main function
state = proj.factory.entry_state(args=['./stateful.exe', sym_argv])

# Create a simulation manager initialized with the starting state
simgr = proj.factory.simulation_manager(state)

# Source code for : https://docs.angr.io/en/stable/_modules/angr/exploration_techniques/veritesting.html
# 參考連結 : https://snyk.io/advisor/python/angr/functions/angr.exploration_techniques
simgr.use_technique(angr.exploration_techniques.Veritesting(enable_function_inlining=True))

# Explore the binary until we reach the "Good Job" message
simgr.explore(find = lambda s: b"Correct!!!" in s.posix.dumps(1))

# Get the first found solution
if len(simgr.found) > 0:
    found = simgr.found[0]
    print(found.solver.eval(sym_argv, cast_to=bytes))
else:
    print("No solution found")