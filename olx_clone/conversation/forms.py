from django import forms

from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        labels = {
            'content': '',  # Setting the label to an empty string to hide it
        }
        widgets = {
            'content': forms.TextInput(attrs={
                'class' : 'w-full py-4 px-6 rounded-xl border',
                'placeholder' : 'Enter your message here...'
            })
        }