from django.db import models
from edc_action_item.models import ActionModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_model.models import BaseUuidModel, OtherCharField
from edc_pharmacy.models import Medication
from edc_sites.models import SiteModelMixin
from edc_utils import get_utcnow
from edc_visit_schedule import SubjectSchedule

from meta_pharmacy.constants import METFORMIN

from ..choices import WITHDRAWAL_STUDY_MEDICATION_REASONS
from ..constants import OFFSTUDY_MEDICATION_ACTION


class OffStudyMedication(
    NonUniqueSubjectIdentifierFieldMixin,
    SiteModelMixin,
    ActionModelMixin,
    BaseUuidModel,
):

    action_name = OFFSTUDY_MEDICATION_ACTION

    subject_schedule_cls = SubjectSchedule

    offschedule_compare_dates_as_datetimes = False

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time", default=get_utcnow
    )

    medications = models.ManyToManyField(Medication, limit_choices_to={"name": METFORMIN})

    stop_date = models.DateField(
        verbose_name="Date decision to stop study medication",
    )

    last_dose_date = models.DateField(
        verbose_name="Date of last known dose",
    )

    reason = models.CharField(
        verbose_name="Reason for stopping study medication",
        max_length=25,
        choices=WITHDRAWAL_STUDY_MEDICATION_REASONS,
    )

    reason_other = OtherCharField()

    comment = models.TextField(
        verbose_name="Comment",
        null=True,
        blank=True,
    )

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Withdrawal of Study Drug"
        verbose_name_plural = "Withdrawal of Study Drug"
