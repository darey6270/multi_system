from django.http import HttpResponseRedirect
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from app_user.forms import UserRegisterForm
from app_user.models import UserProfile
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

import os


# Create your views here.
class LogInfoListView(ListView):
    context_object_name = 'logs'
    model = UserProfile
    template_name = 'activities/log_info_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''

        logs = UserProfile.objects.filter(last_name__contains=str(search_input).lower())
        log = context['logs'].filter(log_status__contains=str(search_input).lower())
        log_name = UserProfile.objects.filter(first_name__name=str(search_input))

        print(logs)
        print(search_input + "it don't work")
        if search_input:
            context['logs'] = logs or log or log_name

        else:
            context['search_input'] = search_input

        return context


class LogReportListView(ListView):
    context_object_name = 'logs'
    model = UserProfile
    template_name = 'activities/log_report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_input = self.request.GET.get('search-area') or ''

        log_name = UserProfile.objects.filter(user__is_superuser=False)


        return context


class LogInfoDetailView(DetailView):
    model = UserProfile
    context_object_name = 'log'
    template_name = 'activities/log_info_detail.html'


class LogInfoUpdateView(UpdateView):
    form_class = UserRegisterForm
    template_name = 'activities/log_info_update.html'
    context_object_name = 'log'
    model = UserProfile

    def get_success_url(self):
        return reverse_lazy('activities:log_info_list')

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class LogInfoDeleteView(DeleteView):
    model = UserProfile
    context_object_name = 'log'
    template_name = 'activities/log_info_delete.html'

    def get_success_url(self):
        return reverse_lazy('activities:log_info_list')


def search_log(request):
    pass


def updateStatus(request, pk, log):
    user = get_object_or_404(UserProfile, user=log, id=pk)
    #user = UserProfile.objects.filter(user=log, id=pk)
    print(user.status)
    if user.status == True:
        user.status = False
    else:
        user.status = True
    user.save()
    return HttpResponseRedirect(reverse('activities:log_report'))
