def parse_record(line : str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError
    city, temperature_str, date = parts[0].strip(), parts[1].strip(), parts[2].strip()

    if not city or not date:
        raise ValueError


    try:
        temperature = float(temperature_str)
    except ValueError:
        raise ValueError

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
