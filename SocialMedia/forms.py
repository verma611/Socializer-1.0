from django import forms


from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'video')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Enter title here...'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-4', 'placeholder': 'Write your post here...'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file mb-4'}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control-file mb-4'}),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)