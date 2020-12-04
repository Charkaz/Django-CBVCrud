from django import forms
from .models import Kitab

class kitabQeydView(forms.ModelForm):
    class Meta:
        model     = Kitab
        fields    = ['kitab_ad','kitab_onsoz','kitab_janr','kitab_seh','kitab_yazar','stokda','sekil'] 

    def __init__(self,*args,**kwargs):
        super(kitabQeydView,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class':'form-control'}
            


