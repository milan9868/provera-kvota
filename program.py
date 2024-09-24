from z3 import *

# Define the constants
kec = 1.9
iks = 3.35
dvojka = 4.75

# Create Z3 solver
solver = Solver()

# Define variables
x = Real('x')
y = Real('y')
z = Real('z')

# Add the new constraints
solver.add(x*kec > x + y + z)
solver.add(y*dvojka > x + y + z)
solver.add(z*iks > x + y+ z)
solver.add(x > 0, y > 0, z > 0)

# Check if the solver can find a solution
if solver.check() == sat:
    model = solver.model()
    print(f"Solution found:")
    print(f"x = {model[x]}")
    print(f"y = {model[y]}")
    print(f"z = {model[z]}")
    
    # Get numerical values
    x_val = model[x].numerator_as_long() / model[x].denominator_as_long()
    y_val = model[y].numerator_as_long() / model[y].denominator_as_long()
    z_val = model[z].numerator_as_long() / model[z].denominator_as_long()
    
    print(f"\nVerification:")
    print(f"Constraint 1: {x_val} * {kec} > {x_val} + {y_val} + {z_val}")
    print(f"{x_val * kec} > {x_val + y_val + z_val}")
    print(f"Holds: {x_val * kec > x_val + y_val + z_val}")
    
    print(f"Constraint 2: {y_val} * {dvojka} > {x_val} + {y_val} + {z_val}")
    print(f"{y_val * dvojka} > {x_val + y_val + z_val}")
    print(f"Holds: {y_val * dvojka > x_val + y_val + z_val}")

    print(f"Constraint 3: {z_val} * {iks} > {x_val} + {y_val} + {z_val}")
    print(f"{z_val * iks} > {x_val + y_val + z_val}")
    print(f"Holds: {z_val * iks > x_val + y_val + z_val}")
else:
    print("No solution found")
