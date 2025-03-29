def filter_nondigits(data: list) -> list:
    clean_data = []

    for entry in data:
        entry = entry.strip()
        if entry.isdigit():
            clean_data.append(int(entry))
    return clean_data