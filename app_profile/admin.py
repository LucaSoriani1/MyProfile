from django.contrib import admin
from . models import (
    UserProfile,
    Project,
    Certificate,
    Skill,
    ContactForm,
    Visitors,
    Visualization,
    VisualizationForIp,
    )

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
    list_display = ('name', 'email', 'subject')

@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
     list_display = ('ip_address', 'location', 'number_of_visit')

@admin.register(VisualizationForIp)
class VisualizationForIpAdmin(admin.ModelAdmin):
    list_display = ('get_ip', 'get_location', 'timestamp')
    
    @admin.display(description='Ip')
    def get_ip(self, obj):
        return obj.ip.ip_address
     
    @admin.display(description='Location')
    def get_location(self, obj):
        return obj.ip.location
     

@admin.register(Visualization)
class VisualizationAdmin(admin.ModelAdmin):
     list_display=('year', 'month', 'tot_visualization')