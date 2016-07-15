from django.views.generic import FormView

from .forms import RegionChoiceForm


class RegionChoiceView(FormView):
    form_class = RegionChoiceForm
    template_name = 'region-choice.html'
