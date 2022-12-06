from django import forms

from web_project.common.models import FeaturedComment


class FeaturedCommentForm(forms.ModelForm):
    class Meta:
        model = FeaturedComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 35,
                    'rows': 10,
                    'placeholder': 'Add comment...'
                },
            ),
        }
# from web_project.common.models import FeaturedComments
#
#
# class NewCommentForm(forms.ModelForm):
#     class Meta:
#         model = FeaturedComments
#         fields = ['content']