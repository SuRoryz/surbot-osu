def bisec(mi: int, ma: int, func: 'function', acc: float) -> list:
    minVal = func(mi)
    if minVal >= acc or mi == ma:
        return (mi, minVal)
    maxVal = func(ma)
    if maxVal <= acc:
        return (ma, maxVal)

    while True:
        if ma == (mi + 1):
            if abs(minVal - acc) < abs(maxVal - acc):
                return (mi, minVal)
            return (ma, maxVal)
        center= (ma + mi) / 2
        centerVal = func(center)
        if centerVal <= acc:
            mi = center
            minVal = centerVal
        else:
            ma = center
            maxVal = centerVal

def str_to_dict(**kwargs) -> dict:
    return kwargs
