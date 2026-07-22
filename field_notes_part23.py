# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: FieldNotes
def render_table(records):
    if not records:
        print("Нет данных.")
        return
    headers = list(records[0].keys())
    widths = {h: len(str(h)) for h in headers}
    for r in records:
        for i, v in r.items():
            w = len(str(v)) if v is not None else 4
            widths[i] = max(widths[i], w)

    lines = []
    sep = "─" * sum(widths.values()) + "┬" * (len(headers) - 1) + "┘"
    header_line = "│" + "─" * widths[headers[0]] + "┼" + "".join(f"─{w}" for w in list(widths.values())[1:]) + "┘"

    lines.append(sep)
    lines.append("│" + headers[0].ljust(widths[headers[0]]) + "│" + "".join(h.ljust(w) for h, w in zip(headers[1:], widths[1:])))
    lines.append(header_line)
    for r in records:
        row = []
        for i, v in r.items():
            val = str(v) if v is not None else "-"
            row.append(val.ljust(widths[i]))
        lines.append("│" + "│".join(row))
    lines.append(sep)

    print("\n".join(lines))


render_table(table_data)
