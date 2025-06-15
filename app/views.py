from django.shortcuts import render,redirect
from .models import Testimonial
from .forms import TestimonialForm
from .models import Blog
from django.http import HttpResponse
from twilio.rest import Client
from django.conf import settings
from django.contrib import messages


# Create your views here.


def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def services(request):
    return render(request, 'app/services.html')

def team(request):
    return render(request, 'app/team.html')

def thank_you(request):
    return render(request, 'app/thank_you.html')

# def testimonials(request):
#     return render(request, 'app/testimonials.html')

# def blog(request):
#     return render(request, 'app/blog.html')

# def contact(request):
#     return render(request, 'app/contact.html')

def testimonials(request):
    testimonials = Testimonial.objects.order_by('-created_at')
    form = TestimonialForm()

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('testimonials')  # name of the URL

    return render(request, 'app/testimonials.html', {
        'testimonials': testimonials,
        'form': form
    })
def blog(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'app/blog.html', {'blogs': blogs})






def contact_form(request):
    if request.method == "POST":
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Construct the WhatsApp message
        whatsapp_message = f"""
New Contact Form Submission:

*Name*: {name}
*Email*: {email}
*Phone*: {phone}
*Subject*: {subject}
*Message*: {message}

Thank you for your inquiry! We will respond to you shortly.
"""

        # Twilio credentials from settings.py
        account_sid = settings.TWILIO_ACCOUNT_SID  # Your Twilio Account SID
        auth_token = settings.TWILIO_AUTH_TOKEN    # Your Twilio Auth Token
        from_whatsapp_number = settings.TWILIO_PHONE_NUMBER  # Your Twilio WhatsApp sandbox number
        to_whatsapp_number = settings.TWILIO_TO_NUMBER  # Your personal/business WhatsApp number

        # Create Twilio client
        client = Client(account_sid, auth_token)

        try:
            # Send the WhatsApp message
            client.messages.create(
                body=whatsapp_message,
                from_=from_whatsapp_number,
                to=to_whatsapp_number
            )

            # Success message for the user after successful submission
            messages.success(request, "Thank you for your message. We will get back to you shortly!")

            # Redirect to a Thank You page
            return redirect('thank_you')  # Redirect to the 'thank_you' page
        except Exception as e:
            # If there is an error sending the message, show an error message
            messages.error(request, f"Sorry, there was an error sending your message: {str(e)}")
            return redirect('contact')  # Redirect back to the contact page if there's an error

    return render(request, 'app/contact.html')  # If it's a GET request, render the empty form


