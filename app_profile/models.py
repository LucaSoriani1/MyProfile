from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Skill(models.Model):

    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
        ordering = ["name"]

    name = models.CharField(max_length=30, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="skills")
    is_language = models.BooleanField(default=False)
    is_cloud = models.BooleanField(default=False)
    is_python = models.BooleanField(default=False)
    is_key_skill = models.BooleanField(default=False)
    is_other = models.BooleanField(default=False)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    title_it = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    bio_it = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv_eng = models.FileField(blank=True, null=True, upload_to="cv")
    cv_it = models.FileField(blank=True, null=True, upload_to="cv")
    phone = models.CharField(max_length=20, blank=True, null=True)
    born = models.DateField(blank=True, null=True)
    experience = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    city_it = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Project(models.Model):

    class Meta:
        verbose_name_plural = 'Projects'
        verbose_name = 'Projects'
        
    name = models.CharField(max_length=200, blank=True, null=True)
    name_it = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    title_it = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_it = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    filter = models.CharField(max_length=100, blank=True, null=True)
    filter_it = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="projects")
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'Certifications'
        verbose_name = 'Certification'

    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    badge = models.ImageField(blank=True, null=True, upload_to="badges")
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_it = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    priority = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class ContactForm(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]
    
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    subject = models.CharField(max_length=200)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name} {self.email}'
    

class Visitors(models.Model):

    class Meta:
        verbose_name_plural = 'Visitors'
        verbose_name = 'Visitor'
        ordering = ["number_of_visit"]

    date_of_visit = models.DateField(blank=True, null=True)
    number_of_visit = models.IntegerField(default=0, blank=True, null=True)
    ip_address = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)


class VisualizationForIp(models.Model):
    class Meta:
        verbose_name_plural = 'Visualizations for IP'
        verbose_name = 'Visualization for IP'
    
    ip = models.ForeignKey(Visitors, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(blank=True, null=True)

class Visualization(models.Model):

    class Meta:
        verbose_name_plural = 'Visualizations'
        verbose_name = 'Visualization'
        ordering = ["year", "month"]

    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    tot_visualization = models.IntegerField(default=0, blank=True, null=True)