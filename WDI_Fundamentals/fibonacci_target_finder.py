def find_fibonacci_starting_pair(target_year):
    """
    Finds the first pair of starting numbers (a, b) that eventually 
    generate the target_year in a Fibonacci-like sequence.
    """
    for total_sum in range(2, target_year):
        for a in range(1, total_sum // 2 + 1):
            b = total_sum - a

            temp_a, temp_b = a, b

            while temp_b <= target_year:
                if temp_b == target_year:
                    return a, b

                temp_a, temp_b = temp_b, temp_b + temp_a

    return None