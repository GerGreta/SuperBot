# logic_number.py
rus_letters = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5, 'Е': 6, 'Ё': 7,
    'Ж': 8, 'З': 9, 'И': 1, 'Й': 2, 'К': 3, 'Л': 4, 'М': 5,
    'Н': 6, 'О': 7, 'П': 8, 'Р': 9, 'С': 1, 'Т': 2,
    'У': 3, 'Ф': 4, 'Х': 5, 'Ц': 6, 'Ч': 7, 'Ш': 8,
    'Щ': 9, 'Ъ': 1, 'Ы': 2, 'Ь': 3, 'Э': 4, 'Ю': 5, 'Я': 6
}

eng_letters = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
    'H': 8, 'I': 9, 'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5,
    'O': 6, 'P': 7, 'Q': 8, 'R': 9, 'S': 1, 'T': 2,
    'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
}

def detect_language(word):
    if word and word[0].upper() in rus_letters:
        return "rus"
    elif word and word[0].upper() in eng_letters:
        return "eng"
    return None

def word_to_sum(word: str) -> int | None:
    lang = detect_language(word)
    word = word.upper()
    if lang == "rus":
        return sum(rus_letters.get(ch, 0) for ch in word)
    elif lang == "eng":
        return sum(eng_letters.get(ch, 0) for ch in word)
    return None

def reduce_to_single_digit(n: int) -> int:
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n
