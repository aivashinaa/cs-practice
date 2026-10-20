import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    valid_records, skipped_count = read_valid(lines)
    averages = averages_by_city(records)
    warmest = warmest_city(averages)


    print(len(valid_records))
    print(skipped_count)

    if warmest and warmest in averages:
        print(f"{averages[warmest]:.1f}")
    else:
        print("Нет данных")

if _name_ == "_main_":
    main()
