from django.urls import path
from recruiters import views

app_name = 'recruiters'

urlpatterns = [
    path("employer_profile/", views.employer_profile, name="emp_profile"),
    path("employer_profile_view/", views.employer_profile_view, name="emp_profile_view"),
    
]