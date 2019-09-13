
def sqlescape(str):
    return str.translate(
        str.maketrans({
            "\0": "\\0",
            "\r": "\\r",
            "\x08": "\\b",
            "\x09": "\\t",
            "\x1a": "\\z",
            "\n": "\\n",
            "\r": "\\r",
            "\"": "",
            "'": "",
            "\\": "\\\\",
            "%": "\\%"
        }))
