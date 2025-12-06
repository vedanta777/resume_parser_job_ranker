# importing libraries and defining nlp

import spacy
'''To process language and search based on keywords'''
import os
'''To handle file directories'''
import re
'''To detect and list repeated expressions. Used for detecting year of graduation'''
import pdfplumber
'''To manipulate pdf files'''
import json
'''To load skills from resume file'''

nlp = spacy.load("en_core_web_sm")
'''Defining nlp variable to process text in order to identify college here'''
file_path = input("Enter absolute file path - ")
    
# extracting name

def name_extractor(file_path) :
    with open (file_path, "r") as f :
        resume_text = f.read()
        doc = nlp(resume_text)
        for ent in doc.ents :
            if ent.label_ == "PERSON" :
                return ent.text
            else :
                print ("No name found !!")

# extracting skills

skills_path = r"C:\Users\Dell\OneDrive\Desktop\Stanford Transfer\ResumeParsing and JobRanker\skills list.txt"

def skill_extractor (file_path) :
    matched_skills = []
    with open (file_path, "r") as f :
         resume_text = f.read()
         updated_resume = resume_text.lower()
    with open (skills_path, "r") as f :
        skills = f.readlines()
        skill_list = [a.strip().lower() for a in skills]
    for i in range (len(skill_list)) :
        if skill_list[i] in updated_resume :
            matched_skills.append(skill_list[i])
    return matched_skills

# extracting education

degree_path = r"C:\Users\Dell\OneDrive\Desktop\Stanford Transfer\ResumeParsing and JobRanker\educational qualifications.txt"

def degree_extractor (file_path) :
    with open (file_path, "r") as f :
        resume_text = f.read()
        updated_resume = resume_text.lower()
    with open (degree_path, "r") as f :
        edu_text = f.readlines()
        edu_list = [ a.strip().lower() for a in edu_text]
    edu_degrees = []
    for i in range (len(edu_list)) :
        if edu_list[i] in updated_resume :
            edu_degrees.append(edu_list[i])
    return edu_degrees
    
def college_extractor (file_path):
    with open (skills_path, "r") as f :
        skills = f.readlines()
        skill_list = [a.strip().lower() for a in skills]
    college_list = []
    with open (file_path, "r") as f :
        resume_text = f.read()
    doc = nlp(resume_text)
    for ent in doc.ents :
        if ent.label_ == "ORG" :
            org = ent.text.strip()
            if org.lower() not in skill_list and len(org.split()) > 1 and not any (c in org for c in ['.', '-', '_']) :
                ''' org is not a skill cause of first condition, second removes terms like SQL and third removes weird acronyms'''
            college_list.append(ent.text)
    return college_list

def year_extractor (file_path):
    with open (file_path, "r") as f :
         resume_text = f.read()
    years = re.findall (r"20\d{2}", resume_text)
    return list(set(years))
            
# calling function and recursion

name = name_extractor (file_path)
college = college_extractor (file_path)
skill = skill_extractor (file_path)
year = year_extractor (file_path)
degree = degree_extractor (file_path)

def search_result () :
    print ("Following detail about the candidate has been found")
    print ("Name - ", name)
    print ("College - ", college)
    print ("Skills - ", skill)
    print ("Years of Graduation - ", year)
    print ("Degree - ", degree)

def data_extraction () :
    print ("Welcome !! Now, type the number corresponding to what you would like to extract from the .txt file -")
    print ("1 - Name of Candidate")
    print ("2 - Colleges attended by Candidate")
    print ("3 - Skills of Candidate")
    print ("4 - Years of Graduation of the Candidate")
    print ("5 - Degrees acquired by Candidate")
    print ("6 - All details")
    print ("7 - Stop")

    choice1 = int(input("Enter your choice - "))

    if choice1 == 1 :
        print ("Following detail about the candidate has been found")
        print ("Name - ", name)
        data_extraction()
    
    elif choice1 == 2 :
        print ("Following detail about the candidate has been found")
        print ("College - ", college)
        data_extraction()
    
    elif choice1 == 3 :
        print ("Following detail about the candidate has been found")
        print ("Skills - ", skill)
        data_extraction()
    
    elif choice1 == 4 :
        print ("Following detail about the candidate has been found")
        print ("Years of Graduation - ", year)
        data_extraction()
        
    elif choice1 == 5 :
        print ("Following detail about the candidate has been found")
        print ("Degree - ", degree)
        data_extraction()

    elif choice1 == 6 :
        print ("Following detail about the candidate has been found")
        print ("Name - ", name)
        print ("College - ", college)
        print ("Skills - ", skill)
        print ("Years of Graduation - ", year)
        print ("Degree - ", degree)
        data_extraction()
        
    elif choice1 == 7 :
        print ("Okay, byeee !!")
        exit ()
    
data_extraction()
