WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)
DELIMITER = ";"

class TIMESTAMP:
    price = 0.00
    consumption = 0.00


def readFile(PFilename: str, PRows: list[str]):
    print(f'Reading file "{PFilename}".'.format(PFilename))
    PRows.clear() 
    with open(PFilename, "r", encoding = "UTF-8") as f: 
        next(f) 
        for line in f:
            if line.strip():
                PRows.append(line.strip()) 
    return None

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PResults.clear()
    weekday_consumption: list[float] = [0.0] * len(WEEKDAYS)
    weekday_price: list[float] = [0.0] * len(WEEKDAYS)
    PResults.append("### Electricity consumption summary ###")

    for row in PRows:
        columns = row.split(DELIMITER)
        Timestamp = TIMESTAMP()
        Timestamp.consumption = float(columns[2])
        Timestamp.price = float(columns[3])
        for index, day in enumerate(WEEKDAYS):
            if row.startswith(day):
                weekday_consumption[index] += Timestamp.consumption
                tprice = (Timestamp.consumption * Timestamp.price)
                weekday_price[index] += tprice

    for index, day in enumerate(WEEKDAYS):
        PResults.append(
            f" - {day} usage {weekday_consumption[index]:.2f} kWh, cost {weekday_price[index]:.2f} €")
    PResults.append("### Electricity consumption summary ###")
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    for line in PResults:
        print(line)
    return None




def  main():
    print("Program starting.")
    rows: list[str] = [] 
    result: list[str] = [] 
    fname = input("Insert filename: ") 
    readFile(fname, rows)
    analyseTimestamps(rows, result) 
    displayResults(result)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()