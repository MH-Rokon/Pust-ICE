from django.db import models

class Contact(models.Model):
    dept_name = models.CharField(max_length=200)
    dept_short_name = models.CharField(max_length=50)
    email = models.EmailField()
    location_image = models.ImageField(upload_to='contacts/media/uploads/', blank=True, null=True)
    phone = models.CharField(max_length=20)
    contact_time = models.CharField(max_length=100, blank=True, null=True) 

    
    def __str__(self):
        return f"{self.dept_name} ({self.dept_short_name})"
