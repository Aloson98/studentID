from django.forms import ModelForm, TextInput, Select, DateInput
from .models import StudentPassport
from time import strftime, gmtime


class StudentForm(ModelForm):
    class Meta:
        model = StudentPassport
        fields = (
            "student_name", "school", "course", "registration_number", "expire_date", 
            "student_pic"
            )
        
        SCHOOLS = (
            ('school', 'select school'),
            ('school 1', 'school 1'),
            ('school 2', 'school 2'),
            ('school 3', 'school 3'),
        )
        COURSES = (
            ('course', 'select course'),
            ('course 1', 'course 1'),
            ('course 2', 'course 2'),
            ('course 3', 'course 3'),
            ('course 4', 'course 4')
        )
        widgets = {
            'student_name': TextInput(
                attrs={
                    "required": True, 
                    "class": "form-control my-2 text-capitalize", 
                    "placeholder": "name"}),
            'registration_number': TextInput(
                attrs={
                    "required": True, 
                    "class": "form-control my-2 text-capitalize", 
                    "placeholder": "Registration Number"}),
            'school': Select(
                choices=SCHOOLS,
                attrs={
                    'class': 'mb-2 form-select py-3',
                    'name' : 'school',
                    "required": True,
                }),
            'course': Select(
                choices=COURSES,
                attrs={
                    'class': 'mb-2 form-select my-3 py-3',
                    'name' : 'course',
                    "required": True, 
                }),
            'expire_date': DateInput(
                attrs={
                    'type': 'date',
                    'name': 'expire',
                    'class': 'form-control my-2 datepicker',
                    'required': True,
                })
        }