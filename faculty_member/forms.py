from django import forms
from .models import Teacher,OfficeStaff,Publication,Experience,Education

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
class OfficeStaffForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'