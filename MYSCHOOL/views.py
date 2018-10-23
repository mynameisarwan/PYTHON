from django.shortcuts import render
# Create your views here.

def student_list(request):
    return render(request, 'MYSCHOOL/student_list.html', {})