def validate_todo_data(data: dict) -> bool:
    return "title" in data and isinstance(data["title"], str)
