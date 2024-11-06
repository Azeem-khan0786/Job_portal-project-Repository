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
    path('dashboard/employer/edit_job/<int:id>', views.edit_job, name='edit_job'),
    path('dashboard/employer/delete_job/<int:id>', views.delete_job, name='delete_job'),
    path('dashboard/employer/close/<int:id>', views.make_close_job, name='make_close_job'),
    path('dashboard/employer/delete_bookmark/<int:id>', views.delete_bookmark, name='delete_bookmark'),
    path('dashboard/employer/applicant_details/<int:id>', views.applicant_details, name='applicant_details'),
    path('dashboard/employer/applicants_list/<int:id>', views.applicants_list, name='applicants_list'),


    path('recruiter_job_view/', views.recruiter_job_view, name='recruiter_job_view'), 


    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'), 

    path('custom_csrf_failure/',views.custom_csrf_failure), 
]




