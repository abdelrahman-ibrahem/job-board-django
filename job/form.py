from .models import Job , Apply
from django import forms

class ApplyJob(forms.ModelForm):
    class Meta:
        model = Apply
        fields = '__all__'


class AddJob(forms.ModelForm):
    class Meta:
        model = Job 
        fields = ['title' , 'description' , 'job_type' , 'salary' , 'vecancy' , 'category' , 'experiance' , 'image' ]