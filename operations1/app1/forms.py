from django import forms

#form structure
class AdditionForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()


class BmiForm(forms.Form):
    weight= forms.IntegerField()
    height= forms.IntegerField()


class SignupForm(forms.Form):
    gender_choices=(('male','Male'),('female','Female'))
    role_choices=(('admin','Admin'),('student','Student'))


    username= forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)
    place= forms.CharField()
    gender= forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    role= forms.ChoiceField(choices=role_choices)
    email= forms.CharField()




class calorieForm(forms.Form):
    gender_choices=(('male','Male'),('female','Female'))
    activity_choices=(('1.2','sedentary'),('1.375','lightly active'),('1.55','moderately active'),('1.725','very active'),('1.9','extra active'))

    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)
    weight= forms.IntegerField()
    height= forms.IntegerField()
    age= forms.IntegerField()
    activity_levels= forms.ChoiceField(choices=activity_choices)






