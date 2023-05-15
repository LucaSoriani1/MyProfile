from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse

from .models import (
    UserProfile,
    Project,
    Certificate,
    Skill,
)
from .forms import ContactModelForm, ContactItModelForm
from .view_utils import get_contact, get_visualization, save_visitor_path

import random
from datetime import datetime


url_check=""

def error404(request, exception):

    global url_check

    status=404
    url = request.build_absolute_uri()


    if url_check != url:
        save_visitor_path(request, status)
        get_visualization(request, status)
        url_check = url
    
    if '/it/' in url:
        return render(request, 'app_profile/it/error/404.html', status=status)
    else:
        return render(request, 'app_profile/eng/error/404.html', status=status)

def error500(request):

    global url_check
    
    status=500
    url = request.build_absolute_uri()


    if url_check != url:
        save_visitor_path(request, status)
        get_visualization(request, status)
        url_check = url
    
    if '/it/' in url:
        return render(request, 'app_profile/it/error/500.html', status=status)
    else:
        return render(request, 'app_profile/eng/error/500.html', status=status)

def index(request):
    global url_check
    filter_type = 'filter'

    url = request.build_absolute_uri()
    template = 'app_profile/eng/index.html'
    form = ContactModelForm()

    if '/it/' in url:
        filter_type = 'filter_it'
        template = 'app_profile/it/index.html'
        form = ContactItModelForm()

    
    if url_check != url:
        save_visitor_path(request)
        get_visualization(request)
        url_check=url

    context = {}
    fil=list()
    projects = list()

    certifications = Certificate.objects.filter(is_active=True).order_by("priority")
    projects_all = list(Project.objects.all())
    skill_language = Skill.objects.filter(Q(show=True) & Q(is_language=True)).order_by('?')
    skill_cloud = Skill.objects.filter(Q(show=True) & Q(is_cloud=True)).order_by('?')
    skill_python = Skill.objects.filter(Q(show=True) & Q(is_python=True)).order_by('?')
    skill_other = Skill.objects.filter(Q(show=True) & Q(is_other=True)).order_by('?')
    filter = list(Project.objects.values_list(filter_type, flat=True).distinct().order_by())

    for f in filter:
        temp = list(Project.objects.filter(Q(show = True) & (Q(filter = f) | Q(filter_it = f))))
        if len(temp)>0:
            fil.append(f)
            projects.extend(random.sample(temp, 3)) if len(temp)>=3 else projects.extend(random.sample(temp, len(temp)))

    random.shuffle(projects)

    user = UserProfile.objects.get(user_id = 1)
    
    if request.method == 'POST':
        
        form = ContactModelForm(request.POST)
        
        if form.is_valid():
            try:
                get_contact(form)
                return JsonResponse(data={"status":"success"}, status=200)
            except:
                return JsonResponse(data={"status":"error"}, status=400)
        else:
            return JsonResponse(data={"status":"invalid"}, status=400)


    context["certifications"] = certifications
    context["projects"] = projects
    context["user"] = user
    context[filter_type] = fil
    context["projects_all"] = projects_all
    context["skill_language"] = skill_language
    context["skill_cloud"] = skill_cloud
    context["skill_python"] = skill_python
    context["skill_other"] = skill_other
    context["age"] = datetime.today().year - user.born.year
    context["experience"] = datetime.today().year - user.experience.year
    context["form"] = form
    
    return render(request, template, context)

def projects_details(request):

    global url_check
    url = request.build_absolute_uri()
    template = 'app_profile/eng/projects-details/main.html'
    filter_type = 'filter'

    if '/it/' in url:
        filter_type = 'filter_it'
        template = 'app_profile/it/projects-details/main.html'

    if url_check != url:
        save_visitor_path(request)
        get_visualization(request)
        url_check=url

    context = {}
    projects = dict()

    filter = list(Project.objects.values_list(filter_type, flat=True).distinct().order_by())

    random.shuffle(filter)

    for f in filter:
        temp = list(Project.objects.filter(Q(show = True) & (Q(filter = f) | Q(filter_it = f))))
        if len(temp)>0:
            random.shuffle(temp)
            projects[f] = temp

    context['projects'] = projects

    return render(request, template, context)

def project_detail(request, page):

    global url_check

    url = request.build_absolute_uri()

    template = 'app_profile/it/projects-details/project-details/project-details.html' if '/it/' in url else 'app_profile/eng/projects-details/project-details/project-details.html'
    if url_check != url:
        save_visitor_path(request)
        get_visualization(request)
        url_check = url

    project = Project.objects.get(page_name = page)

    return render(request, template, {'project': project})