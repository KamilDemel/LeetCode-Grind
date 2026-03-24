def find_max_collatz_steps(limit):
    max_steps = 0
    starting_number_record = 0
    for start in range(2, limit + 1):
        number = start
        current_steps = 0
        while number != 1:
            if number % 2 == 0:
                number = number // 2
            else:
                number = 3 * number + 1
            current_steps += 1

        if current_steps > max_steps:
            max_steps = current_steps
            starting_number_record = start
    return max_steps, starting_number_record