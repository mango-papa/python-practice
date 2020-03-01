def sort(l):
    if len(l) <= 1:
        return l
    else:
        mid = len(l) // 2
        pivot = l[mid]

        left_list = list(filter(lambda x: x < pivot, l))
        mid_list = list(filter(lambda x: x == pivot, l))
        right_list = list(filter(lambda x: x > pivot, l))

        return sort(left_list) + mid_list + sort(right_list)
