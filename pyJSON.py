#
import json

#
data1 = {

    'name':'Hajja Trawally',
    'age':30,
    'city':'Seattle, WA',
    'interests':['Reading', 'Writing','Soccer','Shopping','Baking','Jogging'],
    'is_student': True

}


#
with open('data1.json','w') as json_file:

    #Dump the Data Dictionary into the JSON file:
    json.dump(data1,json_file,indent=4)
    
    print("You have successfully written to data1.json")
    

    