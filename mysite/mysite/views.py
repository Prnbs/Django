__author__ = 'prnbs'

from django.http import HttpResponse, Http404
import datetime
from django.template import Context
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', Context({'current_date' : now}))


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'future.html', Context({'offset':offset, 'time_then':dt}))


def display_meta(request):
    values = request.META.items()
    # values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
    return HttpResponse('<table>%s</table>' %'\n'.join(html))

# views.py

from mysite.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# ...

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['pranabesh.sinha@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject':'I love your site!'})
    return render(request, 'contact_form.html', {'form': form})
