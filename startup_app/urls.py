from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.JobListView.as_view(), name = 'startup-jobs'),
    path('', views.InvestmentListView.as_view(), name = 'startup-home'),
    path('investors/', views.InvestorListView.as_view(), name = 'investors'),
    path('seekers/', views.JobSeekersListView.as_view(), name = 'seekers'),
    path('startups/', views.StartUpListView.as_view(), name = 'startups'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name = 'job-detail'),
    path('investors/<int:pk>/', views.InvestorDetailView.as_view(), name = 'investor-detail'),
    path('startups/<int:pk>/', views.StartUpDetailView.as_view(), name = 'startup-detail'),
    path('seekers/<int:pk>/', views.JobSeekerDetailView.as_view(), name = 'seeker-detail'),
    path('investments/<int:pk>', views.InvestmentDetailView.as_view(), name = 'investment-detail'),
]
