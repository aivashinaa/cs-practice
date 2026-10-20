def parse_record(line : str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Invalid record format")
    city, temp_str, date = parts[0].strip(), parts[1].strip(), parts[2].strip()

    if not city or not date:
        raise ValueError("Empty city or date")


    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Invalid temperature value")

    return {"city": city, "temp": temp, "temperature": temp, "date": date}

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

def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}

    for rec in records:
        city = rec["city"]
        t = rec.get("temp", rec.get("temperature", 0.0))
        totals[city] = totals.get(city, 0.0) + t
        counts[city] = counts.get(city, 0) + 1

    averages = ()
    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)

    return averages

def warmest_city(records: list[dict])-> str:
    averages = averages_by_city(records)
    if not averages:
        return ""

    best_city = min(averages.key(), key=lambda c: (-averages[c], c))
    return best_city
