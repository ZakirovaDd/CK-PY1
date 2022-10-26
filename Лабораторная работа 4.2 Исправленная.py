def get_count_char(str_):
    clear_str = "".join(a for a in str_ if a.isalpha())
    clear_str = clear_str.lower()
    def_count = 0
    dict = {

    }
    for i in clear_str:
        dict[i] = dict.get(i, def_count) + 1
        x = dict

    return x

def prozent_bukv(dict):
    dict_new = get_count_char(dict)
    for i in dict_new:
        DEF_COUNT = sum(dict_new.values())
        dict_new[i] = round(dict_new.get(i) / DEF_COUNT*100,1)

    return dict_new

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(prozent_bukv(main_str))

