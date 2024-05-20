from collections import Counter
import string


def get_count(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()
        text = text.lower()

        for val in string.punctuation + "—":
            text = text.replace(val, "")

        words = text.split()

        stop_words = ["a", "the", "по", "в", "за", "на", "о", "под", "с", "за", "между", "и", "а", "к", "но", "не", "у",
                      "от", "же", "из", "бы", "ли", "то", "что", "так", "это", "до", "над", "там", "чтобы", "со", "при",
                      "этого", "где", "ни", "чем", "он", "я", "его", "вы", "вам", "ему", "мне", "нам", "она", "ей", "ее",
                      "ты", "тебе", "сам", "уже", "меня", "ведь", "ну", "уж", "вот", "как", "всё", "себя", "вас", "того",
                      "него", "все", "тут", "во", "этот", "мы", "ней", "этом", "про", "себе", "тем", "тебя", "они",
                      "их", "или", "для", "эту", "них", "тот", "эти"]

        res = []
        word_occurance = Counter(text.split()).most_common()
        for word in word_occurance:
            if word[0].lower() in stop_words:
                continue
            if word[1] > 50:
                res.append(word)
        return res, words