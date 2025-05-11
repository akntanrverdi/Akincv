from django.shortcuts import render
from .models import CV

def home(request):
    cv_data = CV.objects.first()
    return render(request, 'home.html', {'cv_data': cv_data})
