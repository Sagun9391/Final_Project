from django.shortcuts import render, redirect
from Tour.models.Customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_username(username)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                return redirect('Customer_Home')
            else:
                error_message = 'Username or Password Invalid'
        else:
            error_message = 'Username or Password Invalid'
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('index')
