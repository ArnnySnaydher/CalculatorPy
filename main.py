# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

#print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

test_1 = [0,1,2,3,4,5,6,7,8]
print("hello friend")
sol_1 = mean_var_std.calculate(test_1)
print(sol_1)

print("----------------------------------------")

test_2 = [3,8,2,7,4,15,6,17,8]
print("hello world")
sol_2 = mean_var_std.calculate(test_2)
print(sol_2)

print("----------------------------------------")

test_3 = [6,11,9,13,4,5,6,1,0]
print("hello cat")
sol_3 = mean_var_std.calculate(test_3)
print(sol_3)

print("----------------------------------------")

# Run unit tests automatically
#main(module='test_module', exit=False)