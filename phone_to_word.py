def phone_number_to_word(phone):
    numbers = {"1": "One", "2": "Two", "3": "Three",
               "4": "Four", "5": "Five", "6": "Six",
               "7": "Seven", "8": "Eight", "9": "Nine"
               }
    word = " "

    for ch in phone:
        word += numbers.get(ch, "!") + " "

    return word




