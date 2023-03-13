valid_schema = {
    "type": "object",
    "properties": {
        "code": {"type": "number"},
        "type": {"type": "string"},
        "message": {"type": "string"},
    },
    "required": ["message", "type", "code"]
}
