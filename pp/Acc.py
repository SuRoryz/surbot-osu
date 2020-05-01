from util import bisec

# Acc calculation
def accCalc(hits: list) -> float:
    h300, h100, h50, miss = hits
    total: int = sum(hits)

    if total != 0:
        return (h300 * 300 + h100 * 100 + h50 * 50) / (total *300)

    else:
        return 1.0

# Hits calculation
def accDist(objs: int, misses: int, acc: float) -> list:
    best300s = getBest300s(objs, misses, acc)
    best100s = int(getBest100s(objs, best300s, misses, acc)[0])

    return best300s, best100s, objs - best300s - best100s - misses, misses

# Calculate 300s
def getBest300s(objs: int, misses: int, acc: float) -> int:
    best300s: int = 0
    best: int = getBest100s(objs, 0, misses, acc)

    for i in range(1, (objs - misses)+1):
        val = getBest100s(objs, i, misses, acc)

        if abs(val[1] - acc) < abs(best[1] - acc):
            best = val
            best300s = i

    return best300s

# Calculate 100s
def getBest100s(objs: int, h300: int, misses: int, acc: float) -> int:
    return bisec(0, objs-h300 - misses, lambda x: accCalc([h300, x, objs - h300 - x - misses, misses]), acc*100)

