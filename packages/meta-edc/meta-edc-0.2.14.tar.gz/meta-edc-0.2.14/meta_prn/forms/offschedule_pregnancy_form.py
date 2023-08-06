from django import forms
from edc_action_item.forms.action_item_form_mixin import ActionItemFormMixin
from edc_form_validators.form_validator import FormValidator
from edc_form_validators.form_validator_mixin import FormValidatorMixin
from edc_sites.forms import SiteModelFormMixin
from edc_visit_schedule.modelform_mixins import OffScheduleModelFormMixin

from ..models import OffSchedulePregnancy


class OffSchedulePregnancyFormValidator(FormValidator):
    pass


class OffSchedulePregnancyForm(
    OffScheduleModelFormMixin,
    SiteModelFormMixin,
    FormValidatorMixin,
    ActionItemFormMixin,
    forms.ModelForm,
):

    form_validator_cls = OffSchedulePregnancyFormValidator

    subject_identifier = forms.CharField(
        label="Subject Identifier",
        required=False,
        widget=forms.TextInput(attrs={"readonly": "readonly"}),
    )

    class Meta:
        model = OffSchedulePregnancy
        fields = "__all__"
