# display the "zen of python" (Tim Peters)
import this

message = ("Hello World!!")
print(message)

message = ("Hello again, world!!")
print(message)

name = "Zizi" + " " + "tripo"
print(name.title())
print(name.upper())
print(name.lower())

white_space_name = " moe green "
print("With whitespace: " + white_space_name + ".")
print("Without right whitespace: " + white_space_name.rstrip() + ".")
print("Without left whitespace: " + white_space_name.lstrip() + ".")
print("Without any whitespace: " + white_space_name.strip() + ".")

# testing some nice string effects
# and type casting
example_header = "To do:"
python_version = 3.7
example_item1 = "learn python " + str(python_version)
example_item2 = "excercize"
example_item3 = "play around with 'git'"
print("\n" + example_header.title() +"\n\t" + example_item1 + "\n\t" + example_item2 + "\n\t" + example_item3 + "\n\n")

operating_systems = ['ubuntu','macOS','linux','windows']
print(operating_systems[0])
# accessing the last item on a list by index "-1":
# in genereal, negative indexes just count from the end
# i.e. "-2" returns the 2nd item from the end
print(operating_systems[-1]) 
operating_systems.append('sunOS')
print(operating_systems[-1]) 
# emptying the list
# operating_systems = []
operating_systems.insert(0,'high sierra')
operating_systems.insert(0,'snow leopard')
print(operating_systems)
# deleting an item with a known index:
del operating_systems[2]
print(operating_systems)
popped_OS = operating_systems.pop()
print (popped_OS + " was 'popped'")
print(operating_systems)
operating_systems.append(popped_OS)
print(operating_systems)
# poping a specific list item by index
popped_OS = operating_systems.pop(0)
print (popped_OS + " was 'popped'")
print(operating_systems)
# removing item specifically by its value
# note: this only removes the 1st occurence of this value
operating_systems.remove('windows')
print(operating_systems)
# and now to sort the lis alphabetically:
print(sorted(operating_systems, reverse = True))
print(operating_systems)
operating_systems.sort()
print(operating_systems)
# reverse does not sort, it just reverses the existing order
operating_systems.reverse()
print(operating_systems)
print("We are discussing " + str(len(operating_systems)) + " different operating systems.")



