
from django.contrib import admin
from mysite.models import Contact, Profile
from mysite.models import PostJob
from mysite.models import Apply_job


# Register your models here.

admin.site.register(Contact)
admin.site.register(PostJob)
admin.site.register(Apply_job)
admin.site.register(Profile)

