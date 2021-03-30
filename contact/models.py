from django.db import models

# Create your models here.
class Info(models.Model):
    place = models.TextField(max_length=300)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = ('Info')
        verbose_name_plural = ('Infos')
    def __str__(self):
        return self.email
    


    

