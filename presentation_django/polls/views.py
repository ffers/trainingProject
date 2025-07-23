
from django.http import HttpResponse
from django.template import loader


def detail(request, question_id):
    template = loader.get_template("polls/index.html")
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    template = loader.get_template("polls/index.html")
    latest_question_list = [1,2,3,5]
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))