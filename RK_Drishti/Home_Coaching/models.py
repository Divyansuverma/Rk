from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    disc = models.TextField()
    file = models.FileField(upload_to='media')
    date = models.DateTimeField(auto_now_add=True)
    admin_uploaded = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
# class Course(models.Model):
#     titles = models.CharField(max_length=500)  # Course title
#     discs = models.TextField()  # Course description
#     files = models.FileField(upload_to='media')  # Course files
#     admin_upload = models.BooleanField(default=False)  # Check if admin uploaded the file
#     duration = models.IntegerField(default=0)  # Set your desired default value for duration

#     def __str__(self):
#         return self.titles  # Return course title


class Course(models.Model):
    titles = models.CharField(max_length=500)  # Course title
    discs = models.TextField()  # Course description
    files = models.FileField(
        upload_to='media/videos',
        default='default_course_file.mp4',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
        max_length=1000
    )
    video_image = models.ImageField(upload_to='media', blank=True, null=True)
    admin_upload = models.BooleanField(default=False)  # Check if admin uploaded the file
    duration = models.IntegerField(default=0)  # Set your desired default value for duration

    def __str__(self):
        return self.titles  # Return course title