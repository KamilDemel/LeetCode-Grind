def find_scaled_adjacent_segments(arr):
    n = len(arr)
    l = 3

    while l * 2 <= n:
        for i in range(n - 2 * l + 1):
            is_valid = True

            if arr[i + l] % arr[i] == 0:
                k = arr[i + l] // arr[i]

                for j in range(l):
                    if (arr[i + j + l] == arr[i + j] * k and
                            arr[i + j + l] % arr[i + j] == 0 and
                            arr[i + j + l] > arr[i + j]):
                        is_valid = True
                    else:
                        is_valid = False
                        break
            else:
                is_valid = False

            if is_valid:
                start_index = i
                end_index = i + l - 1
                return start_index, end_index
        l += 1
    return None