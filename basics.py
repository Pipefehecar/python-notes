# integers
a = 100_5934
print(a + 1)
print("\n")

# strings
text = 'my text is "this"'
print(text)
print("\n")

# lists
people: list[str] = ["Mario", "Luigi", "Peach", "Toad"]
print(people[-1])  # Toad
print(people[0:2])  # Mario and luigi
print(people[0:4])  # All
print(people[2:4])  # Peach and Toad

people[0:2] = ["Shy Guy", "Wario"]
print(people)

people.insert(2, "!!!")
print(people)

print("\n")
people2: list[str] = ["Bowser", "Koopa", "Goomba"]
people.extend(people2)
print(people)
people.remove("Koopa")  # by value
people.pop(0)  # by index
print(people)
people.clear()  # remove all
people.reverse()  # reverse
people.sort()  # sort

# tuples
people: tuple[str, str, str] = ("Mario", "Luigi", "Peach")
print(people.count("Mario"))
people = list(people)
people.append("Mario")
people = tuple(people)
print(people.count("Mario"))

# dicts
people_dict: dict = {"person1": "Mario", "person2": "Luigi"}
print(people_dict.setdefault("person3"))
print(people_dict)

# loops
for i in range(10):
    print(i, end="\t")
    # if i == 5:
    #     break
else:
    print("\n...Loops ends without interruptions")


# funtions
def greeting(name: str): # here is a parameter
    print(name.capitalize)

greeting('Luis') # here is an argument
# functions: parameters and arguments


