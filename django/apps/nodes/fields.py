from django.utils import six
from rest_framework.serializers import ChoiceField


class NamedChoiceField(ChoiceField):

    def __init__(self, **kwargs):
        super(NamedChoiceField, self).__init__(**kwargs)
        # support passing the choice display value, not just the database value
        self.choice_strings_to_values.update({
            six.text_type(value) : key for key, value in self.choices.items()
        })

    # return the choice display value instead of the database value
    def to_representation(self, value):
        if value in ('', None):
            return value
        return self.choices[value]
