from django import forms
from .models import Article
from .models import Author

class DateInput(forms.DateInput):
    input_type = 'date'

class TextArea(forms.Textarea):
    rows = 50
    cols = 212
    resize = 'both'

    
class ArticleForm(forms.ModelForm):
        class Meta:
            model = Article
            fields = "__all__"
            widgets = {'publication':DateInput,
                       'text':TextArea,
                       }
        def save(self, commit=True):
            """ Save user and create a pro account """
            instance = super(ArticleForm, self).save(commit=False)
            


            if commit:
                instance.save()
                instance.author.add(Author.objects.get(id=1))
            return instance
            
