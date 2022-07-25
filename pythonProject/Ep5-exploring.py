## We can create an empty tuple with this syntax:

my_tuble = ()
my_set = {}

int_tuple = (1, 2, 3, 4, 5)
string_tuple = ("eye", "nose", "mouth", "ear")
mixed_set = (10, "test", 1.75)

#add element to set
num_set = {10, 30, 40, 50}
num_set.add(20)
print(num_set)

#update element to set
num_set = {2, 4, 6}
num_set.update([1, 3, 5])
print(num_set)

#remove specific element
num_set = {10, 20, 30, 40, 50}
num_set.remove(20)
print(num_set)

#clear all elements
num_set = {10, 20, 30, 40, 50}
num_set.clear()
print(num_set)

#union operator - merge unique elements
set1 = {1,2,3}
set2 = {1,2,4}

set1.union(set2) #1,2,3,4
set1|set2 #1,2,3,4

#intersection - หาค่าที่เหมือนกันในทั้ง 2 set
set1 = {1,2,3}
set2 = {1,2,4}
set1&set2

#difference - หาค่าที่มีใน set1 แต่ไม่มีใน set2
set1 = {1,2,3}
set2 = {1,2,4}
set1.difference(set2)

set1-set2

#symmetric - หาค่าที่ไม่มีของทั้ง 2 set เช่นมีใน 1 แต่ไม่มีใน 2 กับ มีใน 2 แต่ไม่มีใน 1
set1 = {1,2,3}
set2 = {1,2,4}
set1.symmetric_difference(set2)

#In / Not In - หาค่าที่ถูกต้องในแต่ละ set และ return ออกมาเป็น true / false
set1 = {1,2,3}
set2 = {1,2,4}

1 in set1
#true

set1 = {1,2,3}
set2 = {1,2,4}
3 in set2
#false

#dictionary
dict_name = {key1:value1, key2:value2}
my_dictionary = {"name":"Keith","subject":"Python","score":97.50, "ranking":1}

#get method
my_dictionary = {"name":"Keith","subject":"Python","score":97.50, "ranking":1}
my_dictionary.get('name')

#add new value
my_dictionary = {"name":"Keith","subject":"Python","score":97.50, "ranking":1}
my_dictionary['result'] = 'pass'
print(my_dictionary)
#add KEY result VALUE pass to the set

my_dictionary = {"name":"Keith","subject":"Python","score":97.50, "ranking":1}
my_dictionary['score'] = '98'
print(my_dictionary)
#update KEY score VALUE from 97.50 to 98

#delete key-value pair from dictionary
my_dictionary = {"name":"Keith","subject":"Python","score":97.50, "ranking":1}
my_dictionary.pop('subject')
#it will drop subject python from the set

#clear all key
my_dictionary = {"name":"Keith","subject":"Python","score":97.50, "ranking":1}
my_dictionary.clear()
#it will removed all value keys

my_dictionary1 = {"name":"Keith","subject":"Python","score":97.50, "ranking":1}
my_dictionary2 = {"surname":"Williams", "Grade":5, "Score":98}
my_dictionary1.update(my_dictionary2)
#it will update score to 98 and add surname Williams and Grade to the set

my_dictionary = {"name":"Keith","subject":"Python","score":97.50, "ranking":1}
my_dictionary.items()
#it will return all items list in the dictionary

my_dictionary.values()
#it will return all value list in the dictionary

my_dictionary.keys()
#it will return all keys list in the dictionary

#Check membership in a Dictionary
'name' in my_dictionary
#True
'subject' not in my_dictionary
#False

my_dictionary = {"name":"Keith","subject":"Python","score":97.50, "ranking":1}
len(my_dictionary)
#will give 4

pair_list = {('red','apple'), ('yellow','banana'), ('green','kiwi')}
new_dict = dict(pair_list)
print new_dict
