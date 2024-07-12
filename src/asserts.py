def is_number(s: str) -> bool:
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True
