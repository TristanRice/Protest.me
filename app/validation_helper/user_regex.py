password = {
    "regex_description": "Password must contain eight characters, at least one letter and one number",
    "expression": "(?=.*[_!@#$%^&*-])(?=.*[0-9])(?!.*[.\n])(?=.*[a-z])(?=.*[A-Z])^.{8,}$"
}

username = {
    "regex_description": "Username must only contain alphanumeric characters and underscores, and be between 4 and 32 characters",
    "expression": "^[a-zA-Z0-9_]{4,32}$"
}
