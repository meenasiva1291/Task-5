#dictionary list containing details
dict_ = {"name": "john", "age": 20}
dict_1 = {"name": "peter", "age": 15}
dict_2 = {"name": "vishnu", "age": 5}
dict_3 = {"name": "meena", "age": 30}
dict_4 = {"name": "siva", "age": 18}
dict_5 = {"name": "sankar", "age": 60}
#Make it as a list and assign to variable
people = [dict_, dict_1, dict_2, dict_3, dict_4, dict_5]
#Declare variable with empty dict to store new filtered values
new_dict = {}
# Lambda function to filter and add to new_dict
list(filter(lambda person: new_dict.update({person["name"]: person["age"]}) if person["age"] > 18 else False, people))
#print the new dict
print(new_dict)




