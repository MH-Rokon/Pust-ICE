from django import forms
from .models import notice,event,AdmissionNotice,Research

class NoticeForm(forms.ModelForm):
    class Meta:
        model = notice
        fields = '__all__'
class EventForm(forms.ModelForm):
    class Meta:
        model = event
        fields = '__all__'
class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionNotice
        fields = '__all__'
class   ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        fields = '__all__'