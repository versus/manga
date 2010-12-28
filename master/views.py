from django.http import Http404, HttpResponse 
from django.shortcuts import *
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def getip(request):
    return render_to_response('getip.html', {'ip_address': request.META['REMOTE_ADDR']})
