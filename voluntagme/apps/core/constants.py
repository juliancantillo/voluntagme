from django.utils.translation import ugettext_lazy as _, string_concat
from django.utils import translation

CHOICES_CAUSE_CATEGORY = (
    ('', _('My cause is realted to'),),
    ('health', _('Health'),),
    ('emergencies', _('Emergencies'),),
    ('education', _('Education'),),
    ('rescue', _('Rescue'),),
    ('community', _('Community'),),
    ('homeless-and-housing', _('Homeless & Housing'),),
    ('animals', _('Animals'),),
    ('crisis-support', _('Crisis support'),),
    ('environtment', _('Environtment'),),
    ('sports', _('Sports'),),
    ('others', _('Others'),),
)

MENU_CAUSE_CATEGORY = (
    ('all', _('All categories'),),
    ('health', _('Health'),),
    ('emergencies', _('Emergencies'),),
    ('education', _('Education'),),
    ('rescue', _('Rescue'),),
    ('community', _('Community'),),
    ('homeless-and-housing', _('Homeless & Housing'),),
    ('animals', _('Animals'),),
    ('crisis-support', _('Crisis support'),),
    ('environtment', _('Environtment'),),
    ('sports', _('Sports'),),
    ('others', _('Others'),),
)