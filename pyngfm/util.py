def convert_boolean(value):
    if isinstance(value, bool):
        return value
    try:
        value = int(value)
        if value == 0:
            return False
        return True
    except ValueError:
        # couldn't cast string value as an integer
        pass
    if isinstance(value, unicode):
        value = str(value)
    if isinstance(value, str):
        if value.lower() in ["yes", "y", "t", "true", "on"]:
            return True
        return False
    return False


def get_boolean_as_int(value):
    value = convert_boolean(value)
    if value:
        return 1
    return 0
