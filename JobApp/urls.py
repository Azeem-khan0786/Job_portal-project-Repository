from django.urls import path,re_path
from JobApp import views
from django.views.generic import RedirectView
app_name='JobApp'

urlpatterns = [
    

    path('jobs/', views.job_view, name='job_view'),
    path('job-details/<int:job_id>/', views.job_details, name='job_details'),
    path('single_job_view/<int:id>/', views.single_job_view, name='single_job_view'),
    path('apply_job_view/<int:id>/', views.apply_job_view, name='apply_job'),
    path('bookmark_view/<int:id>/', views.bookmark_view, name='bookmark_view'),

    path('create_job/', views.create_job, name='create_job'), 
    path('dashboard_view/', views.dashboard_view, name='dashboard_view'), 

    path('recruiter_job_view/', views.recruiter_job_view, name='recruiter_job_view'), 


    path('about_us/', views.about_us, name='about_us'), 
    path('custom_csrf_failure/',views.custom_csrf_failure), 
]




