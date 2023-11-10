from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import date


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    PAAS = "Paas"
    SAAS = "Saas"
    IAAS = "Iaas"

    SERVICES = (
        (PAAS, 'Platform as a Service (Paas)'),
        (SAAS, 'Software as a Service (Saas)'),
        (IAAS, 'Infrastructure as a Service (IAAS)'),
    )
    Date_of_Birth = models.DateField(null=False, default=date.today)
    Phone_number = models.IntegerField(null=False, default="09023451234")
    Service_required = models.CharField(max_length=30, choices=SERVICES, default=PAAS)
    What_is_your_favourite_color = models.CharField(max_length=23)
    status = models.BooleanField(default=True, blank=False)
    login_time = models.DateTimeField(auto_now=True, blank=True)
    Ip_address = models.GenericIPAddressField(null=False, default="192.168.1.1")

    def clean(self):
        if self.Ip_address:
            self.Ip_address = get_client_ip()
            print("Ip_address %d" % self.Ip_address)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)


def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


post_save.connect(save_user_profile, sender=User)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
