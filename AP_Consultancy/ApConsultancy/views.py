from django.shortcuts import render, redirect
from django.db import models
from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import RegisterJob, ContactForm
from .models import RegisterUser
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.db import IntegrityError
from django.conf import settings

def index(request):
    if request.method == 'POST':
        form = RegisterJob(request.POST)
        if form.is_valid():
            save_data=form.save(commit=False)
            try:
                save_data.save()
            except IntegrityError as e:
                return HttpResponse("already applied")

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            dob=form.cleaned_data['dob']
            job=form.cleaned_data['job']
            subject = "Regarding Job in field of " + job
            message="name: "+name+"\n"+"email: "+email+"\njob: "+job+"\nmobileNo.: "+str(mobile)
            email_from = settings.EMAIL_HOST_USER
            recipient_list=['aptechnologies23@gmail.com']
            #sendMail=EmailMessage(subject,message,emto=['aptechnologies23@gmail.com'])
            #sendMail.send()
            #try:
            #    send_mail( subject, message, email_from, recipient_list )
            #except:
            #    return HttpResponse('Invalid Mail')
            form=RegisterJob()
            return redirect('index')

    else:
        form = RegisterJob()
    return render(request, 'index.html', {'form':form})

def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('about.html', context_dict, context)


def contacts(request):
    if request.method == 'POST':
        form = RegisterJob(request.POST)
        if form.is_valid():
            save_data=form.save(commit=False)
            try:
                save_data.save()
            except IntegrityError as e:
                return HttpResponse("already applied")

    else:
        form = ContactForm()
    return render(request, 'contacts.html', {'form': form})

