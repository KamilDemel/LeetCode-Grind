import math

last_term = math.sqrt(1/2)
product = last_term

for _ in range(1, 200):
    next_term = math.sqrt(0.5 + 0.5 * last_term)
    product *= next_term
    last_term = next_term

calculated_pi = 2 / product