from django.shortcuts import render, get_object_or_404
#get_object_or_404()を活用したら不要
#from django.http import Http404

# Create your views here.
#renderを活用すれば以下の2つが不要になる
#from django.http import HttpResponse
#from django.template import loader

from .models import Question

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#Section 3
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
    
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# show five questions latested in system
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    #NotCool
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    
    #GoodExample
    #template = loader.get_template('polls/index.html')
    context = {'latest_question_list':latest_question_list,}
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

# question detail
def detail(request, question_id):
    # try_catchで404を実現
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question':question})

    #get_object_or_404()を活用した場合
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
