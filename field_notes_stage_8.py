# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: FieldNotes
def run_cli():
    print("=== FieldNotes CLI ===")
    while True:
        cmd = input("\nКоманда (1-4, q=выход): ").strip()
        if not cmd or cmd == 'q': break
        elif cmd in ('1', '2', '3'): print(f"Функция {cmd} скоро будет доступна.")
        else: continue
