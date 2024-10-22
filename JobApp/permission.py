from django.core.exceptions import PermissionDenied

def user_is_recruiter(function):

    def wrap(request, *args, **kwargs):   

        if request.user.user_type == 'recruiter':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap



def user_is_candidate(function):

    def wrap(request, *args, **kwargs):    

        if request.user.user_type == 'candidate':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap