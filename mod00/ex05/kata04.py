import sys

kata = (0, 4, 132.42222, 10000, 12345.67)

def print_module(kata):
    mod, ex, x, y, z = kata
    print(f"module_{mod:02d}, ex_{ex:02d} : {x:.2f}, {y:.2e}, {z:.2e}")

print_module(kata)