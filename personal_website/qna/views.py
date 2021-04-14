from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View, generic

from .models import Question, Answer
from .forms import QuestionPostForm, AnswerPostForm
# Create your views here.


class HomeView(View):
    template_name = "qna/home.html"

    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        context = {
            "questions": questions
        }
        return render(request, context=context, template_name=self.template_name)


class QuestionDetailView(View):
    template_name = 'qna/details.html'
    
    def get(self, *args, **kwargs):
        selected_question = get_object_or_404(Question, slug=kwargs['slug'])
        # selected_question.get_answer_count
        # selected_question.save()
        related_questions = Question.objects.all()
        answers = Answer.objects.filter(article=selected_question)
        form = AnswerPostForm()
        self.context['form'] = form

        context = {
            'question': selected_question,
            'related_articles': related_questions, 
            'comments': answers,
            'comment_count': answers.count()
        }
        
        # self.context.update(context)
        return render(self.request, self.template_name, context=context)
    
    # @login_required(login_url='/auth/login/')
    def post(self, *args, slug, **kwargs):
        form = AnswerPostForm(self.request.POST)     
        selected_question = get_object_or_404(Question, slug=slug)
        print(selected_question)
        if form.is_valid():

            new_answer = Answer.objects.create(
                question=selected_question,
                author=form.cleaned_data['author'], 
                # comment_author = self.request.user.full_name,
                body = form.cleaned_data['body'],
            )        
            new_answer.save()
            messages.success(self.request, "Comment posted!")
            return redirect('/blog/article/detail/'+slug)

        else:
            print("Please fill the form correctly")
            messages.warning(self.request, "Please fill the form correctly");
            return redirect('article-detail')
