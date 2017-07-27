from django import forms
from django.core.exceptions import ValidationError
from profanity import profanity


class CommentForm(forms.Form):
    # author = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())

    def clean_body(self):
        if profanity.contains_profanity(self.cleaned_data['body']):
            raise ValidationError("Body shoudn't contain profanity")
        return self.cleaned_data['body']

    # def clean(self):
        # if self.cleaned_data['author'] == self.cleaned_data.get('body', ''):
        #     raise ValidationError('Author and body are same')
        # return self.cleaned_data
