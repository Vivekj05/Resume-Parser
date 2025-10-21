from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


from .utils.extractor import extract_text_from_pdf
from .utils.cleaner import clean_text, detect_sections
from .utils.matcher import compute_match

# Create your views here.
def home(request):

    parsed_data = None
    if request.method == 'POST':
        uploaded_file =request.FILES.get('resume_file')

        required_skills_input = request.POST.get('required_skills','')
        if not uploaded_file:
            messages.error(request, "No file selected. Please choose a file to upload.")

        elif not required_skills_input.strip():
            messages.error(request, "Please enter the required skills for matching.")    
        
        else:
            text = extract_text_from_pdf(uploaded_file)
            cleaned_text = clean_text(text)
            sections = detect_sections(cleaned_text)
            # print(sections)

            resume_skills= sections.get('skills','')

            required_skills = [skill.strip().lower() for skill in required_skills_input.split(',') if skill.strip()]

            match_result=compute_match(resume_skills, required_skills)


            parsed_data ={
                'file_name': uploaded_file.name,
                'file_size': f"{uploaded_file.size / 1024:.2f} KB",
                'resume_skills': resume_skills,
                'required_skills': required_skills,
                'match_score': match_result['match_percentage'],
                'matched_skills': match_result['matched_skills'],
                'missing_skills': match_result['missing_skills']
            }

            messages.success(request, "Resume Processed and amtched successfully!")
            



    return render(request, 'upload.html', {'parsed_data': parsed_data})

