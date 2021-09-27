from django.utils.translation import ugettext_lazy as _

from mayan.apps.events.classes import EventTypeNamespace

namespace = EventTypeNamespace(label=_('Reviewers'), name='reviewers')

event_reviewer_attached = namespace.add_event_type(
    label=_('Reviewer attached to document'), name='attach'
)
event_reviewer_created = namespace.add_event_type(
    label=_('Reviewer created'), name='reviewer_created'
)
event_reviewer_removed = namespace.add_event_type(
    label=_('Reviewer removed from document'), name='remove'
)
event_reviewer_edited = namespace.add_event_type(
    label=_('Reviewer edited'), name='reviewer_edited'
)