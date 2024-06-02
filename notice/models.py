from django.db import models

class notice(models.Model):
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    attachment = models.FileField(upload_to='notice/media/uploads/', blank=True, null=True)
    image = models.ImageField(upload_to='notice/media/uploads/', blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.time} - {self.description[:50]}"
    
class AdmissionNotice(models.Model):
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    attachment = models.FileField(upload_to='notice/media/uploads/', blank=True, null=True)
    image = models.ImageField(upload_to='notice/media/uploads/', blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.time} - {self.description[:50]}"
    
    
class event(models.Model):
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    image = models.ImageField(upload_to='notice/media/uploads/', blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.time} - {self.description[:50]}"

from django.db import models

class Research(models.Model):
    content_name = models.CharField(max_length=200)
    superadvisor = models.CharField(max_length=200)
    Researchimage = models.ImageField(upload_to='notice/media/uploads/', blank=True, null=True)
    member1 = models.CharField(max_length=200, blank=True, null=True)
    member2 = models.CharField(max_length=200, blank=True, null=True)
    member3 = models.CharField(max_length=200, blank=True, null=True)
    member4 = models.CharField(max_length=200, blank=True, null=True)
    member5 = models.CharField(max_length=200, blank=True, null=True)
    member6 = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=200)
    paper_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.content_name
