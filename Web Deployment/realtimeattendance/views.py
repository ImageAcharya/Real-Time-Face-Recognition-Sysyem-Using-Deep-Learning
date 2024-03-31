from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from student.models import Attendance
from .Project_Face_Detection import opencamera

facultydict = {
    '1':'Civil',
    '2':'Computer',
    '3':'Electrical'
}


def managestd(request):
    return render(request, 'managestudents.html')

def logout(request):
    auth_logout(request)
    return redirect ('/')

def login(request):
    if request.user.is_authenticated:
            return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = authenticate(username = username, password = password)
            except:
                user = None
            if user:
                auth_login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'message':'failed'})
        else:
            return render(request, 'login.html', {'message':''})

def changepass(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        message = None
        if request.method == 'POST':
            opassword = request.POST.get('opassword')
            npassword = request.POST.get('npassword')
            user = authenticate(username='admin', password=opassword)
            if user:
                user.set_password(npassword)
                user.save()
                message = 'done'
                return render(request, 'login.html', {'message':message})
            else:
                message = 'failed'
        return render(request, 'changepassword.html', {'message':message})

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {})
    else:
        return redirect('/')

def classroom(request):
    if request.method == 'POST':
        faculty = facultydict[request.POST.get('faculty')]
        semester = request.POST.get('semester')
        section = request.POST.get('section')
        opencamera(faculty, semester, section)
    return render(request, 'classroom.html', {})

def attendance(request):
    try:
        faculty = request.GET.get('faculty')
        semester = request.GET.get('semester')
        section = request.GET.get('section')
        date = request.GET.get('date')
        attendobj = Attendance.objects.all().filter(faculty = faculty, semester=semester, section=section)
        attendresult = []
        for attend in attendobj:
            if attend.datentime.strftime('%Y-%m-%d') == date:
                attendresult.append(attend)
    except:
        attendresult = []
    return render(request, 'attendance.html', {'attendresult':attendresult, 'faculty':faculty, 'semester':semester, 'date':date, 'section':section})