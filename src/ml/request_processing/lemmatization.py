import pymorphy3

stopword1 = ['и', 'в', 'во', 'не', 'что', 'он', 'на', 'я', 'с', 'со', 'как', 'а', 'то', 'все', 'она', 'так', 'его',
             'но', 'да', 'ты', 'к', 'у', 'же', 'вы', 'за', 'бы', 'по', 'только', 'ее', 'мне', 'было', 'вот', 'от',
             'меня', 'еще', 'нет', 'о', 'из', 'ему', 'теперь', 'когда', 'даже', 'ну', 'вдруг', 'ли', 'если', 'уже',
             'или', 'ни', 'быть', 'был', 'него', 'до', 'вас', 'нибудь', 'опять', 'уж', 'вам', 'ведь', 'там', 'потом',
             'себя', 'ничего', 'ей', 'может', 'они', 'тут', 'где', 'есть', 'надо', 'ней', 'для', 'мы', 'тебя', 'их',
             'чем', 'была', 'сам', 'чтоб', 'без', 'будто', 'чего', 'раз', 'тоже', 'себе', 'под', 'будет', 'ж', 'тогда',
             'кто', 'этот', 'того', 'потому', 'этого', 'какой', 'совсем', 'ним', 'здесь', 'этом', 'один', 'почти',
             'мой', 'тем', 'чтобы', 'нее', 'сейчас', 'были', 'куда', 'зачем', 'всех', 'никогда', 'можно', 'при',
             'наконец', 'два', 'об', 'другой', 'хоть', 'после', 'над', 'больше', 'тот', 'через', 'эти', 'нас', 'про',
             'всего', 'них', 'какая', 'много', 'разве', 'три', 'эту', 'моя', 'впрочем', 'хорошо', 'свою', 'этой',
             'перед', 'иногда', 'лучше', 'чуть', 'том', 'нельзя', 'такой', 'им', 'более', 'всегда', 'конечно', 'всю',
             'между']
stopword2 = ["для", "быть", "если", "или", "который", "это", "при", "тот", "только", "как", "так", "он", "child", "toc",
             "наш", "также", "свой", "мы", "ваш", "однако"]
stopword = stopword1 + stopword2
str_to_replace = "!«»\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~\t\n\r\x0b\x0c\x0a\xa0–0123456789"
replace_dict = str.maketrans(str_to_replace, ' ' * len(str_to_replace))
morph = pymorphy3.MorphAnalyzer()


def remove_non_letters(text):
    '''
    -Заменяет все символы, которые не являются буквами, на пробелы, используя словарь "replace_dict".
    -Приводит все символы к нижнему регистру.
    -Удаляет пробелы в начале и конце строки.
    -Удаляет повторяющиеся пробелы внутри строки.
    '''
    text = text.translate(replace_dict)
    text = text.lower()
    text = text.strip()
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text


def get_normal_form(word):
    '''
    Возвращает нормальную форму слова, которая является его базовой формой (леммой), к которой приводится слово.
    '''
    return morph.parse(word)[0].normal_form


def lemma_text(text):
    '''
    Выполняет лемматизацию текста, то есть приводит все слова к их нормальной форме (лемме),
    удаляет стоп-слова и односимвольные слова, и возвращает отфильтрованный текст
    '''
    text = text.lower()
    for i in str_to_replace:
        text = text.replace(i, ' ')
    text = text.split()
    for i in range(len(text)):
        if text[i] in stopword or len(text[i]) == 1:
            text[i] = ""
        else:
            text[i] = get_normal_form(text[i])
            if text[i] in stopword or len(text[i]) == 1:
                text[i] = ""
    text = ' '.join(text)
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text

