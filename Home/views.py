from django.shortcuts import render, redirect
from django.views.generic import View
# Create your views here.
from django.contrib import messages

from textblob import TextBlob

text = "I have no feelings"
Sem = TextBlob(text)
print(Sem.sentiment)

# create a class based view to get simple html page
from django.views.generic import TemplateView


class HomeView(View):
    template_name = 'Home/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        input = request.POST.get('inputSentiment')
        Sem = TextBlob(input)
        if Sem.sentiment.polarity > 0:
            messages.success(request, 'Positive')
        elif Sem.sentiment.polarity == 0:
            messages.info(request, 'Neutral')
        else:
            messages.error(request, 'Negative')
        return redirect('Home:home')


