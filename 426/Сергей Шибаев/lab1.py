import datetime as dt
import random
import queue

#входные
school_rates = {'Russian': 4,
'Literature': 5,
'Algebra': 5,
'Geometry': 4,
'History': 5,
'Geography': 5,
'Physics': 5,
'Biology': 4,
'Chemistry': 4,
'Computer science': 5,
'English': 5,
'Black Speech': 4,
'Sindarin': 4,
'Khuzdul': 5}

names = ['Ivan', 'Aleksandr', 'Sergey', 'Andrey', 'Dmitriy', 'Aleksey', 'Maksim', 'Evgeniy', 'Vladimir', 'Denis']
surnames = ['Ivanov', 'Petrov', 'Smirnov', 'Sergeev', 'Vasilyev', 'Kuznetsov', 'Andreev', 'Popov']
random_names = [names[random.randint(0, len(names) - 1)] + ' ' + surnames[random.randint(0, len(surnames) - 1)]
for i in range(30)]

western_actor = ('Joel McCrea', dt.datetime(1905, 10, 20))

home_tamandua = 'Smaug the Mighty'

#задание 1
print('задание 1')
print('Average rate: ', sum(school_rates.values())/len(school_rates), '\n')

#задание 2
print('задание 2')
unique_names = []
for name in random_names:
if name in unique_names:
continue
else:
unique_names.append(name)
print(len(unique_names), 'Unique names:', unique_names, '\n')

#задание 3
print('задание 3')
print("All subject's length: ", len("".join(school_rates.keys())), '\n')

#задание 4
print('задание 4')
all_letters = []
for key in school_rates:
unique_letters = ''
for letter in key:
if letter in unique_letters:
continue
else:
unique_letters += letter
all_letters += [unique_letters]
print('Unique letters in subjects:', all_letters, '\n')

#задание 5
print('задание 5')
binary_tamandua = [bin(ord(letter))[2☺ for letter in home_tamandua]
print('Binary name of tamandua :', binary_tamandua, '\n')
#for elem in binary_tamandua: #выведет имя тамандуа обратно
# print(chr(int(elem,2)))

#задание 6
print('задание 6')
print('Days since birthday of', western_actor[0], ':', dt.datetime.today() - western_actor[1], '\n')

#задание 7
print('задание 7')
build_materials = queue.Queue()
material = ''
while material != '0':
material = input("Enter materials(0 = exit):")
if material != '0': build_materials.put(material)
print(build_materials.queue, '\n')

#задание 8
print('задание 8')
year, month, day = western_actor[1].year, western_actor[1].month, western_actor[1].day
number = (day + month**2 + year) % 39 + 1 # =37
chinese_emperor = 'Чжоу Нань-ван'
index = int(input('Enter index(0-29):'))
random_names.sort()
random_names[index] = chinese_emperor
print(random_names, '\n')

#задание 9
print('задание 9')
middle_earth_realms = ['Lindon', 'Arnor', 'The Shire', 'Eriador', 'Moria', 'Rohan', 'Gondor', 'Mordor',
'Rhovanion', 'Erebor', 'Rivendell']
class Node:
def init(self, data=None):
self.data = data
self.next = None

class LinkedList:
def init(self):
self.head = None

def append(self, data):
new_node = Node(data)
if self.head is None:
self.head = new_node
else:
current_node = self.head
while current_node.next:
current_node = current_node.next
current_node.next = new_node

def remove(self, index):
step = 0
if index == 0:
self.head.data = "Конец"
else:
current_node = self.head
while step < index:
current_node = current_node.next
step += 1
current_node.data = "Конец"

def destroy(self, value):
if self.head.data == value:
self.head = self.head.next
return

current = self.head
while current:
if current.data == value:
break
previous = current
current = current.next
if current is None:
