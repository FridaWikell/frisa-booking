from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages

from .forms import ContactForm

response = """
<h2>Whoa, that was fast!</h2>
<p>&#128640; Your question just zoomed through the internet and 
landed in our inbox with a superhero landing! We're currently 
assembling a team of highly trained squirrels to craft the perfect response. 
We aim to get back to you within 48 hours, assuming the squirrels don&#146t 
get distracted by any shiny objects...</p>
"""

# Create your views here.
# Ändra detta till about.html?
def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('about/emails/form.html', {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'content': content
            })

            send_mail('The contact form subject', 'This is the message', 'noreply@codewithsten.com', ['frida.wikell@gmail.com'], html_message=html)
            
            if request.headers.get('HX-Request'):
                # Return a simple HttpResponse with a success message
                return HttpResponse(response)
        else:
            if request.headers.get('HX-Request'):
                # For invalid form with htmx request, return only the form fragment
                return render(request, 'about/_contact_form.html', {'form': form})

    else:
        form = ContactForm()

    return render(request, 'about/about.html', {
        'form': form
    })