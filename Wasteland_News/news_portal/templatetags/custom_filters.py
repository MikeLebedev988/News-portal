from django import template

register = template.Library()


@register.filter()
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
                                    text = text.replace(text[i+1:i+count], '*' * (count-1))
                                    count = 0
                            else:
                                count = 0
                                continue
                    except IndexError:
                        continue
                else:
                    count = 0
    return text
