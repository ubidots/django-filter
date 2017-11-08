
from django.contrib.postgres.forms import ranges
from .widgets import RangeWidget

__all__ = [
    'IntegerRangeField',
    'FloatRangeField',
    'DateTimeRangeField',
    'DateRangeField',
]


class SuffixedRangeField:
    def __init__(self, **kwargs):
        # This is copied from 'django.contrib.postgres.forms.ranges', but using
        # django-filter's SuffixedMultiWidget-based RangeWidget.
        if 'widget' not in kwargs:
            kwargs['widget'] = RangeWidget(self.base_field.widget)
        super(SuffixedRangeField, self).__init__(**kwargs)


class IntegerRangeField(SuffixedRangeField, ranges.IntegerRangeField):
    pass


class FloatRangeField(SuffixedRangeField, ranges.FloatRangeField):
    pass


class DateTimeRangeField(SuffixedRangeField, ranges.DateTimeRangeField):
    pass


class DateRangeField(SuffixedRangeField, ranges.DateRangeField):
    pass
