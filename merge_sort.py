def sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left_list = l[:mid]
        right_list = l[mid:]
        sort(left_list)
        sort(right_list)

        i, j, k = 0, 0, 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] <= right_list[j]:
                l[k] = left_list[i]
                i += 1
            else:
                l[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            l[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            l[k] = right_list[j]
            j += 1
            k += 1

        return l
