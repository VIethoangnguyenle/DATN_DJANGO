from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
import json
from django.core.mail import send_mail
from .models import test,pen_show, filterByDay
from thienlong.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

class loginSite(LoginView):
    template_name = 'controlApp/login.html'

# Create your views here.
@login_required
def control(request):
    data = filterByDay.objects.get(id=1)
    filterDay = data.date
    print("filter " + filterDay)

    pen_good = pen_show.objects.filter(time = filterDay).order_by()
    context ={
        'pen_good':pen_good,
        'date': filterDay,
        }
    return render(request,'controlApp/control.html',context)
# class control(LoginRequiredMixin, TemplateView):
#     template_name = 'controlApp/control.html'

def submitData(request):
    # HttpResponse(status=200)
    try:
        request_body = json.loads(request.body.decode('utf8'))
        print(request_body)
        sizepaper = request_body['sizepaper']
        print(sizepaper)
        speed = request_body['speed']
        error = request_body['error']
        status = request_body['state']
        tests = test.objects.get(id=1)

        # print(request_body)
        tests.speed = speed
        tests.error = error
        tests.sizepaper=sizepaper
        tests.state = status
        tests.save()
        return HttpResponse(status=200)
    except Exception:
        return HttpResponse(status=400)

def sendmail(request):
    try:
        
        request_body = json.loads(request.body.decode('utf8'))
        email_to_send = request_body['email']
        date = request_body['date']
        pen_good = pen_show.objects.filter(time=date).order_by()
        context = {
            'pen_good': pen_good,
        }
        message = render_to_string(
                'controlApp/message.html',
                context,
                )
        plain_message = strip_tags(message)
        send_mail('Hello', plain_message,EMAIL_HOST_USER, [email_to_send], html_message=message)
        return HttpResponse(status = 200)
    
    except Exception:
        return HttpResponse(status = 400)

def filterDay(request):
    try:
        request_body = json.loads(request.body.decode('utf8'))
        date = request_body['date']
        data = filterByDay.objects.get(id=1)
        data.date = date
        data.save()
        return HttpResponse(status = 200)
    except Exception():
        return HttpResponse(status = 400)

def stop(request):
    # HttpResponse(status=200)
    try:
        request_body = json.loads(request.body.decode('utf8'))
        print(request_body)
        sizepaper = request_body['sizepaper']
        print(sizepaper)
        speed = request_body['speed']
        error = request_body['error']
        status = request_body['state']
        tests = test.objects.get(id=1)

        # print(request_body)
        tests.speed = speed
        tests.error = error
        tests.sizepaper=sizepaper
        tests.state = status
        tests.save()
        return HttpResponse(status=200)
    except Exception:
        return HttpResponse(status=400)