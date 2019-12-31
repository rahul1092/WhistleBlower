from django.db import models
from whistle_blower.choices import USER_ACTIVE, USER_STATUSES


class WhistleUser(models.Model):
    """
    Details of the Whistle user
    """
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=False, null=False, unique=True)
    email_verified = models.BooleanField(default=False)
    isd_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    phone_verified = models.BooleanField(default=False)
    status = models.PositiveSmallIntegerField(
        default=USER_ACTIVE, choices=USER_STATUSES)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'WhistleUser'
