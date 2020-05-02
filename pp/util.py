def bisec(mi: int, ma: int, func, acc: float) -> list:
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

def mod_convert(mods: str):
    mod_list = {
        'hardrock': 'hr',
        'doubletime': 'dt',
        'hidden': 'hd',
        'easy': 'ez',
        'flashlight': 'fl',
        'halftime': 'ht'
        }

    res = list()
    mods = mods[mods.index('+')+1:].strip('+').split()
    for i in mods:
        try:
            res.append(mod_list[i.lower()])
        except:
            continue

    return res
