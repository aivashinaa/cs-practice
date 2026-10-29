def parse_event(line: str) -> dict:
    """
    ׀אחבטנאוע סענמךף זףנםאכא םא ענט קאסעט: גנולÿ, ףנמגוםü ט סממבשוםטו.
    ֿנט םוגונםמל פמנלאעו גמחבףזהאוע ValueError.
    """
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError(f"־זטהאכמסü 3 ןמכÿ, ןמכףקוםמ {len(parts)}")
    
    time_str, level_str, message_str = parts
    return {
        "time": time_str,
        "level": level_str,
        "message": message_str
    }
 
def count_levels(lines) -> dict:
    """
    ׁקטעאוע ךמכטקוסעגמ סענמך ךאזהמדמ ףנמגםÿ.
    ֽודמהםûו סענמךט (גûחûגא‏שטו ValueError) סקטעא‏עסÿ ןמה ךכ‏קמל "BROKEN".
    Lines למזוע בûעü סןטסךמל סענמך טכט מעךנûעûל פאיכמל.
    """
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
    return counts
 
def top_errors(lines, n: int) -> list[list]:
    """
    ֲמחגנאשאוע n סאלûץ קאסעûץ סממבשוםטי ףנמגםÿ ERROR ג גטהו ןאנ [סממבשוםטו, סךמכüךמ נאח].
    ֿנט נאגוםסעגו קאסעמעû סמנעטנמגךא ןמ אכפאגטעף סממבשוםטי (ןמ גמחנאסעאםט‏).
    """
    error_counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue
            
    sorted_errors = sorted(
        error_counts.items(),
        key=lambda item: (-item[1], item[0])
    )
    
    result = [[msg, count] for msg, count in sorted_errors[:n]]
    return result
 
def format_report(counts: dict, errors: list[list]) -> str:
    """
    װמנלטנףוע עוךסע מעק¸עא ןמ דמעמגûל ןמהסק¸עאל.
    """
    lines = ["־עק¸ע ןמ זףנםאכף", ""]
    
    for level in sorted(counts.keys()):
        lines.append(f"{level}: {counts[level]}")
        
    lines.append("")
    lines.append("׳אסעûו מרטבךט:")
    for msg, count in errors:
        lines.append(f"- {msg} – {count}")
        
    return "\n".join(lines)
