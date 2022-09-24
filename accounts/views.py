from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CUCREATIONFORM

class SignUp(CreateView):
    form_class = CUCREATIONFORM
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')