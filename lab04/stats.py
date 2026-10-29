def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 поля, полученно {len(parts)}")

    city, temp_str, date = parts


    city = city.strip()
    temp_str = temp_str.strip()
    date = date.strip()

    if not city or not date:
        raise ValueError("Город или дата пустые")


    try:
        temperature = float(temp_str)
    except ValueError:
        raise ValueError("Температура '{temp_str}' не является числом")

    return {"city": city, "temperature": temperature, "date": date}

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
    total_temp = {}
    count_records = {}

    for rec in records:
        city = rec["city"]
        temp = rec["temperature"]

        total_temp[city] = total_temp.get(city, 0.0) + temp
        count_records[city] = count_records.get(city, 0) + 1

    averages = {}
    for city in total_temp:
        averages[city] = total_temp[city] / count_records[city]

    return averages

def warmest_city(records: list[dict]) -> str:
    if not records:
        return ""
    averages = averages_by_city(records)
    if not averages:
        return""
    sorted_cities = sorted(
        averages.keys()
        key = lambda city: (-averages[city], city)
        )

    return sorted_cities[0]
