from django.shortcuts import render
from django.views import  View
# Create your views here.


class HomeView(View):
    """ Defining Home Page View """

    template_name = "landing/index.html"

    def get(self, request):
        """ Defining the GET method oon Home Page View """
        return render(request, template_name=self.template_name)

