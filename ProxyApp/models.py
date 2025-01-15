from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class MainModel(models.Model):
    name=models.CharField(_("Name"), max_length=50,null=True)
    age = models.IntegerField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)

class ProxyModel(MainModel):
    # location=models.CharField(_("location"), max_length=50)
    class Meta:
        proxy=True
    

    class ProxyManager(models.Manager):
         def get_queryset(self, *args, **kwargs):
         # Exclude superusers in the queryset
             return super().get_queryset(*args, **kwargs).exclude(is_superuser=True)
     

    def __str__(self):
        return self.name.upper()
    
    def hello(self):
        return 'helli'
    