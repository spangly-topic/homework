# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: FieldNotes
class ValidationError(Exception): pass

def validate_input(data: dict) -> bool:
    if not isinstance(data, dict): return False
    required = ['location', 'category', 'notes']
    for key in required:
        if key not in data or not isinstance(data[key], str): raise ValidationError(f"Missing/Invalid {key}")
        if len(data[key]) < 1 or len(data[key]) > 500: raise ValidationError(f"{key} length out of bounds")
    return True

def sanitize_input(raw_data: dict) -> dict:
    try: validate_input(raw_data)
    except ValidationError as e: print(e); exit(1)
    cleaned = {k: v.strip() for k, v in raw_data.items()}
    if not cleaned['location'].lower().startswith(('russia', 'moscow')): raise ValidationError("Invalid location prefix")
    return cleaned
