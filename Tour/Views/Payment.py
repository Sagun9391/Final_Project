from django.shortcuts import render
from django.views import View


class payment(View):
    def get(self, request):
        return render(request, "Payment.html")
