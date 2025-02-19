from datetime import datetime, timezone

from sentry.incidents.models.alert_rule import AlertRuleTrigger
from sentry.incidents.models.incident import (
    Incident,
    IncidentStatus,
    IncidentTrigger,
    TriggerStatus,
)
from sentry.models.organization import Organization
from sentry.testutils.cases import TestCase
from sentry.testutils.silo import region_silo_test


@region_silo_test
class AddProjectToIncludeAllRulesTest(TestCase):
    def test_include_all_projects_enabled(self):
        alert_rule = self.create_alert_rule(include_all_projects=True)
        new_project = self.create_project()
        assert alert_rule.snuba_query.subscriptions.filter(project=new_project).exists()

    def test_include_all_projects_disabled(self):
        alert_rule = self.create_alert_rule(include_all_projects=False)
        new_project = self.create_project()
        assert not alert_rule.snuba_query.subscriptions.filter(project=new_project).exists()

    def test_update_noop(self):
        new_project = self.create_project()
        alert_rule = self.create_alert_rule(
            include_all_projects=True, excluded_projects=[new_project]
        )
        new_project.update(name="hi")
        assert not alert_rule.snuba_query.subscriptions.filter(project=new_project).exists()


class PreSaveIncidentTriggerTest(TestCase):
    def test_update_date_modified(self):
        org = Organization.objects.create(name="chris' test org")
        alert_rule = self.create_alert_rule(include_all_projects=False)
        alert_rule.query = "event.type:error"
        trigger = AlertRuleTrigger.objects.create(
            alert_rule=alert_rule,
            label="warning",
            threshold_type=0,
            alert_threshold=100,
            resolve_threshold=50,
        )
        incident = Incident.objects.create(
            organization=org,
            detection_uuid=None,
            status=IncidentStatus.WARNING.value,
            type=2,
            title="a custom incident title",
            date_started=datetime.now(timezone.utc),
            date_detected=datetime.now(timezone.utc),
            alert_rule=alert_rule,
        )
        incident_trigger = IncidentTrigger.objects.create(
            incident=incident, alert_rule_trigger=trigger, status=TriggerStatus.ACTIVE.value
        )
        date_modified = incident_trigger.date_modified
        incident_trigger.status = TriggerStatus.RESOLVED.value
        incident_trigger.save()
        incident_trigger.refresh_from_db()
        assert date_modified < incident_trigger.date_modified
