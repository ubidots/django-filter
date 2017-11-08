
from ..widgets import SuffixedMultiWidget


class RangeWidget(SuffixedMultiWidget):
    template_name = 'django_filters/widgets/multiwidget.html'
    suffixes = ['lower', 'upper']

    def __init__(self, base_widget, attrs=None):
        widgets = (base_widget, base_widget)
        super(RangeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return (value.lower, value.upper)
        return (None, None)
