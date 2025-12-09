from datetime import datetime

MONTHS = (
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
)

WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
)

def readTimestamps(PFilename: str) -> list[datetime]:
    timestamps = []
    formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]
    with open(PFilename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parsed = False

            for fmt in formats:
                try:
                    ts = datetime.strptime(line, fmt)
                    timestamps.append(ts)
                    parsed = True
                    break

                except ValueError:
                    continue

            if not parsed:
                print(f"Skipping invalid line: {line}")

        print(f"File '{PFilename}' read successfully.\n")
    return timestamps

def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    return sum(1 for ts in PTimestamps if ts.year == PYear)

def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    month_index = MONTHS.index(PMonth.capitalize()) + 1
    return sum(1 for ts in PTimestamps if ts.month == month_index)

def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    weekday_index = WEEKDAYS.index(PWeekday.capitalize())
    return sum(1 for ts in PTimestamps if ts.weekday() == weekday_index)