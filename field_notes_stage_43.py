# === Stage 43: Добавь пагинацию длинных списков ===
# Project: FieldNotes
def paginate(items, page_size=10, page=1):
    """Return a dict with page data for long lists."""
    total_pages = (len(items) + page_size - 1) // page_size
    start = (page - 1) * page_size
    end = start + page_size
    page_items = items[start:end]
    return {
        "items": page_items,
        "page": page,
        "total_pages": total_pages,
        "total": len(items),
    }
