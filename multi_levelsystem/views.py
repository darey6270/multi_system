from django.views.generic import TemplateView, CreateView
# from .forms import UserRegisterForm
# from .models import UserInfoModel
from django.urls import reverse_lazy


# Create your views here.

class HomeView(TemplateView):
    template_name = 'multi_levelsystem/index.html'


class AboutView(TemplateView):
    template_name = 'multi_levelsystem/about.html'


class ContactView(TemplateView):
    template_name = 'multi_levelsystem/contact.html'


# class UserRegister(CreateView):
#     form_class = UserRegisterForm
#     model = UserInfoModel
#     context_object_name = 'User'
#     template_name = 'multi_levelsystem/sign-up.html'
#
#     def get_success_url(self):
#         return reverse_lazy('multi_levelsystem:index')
