def parse_record(line : str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(" —трока должна содержать ровно 3 пол€, разделенных ';' ")
    city, temp_str, date = parts[0].strip(), parts[1].strip(), parts[2].strip()

    if not city or not date:
        raise ValueError


    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError

    return {"city": city, "temp": temp, "date": date}
