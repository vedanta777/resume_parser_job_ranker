This is a simple walkthrough of the code I've written and my understanding of it.

Coding Language - Python
Libraries - os (to handle file paths), re (for pattern based detection), pdfplumber (to manipulate pdf files), spacy (nlp toolkit for rule based extraction)

What does the code do ?

1. Accepts a text or pdf file, reads it and stores it's contents in a list for accessing each line of the file.
2. Extracts email, phone number, educational qualification, skills and experience from the resume
3. Ranks suitability to a job based on match with criteria

How does the code work ?

1. pdfplumber helps extract data from pdf files and the normal file open method can be used for ".txt" files.
2. Phone number, email and name are extracted using their regex patterns. The extracting pattern can be modified accordingly to fit the standard set by the company.
3. Skills are extracted by running each line of t he resume agsinst a preset list of skills, comparing them and whenever there's a match, it's stored in a list which is then returned.
4. Experience, ie, previous company, years of working there, role there follow the same pattern.
5. Company is extracted by setting criteria to organisation for each token, and whenever there is a match, it is stored if it doesn't match any of the banned words like that of a school or some random name.
6. Years are extracted using regex patterns and roles using the same logic for skills.

Functionalities provided - 

1. Data Extraction
2. Job Suitability Ranking (will be added soon!)

