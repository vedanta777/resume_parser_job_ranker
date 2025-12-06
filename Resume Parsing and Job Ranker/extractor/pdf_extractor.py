# importing libraries

import os
'''To handle file paths'''

import pdfplumber
'''To read and extract data from pdf'''

# defining function

def pdf_extractor (file_path) :
    extracted_file = []
    '''empty string to which extracted data from pdf gets appended''' 
    try :
        with pdfplumber.open (file_path) as pdf :
            
            '''opening file using with open'''
            for page in pdf.pages :
                text = page.extract_text()
                '''command to extract pages and text in each'''
                
                if text :
                    '''if text means that if page has text only then it will execute'''
                    extracted_file.append(text)
                    
        return extracted_file
        '''data from pdf is appended to initially empty string and that string is stored in function now''' 
    
    except FileNotFoundError :
        print ("File Not Found !!!")
        exit()
        
file_path = r"..\sample resume\resume 20.pdf"
file = pdf_extractor (file_path)
for line in file :
    print (line)
