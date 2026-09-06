# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: FieldNotes
def dry_run(mode='write', action='insert', table=None, **kwargs):
    """Демон-режим: записывает операции в отдельный файл, не в БД."""
    import os, sys, json
    if not os.path.exists('dry_run.log'):
        open('dry_run.log', 'w').close()
    with open('dry_run.log', 'a') as f:
        f.write(json.dumps({'mode': mode, 'action': action, 'table': table, 'data': kwargs}, default=str))
        f.write('\n')
    print(f"[DRY-RUN] {mode} -> {action} on {table}: {kwargs}")
    return True
