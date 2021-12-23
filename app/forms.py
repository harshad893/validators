from django import forms

def check_for_a(value):
    if value[0].lower()=='a' :
        raise forms.ValidationError('name should not start with a')
def check_for_length(value):
    if len(value)>5:
        raise forms.ValidationError('name should not have motr than 5')


class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_length,check_for_a])
    email=forms.EmailField()
    re_email=forms.EmailField()
    age=forms.IntegerField()
    botcatcher=forms.CharField(max_length=200,widget=forms.HiddenInput,required=False)

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot is catched')

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_email']
        if e!=r:
            raise forms.ValidationError('emails not matched')
    