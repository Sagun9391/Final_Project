from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView
from Tour.models import Package


class CustomerHomeView(TemplateView):
    template_name = 'Customer_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_packages'] = Package.objects.filter(is_featured=True)[:3]
        return context
