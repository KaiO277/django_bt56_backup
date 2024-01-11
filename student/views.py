from django.shortcuts import render
from .models import student
from django.core.paginator import Paginator 
from django.contrib import messages

# Create your views here.

def index(request):
    students = student.objects.all()
    paginator = Paginator(students, 10)  # 10 items per page

    page = request.GET.get('page')
    my_data = paginator.get_page(page)
    use_bootstrap = True  
    template_name = 'index.html'
    # if use_bootstrap else 'tailwind_layout.html'
    return render(request, template_name,{'students':students, 'my_data':my_data})

def main(request):
    return render(request, 'base.html')

def add(request):
    return render(request, 'insert.html')

def insert(request):
    if(request.method == "POST"):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        print(first_name +" "+ last_name)
        if first_name.isdigit():
            print("numer")
            messages.error(request, "trong first name dang co so")
            return render(request, 'insert.html')
        elif   last_name.isdigit():
            messages.error(request, "trong last name dang co so")
            return render(request, 'insert.html')
        else:
            new_st = student.objects.create(first_name=first_name, last_name=last_name)
            new_st.save()
            return render(request, 'insert.html')
    