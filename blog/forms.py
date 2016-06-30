from django import forms
from .models import Post,result

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['style'] = 'width:1000px;height:100px;font-size:160%'


class resultform(forms.ModelForm):
    class Meta:
        model = result
        fields = ('title', 'technology', 'Version', 'release', 'file1', 'file2','remarks',)

    def __init__(self, *args, **kwargs):
        super(resultform, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['style'] = 'width:300px;height:30px;font-size:130%'
        self.fields['technology'].widget.attrs['style'] = 'width:300px;height:30px;font-size:130%'
        self.fields['Version'].widget.attrs['style'] = 'width:150px;height:30px;font-size:130%'
        self.fields['file1'].widget.attrs['style'] = 'width:300px;height:30px;font-size:90%'
        self.fields['file2'].widget.attrs['style'] = 'width:300px;height:30px;font-size:90%'
        self.fields['release'].widget.attrs['style'] = 'width:300px;height:30px;font-size:130%'
        self.fields['remarks'].widget.attrs['style'] = 'width:1000px;height:100px;font-size:130%'
