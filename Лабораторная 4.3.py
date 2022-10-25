
def delete(list_, index=None):
    list_[:index] + list_[index:]
    if index != None:
        #list_.remove(index)
        x = list_[:index] + list_[index +1:]
    else:
       x = list_[:-1]
    return x

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

#проверка
print(delete([0,0,0,0,5], index=2))

#либо через remove
#def delete(list_, index=None):
    #list_[:index] + list_[index:]
    #if index != None:
        #x = list_.pop(index)
        #x = list_[:index] + list_[index:]
    #else:
       #x = list_[:-1]
    #return x
# Не до конца поняла задание - по заданию написано, что "по умолчанию удаляется последний элемент из списка"
# но в ожидаемых ответах последний элемент удаляется только там, где не указан индекс
# Опять же, если смотреть на исходные комментарии после принт
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 3]
# То можно понять, что последний элемент удаляется в ЛЮБОМ списке - указан там индекс или нет