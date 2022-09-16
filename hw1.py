#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

some_list = 'абвнн секот вапкфиму трзабви вплнг апроабв кабвпро флпь'.split()
new_list = list(filter(lambda i: not 'абв' in i, some_list))
print(' '.join(new_list))

