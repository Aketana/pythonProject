
# print 5
nested_list = ['Monday', [1, 2, 3, 4, 5]]
nested_list[-1]

## print Monday
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekday[0]

## append method - adding 1 element to a list
num_list = [10, 20, 30, 40, 50]
num_list.append(60)
print(num_list)

## extend method - add 2 or more elements to a list
num_list = [10, 20, 30, 40, 50]
num_list.extend([60, 70, 80, 90, 100])
print(num_list)

## insert method - insert elements to specific index
num_list = [1, 2, 4, 8, 9, 10]
num_list.insert(2, 3)
print(num_list)

## insert range of elements to a specific index in a list - list[index:number of element]
num_list = [1, 2, 3, 4, 8, 9, 10]
num_list[4:3] = [5, 6, 7]
print(num_list)

## changing an element in a list - num_list[index] = element
num_list = [10, 20, 30, 40, 50]
num_list[0] = 0
print(num_list)

# changing a range of element in a list num_list[index:number of element] = elements
num_list = [10, 20, 30, 40, 50]
num_list[0:3] = [0, 1, 2]
print(num_list)

#combine 2 variable together
weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
week = weekday+weekend
print(week)

#repeating list [element]*3 means will print 3 times
num_list = [1, 2, 3, 4, 5]*3
print(num_list)

#delete element
num_list = [10, 20, 30, 40, 50]
num_list.remove(20)
print(num_list)

#delete by index list.pop(specific index)
num_list = [10, 20, 30, 40, 50]
num_list.pop(0)
print(num_list)

#delete elements by range
num_list = [10, 20, 30, 40, 50] # delete index 1
del num_list[1]
print(num_list)

#delete elements by index and elements
num_list = [10, 20, 30, 40, 50] ## delete from index 0 by 2 elements
del num_list[0:2]
print(num_list)

#clear elements from a list
num_list = [10, 20, 30, 40, 50]
num_list.clear()
print(num_list)

#clear elements with empty space
num_list = [10, 20, 30, 40, 50]
num_list[:] = []
print(num_list)


#check membership in a lists
num_list = [10, 20, 30, 40, 50]
40 in num_list

50 not in num_list

weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
"Friday" in weekday
"Sunday" not in weekday