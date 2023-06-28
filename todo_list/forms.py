from django import forms
from django.core.exceptions import ValidationError

from todo_list.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = "__all__"

    def clean_tags(self):
        tags = self.cleaned_data.get("tags")
        if not tags:
            raise ValidationError("Please select at least one tag.")
        return tags


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
