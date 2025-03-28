from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, DocumentForm
from .models import Document, CustomUser

# Home Page
def home(request):  
    return render(request, 'users/home.html')

# User Registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            # Role-based redirection
            if user.role == CustomUser.ADMIN:
                return redirect('admin_dashboard')
            elif user.role == CustomUser.TRAINER:
                return redirect('trainer_dashboard')
            else:
                return redirect('student_dashboard')

    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            
            # Role-based redirection
            if user.role == CustomUser.ADMIN:
                return redirect('admin_dashboard')
            elif user.role == CustomUser.TRAINER:
                return redirect('trainer_dashboard')
            else:
                return redirect('student_dashboard')
            
    return render(request, 'login.html')

# General Dashboard View
def dashboard(request):
    return render(request, 'dashboard.html')

# Role-Based Dashboards
def admin_dashboard(request):
    return render(request, 'dashboards/admin_dashboard.html')

def trainer_dashboard(request):
    return render(request, 'dashboards/trainer_dashboard.html')

def student_dashboard(request):
    return render(request, 'dashboards/student_dashboard.html')

# File Upload View
def upload_file(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Saves to Cloudinary
            return redirect('upload')  # Refresh page after upload
    
    else:
        form = DocumentForm()

    documents = Document.objects.all()  # Retrieve all uploaded files
    return render(request, "upload.html", {"form": form, "documents": documents})


