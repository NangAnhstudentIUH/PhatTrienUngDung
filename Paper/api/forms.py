from django import forms

class User(forms.Form):
    username = forms.CharField(
        label=False,  
        max_length=100, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Vui lòng nhập Email của bạn',
            'type': 'email',
            'id': 'username',
        })
    )
    password = forms.CharField(
        label=False,  
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Vui lòng nhập Mật khẩu của bạn',
            'type': 'password',
            'id': 'password',
        })
    )
    
class Signup(forms.Form):
    firstname = forms.CharField(
        label=False,  
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Họ đệm',
            'type': 'text',
            'id': 'firstname',
        })
    )
    
    lastname = forms.CharField(
        label=False,  max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Tên',
            'type': 'text',
            'id': 'lastname',
        })
    )

    birthday = forms.DateField(
        label=False,
        widget=forms.TextInput(attrs={
            'type': 'date',
            'id': 'birthday',
            'min': '1950-01-01',
            'max':'2024-12-12'

        })
    )
    
    
    address = forms.CharField(
        label=False,  
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Địa chỉ',
            'type': 'text',
            'id': 'address',
        })
    )

    gender = forms.ChoiceField(
        label=False, 
        choices=[
            ('Giới tính', 'Giới tính'),
            ('Nam', 'Nam'),
            ('Nữ', 'Nữ'),
            ('Khác', 'Khác'), 
        ],
        initial='Giới tính',
    )
    
    username = forms.CharField(
        label=False,  
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Email',
            'type': 'email',
            'id': 'username',
        })
    )
    
    password = forms.CharField(
        label=False,  
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Mật khẩu',
            'type': 'password',
            'id': 'password',
        })
    )
    retype = forms.CharField(
        label=False, 
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Gõ lại mật khẩu',
            'type': 'password',
            'id': 'retype',
        })
    )