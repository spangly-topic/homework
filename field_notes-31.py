# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: FieldNotes
import json, os

DEFAULT = {"profile": "default", "name": "", "color": "#2196F3"}
PROFILES_FILE = "./profiles.json"


def load_profiles():
    try: return json.load(open(PROFILES_FILE))
    except FileNotFoundError: return {}


def save_profiles(data):
    os.makedirs(os.path.dirname(PROFILES_FILE) or ".", exist_ok=True)
    with open(PROFILES_FILE, "w") as f:
        json.dump(data, f)


def get_active_profile():
    profiles = load_profiles()
    active = profiles.get("active", "default")
    return profiles.get(active, DEFAULT.copy())


def set_active_profile(name):
    profiles = load_profiles()
    if name not in profiles:
        profiles[name] = DEFAULT.copy()
    profiles["active"] = name
    save_profiles(profiles)
