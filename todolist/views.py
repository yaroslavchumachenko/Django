from django.shortcuts import render

# Create your views here.
from .forms import NameForm
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def about(request):
    return render(request, 'todolist/about.html')

def home(request):
    return render(request, 'todolist/homepage.html')

# HOMEWORK

def nodes(request):
    return HttpResponse("Hello from Notes app.")

# HOMEWORK

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "todolist/authorisation.html", {"form": form})

def contact_us(request):
    if form.is_valid():
        form = NameForm(request.POST)
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]
        sender = form.cleaned_data["sender"]
        cc_myself = form.cleaned_data["cc_myself"]

    recipients = ["info@example.com"]
    if cc_myself:
        recipients.append(sender)

    send_mail(subject, message, sender, recipients)
    return HttpResponseRedirect("/thanks/")