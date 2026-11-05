import sys
from stats import read_valid, average_by_city, warmest_city, parse_record
 
def main():
    lines = sys.stdin.read().splitlines()
    
    parsed_count = 0
    error_count = 0
    
    for line in lines:
        if not line.strip():
            continue
        try:
            parse_record(line)
            parsed_count += 1
        except ValueError:
            error_count += 1
            
    valid_records = read_valid(lines)
    
    print(parsed_count)
    print(error_count)
    
    if valid_records:
        best_city = warmest_city(valid_records)
        averages = average_by_city(valid_records)
        print(f"{averages[best_city]:.1f}")
 
if __name__ == "__main__":
    main()
