from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Main page'
        context['content'] = 'Magazine of furniture'
        return context







class AboutView(TemplateView):
    template_name = 'main/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - about page'
        context['content'] = 'Here is some text about us'
        context['text_on_page'] = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text '
        return context