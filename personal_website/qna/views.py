from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View, generic
from django.contrib.auth.decorators import login_required

from .models import Question, Answer
from .forms import QuestionPostForm, AnswerPostForm

# Create your views here.


class HomeView(View):
    template_name = "qna/home.html"

    def get(self, request, *args, **kwargs):
        questions = Question.objects.filter(featured=True)
        context = {
            "questions": questions
        }
        return render(request, context=context, template_name=self.template_name)


class QuestionDetailView(View):
    template_name = 'qna/details.html'
    
    def get(self, request, *args, **kwargs):
        selected_question = get_object_or_404(Question, slug=kwargs['slug'])
        print(selected_question.author.bio)
        # selected_question.get_answer_count
        # selected_question.save()
        related_questions = Question.objects.all()
        answers = Answer.objects.filter(question=selected_question)
        form = AnswerPostForm()
        
        context = {
            'question': selected_question,
            'related_questions': related_questions, 
            'answers': answers,
            'answer_count': answers.count(),
            'form': form,
        }
        # self.context.update(context)
        return render(request, self.template_name, context=context)
    
    # @login_required(login_url='/auth/login/')
    def post(self, *args, slug, **kwargs):
        form = AnswerPostForm(self.request.POST)     
        selected_question = get_object_or_404(Question, slug=slug)
        print(selected_question)
        if form.is_valid():

            new_answer = Answer.objects.create(
                question=selected_question,
                author=form.cleaned_data['author'], 
                body = form.cleaned_data['body'],
            )        
            new_answer.save()
            selected_question.get_answer_count
            selected_question.save()
            messages.success(self.request, "Your Answer is posted!")
            return redirect('/community/question/detail/'+slug)

        else:
            print("Please fill the form correctly")
            messages.warning(self.request, "Please fill the form correctly")
            # return redirect('article-detail')
            return redirect('/community/question/detail/'+slug)


@login_required(login_url='/auth/login/', redirect_field_name='qna-create')
def create_question_view(request):
    template_name = 'qna/question-form.html'
    context = {}
    if request.method == "POST":
        form = QuestionPostForm(request.POST, request.FILES or None)
        print(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new_question = Question.objects.create(
                author=request.user, 
                title = form.cleaned_data['title'],
                body = form.cleaned_data['body'],
                tags = form.cleaned_data['tags'],
            )
            new_question.save()
            print("question is created")
            messages.success(request, "Post will be published Soon!")
            return redirect('qna-home')
    else:
        form = QuestionPostForm()
        context['form'] = form
    
    return render(request, template_name, context=context)

  
def question_list_view(request):
    template_name = 'qna/question-list.html'
    questions = Question.objects.all()
    # related_topics = get_all_related_topic()

    context = {
        "questions": questions,
        # "related_topics": related_topics
    }
    return render(request, template_name=template_name, context=context)  
  