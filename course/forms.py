from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Form definition for MODELNAME."""
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control rounded-0',
        'placeholder': 'دیدگاه'
    }))

    class Meta:
        """Meta definition for MODELNAMEform."""
        model = Comment
        fields = ('content',)


    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ""
