from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_filters import filterset

from .. import compat
from .filters import BooleanFilter, IsoDateTimeFilter


class FilterSet(filterset.FilterSet):
    FILTER_DEFAULTS = {
        models.DateTimeField: {'filter_class': IsoDateTimeFilter},
        models.BooleanField: {'filter_class': BooleanFilter},
    }

    @property
    def form(self):
        form = super(FilterSet, self).form

        if compat.is_crispy():
            from crispy_forms.helper import FormHelper
            from crispy_forms.layout import Layout, Submit

            layout_components = list(form.fields.keys()) + [
                Submit('', _('Submit'), css_class='btn-default'),
            ]
            helper = FormHelper()
            helper.form_method = 'GET'
            helper.template_pack = 'bootstrap3'
            helper.layout = Layout(*layout_components)

            form.helper = helper

        return form
