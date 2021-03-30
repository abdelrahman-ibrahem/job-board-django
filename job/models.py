from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
JOBTYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)
#class jobs
class Job(models.Model):
    owner = models.ForeignKey(User , related_name="owner_job", on_delete=models.CASCADE , blank=True , null=True)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100 , choices =JOBTYPE )
    description = models.TextField(max_length=400)
    published_at =  models.DateTimeField(auto_now=True)
    vecancy = models.IntegerField(default=1)
    salary = models.IntegerField()
    experiance = models.IntegerField(default=1)
    category = models.ForeignKey('Category' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to="imageJob/" , blank=True , null= True)
    
    

    

    def __str__(self):
        return self.title



#class catefory
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Apply(models.Model):
    name = models.CharField(max_length=50)
    email =  models.EmailField(max_length=254)
    website = models.URLField(max_length = 200 , blank=True , null=True)
    cv = models.FileField(upload_to='cvs', max_length = 100, blank=True , null=True)
    cover = models.TextField(max_length=260, blank=True , null=True)

    def __str__(self):
        return str(self.name)
    
    
    
    
    