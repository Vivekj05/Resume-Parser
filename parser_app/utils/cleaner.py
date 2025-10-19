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
    # Normalize spaces, but keep line breaks
    text = re.sub(r'[ \t]+', ' ', text)      # collapse spaces/tabs
    text = re.sub(r'\n{2,}', '\n', text)     # collapse multiple newlines into one
    text = text.strip()

    
    return text

def detect_sections(text):
    section_patterns = {
        'education':re.compile(r'^(education|academic background|qualifications)\b', re.IGNORECASE), #\bis used to match whole words only it gives boundary to the word
        'experience': re.compile(r'^(experience|work history|professional experience|employment)\b', re.IGNORECASE),
        'skills': re.compile(r'^(skills|technical skills|expertise)\b', re.IGNORECASE),
        'projects': re.compile(r'^(projects|personal projects|portfolio)\b', re.IGNORECASE),
        'certifications': re.compile(r'^(certifications|licenses|accreditations)\b', re.IGNORECASE),
        'summary': re.compile(r'^(summary|professional summary|profile)\b', re.IGNORECASE),
        'achievements': re.compile(r'^(achievements|awards|honors)\b', re.IGNORECASE),
        'publications': re.compile(r'^(publications|research|papers)\b', re.IGNORECASE),
        'languages': re.compile(r'^(languages|language proficiency|spoken languages)\b', re.IGNORECASE),
        'interests': re.compile(r'^(interests|hobbies|personal interests)\b', re.IGNORECASE),
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
            sections[current_section].append(line)

    for sec in sections:
        if isinstance(sections[sec], list):
            sections[sec] = " ".join(sections[sec]).strip()

    return sections            