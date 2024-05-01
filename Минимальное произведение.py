'''
Задача A. Найди кота

Маша много читает, и, когда она видит какое-то длинное слово, она любит играть в игру «найди
кота». Для того, чтобы найти кота в слове, нужно найти в нем буквы К, О и Т в правильном порядке.
Например, кота можно найти в слове «КОмпьюТер» или «блоКнОТ».
Сейчас Маша учит английский язык, поэтому она хочет научиться искать котов и в английских
словах. Для того, чтобы найти кота в английском слове, нужно найти в нем буквы C, A и T в
правильном порядке. То есть, C должна идти перед A, а A — перед T. Например, «ClAssmaTe» или
«sCrATch». Помогите ей.
'''
data = input("Введите n и k через запятую\n")
data = data.split(" ")


n = int(data[0])

k = int(data[1])

elements = input("Введите элементы n:\n")
elements = elements.split(" ")

for i in range(0,len(elements)):
    elements[i] = int(elements[i])


min = elements[0] + elements[1]
for i in range(0,len(elements)-1):

    for y in range(i+1,len(elements)):
        if elements[i] * elements[y] < min and k <= abs(i-y):
            min = elements[i]*elements[y]
        print(f'a[{i}] * a[{y}] = {elements[i]*elements[y]}')
print(f'min = {min}')

