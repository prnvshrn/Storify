from django import forms


class UsernameForm(forms.Form):
    UsernameTextbox = forms.CharField(max_length=50)
    
class StoryForm(forms.Form):
    TitleTextbox = forms.CharField(max_length=100)
    ContentTextbox = forms.CharField(max_length=600)
    #categoryTextbox = forms.CharField(max_length=20)
    SynopsisTextbox = forms.CharField(max_length=150)