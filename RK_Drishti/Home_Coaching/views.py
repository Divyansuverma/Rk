from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.urls import path
from .models import Note
from .models import Course
import os

# # for Uploade Notes....
# from django.contrib import messages
# from django.contrib.auth.decorators import user_passes_test
# from .forms import NoteForm
# from .models import Note

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello Bro:")
    # if request.user.is_anonymous:
    #     return redirect('/login')
    
    # return render(request,'home.html')

def home(request):
    # return render(request,'home.html')
    if request.user.is_anonymous:
        return redirect('/login')
    
    return render(request,'home.html')

def singup(request):
    # return render(request, 'singup.html')
    # return HttpResponse("Hello Bro:")
    
    if request.method=='POST':
        username=request.POST['Username']
        email=request.POST['email']
        password=request.POST['password']
        data= User.objects.create_user(username=username,email=email,password=password)
        data.save()
        
    return render(request,'singup.html')

def loginUser(request):
    # return render(request, 'login.html')
    # return HttpResponse("Hello Bro:")
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['password']
        
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html')
        
    return render(request,'login.html')

def logout(request):
    logout(request)
    return redirect('/login')

def notes(request):
    # return render(request,'notes.html')
    context = {'file':Note.objects.all()}
    return render(request,'notes.html',context)

def courses(request):
    context = {'file':Course.objects.all()}
    return render(request,'courses.html',context)

def uploadcourses(request):
    return render(request,'upload-courses.html')

def feedback(request):
    return render(request,'feedback.html')

def demo(request):
    return render(request,'demo.html')

def about(request):
    return render(request,'about.html')

# @user_passes_test(lambda u: u.is_staff)
# def uploadnotes(request):
#     if request.method == 'POST':
#         form = NoteForm(request.POST, request.FILES)
#         if form.is_valid():
#             note = form.save(commit=False)
#             note.admin_uploaded = True
#             note.save()
#             messages.success(request, 'Note uploaded successfully!')
#             return redirect('home')  # Replace 'home' with the name of your home page URL pattern
#     else:
    #     form = NoteForm()

    # return render(request, 'upload_note.html', {'form': form})
def uploadnotes(request):
    return render(request,'upload-notes.html')


# def download(request,path):
#     file_path = os.path.join(settings.MEDIA_ROOT,path)
#     if os.path.exists(file_path):
#         with open(file_path,"rb") as fh:
#             response = HttpResponse(fh.read(), context_type='application/file')
#             response ['Content-Disposition'] = 'inline;filename'+os.path.basename(file_path)
#             return response
    # return Http404
    

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            response = HttpResponse(fh.read(), content_type='application/file')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404("File not found")