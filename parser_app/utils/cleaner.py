import re
import string

def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # remove lines
    text=re.sub(r'\n+','\n',text)
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra whitespace
    text= re.sub(r'\s+', ' ', text).strip()
    
    return text

def detect_sections(text):
    section_patterns = {
        'education':re.compile(r'\b(education|academic background|qualifications)\b', re.IGNORECASE), #\bis used to match whole words only it gives boundary to the word
        'experience': re.compile(r'\b(experience|work history|professional experience|employment)\b', re.IGNORECASE),
        'skills': re.compile(r'\b(skills|technical skills|expertise)\b', re.IGNORECASE),
        'projects': re.compile(r'\b(projects|personal projects|portfolio)\b', re.IGNORECASE),
        'certifications': re.compile(r'\b(certifications|licenses|accreditations)\b', re.IGNORECASE),
        'summary': re.compile(r'\b(summary|professional summary|profile)\b', re.IGNORECASE),
        'achievements': re.compile(r'\b(achievements|awards|honors)\b', re.IGNORECASE),
        'publications': re.compile(r'\b(publications|research|papers)\b', re.IGNORECASE),
        'languages': re.compile(r'\b(languages|language proficiency|spoken languages\b', re.IGNORECASE),
        'interests': re.compile(r'\b(interests|hobbies|personal interests)\b', re.IGNORECASE),
    }

    lines=text.split('\n')
    sections={}

    current_section = None

    for line in lines:
        line=line.strip()
        if not line:
            continue  #skip empty lines

        matched = False
        for section_name, pattern in section_patterns.items():
            if pattern.search(line):
                current_section=section_name
                sections[current_section] = []
                matched = True
                break


        if not matched and current_section:
            sections[current_section] += line + " "   

    for sec in sections:
        sections[sec] = sections[sec].strip()


    return sections            