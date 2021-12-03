# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 03:42:22 2021

@author: hp
"""

# Name - 
# Roll No - 

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''


# Write the code here for creating an interactive program.
import json
import a2
file_path="data.json"
with open(file_path,'r') as data:
    records=json.load(data)
print("""
*********************************************************************    

*****************   WELCOME TO OFFICIAL REGISTER  *******************   

*********************************************************************
                    
1.      Read the data.json file, and convert it into a dictionary

2.      Search the records to find all persons with the first name            

3.      Search the records to find all persons with the last name         

4.      Search the records to find all persons with the full name      

5.      Search the records to find all persons whose age lies in the 
        given age range      

6.      Count the number of males and females      

7.      Filter the person records whose address matches the given 
        address     

8       Find all the alumni of the given institute name

9.      Find topper of each institute     

10.     Find all donors who can donate blood to the person with the 
        given receiver ID.     

11.     Find the common friends of all the people with the given IDs     

12.     Check if 2 persons are friends     

13.     Delete a record from the records register   

14.     Make 2 people friends of each other     

15.     Remove friends from the record

16.     Add an education record
 
********************************************************************""")
records= a2.read_data_from_file()

while(True):
    i=input("Enter your querry, press -1 to exit:        ")
    if i=="-1":
        break
    elif i=="1":
        records= a2.read_data_from_file()
    elif i=="2":
        first_name=input("Enter the first name you want to search in records:  ")
        print("The ids of people with the name ",first_name,"are ",a2.filter_by_first_name(records,first_name))
        if(a2.filter_by_first_name(records, first_name)==[]):
           print("Sorry, no person with the name",first_name,"found")
    elif i=="3":
        last_name=input("Enter the last name you want to search in the records")
        print("The ids of people with the last name ",last_name,"are",a2.filter_by_last_name(records,last_name))
        if(a2.filter_by_last_name(records, last_name)==[]):
           print("Sorry, no person with the last name",last_name,"found")
        
    elif i=="4":
        full_name=input("Enter the name you want to search in the records, space separated: ")
        print("The ids of people with thelast name ",full_name,"are",a2.filter_by_full_name(records, full_name))
        
        if(a2.filter_by_full_name(records, full_name)==[]):
           print("Sorry, no person with the name",full_name,"found")
    elif i=="5":
        min_age=int(input("Enter min age: "))
        max_age=int(input("Enter max age: "))
        k=a2.filter_by_age_range(records, min_age,max_age)
        if(k==[]):
           print("Sorry, no person within the range",min_age,max_age,"found")
        else:
             print("The ids of people with thelast name ",full_name,"are", k)
    elif i=="6":
        print(a2.count_by_gender(records))
    elif i=="7":
        address={}
        house_no=(input("Enter house no , else leave blank"))
        if house_no:
            address["house_no"]=int(house_no)
        block=input("Enter block , else leave blank")
        if block:
            address["block"]=block
        town=input("Enter town, else leave blank"  )
        if town:
            address["town"]=town
        city=input("Enter city, else leave blank ") 
        if city:
            address["city"]=city
        state=input("Enter state, else leave blank ")
        if state:
            address["state"]=state
        pincode=(input("Enter pin code, else leave blank " ))
        if pincode:
            address["pincode"]=int(pincode)
        print(address)              
        print(a2.filter_by_address(records, address))
        
    elif i=="8":
        institute_name=input("Enter institute name: ")
        print(a2.find_alumni(records, institute_name))
    elif i=="9":
        print(a2.find_topper_of_each_institute(records))
    elif i=="10":
        receiver_person_id=int(input("Enter the blood receiver id: "))
        k=0
        for i in records:
        
            if receiver_person_id == i["id"]:
                k=1
                break
        if k!=1:
                print("Invalid id")
        else:
                 print("These are the potential donees and their contact nos:   ","\n",a2.find_blood_donors(records, receiver_person_id))
                 
    elif i=="11":
        list_of_ids=list(map(int,input("Enter the list of ids(space separated):  ").split()))
        for ids in list_of_ids:
            for i in records:
                if ids == i["id"]:
                    k=1
                    break
        if k!=1:
                print("Invalid id entered.")
        else:
                print("The IDs of all the common friends of the specified list of people ",a2.get_common_friends(records,list_of_ids))
    elif i=="12":
        pass
    #not attempted
     
    elif i=="13":
        person_id=int(input(("Enter the person's id to be deleted :  ")))
        
        for i in records:
                if person_id == i["id"]:
                    k=1
                    break
        if k!=1:
                print("Invalid id entered.")
        else:
            print(""""The updated list is""",
                  a2.delete_by_id(records, person_id))
    elif i=="14":
        person_id=int(input("Enter the person's id: "))
        friend_id=int(input("Enter the friends's id: "))
        for i in records:
                if person_id == i["id"]:
                    k=1
                    break
        k=0
        for i in records:
                if friend_id == i["id"]:
                    k=1
                    break
        if k!=1:
                print("Invalid id entered.")
        
        else:
             print(a2.add_friend(records, person_id, friend_id))
                
       
    elif i=="15":
         person_id=int(input("Enter the person's id: "))
         friend_id=int(input("Enter the friends's id: "))
         for i in records:
                if person_id == i["id"]:
                    k=1
                    break
         k=0       
         for i in records:
                if friend_id == i["id"]:
                    k=1
                    break
         if k!=1:
                print("Invalid id entered.")
        
         print(a2.remove_friend(records, person_id, friend_id))
    elif i=="16":
        person_id=int(input(("Enter the person's id: ")))
        institute_name=input("Enter the institute name: ")
        ongoing=(input("Is it ongoing ?(Enter only 'True' or 'False':  "))
        if ongoing=="True" or "true":
            ongoing=True;
            percentage=0
        
        if ongoing=="False" or "false":
            percentage=float(input("Enter the percentage"))
            ongoing=False
        
            
        
        print(a2.add_education(records, person_id, institute_name, ongoing, percentage))
     
print("Thankyou for Visiting !")







