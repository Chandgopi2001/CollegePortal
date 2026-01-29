from django.contrib import admin
from .models import Admission,Contact
# Register your models here.
class AdmissionAdmin(admin.ModelAdmin):
    list_display=['student_name','parent_name','student_email','mobile_number','date_of_birth','gender','department']
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','message','created_at']
admin.site.register(Admission,AdmissionAdmin)
admin.site.register(Contact,ContactAdmin)
