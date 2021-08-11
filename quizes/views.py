from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Question, Answer
from results.models import Result

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/main.html'


#To display list of quiz topics
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizes/quiz.html',{'quiz_obj':quiz})



#To save the quiz after attempting
def save_quiz_view(request,pk):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        for key in data_.keys():
            question = Question.objects.get(text=key)
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number
        results = []
        correct_answer = None

        for q in questions:
            selected = request.POST.get(q.text)

            if selected !="":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if selected == a.text:
                        if a.correct:
                            score +=1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer':correct_answer,'answered':selected}})   
            else:
                results.append({str(q): 'not answered'})

        score_ = score*multiplier 
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score_ >= quiz.score_to_pass:
            return JsonResponse({'passed':True, 'score':score_, 'results':results})

        else:
            return JsonResponse({'passed':False, 'score':score_, 'results':results})



#To display the quiz questions
def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for ques in quiz.get_questions():
        ans=[]
        for a in ques.get_answers():
            ans.append(a.text)
        questions.append({str(ques):ans})
    return JsonResponse({
        'data':questions,
        'time':quiz.time,
    })