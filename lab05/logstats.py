VALID_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}
ALL_LEVELS = ["BROKEN", "DEBUG", "ERROR", "INFO", "WARNING"]
 
def parse_event(line: str) -> dict:
    clean = line.rstrip("\r\n")
    if not clean.strip():
        raise ValueError("Empty log line")
 
    parts = clean.split(" ", 2)
    if len(parts) != 3:
        raise ValueError("Invalid log line format")
 
    time_str, level, message = parts[0].strip(), parts[1].strip(), parts[2].strip()
    if not time_str or level not in VALID_LEVELS or not message:
        raise ValueError("Invalid log event fields")
 
    return {
        "time": time_str,
        "level": level,
        "message": message,
    }
 
def count_levels(lines) -> dict:
    counts = {lvl: 0 for lvl in ALL_LEVELS}
 
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            counts[event["level"]] += 1
        except ValueError:
            counts["BROKEN"] += 1
 
    return counts
 
def top_errors(lines, n: int) -> list[list]:
    if n <= 0:
        return []
 
    error_counts: dict[str, int] = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
 
        if event["level"] == "ERROR":
            msg = event["message"]
            error_counts[msg] = error_counts.get(msg, 0) + 1
 
    ranked = sorted(error_counts.items(), key=lambda item: (-item[1], item[0]))
    return [[msg, cnt] for msg, cnt in ranked[:n]]
 
def format_report(counts: dict, errors: list[list]) -> str:
    lines_out = [
        "Отчёт по журналу",
        "",
    ]
    for lvl in ALL_LEVELS:
        lines_out.append(f"{lvl}: {counts.get(lvl, 0)}")
 
    if errors:
        lines_out.append("")
        lines_out.append("Частые ошибки:")
        for item in errors:
            msg, cnt = item[0], item[1]
            lines_out.append(f"{msg}: {cnt}")
 
    return "\n".join(lines_out) + "\n"
