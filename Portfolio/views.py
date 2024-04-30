from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def project(request):
    return render(request, "project.html")

def contact(request):
    return render(request, "contact.html")

def contact_submit(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print(f"Name: {name}, Email: {email}, Subject: {subject}, Message: {message}")
        return HttpResponse('Form submitted successfully! Thank you for contacting us.')
    return HttpResponse('Invalid request method.')
