from django import forms


class WebHookDetailsQueryParamForm(forms.Form):
    past_mins = forms.IntegerField(required=False)
    last_hits = forms.IntegerField(required=False)
