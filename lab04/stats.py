 
def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Ñòðîêà äîëæíà ñîäåðæàòü ðîâíî 3 ïîëÿ, ðàçäåë¸ííûõ ';'")
    
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    
    if not city or not date:
        raise ValueError("Ïîëÿ 'ãîðîä' è 'äàòà' íå ìîãóò áûòü ïóñòûìè")
    
    try:
        temp = float(temp_str)
    except ValueError as e:
        raise ValueError(f"Íåâîçìîæíî ïðåîáðàçîâàòü òåìïåðàòóðó '{temp_str}' â ÷èñëî") from e
        
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
