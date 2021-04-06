twitter_link = {
    "regex_description": "Twitter link must be a valid twitter link to a twitter user",
    "expression": r"^(http(?:s))?:\/\/(?:www\.)?twitter\.com\/([a-zA-Z0-9_]+)$" 
}

youtube_link = {
    "regex_description": "Youtube link must be a valid link to a youtube channel",
    "expression": r"(https?:\/\/)?(www\.)?youtube\.com\/(channel|user)\/[\w-]+"
}

facebook_link = {
    "regex_description": "Facebook url must be a valid URL",
    "expression": r"(?:https?:\/\/)?(?:www\.)?facebook\.com\/.(?:(?:\w)*#!\/)?(?:pages\/)?(?:[\w\-]*\/)*([\w\-\.]*)"
}

instagram_link = {
    "regex_description": "Instagram link must be a valid instagram profile url",
    "expression": r"^(http(?:s))?:\/\/(?:www\.)?instagram\.com\/([a-zA-Z0-9_]+)$"
}
