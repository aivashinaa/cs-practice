import sys
from logstats import count_levels, top_errors, format_report
 
def main():
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return
    
    log_filename = input_lines[0].strip()
    
    try:
        with open(log_filename, "r", encoding="utf-8") as f:
            pass
    except FileNotFoundError:
        print(f"Τΰιλ {log_filename} νε νΰιδεν")
        return
 
    with open(log_filename, "r", encoding="utf-8") as f:
        counts = count_levels(f)
        
    with open(log_filename, "r", encoding="utf-8") as f:
        errors = top_errors(f, 5)
    total_lines = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)
    
    print(total_lines)
    print(error_count)
    print(broken_count)
    
    report_text = format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report_text)
 
if __name__ == "__main__":
    main()
