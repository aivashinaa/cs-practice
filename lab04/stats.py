def parse_record(line):
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Строка должна содержать 3 поля")
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()

    if not city or not date:
        raise ValueError("Город или дата пустые")


    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Температура должна быть числом")

    return city, temp, date

def read_valid(lines):
    valid_records = []
    skipped_count = 0
    
    for line in lines:
        line_clean = line.strip()

        if not line_clean:
            continue
        try:
            record = parse_record(line_clean)
            valid_records.append(record)
        except ValueError:
            skipped_cound +=1
        
    return valid_records, skipped_count

def average_by_city(records):
    totals = {}
    counts = {}

    for city, temp, date in records:
        totals[city] = totals.get(city, 0.0) + temp
        counts[city] = counts.get(city, 0) + 1

    averages = {}
    for city in totals:
        averages[city] = totals[city] / counts[city]

    return averages

def warmest_city(averages):
    if not averages:
        return None

    best_city = None
    max_avg = float('-inf')

    for city, avg in averages.items():
        if avg > max_avg:
            max_avg = avg
            best_city = city
            
    return best_city
