
from django.contrib.postgres import forms

from ..conf import settings
from ..filters import Filter

from . import fields

__all__ = [
    'ArrayFilter',
    'HStoreFilter',
    'JSONFilter',
    'IntegerRangeFilter',
    'FloatRangeFilter',
    'DateTimeRangeFilter',
    'DateRangeFilter',
]


class ArrayFilter(Filter):

    @property
    def field(self):
        # It's necessary to rely on the model field's `.formfield()`, due to its nested structure.
        if not hasattr(self, '_field'):
            field_kwargs = self.extra.copy()

            if settings.DISABLE_HELP_TEXT:
                field_kwargs.pop('help_text', None)

            model_field = self.model._meta.get_field(self.field_name)
            self._field = model_field.formfield(label=self.label, **field_kwargs)
        return self._field


class HStoreFilter(Filter):
    field_class = forms.HStoreField


class JSONFilter(Filter):
    field_class = forms.JSONField


class IntegerRangeFilter(Filter):
    field_class = fields.IntegerRangeField


class FloatRangeFilter(Filter):
    field_class = fields.FloatRangeField


class DateTimeRangeFilter(Filter):
    field_class = fields.DateTimeRangeField


class DateRangeFilter(Filter):
    field_class = fields.DateRangeField
