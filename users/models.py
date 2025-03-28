from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ADMIN = 'admin'
    TRAINER = 'trainer'
    STUDENT = 'student'
    
    USER_ROLES = [
        (ADMIN, 'Admin'),
        (TRAINER, 'Trainer'),
        (STUDENT, 'Student'),
    ]
    
    role = models.CharField(max_length=20, choices=USER_ROLES, default=STUDENT)
    school = models.CharField(max_length=255, blank=True, null=True)  # Add this field
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)  # Add this field

    def __str__(self):
        return f"{self.username} ({self.role})"

from django.db import models
from cloudinary.models import CloudinaryField

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = CloudinaryField("document")  # Automatically uploads to Cloudinary
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

