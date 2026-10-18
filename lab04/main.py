import sys
from stats import parse_record

def main():
    lines = sys.stdin.read().splitlines()
    print(f"Прочитанно строкЖ {len(lines)}")

if __name__ == "__main__":
    main()
    
import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    lines sys.stdin.read().splitlines()
    records, skipped = read_valid(lines)

    city = warmest_city(records)
    if city:
        averages = averages_by_city(records)
        warmest_avg = round(averages[city], 1)
    else:
        warmest_avg = 0.0

    print(len(records))
    print(skipped)
    print(f"{warmest_avg:.1f}")

if _name_ == "_main_":
    main()
