from nbody_simulation import run_sim
from calc_pi import calc
import time

def char_combo_find(string):
    bitMask = 0

    for i in range(2 ** len(string)):
        inputMasked = ''
        for j in range(len(string)):
            if bitMask >> j & 1:
                inputMasked += string[j]
        bitMask += 1

def recursive_fib(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    else:
        return(recursive_fib(n-1) + recursive_fib(n-2))

print("starting")
start_time = time.time()

calc(500)

pi_time = time.time()
print("finished calculating 7000 digits of pi in:")
print(pi_time - start_time)

for i in range(15, 25):
    char_combo_find('a' * i)

combo_find_time = time.time()
print("finished char combo finding in:")
print(combo_find_time - pi_time)

for i in range(40):
    recursive_fib(i)

fib_time = time.time()
print("finished fib-ing in:")
print(fib_time - combo_find_time)

run_sim(7000000)

sim_time = time.time()
print("finished sim-ing in:")
print(sim_time - fib_time)