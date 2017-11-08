from django.contrib.postgres import fields

from .. import filterset
from . import filters


class FilterSet(filterset.FilterSet):
    FILTER_DEFAULTS = {
        fields.ArrayField:              {'filter_class': filters.ArrayFilter},
        fields.HStoreField:             {'filter_class': filters.HStoreFilter},
        fields.JSONField:               {'filter_class': filters.JSONFilter},
        fields.IntegerRangeField:       {'filter_class': filters.IntegerRangeFilter},
        fields.BigIntegerRangeField:    {'filter_class': filters.IntegerRangeFilter},
        fields.FloatRangeField:         {'filter_class': filters.FloatRangeFilter},
        fields.DateTimeRangeField:      {'filter_class': filters.DateTimeRangeFilter},
        fields.DateRangeField:          {'filter_class': filters.DateRangeFilter},
    }
