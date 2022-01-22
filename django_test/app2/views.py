from django.shortcuts import render
from .forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import HttpResponse


# Create your views here.
class ReviewEmailView(FormView):
    # define template and form
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = "thanks for the review!"
        return HttpResponse(msg)
