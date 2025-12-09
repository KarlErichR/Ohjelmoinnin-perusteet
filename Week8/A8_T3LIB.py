def Summ(PValues: list[float]):
    return round(sum(PValues), 1)

def average(PValues: list[float]):
    if len(PValues) == 0:
        print("No values - 0")
    else:
        return round(sum(PValues) / len(PValues), 1)