# %%
def polyn(n):
    total = 0
    for _ in range(n):
        total += (7*n*n) + (-3*n) + 42
    return total

%timeit -n 10_000 polyn(1000) #10,000 iteractions (to see how much time it takes)

# %%
import numba #now let´s use Numba and see how much it takes

@numba.jit # we decorate the function 
def polyn_jit(n):
    total = 0
    for _ in range(n):
        total += (7*n*n) + (-3*n) + 42
    return total

%timeit -n 10_000 polyn_jit(1000)

# %%
