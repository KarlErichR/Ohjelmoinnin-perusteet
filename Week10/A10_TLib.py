
def readValues(filename, values):
    try:
        with open(filename, "r") as f:
            data = f.read()
            parts = data.replace(",", " ").split()
            for p in parts:
                if p.isdigit():
                    values.append(int(p))
    except:
        print("File not found!", filename)

def displayValues(filename, values, label):
    print(label, "'" + filename + "' ->", ", ".join(str(v) for v in values))

def bubbleSort(values, PAsc=True):
    n = len(values)
    for i in range(n):
        for j in range(0, n - i - 1):
            if PAsc:
                if values[j] > values[j + 1]:
                    values[j], values[j + 1] = values[j + 1], values[j]
            else:
                if values[j] < values[j + 1]:
                    values[j], values[j + 1] = values[j + 1] , values[j]