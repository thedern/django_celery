from django import forms
from .tasks import send_review_email_task


class ReviewForm(forms.Form):
    """
    user input for email
    uses built in django forms
    """
    name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))
    email = forms.EmailField(
        max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'form-email'}))
    review = forms.CharField(
        label="Review", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

    # sends the form to the task to be executed by celery (via the broker)
    def send_email(self):
        send_review_email_task.delay(
            self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['review'])
