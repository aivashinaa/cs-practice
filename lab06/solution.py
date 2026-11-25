def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for path in paths:
        filename = path.rsplit("/", 1)[-1]
        if "." in filename:
            ext = filename.rsplit(".", 1)[-1].lower()
        else:
            ext = ""
        counts[ext] = counts.get(ext, 0) + 1
    return counts
 
def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))
 
def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    for unit in units:
        if size < 1024 or unit == units[-1]:
            if unit == "Б":
                return f"{int(size)} Б"
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{n_bytes} Б"
