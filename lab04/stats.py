def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Invalid field count")
    
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    
    if not city or not date:
        raise ValueError("Empty city or date")
        
    temp = float(temp_str)
    
    return {
        "city": city,
        "temperature": temp,
        "date": date
    }
 
def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue
    return valid_records
 
def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    for rec in records:
        city = rec["city"]
        temp = rec["temperature"]
        totals[city] = totals.get(city, 0.0) + temp
        counts[city] = counts.get(city, 0) + 1
        
    averages = {}
    for city, total_temp in totals.items():
        averages[city] = round(total_temp / counts[city], 1)
    return averages
 
def warmest_city(records: list[dict]) -> str:
    if not records:
        return ""
    averages = average_by_city(records)
    sorted_cities = sorted(averages.keys(), key=lambda city: (-averages[city], city))
    return sorted_cities[0]
