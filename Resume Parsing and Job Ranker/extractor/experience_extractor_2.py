# importing libraries

import spacy
'''To process named entities'''

import re
'''To detect dates using patterned expressions'''

import os
'''To handle file paths and directories'''

# important file paths and variables

nlp = spacy.load("en_core_web_sm")

designation_list = r"C:\Users\Dell\OneDrive\Desktop\Stanford Transfer\ResumeParsing and JobRanker\designation list.txt"

year_pattern = [r"(?i)(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[.,]?\s?\d{4}",
    r"\b(20\d{2})\s?[-–to]+\s?(Present|Now|20\d{2})\b",
    r"(?i)(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]\s\d{4}\s?[-–to]+\s?(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)?[a-z]\s?(Present|Now|\d{4})",
    r"\b20\d{2}\b"]

skills_path = skills_path = r"..\extraction data\skills_list.txt"
with open (skills_path , "r") as f :
    skills_list = [ a.lower() for a in f.readlines() ]
    
designation_path = r"..\extraction data\designation_list.txt"
with open (designation_path , "r") as f :
    designation_list = [ a.lower() for a in f.readlines() ]

# defining functions

def company_extractor (file_path) :
    company = None
    company_list = []
    banned_words = ["university","iit","iiit","mit","oxford","nit"]
    with open (file_path , 'r') as f :
        resume_file = f.read()
        doc = nlp(resume_file)
        for ent in doc.ents :
            if ent.label_ == "ORG" :
               if ent.text not in banned_words and designation_list:
                    company = ent.text
                    company_list.append(company)
    return company_list

def designation_extractor (file_path) :
    designation = None
    designations_list = []
    with open (file_path , 'r') as f :
        resume_line = [a.strip().lower() for a in f.readlines()]
    for i in designation_list :
        for j in resume_line :
            if i in j :
                designations_list.append(i)
    return designations_list


# calling functions

file_path = input("Enter absolute file path of the resume file - ")

'''companies = company_extractor(file_path)
print (companies)'''

designations = designation_extractor(file_path)
print(designations)                
        
