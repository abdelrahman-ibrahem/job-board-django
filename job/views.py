from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .filters import JobFilter
from .form import ApplyJob , AddJob
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def jobs(request):
    jobs = Job.objects.all()
    counter = jobs.count()
    #filter 
    myFilter = JobFilter(request.GET , queryset= jobs)
    jobs = myFilter.qs
    paginator = Paginator(jobs , 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"jobs":page_obj , "counter":counter , "myFilter":myFilter}
    return render(request , "job/jobs.html" , context)


def job_details(request , id_number):
    job_details = Job.objects.get(id=id_number)
    if request.method == "POST":
        form = ApplyJob(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            print('save')
            return HttpResponseRedirect(reverse('home:index'))
    else:
        form = ApplyJob()
    context = {"job_details":job_details , "form1":form}
    return render(request , "job/job_details.html" , context)




def add_job(request):
    if request.method == 'POST':
        form = AddJob(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home:index'))
    else:
        form = AddJob(request.POST)
    return render(request , 'job/add_job.html' , {
        'form':form
    })
