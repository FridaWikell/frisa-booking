from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string

from .forms import ContactForm

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

            return redirect('about')

    else:
        form = ContactForm()

    return render(request, 'about/about.html', {
        'form': form
    })