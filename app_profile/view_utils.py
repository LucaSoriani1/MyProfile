from .models import (
    ContactForm,
    Visitors,
    Visualization,
    VisualizationForIpDetail
)
from django.core.mail import send_mail
from django.conf import settings
from datetime import date
from ip2geotools.databases.noncommercial import DbIpCity
from django.utils import timezone

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
    

def get_visualization(request, status=200):

    ip = get_ip(request)
    
    visitor, created = Visitors.objects.get_or_create(ip_address = ip)
    
    visualization, _ = Visualization.objects.get_or_create(month=date.today().month, year=date.today().year)

    if not created and visitor.date_of_visit != date.today():
        visitor.date_of_visit = date.today()
        visitor.number_of_visit += 1
        visitor.save()
        visualization.tot_visualization += 1
        visualization.save()
    elif created:
        visualization.tot_visualization += 1
        visualization.save()
        res = DbIpCity.get(ip, api_key='free')
        location = f"{res.city}, {res.region}, {res.country}"
        visitor.date_of_visit = date.today()
        visitor.number_of_visit = 1
        visitor.location = location
        visitor.path = ""
        visitor.save()
    
    update_path(visitor, request, status)

def get_ip(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')

    return user_ip.split(',')[0] if user_ip else request.META.get('REMOTE_ADDR')
    

def update_path(visitor, request, status):
    url = request.build_absolute_uri()
    ignored_extensions = (".png", ".jpg", ".css", ".ico", ".gif", ".jpeg", ".js")
    if not any(ext in url.lower() for ext in ignored_extensions):
        end = ".com/" if ":8000/" not in url else ":8000/"
        sl = len(end) - 1
        path = url[url.index(end) + sl:]
        path = "/eng" + path if "/it/" not in path else path
        path = f"({status}) {path}" if status != 200 else path
        new_path = path + " --> "
        visitor.path = visitor.path + new_path if visitor.path else new_path
        visitor.save()


def save_visitor_path(request, status=200):
    url = request.build_absolute_uri()
    ignored_extensions = (".png", ".jpg", ".css", ".ico", ".gif", ".jpeg", ".js")
    if not any(ext in url.lower() for ext in ignored_extensions):
        path = f"({status}) {url}" if status != 200 else url
        VisualizationForIpDetail(ip=get_ip(request), timestamp=timezone.now(), path=path).save()