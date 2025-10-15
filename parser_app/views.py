from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


from .utils.extractor import extract_text_from_pdf

# Create your views here.
def home(request):

    parsed_data = None
    if request.method == 'POST':
        uploaded_file =request.FILES.get('resume_file')

        if not uploaded_file:
            messages.error(request, "No file selected. Please choose a file to upload.")
        
        else:
            text = extract_text_from_pdf(uploaded_file)
            parsed_data ={
                'file_name': uploaded_file.name,
                'file_size': f"{uploaded_file.size / 1024:.2f} KB",
            }

            messages.success(request, "File uploaded successfully!")
            



    return render(request, 'upload.html', {'parsed_data': parsed_data})

