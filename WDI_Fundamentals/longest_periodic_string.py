def find_longest_periodic_string(string_list):
    """
    Finds the length of the longest string that is a multiple
    of its own prefix (e.g., 'abcabc' is a multiple of 'abc').
    """
    max_length = 0

    for text in string_list:
        length = len(text)
        is_periodic = False

        for divisor in range(1, (length // 2) + 1):
            if length % divisor == 0:
                pattern = text[:divisor]
                if pattern * (length // divisor) == text:
                    is_periodic = True
                    break

        if is_periodic:
            if length > max_length:
                max_length = length

    return max_length