from django.shortcuts import render
from .resources import AgencyResource, SitePartResource
from tablib import Dataset

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required # this one requires login from user. 
from django.views.generic import (TemplateView, ListView, DetailView)


class AboutView(TemplateView):
    template_name = 'myapp/about.html'
class ThanksPage(TemplateView):
    template_name = 'myapp/thanks.html'
class RegisterPage(TemplateView):
    template_name = 'myapp/register.html'

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')




def simple_upload(request):
    # error_import = None
    # success_import = None
    if request.method == 'POST':
        agency_resource = AgencyResource()
        print(agency_resource)
        sitepart_resource = SitePartResource()
        print(sitepart_resource)
        dataset = Dataset()
        new_r = request.FILES['myfile']


        #     success_import = "import Successful..."
        imported_data = dataset.load(new_r.read().decode("utf-8"), format='csv')
        result = agency_resource.import_data(dataset, dry_run=True, raise_errors= True) 
        if not result.has_errors():
            # error_import = "Oops. something went wrong could not import..."
            agency_resource.import_data(dataset, dry_run=False)  # Actually import now
            # system_resource.import_data(dataset, dry_run=False) 
    return render(request, 'myapp/importer.html')

