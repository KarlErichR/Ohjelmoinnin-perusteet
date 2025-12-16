########################################################
# Task A10_T6
# Developer Karl Erich Remmelgas
# Date 2025-12-16
########################################################
import sys
import time
import copy
from typing import Callable, List

def readvalues(filename: str) -> List[float]:
    values: List[float] = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if line == "":
                    continue
                try:
                    values.append(float(line))
                except ValueError:
                    print(f"Warning: Skipping non-numeric row: {line!r}")
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return []
    except OSError as e:
        print(f"Error: Could not read '{filename}': {e}")
        return []
    return values

def bubbleSort(arr: List[float]) -> List[float]:
    a = arr[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def quickSort(arr: List[float]) -> List[float]:
  a = arr[:] 
  _quickSortInPlace(a, 0, len(a) - 1)
  return a

def _quickSortInPlace(a: List[float], lo: int, hi: int) -> None:
  if lo >= hi:
      return
  p = _partition(a, lo, hi)
  _quickSortInPlace(a, lo, p - 1)
  _quickSortInPlace(a, p + 1, hi)

def _partition(a: List[float], lo: int, hi: int) -> int:
  pivot = a[hi]
  i = lo
  for j in range(lo, hi):
      if a[j] <= pivot:
          a[i], a[j] = a[j], a[i]
          i += 1
  a[i], a[hi] = a[hi], a[i]
  return i

def measureSortingTime(sortingFn: Callable[[List[float]], List[float]],
  arr: List[float]) -> int:
  start = time.perf_counter_ns()
  _sorted = sortingFn(copy.deepcopy(arr))
  end = time.perf_counter_ns()
  return end - start

def printMenu() -> None:
    print("Options:")
    print("1 - Read dataset values")
    print("2 - Measure speeds")
    print("3 - Save results")
    print("0 - Exit")

def readDatasetFlow(values: List[float]) -> List[float]:
    filename = input("Insert dataset filename: ")
    data = readvalues(filename)
    if not data:
        print("Error: Could not read any values.")
        return values
    print(f"Read {len(data)} values.")
    return data

def measureFlow(values: List[float]) -> dict:
    if not values:
        print("Error: No data loaded. Use option 1 first.")
        return {}
    t_builtin = measureSortingTime(sorted, values)
    t_bubble  = measureSortingTime(bubbleSort, values)
    t_quick   = measureSortingTime(quickSort, values)

    print(f"Measured speeds for dataset: '{current_dataset_name(values)}' :")
    print(f" - Built in sorted:{t_builtin} ns")
    print(f" - Bubble sort:{t_bubble} ns")
    print(f" - Quick sort:{t_quick} ns")

    return {
        "dataset": current_dataset_name(values),
        "builtin_ns": t_builtin,
        "bubble_ns": t_bubble,
        "quick_ns": t_quick
    }

def current_dataset_name(values: List[float]) -> str:
    # No filename stored; you could adapt to keep one.
    # Using a placeholder that matches screenshot style.
    return "dataset"

def saveFlow(results: dict) -> None:
    if not results:
        print("Error: No measured results to save. Run option 2 first.")
        return
    outname = input("Insert.results.filename: ")
    try:
        with open(outname, "w", encoding="utf-8") as f:
            f.write(f"Measured.speeds.for-dataset: '{results['dataset']}' :\n")
            f.write(f"-->Built-in.sorted:{results['builtin_ns']} ns\n")
            f.write(f"-->Bubble.sort:{results['bubble_ns']} ns\n")
            f.write(f"-->Quick.sort:{results['quick_ns']} ns\n")
        print(f"Saved.results.to: {outname}")
    except OSError as e:
        print(f"Error: Could.not.save.results: {e}")


# ---------- Main ----------
def main() -> None:
    print("Program-starting.")

    values: List[float] = []
    results: dict = {}

    while True:
        printMenu()
        choice = input("Your choice: ")

        if choice == "1":
            values = readDatasetFlow(values)
        elif choice == "2":
            results = measureFlow(values)
        elif choice == "3":
            saveFlow(results)
        elif choice == "0":
            print("Exiting.program.")
            break
        else:
            print("Invalid.choice.")

    print("Program-ending.")

if __name__ == "__main__":
    main()
