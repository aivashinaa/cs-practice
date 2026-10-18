def parse_record(line : str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Строка должна содержать ровно 3 поля, разделённых ';'")
    city, temperature_str, date = parts[0].strip(), parts[1].strip(), parts[2].strip()

    if not city or not date:
        raise ValueError("Название города и дата не могут быть пустыми")


    try:
        temperature = float(temperature_str)
    except ValueError:
        raise ValueError(f"Некорректное значение температуры: '{temperatyre_str}'")

    return {"city": city, "temperature": temperature, "date": date}

def read_valid(lines: list[str]) -> tuple[list[dict], int]:
    valid_records = []
    skipped_count = 0

for line in lines:
    if not line.strip():
        skipped_count +=1
        continue
    try:
        record = parse_record(line)
        valid_records.append(record)
    except ValueError:
        skipped_cound +=1

    return valid_records, skipped_count

def average_by_city(records: list[dict]) -> dict[str,float]:
    totals = {}
    counts = {}

    for rec in records:
        city = rec["city"]
        totals[city] = totals.get(city, 0.0) + rec["temperature"]
        counts[city] = counts.get(city, 0) + 1

    averages = {}
    for city in totals:
        averages[city] = totals[city] / counts[city]

    return averages

def warmest_city(records: list[dict])-> str:
    averages = averages_by_city(records)
    if not averages:
        return ""

    best_city = min(averages.key(), key=lambda c: (-averages[c], c))
