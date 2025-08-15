from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) < 5:
            raise forms.ValidationError("Заголовок должен быть длиннее 5 символов")
        return title

    def clean(self):
        cleaned_data = super().clean()
        body = cleaned_data.get("body")
        if body and "запрещено" in body.lower():
            self.add_error("body", "Текст содержит запрещённое слово")
        return cleaned_data
