def emoji_convert(mess):
    words = mess.split(' ')
    emojis = {":)": "😁", ":(": "☹️", "<3": "❤️"}
    result = " "
    for word in words:
        result += emojis.get(word, word) + " "

    return result

