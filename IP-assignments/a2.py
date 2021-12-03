# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 02:32:41 2021

@author: hp
"""

# Assignment - 2
# Name - Shagun Mohta
# Roll No - 2020468

import json


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''

def read_data_from_file(file_path="data.json"):
    '''
    **** DO NOT modify this function ****
    Description: Reads the data.json file, and converts it into a dictionary.

    Parameters: 
    - file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

    Returns:
    - A dictionary containing the data read from the file
    '''
    
    with open(file_path, 'r') as data:
        records = json.load(data)

    return records


def filter_by_first_name(records, first_name):
    '''
    Description: Searches the records to find all persons with the given first name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - first_name (STRING): The first name

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given first name
        Case 1: No person found => Returns an empty list
        Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''
    id_list=[]
    for i in records:
        if i["first_name"]==first_name.capitalize():
            id_list.append(i["id"])
    return id_list
            
            


            
            
            
            


def filter_by_last_name(records, last_name):
    '''
    Description: Searches the records to find all persons with the given last name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - last_name (STRING): The last name

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given last name
        Case 1: No person found => Returns an empty list
        Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''
    id_list=[]
    for i in records:
        if i["last_name"].lower()==last_name.lower():
            id_list.append(i["id"])
    return id_list


def filter_by_full_name(records, full_name):
    '''
    Description: Searches the records to find all persons with the given full name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given full name
        Case 1: No person found => Returns an empty list
        Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''
    id_list=[]
    for i in records:
        if i["first_name"].lower()+" "+ i["last_name"].lower()==full_name.lower():
            id_list.append(i["id"])
    return id_list


def filter_by_age_range(records, min_age, max_age):
    '''
    Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - min_age (INTEGER): The minimum age (inclusive)
    - max_age (INTEGER): The maximum age (inclusive)

    Note: 0 < min_age <= max_age

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given full name
        Case 1: No person found => Returns an empty list
        Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''
    id_list=[]
    for i in records:
        if 0<min_age<=i["age"]<=max_age:
            id_list.append(i["id"])
    return id_list
            
        


def count_by_gender(records):
    '''
    Description: Counts the number of males and females

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)

    Returns:
    - A dictionary with the following two key-value pairs:
        KEY        VALUE
        "male"     No of males (INTEGER)
        "female"   No of females (INTEGER)
    '''
    male=0
    female=0
    for i in records:
        if i.get("gender")=="male" :
            male=male+1
        elif i["gender"]=="female":
            female=female+1
    dict1={"male":male,"female":female}
    return dict1

def filter_by_address(records, address):
    '''
    Description: Filters the person records whose address matches the given address. 

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
        Some examples are:
            Case 1: {} 
                => All records match this case
            
            Case 2: { "block": "AD", "city": "Delhi" } 
                => All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)
            
            Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

    Returns:
    - A LIST of DICTIONARIES with the following two key-value pairs:
        KEY            VALUE
        "first_name"   first name (STRING)
        "last_name"    last name (STRING)
    '''
    list1=[];
    
    if address=={}:
        for i in records:
            dict1={}
            dict1["first_name"]=i["first_name"]
            dict1["last_name"]=i["last_name"]
            list1.append(dict1)
        return list1
    
    for i in records:
        a=0
        for key in address:
            if key=="house_no":
                
                    if int(address[key]!=(i["address"])["house_no"]):
                        a=1
                    
            elif key=="block" :
                   
                       if str(address[key].lower()!=(i["address"])["block"].lower()):
                           a=1
                           
            elif key=="town":
                 
                     if str(address[key]).lower()!=(i["address"])["town"].lower():
                         a=1
                         
            elif key=="city":
               
                   if str(address[key]).lower()!=(i["address"])["city"].lower():
                       a=1
            elif key=="state":
                
                    if str(address[key]).lower()!=(i["address"])["state"].lower():
                        a=1
            elif key=="pincode" :
                
                    if int(address[key])!=(i["address"])["pincode"]:
                         a=1
            if a==0:
                dict1={}
                dict1["first_name"]=i["first_name"]
                dict1["last_name"]=i["last_name"]
                list1.append(dict1)
    return list1
   
    
                
                    
            
    


def find_alumni(records, institute_name):
    '''
    Description: Find all the alumni of the given institute name (case-insensitive). 
    
    Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - institute_name (STRING): Name of the institute (case-insensitive)

    Returns:
    - A LIST of DICTIONARIES with the following three key-value pairs:
        KEY            VALUE
        "first_name"   first name (STRING)
        "last_name"    last name (STRING)
        "percentage"   percentage (FLOAT)
    '''
    list1=[];
    
    for i in records:
        if(i.get("education")):
            for j in i["education"]:
                if (str(j.get("institute")).lower()==(institute_name.lower())) and (bool(j.get("ongoing"))== False):
                 dict1={}
                 dict1["first_name"]=i["first_name"]
                 dict1["last_name"]=i["last_name"]
                 dict1["percentage"]=j.get("percentage")
                 list1.append(dict1)
    return (list1)

                
           


def find_topper_of_each_institute(records):
    '''
    Description: Find topper of each institute

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)

    Returns:
    - A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

    Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
    '''
    inst_names=[]
    for i in records:
        if(i.get("education")):
            for j in i["education"]:
                inst_names.append((j.get("institute")))
    dict1={}           
    inst_names=list(set(inst_names))
    for inst in inst_names:
        max=0
        for i in records:
            if(i.get("education")):
                for j in i["education"]:
                    if inst==j.get("institute") and j.get("ongoing")==False and j.get("percentage")>max:
                        max=j.get("percentage")
                        id=i.get("id")
        dict1[inst]=id
        
    return(dict1)

            
            
                        
                    
            
    
                                  
   


def find_blood_donors(records, receiver_person_id):
    '''
    Description: Find all donors who can donate blood to the person with the given receiver ID.

        Note: 
        - Possible blood groups are "A", "B", "AB" and "O".

        Rules:
        BLOOD GROUP      CAN DONATE TO
        A                A, AB
        B                B, AB
        AB               AB
        O                A, B, AB, O

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - receiver_person_id (INTEGER): The ID of the donee
        Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

    Returns:
    - A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
    '''
    dict1={}
    
    for i in records:
        if receiver_person_id==i.get("id"):
            receiver_person_id=records.index(i)
            break
        
    receiver_blood_group = records[receiver_person_id].get("blood_group")
    if receiver_blood_group =="AB":
        for i in records:
            if i["id"]==receiver_person_id:
                continue
            dict1[i["id"]]=(i["contacts"])
    elif receiver_blood_group=="A":
        for i in records:
            if i["blood_group"]=="A" or i["blood_group"]=="O":
                if i["id"]==receiver_person_id:
                    continue
                dict1[i["id"]]=(i["contacts"])
    
    elif receiver_blood_group=="B":
        for i in records:
            if i["blood_group"]=="B" or i["blood_group"]=="O":
                if i["id"]==receiver_person_id:
                    continue
                dict1[i["id"]]=(i["contacts"])
    elif receiver_blood_group=="O":
        for i in records:
            if i["blood_group"]=="O":
                if i["id"]==receiver_person_id:
                    continue
                dict1[i["id"]]=(i["contacts"])
    
    return(dict1)
            

def get_common_friends(records, list_of_ids):
    '''
    Description: Find the common friends of all the people with the given IDs

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

    Returns:
    - A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
    '''
    friend_ids=[]; common_friend_ids=[]
    for i in range(len(list_of_ids)):
        for j in records:
            if j.get("id")==list_of_ids[i]:
                list_of_ids[i] = records.index(j)
    for ids in list_of_ids:
        friend_ids.append(records[ids].get("friend_ids"))
    
    
    k=friend_ids[0]
    list1=k.copy()
    
    
    for h in friend_ids[1:]:
        for i in k:
            if (i in list1 ) and (i not in h):
                list1.remove(i)
                
            
    return(list1)
                
            
        
                 
 

def is_related(records, person_id_1, person_id_2):
    '''
    **** BONUS QUESTION ****
    Description: Check if 2 persons are friends

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id_1 (INTEGER): first person ID
    - person_id_2 (INTEGER): second person ID

    Returns:
    - A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
    '''
    for i in records:
       if i["id"]==person_id_1:
           id1=person_id_1
           break
    if person_id_2 in (records[id1].get("friend_ids")):
         return True
    else:
         for i in records[id1].get("friend_ids"):
             if(is_related(records,i,person_id_2)):
                 return True
                 break    
    
    
    
    
   
    return True     
     

            
        
        
    
    


def delete_by_id(records, person_id):
    '''
    Description: Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    
    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''
   
    #pop function removes the element containing the id from the list
    for j in records:
        k=j.get("friend_ids")
        for i in k[:]:
            if i==person_id:
                k.remove(i)
                
    for j in records:
         if j.get("id")==person_id:
                person_id= records.index(j)
                records.pop(person_id) #
                break
    
    
    return records


def add_friend(records, person_id, friend_id):
    '''
    Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - friend_id (INTEGER): The friend id
    
    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''
    k=1;
    person_id_index=0
    friend_id_index=0
    for j in records:
            if j.get("id")==person_id:
                person_id_index=records.index(j)
                k=0
                break
            
    
    if k==1:
       return records
    
    k=1             
    for j in records:
            if j.get("id")==friend_id:
                friend_id_index=records.index(j)
                k=0
                break
    if k==1:
      return records        
    
    
    if friend_id not in records[person_id_index].get("friend_ids"):
        records[person_id_index].get("friend_ids").append(friend_id)
    if person_id not in records[friend_id_index].get("friend_ids"):
       records[friend_id_index].get("friend_ids").append(person_id)
    return records
    
    

def remove_friend(records, person_id, friend_id):
    '''
    Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - friend_id (INTEGER): The friend id
    
    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''
    k=1;
    
    for j in records:
            if j.get("id")==person_id:
                person_id_index=records.index(j)
                k=0
                break
            
    
    if k==1:
      return records
    
    k=1             
    for j in records:
            if j.get("id")==friend_id:
                friend_id_index=records.index(j)
                k=0
                break
    if k==1:
     return records        
    
    
        
    if friend_id in (records[person_id_index].get("friend_ids")):
        records[person_id_index].get("friend_ids").remove(friend_id)
        
    if person_id in records[friend_id_index].get("friend_ids"):
                records[friend_id_index].get("friend_ids").remove(person_id)
    return records


def add_education(records, person_id, institute_name, ongoing, percentage):
    '''
    Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - institute_name (STRING): The institute name (case-insensitive)
    - ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
    - percentage (FLOAT): The person's score in percentage

    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''
    k=0
    for j in records:
            if j.get("id")==person_id:
                person_id_index=records.index(j)
                k=1
                break
    if k==0:
        return records
    dict1={}
    if institute_name:
        dict1["institute"]=institute_name.upper();
    if str(ongoing):
        dict1["ongoing"]=bool(ongoing)
    if ongoing==False:
        dict1["percentage"]=float(percentage)
    (records[person_id_index].get("education")).append(dict1)
    
    return records