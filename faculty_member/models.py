from django.db import models
class OfficeStaff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='faculty_member/media/uploads/', blank=True, null=True)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    staff_id = models.AutoField(primary_key=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)  # Added field
    email = models.EmailField(max_length=254, blank=True, null=True)  # Added field
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.designation} - {self.department}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='faculty_member/media/uploads/', blank=True, null=True)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    teacher_id = models.AutoField(primary_key=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)  # Added field
    email = models.EmailField(max_length=254, blank=True, null=True)  # Added field
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.designation} - {self.department}"


class Education(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.degree} - {self.institution} - {self.year}"

class Experience(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='experiences')
    position = models.CharField(max_length=100)
    organization = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.position} - {self.organization} ({self.start_date} to {self.end_date})"

class Publication(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='publications')
    title = models.CharField(max_length=500)
    journal = models.CharField(max_length=200)
    volume = models.CharField(max_length=50, blank=True, null=True)
    issue = models.CharField(max_length=50, blank=True, null=True)
    pages = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField()
    doi = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    publication_type = models.CharField(max_length=50, choices=[('Journal', 'Journal'), ('Conference', 'Conference'), ('Book', 'Book')], default='Journal')

    def __str__(self):
        return self.title

