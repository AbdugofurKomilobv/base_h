from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'text']

    def save(self, user=None, commit=True):
        message = super().save(commit=False)
        if user:
            message.user = user
        if commit:
            message.save()
        return message
