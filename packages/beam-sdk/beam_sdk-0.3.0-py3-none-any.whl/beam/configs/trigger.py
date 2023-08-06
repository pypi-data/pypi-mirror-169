from typing import Any, Dict, List

from beam.base import AbstractDataLoader, BaseConfiguration
from beam.dataclass import (
    CronJobConfiguration,
    RestAPIConfiguration,
    WebhookConfiguration,
)
from beam.serializer import BaseTriggerSerializer, CronJobTriggerSerializer
from beam.types import Types


class Webhook(BaseConfiguration):
    def __init__(self, inputs: Dict[str, Types], handler: str) -> None:
        self.config = WebhookConfiguration(inputs=inputs, handler=handler)

        BaseTriggerSerializer().validate(self.config.to_dict(), raise_exception=True)


class CronJob(BaseConfiguration):
    def __init__(
        self, inputs: Dict[str, Types], cron_schedule: str, handler: str
    ) -> None:
        self.config = CronJobConfiguration(
            inputs=inputs, cron_schedule=cron_schedule, handler=handler
        )

        CronJobTriggerSerializer().validate(self.config.to_dict(), raise_exception=True)


class RestAPI(BaseConfiguration):
    def __init__(
        self, inputs: Dict[str, Types], outputs: Dict[str, Types], handler: str
    ) -> None:
        self.config = RestAPIConfiguration(
            inputs=inputs, outputs=outputs, handler=handler
        )

        BaseTriggerSerializer().validate(self.config.to_dict(), raise_exception=True)


class TriggerManager(AbstractDataLoader):
    def __init__(self) -> None:
        self.webhooks: List[Webhook] = []
        self.cron_jobs: List[CronJob] = []
        self.rest_apis: List[RestAPI] = []

    def Webhook(self, inputs: Dict[str, Types], handler: str):
        """
        Arguments:
            inputs: dictionary specifying how to serialize/deserialize input arguments
        """
        self.webhooks.append(Webhook(inputs=inputs, handler=handler))

    def CronJob(self, inputs: Dict[str, Types], cron_schedule: str, handler: str):
        """
        Arguments:
            inputs: dictionary specifying how to serialize/deserialize input arguments
            cron_schedule: CRON string to indicate the schedule in which the job is to run
                - https://en.wikipedia.org/wiki/Cron
        """
        self.cron_jobs.append(
            CronJob(inputs=inputs, cron_schedule=cron_schedule, handler=handler),
        )

    def RestAPI(
        self, inputs: Dict[str, Types], outputs: Dict[str, Types], handler: str
    ):
        """
        Arguments:
            inputs: dictionary specifying how to serialize/deserialize input arguments
            outputs: dictionary specifying how to serialize/deserialize return values
        """
        self.rest_apis.append(RestAPI(inputs=inputs, outputs=outputs, handler=handler))

    def dumps(self):
        return {
            "webhooks": [w.dumps() for w in self.webhooks],
            "cron_jobs": [c.dumps() for c in self.cron_jobs],
            "rest_api": [r.dumps() for r in self.rest_apis],
        }

    def from_config(self, triggers):
        webhooks = triggers.get("webhooks")
        cron_jobs = triggers.get("cron_jobs")
        rest_apis = triggers.get("rest_api")

        for w in webhooks:
            self.Webhook(**w)

        for c in cron_jobs:
            self.CronJob(**c)

        for r in rest_apis:
            self.RestAPI(**r)
