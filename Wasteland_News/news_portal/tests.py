from django.test import TestCase

# Create your tests here.
text = 'Полковник Мур поведает игроку, что она хочет убрать мистера Хауса. ' \
       'Для этого идите в Лаки 38 и поднимитесь на лифте до …'


def censor(text):
    cens_list = ['голову', 'убрать', 'полковник', 'шар', ]
    text_lower = text.lower()
    count = 0

    for i in range(len(text_lower)):
        for z in range(len(cens_list)):
            for x in range(len(cens_list[z])):
                if text_lower[i] == cens_list[z][x]:
                    try:
                        for g in range(len(cens_list[z])):
                            if text_lower[i + g] == cens_list[z][x + g]:
                                count += 1
                                if count == len(cens_list[z]):
                                    print(f"text_lower[i] = {text_lower[i]}")
                                    print(f"i = {i}")
                                    print(f"count = {count}")
                                    print(f"text[i+1:i+count] = {text[i+1:i+count]}")
                                    text = text.replace(text[i+1:i+count], '*'* (count-1))
                                    count = 0
                            else:
                                count = 0
                                continue
                    except IndexError:
                        continue
                else:
                    count = 0
    return text

print(censor(text))