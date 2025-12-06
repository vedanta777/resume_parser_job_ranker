# importing libraries

import re
'''To detect and extract repeated expressions'''

import os
'''To handle file paths and directories'''

import pdfplumber
'''To manipulate pdf files'''

# email extractor

def email_extractor (text) :
    email_pattern = r"[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    #regex pattern for email, first square bracket means the part of email before @, +@ means literally
    #@, second square bracket for domain name like google, yahoo etc, \. for the dot like gmail.com
    #and last square bracket for com
    
    emails = re.findall(email_pattern,text)
    return emails

# phone number extractor
def phone_extractor (text) :
    phone_pattern = r"(?:\+91[\s\-]?)?[6-9]\d{9}"
    #regex pattern for phone number, '+91" is optional so its between ?? and followed by s-...
    #after that [6-9] is used because in India phone numbers have first digits between 6 to 9
    #d{9} means that remaining 9 digits can be any 9 digits
    phone_number = re.findall(phone_pattern,text)
    return phone_number

# extracting from pdf and text files

def data_extraction_1 () :
    print("Welcome !! Enter 1 if you want to extract email and phone number from .txt file")
    print("Welcome !! Enter 2 if you want to extract email and phone number from .pdf file")
    print("Type No if you want to stop or dont want to continue")

    choice = (input("Enter your choice - "))

    if choice == "1" :
        file_path = input("Enter absolute path of file - ")
        with open ( file_path , "r") as f :
            text = f.read()
            txt_email = email_extractor(text)
            txt_phone = phone_extractor(text)
        print ("Email : ", txt_email)
        print ("Phone Number : ", txt_phone)
        data_extraction_1()

    elif choice == "2" :
        file_path = input("Enter absolute path of file - ")
        def pdf_to_text (file_path) :
             with pdfplumber.open ( file_path ) as pdf :
                  full_text =""
                  for page in pdf.pages :
                     text = page.extract_text()
                     if text :
                       full_text += text + "\n"
             return full_text
        pdf_file = pdf_to_text (file_path)
        pdf_email = email_extractor(pdf_file)
        pdf_phone = phone_extractor(pdf_file)
        print ("Email : ", pdf_email)
        print ("Phone Number : ", pdf_phone)
        data_extraction_1()

    elif choice == "No" :
        print("Okay, byeee")
        exit()


data_extraction_1()

