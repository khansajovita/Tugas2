from django import forms
 
class TodoForm(forms.Form):
    judul = forms.CharField(max_length=100)
    deskripsi = forms.CharField(max_length=250)