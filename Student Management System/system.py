class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

new_class = class_1 + class_2

new_class.append('Peter Warden')

new_class.remove('Carla Gentry')

print(new_class)

courses = {'Math':65,'English':70,'History':80,'French':70,'Science':60}
variable = courses.values()

total = sum(variable)

print(total)

percentage = total / 5

print(percentage)

mathematics = {'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benijo':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}

names = list(mathematics.keys())
math_marks = list(mathematics.values())
top = max(math_marks)
ind = math_marks.index(top)
topper = names[ind]

 
first_name,last_name = topper.split(" ")

full_name = last_name + " " + first_name

print(full_name)

certificate_name = full_name.upper()

print(certificate_name)
