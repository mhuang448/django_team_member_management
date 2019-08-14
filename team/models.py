from django.db import models

class TeamMember(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    admin_status = models.BooleanField(default = False)
    email = models.CharField(max_length=30)
    def __str__(self):
        if (self.admin_status):
            return self.first_name + " " + self.last_name + " (Admin)"
        else:
            return self.first_name + " " + self.last_name



# Create your models here.
