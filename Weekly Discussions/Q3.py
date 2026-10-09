animals = ["cat", "dog", "manta ray", "horse", "crouching tiger"]

for i in range(len(animals)):
    print(animals[i])

countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
the_fifth_element = -999

countdown = sorted(countdown, reverse = True)

the_fifth_element = countdown[4]
print(the_fifth_element)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)

list2 = [5, 20, 30, 15, 20, 30, 20]

while ( 20 in list2): 
    list2.remove(20)

print(list2)

dict = {"Course": "DATA 606", "Program": "MSDS", "School": "CUNYSPS"}

print(dict["Course"])
dict["Course"] = "DATA 602"

dict["Professor"] = "Schettini"

print(dict)

print(len(dict))

sample_dict = {
    'emp1': {'name': 'Amanda', 'salary': 8200},
    'emp2': {'name': 'John', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 700}
}

sample_dict["emp3"]["salary"] = 7500

print(sample_dict["emp3"])