from pathlib import Path
from logstats import count_levels, format_report, top_errors
 
def main() -> None:
    log_name = input().strip()
    base_dir = Path(__file__).resolve().parent
    log_path = Path(log_name)
    if not log_path.is_absolute():
        log_path = base_dir / log_path
 
    with open(log_path, encoding="utf-8") as f:
        counts = count_levels(f)
 
    with open(log_path, encoding="utf-8") as f:
        errors = top_errors(f, 5)
 
    total_parsed = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)
 
    print(total_parsed)
    print(error_count)
    print(broken_count)
 
    report_text = format_report(counts, errors)
    report_path = base_dir / "report.txt"
    with open(report_path, "w", encoding="utf-8") as out:
        out.write(report_text)
 
if __name__ == "__main__":
    main()
