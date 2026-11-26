import sys
from logstats import parse_event, count_levels, top_errors, format_report

def main():
    try:
        filename = input().strip()
    except EOFError:
        return

    if not filename:
        return

    total_parsed = 0
    total_errors = 0
    total_broken = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return

    counts = count_levels(lines)
    top_errs = top_errors(lines, 3)

    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            total_parsed += 1
            if event["level"] == "ERROR":
                total_errors += 1
        except ValueError:
            total_broken += 1

    print(total_parsed)
    print(total_errors)
    print(total_broken)

    report_text = format_report(counts, top_errs)
    
    with open("report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report_text)

if __name__ == "__main__":
    main()
