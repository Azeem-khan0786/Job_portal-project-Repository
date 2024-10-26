# Import your template here
from django import template
from JobApp.models import BookmarkJob

register=template.Library()

@register.simple_tag(name='is_job_already_saved')
def is_job_already_saved(job,user):
    is_saved=BookmarkJob.objects.filter(job=job, user=user)
    if  is_saved:
        return True
    else:
        return False    
    pass



    
