from django.conf import settings
from django.shortcuts import HttpResponse, render, get_object_or_404

import requests
from urllib.parse import quote

from .models import Service

def form(request):
    services = Service.objects.all
    context = {'services': services}
    return render(request, 'sms/form.html', context)
def send (request):
    service_name = request.POST['service']
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    service = Service.objects.get(service_name=service_name)
    service_message = service.get_message()
    message = quote("שלום, " + first_name + "\n" + service_message)
    url = "https://cellactpro.net/GlobalSms/ExternalClient/GlobalAPI.asp"
    XMLString = "XMLString="\
        "%3CPALO%3E"\
        "%3CHEAD%3E"\
        "%3CFROM%3E" + settings.ORGANIZATION_NAME + "%3C%2FFROM%3E"\
        "%3CAPP%20USER%3D%22" + settings.USER_NAME + "%22"\
        "%20PASSWORD%3D%22" + settings.PASSWORD + "%22%2F%3E"\
        "%3CCMD%3E" + "sendtextmt" + "%3C%2FCMD%3E"\
        "%3CCONF_LIST%3E%20%3CTO%3Ehttp%3A%2F%2F0.0.0.0%2Fconf.asp%3C%2FTO%3E%20%3C%2FCONF_LIST%3E"\
        "%3C%2FHEAD%3E"\
        "%3CBODY%3E"\
        "%3CCONTENT%3E" + message + "%3C%2FCONTENT%3E"\
        "%3CDEST_LIST%3E"\
        "%3CTO%3E%2B972547278511%3C%2FTO%3E"\
        "%3C%2FDEST_LIST%3E"\
        "%3C%2FBODY%3E"\
        "%3COPTIONAL%3E"\
        "%3CCALLBACK%3E%20%2B972546227127%3C%2FCALLBACK%3E"\
        "%3CSIGNATURE%2F%3E"\
        "%3C%2FOPTIONAL%3E"\
        "%3C%2FPALO%3E"
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'ASPSESSIONIDQASBQCBQ=JBOAKHHDPJKCCKIOKJHGKBFC'

    }

    response = requests.request("POST", url, headers=headers, data=XMLString)
    if response.status_code == 200:
        return HttpResponse(response.text)
    return HttpResponse('Could not save data')