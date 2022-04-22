#HW:написать валидацию на Номера Транспартов будет класс ValidCarNumber —> будет метод
# is_valid(self, number) который принимает 1 аргумент number и проверяет на валидность то есть:
# Input: 01KG777BMW , hhh777hhh

import re
carNumber = input('ValidCarNumber:')
is_valid = re.search(r"[a-zA-Z0-9]+(BMW|hhh)", carNumber)
print(is_valid)

