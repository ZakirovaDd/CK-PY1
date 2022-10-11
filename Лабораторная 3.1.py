src = not False and True or False and not True

result = True and True or False and False # в первую очередь избавляемся от отрицаний
result = True or False # избавляемся от логического "И"
result = True # Избавляемся от логического "или"

print(src == result)
