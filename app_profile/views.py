from django.shortcuts import render
from .models import (
    UserProfile,
    Project,
    Certificate,
    ContactForm,
    Skill,
    Visitors,
    Visualization,
    VisualizationForIp,
)
from django.core.mail import send_mail
import random
from django.http import JsonResponse
from django.conf import settings
from datetime import date, datetime
from ip2geotools.databases.noncommercial import DbIpCity



def error404(request, exception):
    if '/it/' in request.build_absolute_uri():
        return render(request, 'app_profile/it/error/404.html', status=404)
    else:
        return render(request, 'app_profile/eng/error/404.html', status=404)


def error500(request):
    if '/it/' in request.build_absolute_uri():
        return render(request, 'app_profile/it/error/500.html', status=500)
    else:
        return render(request, 'app_profile/eng/error/500.html', status=500)



def index_eng(request):
    get_visualization(request)

    context = {}
    certifications = Certificate.objects.filter(is_active=True).order_by("priority")
    projects_all = list(Project.objects.all())
    skill_language = Skill.objects.filter(show=True).filter(is_language=True).order_by('?')
    skill_cloud = Skill.objects.filter(show=True).filter(is_cloud=True).order_by('?')
    skill_python = Skill.objects.filter(show=True).filter(is_python=True).order_by('?')
    skill_other = Skill.objects.filter(show=True).filter(is_other=True).order_by('?')
    fil=list()
    filter_eng = list(Project.objects.values_list('filter', flat=True).distinct().order_by())
    projects = list()
    for f in filter_eng:    
        temp = list(Project.objects.filter(show = True).filter(filter = f))
        if len(temp)>0:
            fil.append(f)
            if len(temp) >=3:
                projects.extend(random.sample(temp, 3))
            else:
                projects.extend(random.sample(temp, len(temp)))
    random.shuffle(projects)
    user = UserProfile.objects.first()
    
    
    
    if request.method == 'POST':
        if get_contact(request):
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error'})

    context["certifications"] = certifications
    context["projects"] = projects
    context["user"] = user
    context["filter"] = fil
    context["projects_all"] = projects_all
    context["skill_language"] = skill_language
    context["skill_cloud"] = skill_cloud
    context["skill_python"] = skill_python
    context["skill_other"] = skill_other
    context["age"] = datetime.today().year - user.born.year
    context["experience"] = datetime.today().year - user.experience.year
    
    return render(request, 'app_profile/eng/index.html', context)


def index_it(request):
    get_visualization(request)
    context = {}
    certifications = Certificate.objects.filter(is_active=True).order_by("priority")
    projects = list()
    fil = list()
    projects_all = list(Project.objects.all())
    skill_language = Skill.objects.filter(show=True).filter(is_language=True).order_by('?')
    skill_cloud = Skill.objects.filter(show=True).filter(is_cloud=True).order_by('?')
    skill_python = Skill.objects.filter(show=True).filter(is_python=True).order_by('?')
    skill_other = Skill.objects.filter(show=True).filter(is_other=True).order_by('?')
    filter_it = list(Project.objects.values_list('filter_it', flat=True).distinct().order_by())
    for f in filter_it:
        temp = list(Project.objects.filter(show = True).filter(filter_it = f))
        if len(temp)>0:
            fil.append(f)
            if len(temp) >=3:
                projects.extend(random.sample(temp, 3))
            else:
                projects.extend(random.sample(temp, len(temp)))
    random.shuffle(projects)
    user = UserProfile.objects.first()
    if request.method == 'POST':
        if get_contact(request):
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error'})
        

    context["certifications"] = certifications
    context["projects"] = projects
    context["user"] = user
    context["filter_it"] = fil
    context["projects_all"] = projects_all
    context["skill_language"] = skill_language
    context["skill_cloud"] = skill_cloud
    context["skill_python"] = skill_python
    context["skill_other"] = skill_other
    context["age"] = datetime.today().year - user.born.year
    context["experience"] = datetime.today().year - user.experience.year

    return render(request, 'app_profile/it/index.html', context)


def projects_details_eng(request):
    context = {}
    projects = dict()
    filter_eng = list(Project.objects.values_list('filter', flat=True).distinct().order_by())
    random.shuffle(filter_eng)
    for f in filter_eng:
        temp = list(Project.objects.filter(show = True).filter(filter = f))
        if len(temp)>0:
            random.shuffle(temp)
            projects[f] = temp
    context['projects'] = projects
    return render(request, 'app_profile/eng/projects-details/main.html', context)




def projects_details_it(request):
    context = {}
    projects = dict()
    filter_it = list(Project.objects.values_list('filter_it', flat=True).distinct().order_by())
    random.shuffle(filter_it)
    for f in filter_it:
        temp = list(Project.objects.filter(show = True).filter(filter_it = f))
        if len(temp)>0:
            random.shuffle(temp)
            projects[f] = temp
    context['projects'] = projects
    return render(request, 'app_profile/it/projects-details/main.html', context)



def project_detail_eng(request, id):
    project = Project.objects.filter(id=id)
    return render(request, 'app_profile/eng/projects-details/project-details/project-details.html', {'project': project.first()})


def project_detail_it(request, id):
    project = Project.objects.filter(id=id)
    return render(request, 'app_profile/it/projects-details/project-details/project-details.html', {'project': project.first()})


def get_contact(request):
    contact = ContactForm()
    contact.name = request.POST.get("name")
    contact.email = request.POST.get("email")
    contact.subject = request.POST.get('subject')
    contact.message = request.POST.get('message')
    email_body = f"Email: {contact.email}\n\nFrom: {contact.name}\n\n\nMessage:\n {contact.message}"
    try:
        send_mail(
                contact.subject, 
                email_body,
                settings.EMAIL_HOST_USER,            
                [settings.EMAIL_HOST_USER]
            )
        contact.save()
        return True
    except:
        return False
    

def get_visualization(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        
    visitor = Visitors.objects.filter(ip_address = ip)
    visualization = Visualization.objects.filter(month=date.today().month).filter(year=date.today().year)
    if len(visitor)>=1 and visitor.first().date_of_visit != date.today():
        visitor.update(date_of_visit=date.today())
        visitor.update(number_of_visit = visitor.first().number_of_visit + 1)
        if visualization.exists():
            visualization.update(tot_visualization = visualization.first().tot_visualization + 1) 
        else:
            visualization = Visualization(year = date.today().year, month=date.today().month, tot_visualization = 1)
            visualization.save()
    elif len(visitor)==0:
        if visualization.exists():
           visualization.update(tot_visualization = visualization.first().tot_visualization + 1) 
        else:
            visualization = Visualization(year = date.today().year, month=date.today().month, tot_visualization = 1)
            visualization.save()
        res = DbIpCity.get(ip, api_key='free')
        location = f"{res.city}, {res.region}, {res.country}"
        visitor = Visitors(ip_address = ip, date_of_visit=date.today(), number_of_visit=1, location=location)
        visitor.save()
        new_visua = VisualizationForIp(ip = visitor, timestamp=datetime.now())
        new_visua.save()