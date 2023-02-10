from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)                             ##why we used forms

    def send_mail(self):
        pass