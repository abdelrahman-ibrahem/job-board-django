from django.shortcuts import render
from job import models
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    home  = models.Job.objects.all()
    counter = home.count()
    paginator = Paginator(home , 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"home":page_obj , "counter":counter}
    return render(request ,"home/index.html" , context)