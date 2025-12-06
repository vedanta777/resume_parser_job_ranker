# importing libraries

import spacy
'''To process named entities'''

import re
'''To detect dates using patterned expressions'''

import os
'''To handle file paths and directories'''

# important file paths and variables

nlp = spacy.load("en_core_web_sm")
designation_list = r".\extraction data\designation list.txt"
year_pattern = [r"(?i)(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[.,]?\s?\d{4}",
    r"\b(20\d{2})\s?[-–to]+\s?(Present|Now|20\d{2})\b",
    r"(?i)(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]\s\d{4}\s?[-–to]+\s?(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)?[a-z]\s?(Present|Now|\d{4})",
    r"\b20\d{2}\b"]

skills_path = r".\extraction data\skills list.txt"
with open (skills_path , "r") as f :
    skills_list = [ a.strip().lower() for a in f.read() ]

# experience extractor

def experience_extractor (file_path) :
    
    with open (designation_list, "r", encoding = "utf-8") as f :
        title_list = [ x.strip().lower() for x in f.readlines()]
        tl_length = len(title_list)
        
    with open (file_path, "r", encoding = "utf-8") as f :
        resume_text = f.readlines()
        line_list = [word.lower() for word in resume_text]
        ll_length = len(line_list)

    company = None
    designation = None
    years = None

    for i in range (ll_length) :
        
        resume_line = line_list[i]
        doc = nlp(resume_line)
        for ent in doc.ents :
            company_candidate = ent.text
            ent_item = company_candidate.lower()
            if ent.label_ == "ORG" :
                ban_words = ["university","iit","iiit","mit","oxford","nit"]
                for words in ban_words :
                    if words not in company_candidate :
                        company = ent.text
                        print ("The individual has worked at this company - " , company)
                        break
                    break
        
        resume_line_lower = resume_line.lower()
        for title in title_list :
            if title in resume_line_lower and title not in skills_list :
                designation = title
                print ("Designation of person - ", designation)
                break

        
        for pattern in year_pattern :
            year = re.search( pattern , resume_line)
            if year :
                years = year.group()
                print("Years of working - ", years)
                break
                
        if company and designation and years :
            work_details = { "Company" : company ,
                                     "Designation" : designation ,
                                    "Years" : years}
            print ("Following details have been found")
            print(work_details)
            company = None
            designation = None
            years = None
        
    
file_path = input("Enter absolute path of file - ")
experience_extractor(file_path)











