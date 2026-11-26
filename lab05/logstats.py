def parse_event(line):
    parts = line.strip().split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("Некорректный формат строки")
    time_str, level, message = parts
    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in valid_levels:
        raise ValueError("Неизвестный уровень логирования")
    return {
        "time": time_str,
        "level": level,
        "message": message
    }

def count_levels(lines):
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
    return counts

def top_errors(lines, n):
    error_counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            pass
    sorted_errors = sorted(
        error_counts.items(), 
        key=lambda x: (-x[1], x[0])
    )
    return [[msg, count] for msg, count in sorted_errors[:n]]

def format_report(counts, errors):
    report_lines = ["Отчёт по журналу"]
    for level in sorted(counts.keys()):
        report_lines.append(f"{level}: {counts[level]}")
    report_lines.append("")
    report_lines.append("Частые ошибки:")
    if not errors:
        report_lines.append("Нет ошибок")
    else:
        for msg, count in errors:
            report_lines.append(f"- {msg} — {count}")
    return "\n".join(report_lines) + "\n"
