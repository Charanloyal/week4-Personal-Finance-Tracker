def validate_amount(value):
    try:
        return float(value) > 0
    except ValueError:
        return False


def validate_text(text):
    return len(text.strip()) > 0