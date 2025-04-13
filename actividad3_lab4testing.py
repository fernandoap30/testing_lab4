def stats(lst):
    min_val = None
    max_val = None
    freq = {}

    for i in lst:
        if min_val is None or i < min_val:
            min_val = i
        if max_val is None or i > max_val:
            max_val = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    median = None
    if lst:
        lst_sorted = sorted(lst)
        if len(lst_sorted) % 2 == 0:
            middle = len(lst_sorted) // 2
            median = (lst_sorted[middle] + lst_sorted[middle - 1] + 1) / 2
        else:
            median = lst_sorted[len(lst_sorted) // 2]

    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i

    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append(num)

    return {
    "list": lst,
    "min": min_val,
    "max": max_val,
    "median": median,
    "mode": mode
    }


def test():
    stats([])
    stats([10])
    stats([1, 3, 2])
    stats([4, 2, 1, 3])
    stats([1, 2, 2, 3, 3])

#test()

def test_con_error_detectado():
    resultado = stats([1, 2, 3, 4])  
    assert resultado["median"] == 3.0, f"Error detectado: se esperaba 2.5 pero se obtuvo {resultado['median']}"

test_con_error_detectado()