from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from .forms import ContactForm


def about(request):
    """
    Validate contact form and send the filled out form to chosen backend.
    An htmx response is rendered when the contact form is sent.
    """
    response = """
    <h2>Whoa, that was fast!</h2>
    <p>&#128640; Your question just zoomed through the internet and
     landed in our inbox with a superhero landing! We're currently
     assembling a team of highly trained squirrels to craft the perfect
     response. We aim to get back to you within 48 hours, assuming
     the squirrels don't get distracted by any shiny objects...</p>
    """

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

            send_mail('New message from contact form', 'Message',
                      'frisa.craft@gmail.com', ['frisa.craft@gmail.com'],
                      html_message=html)

            if request.headers.get('HX-Request'):
                return HttpResponse(response)
        else:
            if request.headers.get('HX-Request'):
                return render(request, 'about/_contact_form.html',
                              {'form': form})

    else:
        form = ContactForm()

    return render(request, 'about/about.html', {
        'form': form
    })
