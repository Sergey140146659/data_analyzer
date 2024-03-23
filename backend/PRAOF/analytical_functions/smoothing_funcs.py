def supsmooth(lst, k):
    if k <= 1:
        return lst
    smoothed_lst = []
    for i in range(len(lst)):
        total = 0
        cnt = 0
        for j in range(-k, k + 1):
            if i + j >= 0 and i + j < len(lst):
                total += lst[i + j] if j != 0 else lst[i + j]
                cnt += 1
            else:
                if i + j < 0:
                    total += lst[i]
                if i + j >= len(lst):
                    total +=  lst[i]
        smoothed_lst.append(total / (2 * k + 1))
    return smoothed_lst
