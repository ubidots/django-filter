
# import mock

# from django.test import TestCase

# from django_filters.postgres import NumericRangeFilter


# class NumericRangeFilterTests(TestCase):

#     def test_default_field(self):
#         f = NumericRangeFilter()
#         field = f.field
#         self.assertIsInstance(field, NumericRangeField)

#     def test_filtering(self):
#         qs = mock.Mock(spec=['filter'])
#         value = mock.Mock(start=20, stop=30)
#         f = NumericRangeFilter()
#         f.filter(qs, value)
#         qs.filter.assert_called_once_with(None__exact=(20, 30))

#     def test_filtering_exclude(self):
#         qs = mock.Mock(spec=['exclude'])
#         value = mock.Mock(start=20, stop=30)
#         f = NumericRangeFilter(exclude=True)
#         f.filter(qs, value)
#         qs.exclude.assert_called_once_with(None__exact=(20, 30))

#     def test_filtering_skipped_with_none_value(self):
#         qs = mock.Mock(spec=['filter'])
#         f = NumericRangeFilter()
#         result = f.filter(qs, None)
#         self.assertEqual(qs, result)

#     def test_field_with_lookup_expr(self):
#         qs = mock.Mock()
#         value = mock.Mock(start=20, stop=30)
#         f = NumericRangeFilter(lookup_expr=('overlap'))
#         f.filter(qs, value)
#         qs.filter.assert_called_once_with(None__overlap=(20, 30))

#     def test_zero_to_zero(self):
#         qs = mock.Mock(spec=['filter'])
#         value = mock.Mock(start=0, stop=0)
#         f = NumericRangeFilter()
#         f.filter(qs, value)
#         qs.filter.assert_called_once_with(None__exact=(0, 0))

#     def test_filtering_startswith(self):
#         qs = mock.Mock(spec=['filter'])
#         value = mock.Mock(start=20, stop=None)
#         f = NumericRangeFilter()
#         f.filter(qs, value)
#         qs.filter.assert_called_once_with(None__startswith=20)

#     def test_filtering_endswith(self):
#         qs = mock.Mock(spec=['filter'])
#         value = mock.Mock(start=None, stop=30)
#         f = NumericRangeFilter()
#         f.filter(qs, value)
#         qs.filter.assert_called_once_with(None__endswith=30)
