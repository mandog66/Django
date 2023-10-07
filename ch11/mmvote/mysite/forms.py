from django.forms import ModelForm
from mysite import models

class PollForm(ModelForm):
    class Meta:
        model = models.Poll
        fields = ['name', 'enabled']
    def __init__(self, *args, **kwargs):
        super(PollForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '標題'
        self.fields['enabled'].label = '啟用'

class PollItemForm(ModelForm):
    class Meta:
        model = models.PollItem
        fields = ['name', 'image_url', 'vote']
    def __init__(self, *args, **kwargs):
        super(PollItemForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '選項名稱'
        self.fields['image_url'].label = '圖片網址'
        self.fields['vote'].label = '起始票數'
