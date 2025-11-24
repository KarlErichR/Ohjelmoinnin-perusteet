WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

def readFile(PFilename: str, PRows: list[str]) -> None:
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
    weekday_count: list[int] = [0] * len(WEEKDAYS)
    for row in PRows:
        for index, day in enumerate(WEEKDAYS):
            if row.startswith(day):
                weekday_count[index] += 1
    PResults.append("### Timestamp analysis ###")
    for index, day in enumerate(WEEKDAYS):
        PResults.append(f" - {day}: {weekday_count[index]} stamps")
    PResults.append("### Timestamps analysis ###")
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    for line in PResults:
        print(line)
    return None

def main() -> None:
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