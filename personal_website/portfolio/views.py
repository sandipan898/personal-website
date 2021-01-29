from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Achievement, Education, Hobby, Skill, Project
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import View
from .forms import ContactForm

# Create your views here.

def home_view(request):

    template_name = 'portfolio/index.html'
    context = {}
    technology = Skill.objects.filter(skill_type='TE')
    tool = Skill.objects.filter(skill_type='TO')
    programming = Skill.objects.filter(skill_type='P')

    education = Education.objects.all

    projects = Project.objects.all

    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(request.POST)          
        if form.is_valid():
            print(form.cleaned_data)

            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            form.clean()
            try:    
                send_mail(
                    subject, 
                    message, 
                    from_email, 
                    ['sandipan.das898@gmail.com'])
                messages.success(request, ('Thanks for your valuable feedback!'))
            except BadHeaderError:
                print('Invalid header found.')
    else:
        form = ContactForm()
        context['form'] = form

    context1 = {
                'technologies': technology,
                'tools': tool,
                'educations': education,
                'projects': projects,
        }
    context.update(context1)
    return render(request, template_name, context=context)


class HomeView(View):
    template_name = 'portfolio/index.html'
    context = {}
    def get(self, *args, **kwargs):
        technology = Skill.objects.filter(skill_type='TE')
        tool = Skill.objects.filter(skill_type='TO')
        programming = Skill.objects.filter(skill_type='P')
        # for i in programming:
        #     print (i.icon)
        education = Education.objects.all
        projects = Project.objects.all
        achievements = Achievement.objects.all
        hobbies = Hobby.objects.all

        form = ContactForm()
        self.context['form'] = form
        context1 = {
                'technology_objects': technology,
                'tool_objects': tool,
                'programming': programming,  
                'educations': education,
                'projects': projects,
        }
        self.context.update(context1)
        return render(self.request, self.template_name, context=self.context)

    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST)          
        if form.is_valid():

            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            form.clean()
            try:    
                send_mail(
                    subject, 
                    message, 
                    from_email, 
                    ['sandipan.das898@gmail.com'])
                    
                messages.success(self.request, 'Your message has been sent successfully!')
                return redirect('home')
            except Exception as e:
                print(e)
                messages.error(self.request, ('Invalid header found.'))
        else:
            print("Please fill the form correctly")
            messages.warning(self.request, "Please fill the form correctly");
            return redirect('home')

