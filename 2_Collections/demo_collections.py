#! /usr/bin/python
# Author: QA2.0 LIVE, V1.0
# Description: This program will 
"""
    Docstring: This program/module will..
"""
name_1= 'Naomi'
name_2= "Derrek"
name_3= "Paul"

name_tuple = 'Naomi', "Derrek", "Paul"
name_tuple2 = ('Ricky', "Simon", "Andrew")
print(type(name_tuple))
print(name_tuple)
print(type(name_tuple2))
print(name_tuple2)
print(name_tuple[0])
name_list = ['Naomi', "Derrek", "Paul"]
print(name_list)
print(type(name_list))
name_list[2] = "Victoria"
print(name_list)
name_list.append("Paul")
print(name_list)
last_person=name_list.pop()
print(name_list)
print(f"The person removed is : {last_person}")

people_dict = {'Andrew': 1, 'Derrek': 2, 'Ricky': 3}
print(people_dict)
print(people_dict.keys())
print(people_dict.values())