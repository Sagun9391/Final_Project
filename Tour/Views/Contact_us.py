from django.shortcuts import render, redirect
from Tour.models.Contact_us import Contact_Us
from django.views import View
from django.contrib import messages


class Contact_Us(View):

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create a new Contact object and save it to the database
        contact = Contact_Us(name=name, email=email, subject=subject, message=message)
        contact.save()

        # Add a success message
        messages.success(request, 'Your message has been received successfully. We will get back to you soon.')

        return redirect('Contact_us')  # Redirect to the 'Contact_us' page

    def get(self, request):
        return render(request, 'Contact_us.html', {'message_received': False})
