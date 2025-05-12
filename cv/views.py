from django.shortcuts import render
from .models import CV, Project, Education, Contact

def home(request):
    cv_data = CV.objects.first()
    return render(request, 'home.html', {'cv_data': cv_data})

def projects(request):
    projects_data = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects_data})

def education(request):
    education_data = Education.objects.all()
    return render(request, 'education.html', {'education': education_data})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')
