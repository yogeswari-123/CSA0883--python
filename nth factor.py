def nth_factor(num, n):
    factors = [i for i in range(1, num + 1) if num % i == 0]
    return factors, factors[n - 1] if n <= len(factors) else None
given_number = 100
N = 4
factors, nth_factor_value = nth_factor(given_number, N)
print(f"Number of factors = {len(factors)}")
if nth_factor_value is not None:
    print(f"{N}th factor of {given_number} = {nth_factor_value}")
else:
    print(f"{N}th factor does not exist")

