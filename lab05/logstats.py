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
