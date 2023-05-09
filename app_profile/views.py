from django.shortcuts import render
from .models import (
    UserProfile,
    Project,
    Certificate,
    Skill,
)
import random
from django.http import JsonResponse
from datetime import datetime
from .view_utils import get_contact, get_visualization, save_visitor_path

url_check=""

def error404(request, exception):

    status=404
    url = request.build_absolute_uri()

    global url_check

    if url_check != url:
        save_visitor_path(request, status)
        get_visualization(request, status)
        url_check = url
    
    if '/it/' in url:
        return render(request, 'app_profile/it/error/404.html', status=status)
    else:
        return render(request, 'app_profile/eng/error/404.html', status=status)

def error500(request):

    status=500
    url = request.build_absolute_uri()

    global url_check

    if url_check != url:
        save_visitor_path(request, status)
        get_visualization(request, status)
        url_check = url
    
    if '/it/' in url:
        return render(request, 'app_profile/it/error/500.html', status=status)
    else:
        return render(request, 'app_profile/eng/error/500.html', status=status)

def index_eng(request):

    global url_check

    if url_check != request.build_absolute_uri():
        save_visitor_path(request)
        get_visualization(request)
        url_check=request.build_absolute_uri()

    context = {}
    fil=list()
    projects = list()

    certifications = Certificate.objects.filter(is_active=True).order_by("priority")
    projects_all = list(Project.objects.all())
    skill_language = Skill.objects.filter(show=True).filter(is_language=True).order_by('?')
    skill_cloud = Skill.objects.filter(show=True).filter(is_cloud=True).order_by('?')
    skill_python = Skill.objects.filter(show=True).filter(is_python=True).order_by('?')
    skill_other = Skill.objects.filter(show=True).filter(is_other=True).order_by('?')
    filter_eng = list(Project.objects.values_list('filter', flat=True).distinct().order_by())

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

    global url_check

    if url_check != request.build_absolute_uri():
        save_visitor_path(request)
        get_visualization(request)
        url_check=request.build_absolute_uri()
    
    context = {}
    fil = list()
    projects = list()

    certifications = Certificate.objects.filter(is_active=True).order_by("priority")
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

    global url_check

    if url_check != request.build_absolute_uri():
        save_visitor_path(request)
        get_visualization(request)
        url_check=request.build_absolute_uri()

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

    global url_check

    if url_check != request.build_absolute_uri():
        save_visitor_path(request)
        get_visualization(request)
        url_check=request.build_absolute_uri()

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

    global url_check

    if url_check != request.build_absolute_uri():
        save_visitor_path(request)
        get_visualization(request)
        url_check=request.build_absolute_uri()

    project = Project.objects.filter(id=id)

    return render(request, 'app_profile/eng/projects-details/project-details/project-details.html', {'project': project.first()})

def project_detail_it(request, id):

    global url_check

    if url_check != request.build_absolute_uri():
        save_visitor_path(request)
        get_visualization(request)
        url_check=request.build_absolute_uri()

    project = Project.objects.filter(id=id)

    return render(request, 'app_profile/it/projects-details/project-details/project-details.html', {'project': project.first()})