DELIMITER = ";"

class TIMESTAMP:
    weekday = ""
    time = ""
    price = 0.00
    consumption = 0.00

def readTimestamps(PFilename: str, PRows: list[str]):
    print(f"Reading file \"{PFilename}\".".format(PFilename))
    with open(PFilename, "r", encoding = "UTF-8") as f:
        next(f)
        for line in f:
            if line.strip():
                PRows.append(line.strip())
    return None

def displayTimestamps(prows):
    print("Electricity usage:")
    for row in prows:
        columns = row.split(DELIMITER)
        Timestamp = TIMESTAMP()
        Timestamp.weekday = columns[0]
        Timestamp.time = columns[1]
        Timestamp.consumption = float(columns[2])
        Timestamp.price = float(columns[3])
        print(f" - {Timestamp.weekday} {Timestamp.time}:00, price {Timestamp.price}, consumption {Timestamp.consumption:.2f} kWh, total {Timestamp.consumption * Timestamp.price:.2f} €")
        columns.clear()


def  main():
    print("Program starting.")
    rows: list[str] = []
    fname = input("Insert filename: ")
    readTimestamps(fname, rows)
    Timestamp = TIMESTAMP()
    displayTimestamps(rows)
    print("Program ending.")

if __name__ == "__main__":
    main()