def calculate_alternating_neighbor_products(arr):
    n = len(arr)
    if n < 2:
        return 0, 0

    even_indexed_sum = 0
    odd_indexed_sum = arr[0] + arr[n - 1]

    i = 0
    while i < n - 1:
        product = arr[i] * arr[i + 1]

        if i % 2 == 0:
            even_indexed_sum += product
        else:
            odd_indexed_sum += product
        i += 1

    return even_indexed_sum, odd_indexed_sum