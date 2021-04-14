from django.shortcuts import render
from django.views import View, generic

# Create your views here.


class HomeView(View):
    template_name = "code_arena/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        pass

class QuestionDetailsView(generic.DetailView):
    template_name = "code_arena/index.html"
