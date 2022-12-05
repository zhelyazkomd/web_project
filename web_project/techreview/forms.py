from cloudinary.forms import CloudinaryFileField
from django import forms

from web_project.techreview.models import Featured


class BaseFeaturedForm(forms.ModelForm):
    class Meta:
        model = Featured
        exclude = ('user',)
        image = CloudinaryFileField(
            options={
                'tags': "directly_uploaded", })


class CreateFeaturedForm(BaseFeaturedForm):
    pass
