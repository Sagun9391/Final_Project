from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages
from Tour.models.Customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class Signup(View):
    def get(self, request):
        values = {}  # Initialize an empty dictionary
        return render(request, 'signup.html', {'values': values})

    def post(self, request):
        values = {}  # Initialize an empty dictionary
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        errors = []

        if not full_name or not username or not password or not email or not phone_number or not address:
            errors.append("All fields are required.")
        else:
            values['full_name'] = full_name
            values['username'] = username
            values['email'] = email
            values['phone_number'] = phone_number
            values['address'] = address

        if len(phone_number) != 10 or not phone_number.isdigit():
            errors.append("Phone number should be 10 digits long and contain only digits.")

        try:
            validate_email(email)
        except ValidationError:
            errors.append("Invalid email format.")

        if errors:
            for error in errors:
                messages.error(request, error)
            # Pass the 'values' dictionary back to the template
            return render(request, 'signup.html', {'errors': errors, 'values': values})

        hashed_password = make_password(password)

        customer = Customer(
            full_name=full_name,
            username=username,
            password=hashed_password,
            email=email,
            phone_number=phone_number,
            address=address
        )

        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            customer.profile_picture = profile_picture

        customer.register()

        messages.success(request, "Signup successful. You can now login.")
        return redirect('login')