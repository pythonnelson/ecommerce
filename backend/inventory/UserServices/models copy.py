from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.contrib.auth.hashers import make_password
from InventoryServices.choices import *

class Users(AbstractUser):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=100)
    social_media_links = models.JSONField(null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, blank=True, null=True)
    address = models.TextField()
    pincode = models.CharField(max_length=10, blank=True, null=True)
    profile_pic = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    country = CountryField(blank_label="(select country)")
    account_status = models.CharField(max_length=50, blank=True, null=True, choices=ACCOUNT_CHOICES)
    role = models.CharField(max_length=100, blank=True, null=True, choices=ROLES)
    dob=models.DateField(null=True, blank=True)
    additonal_details = models.JSONField(null=True, blank=True)
    language = models.CharField(max_length=150, blank=True, null=True, choices=LANGAUGES)
    department = models.CharField(max_length=100, blank=True, null=True, choices=DEPARTMENTS)
    designation = models.CharField(max_length=150, blank=True, null=True, choices=DESIGNATION)
    time_zone = models.CharField(max_length=100, blank=True, null=True, choices=TIME_ZONES)
    last_login = models.DateTimeField(blank=True, null=True)
    last_device = models.CharField(max_length=100, blank=True, null=True)
    last_ip = models.GenericIPAddressField(blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True, null=True, choices=CURRENCIES)
    domain_user_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="domain_user_id_user")
    domain_name = models.CharField(max_length=50, blank=True, null=True)
    plan_type = models.CharField(max_length=50, blank=True, null=True, choices=PLAN_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def defaultKey():
        return 'username'
    
    def save(self, *args, **kwargs):
        if not self.domain_user_id and self.id:
            self.domain_user_id = Users.objects.get(id=self.id)

        if not self.pk or Users.objects.filter(pk=self.pk).values('password').first()['password'] != self.password:
            self.password = make_password(self.password)

        super().save(*args, **kwargs)



class UserShippingAddress(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPES)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    country = CountryField(blank_label="(select country)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Modules(models.Model):
    id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=50, unique=True)
    module_icon = models.TextField()
    is_menu = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    module_url = models.TextField()
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    display_order = models.IntegerField(default=0)
    module_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserPermissons(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    can_view = models.BooleanField(default=False)
    can_add = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name="domain_user_id_user_permissions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ActivityLog(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    activity = models.TextField()
    activity_type = models.CharField(max_length=50, blank=True, null=True)
    activity_date = models.DateTimeField(auto_now=True)
    activity_ip = models.GenericIPAddressField()
    activity_device = models.CharField(max_length=50, blank=True, null=True)
    domain_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True, related_name="domain_user_id_acitivity_log")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
