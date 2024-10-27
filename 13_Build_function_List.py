students = ['ram', 'sita', 'shyam', 'sapana', 'bipana']
course = ['basic', 'diploma', 'graphics', 'tally']

print(len(students))

# append in last
students.append('samjhana')

# extend merge two list
students.extend(course)
print(students)

# insert between
students.insert(2,'kamal')
print(students)

# count no of elements and no print error print 0
print(students.count('kamal'))

# index location of elements and print error

# #remove 
students.remove('kamal')
print(students)

# pop display value and remove 
students.pop()
print(students)

# Reverse the elements of list
students.reverse()
print(students)

# short assending form
students.sort()
print(students)

students.sort(reverse=True)
print(students)

marks = [5, 15, 87, 69, 35, 85]
print(min(marks))
print(max(marks))
print(sum(marks))
print(len(marks))
print(id(marks))
