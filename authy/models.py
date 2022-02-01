from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.forms import ModelForm
#from post.models import Post


# Create your models here.
class Passenger(models.Model):
    ROLE_CHOICES = (
    ('Passanger', 'Passanger'),
    ('Gate_manager', 'Gate_manager'),
    ('Check_in_manager', 'Check_in_manager'),
    ('Supervisor', 'Supervisor'),
)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    profile_info = models.TextField(max_length=150, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True, verbose_name='Picture')
    role = models.CharField(choices=ROLE_CHOICES,
                            max_length=100, null=True, blank=True, default='Passanger')

    def __str__(self):
        return self.user.username


class PassangerForm(ModelForm):
    class Meta:
        model = Passenger
        fields = ['role']


