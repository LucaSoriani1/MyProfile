from django.contrib import admin

from . models import (
    UserProfile,
    Project,
    Certificate,
    Skill,
    Visitors,
    Visualization,
    VisualizationForIpDetail,
    )

from .forms import ContactForm

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'id')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'filter', 'show', 'url', 'id', )

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'startDate', 'endDate', 'is_active', 'id')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name','score', 'is_language', 'is_cloud', 'is_python', 'is_key_skill', 'is_other', 'show','id')

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'timestamp')

@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
     list_display = ('ip_address', 'location', 'path', 'number_of_visit', 'date_of_visit')
     search_fields = ['ip_address', 'location']     

@admin.register(Visualization)
class VisualizationAdmin(admin.ModelAdmin):
     list_display=('year', 'month', 'tot_visualization')

@admin.register(VisualizationForIpDetail)
class VisualizationForIpDetailAdmin(admin.ModelAdmin):
    list_display=('ip', 'timestamp', 'path')
    search_fields = ['ip']
