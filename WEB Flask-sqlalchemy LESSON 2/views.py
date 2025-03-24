from django.shortcuts import render
from django.views.generic import TemplateView
from flask import request
from data.news import News

class MainView(TemplateView):
    template_name = 'news_main.html'

    def get(self, request):
        if request.user.is_authenticated:
            new = News.objects.filter(author = request.user)
            ctx = {'news': news}
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})

