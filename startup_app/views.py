from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Jobs, Investment_table, Investors, Job_Seekers, StartUps
# Create your views here.
class JobListView(ListView):
    model = Jobs
    template_name = "startup_app/available_jobs.html"
    context_object_name = 'jobs'
    ordering = ['job_type']
    
class InvestmentListView(ListView):
    model = Investment_table
    template_name = "startup_app/home.html"
    context_object_name = 'itable'

class InvestorListView(ListView):
    model = Investors
    template_name = 'startup_app/investorlist.html'
    context_object_name = 'investor_table'
    ordering = ['name']

class JobSeekersListView(ListView):
    model = Job_Seekers
    template_name = 'startup_app/jobseekerlist.html'
    context_object_name = 'seeker_table'

class StartUpListView(ListView):
    model = StartUps
    template_name = 'startup_app/startup_table.html'
    context_object_name = 'startup_table'

class JobDetailView(DetailView):
    model = Jobs
    template_name = "startup_app/job_detail.html"
    context_object_name = 'job_detail'


class InvestorDetailView(DetailView):
    model = Investors
    template_name = 'startup_app/investor_detail.html'
    context_object_name = 'investor'

class StartUpDetailView(DetailView):
    model = StartUps
    template_name = 'startup_app/startup_detail.html'
    context_object_name = 'startup'

class JobSeekerDetailView(DetailView):
    model = Job_Seekers
    template_name = 'startup_app/seeker_detail.html'
    context_object_name = 'seeker'

class InvestmentDetailView(DetailView):
    model = Investment_table
    template_name = 'startup_app/investment_detail.html'
    context_object_name = 'investment'
