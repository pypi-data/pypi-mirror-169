from .apps import *
from .utils import *
import os

JOB_STATES = ["queued", "completed", "skipped", "error"]
ENV_VAR_MSG = "Specified environment variable is not set."


class AbstractService:

    def __init__(self, config: dict, job: dict, app) -> None:
        self.config = config
        self.job = job
        self.app = app

    def execute_service(self):
        pass


class MissionRealty(AbstractService):

    def __init__(self, config: dict, job: dict, app: SierraInteractive) -> None:
        self.config = config
        self.job = job
        self.app = app
        super().__init__(config, job, app)

    def execute_service(self) -> dict:

        app_instance = self.app(self.config['params']['apiKey'], 'AT')

        notes = self.job['request']['notes'] if self.job['request']['notes'] else self.job['request']['disposition']

        lead = app_instance.find_leads(
            lead_phone=f"+1{self.job['request']['phone']}", lead_email=self.job['request']['email'])

        if not lead:

            lead = app_instance.add_new_lead(self.job['request'])

        lead_id = lead['leadId'] if 'leadId' in lead else lead['id']

        notes_response = app_instance.add_note(
            lead_id, notes)

        if not notes_response['success']:

            self.job['state'] = JOB_STATES[2]
            self.job['state_msg'] = notes_response

        self.job['state'] = JOB_STATES[1]
        self.job['state_msg'] = notes_response

        return self.job


class OwnLaHomes(AbstractService):

    def __init__(self, config: dict, job: dict, app: SierraInteractive) -> None:
        self.config = config
        self.job = job
        self.app = app
        super().__init__(config, job, app)

    def execute_service(self):

        app_instance = self.app(self.config['params']['apiKey'], 'AT')

        notes = self.job['request']['notes'] if self.job['request']['notes'] else self.job['request']['disposition']

        lead = app_instance.find_leads(
            lead_phone=f"+1{self.job['request']['phone']}", lead_email=self.job['request']['email'])

        if not lead:

            self.job['state'] = JOB_STATES[2]
            self.job['state_msg'] = "Lead not found, update skipped"

            return self.job

        lead_id = lead['leadId'] if 'leadId' in lead else lead['id']

        notes_response = app_instance.add_note(
            lead_id, notes)

        if not notes_response['success']:

            self.job['state'] = JOB_STATES[2]
            self.job['state_msg'] = notes_response

        self.job['state'] = JOB_STATES[1]
        self.job['state_msg'] = notes_response

        return self.job


class MultiLeadUpdate(AbstractService):

    """
    Job data structure
    {
        "request": {
            'first_name': str,
            'last_name': str,
            'email': str,
            'type_name': str,
            'DNIS': str,
            'ANI': str,
            'campaign_name': str
        },
        "state_msg": str or dict (depends on state),
        "service_instance": dict,
        "retry_attempt": int,
        "created": datetime,
        "state": str
    }
    """

    def __init__(self, config: dict, job: dict, app: Five9Custom) -> None:
        self.config = config
        self.job = job
        self.app = app
        self.search_criteria = {
            'contactIdField': 'contact_id',
            'criteria': [{'field': field, 'value': self.job['request'][field]}
                         for field in self.config['params']['searchFields']]
        }
        self.data_to_match = {value: self.job['request'][value]
                              for value in self.config['params']['searchFields']}
        self.number_to_skip = self.job['request']['DNIS'] if self.job['request'][
            'type_name'] != "Inbound" else self.job['request']['ANI']
        super().__init__(config, job, app)

    def execute_service(self):

        if all([value == "" for value in self.data_to_match.values()]):
            self.job['state'] = JOB_STATES[2]
            self.job['state_msg'] = "All search values are empty"
            return self.job

        app_instance = self.app(
            self.config['params']['user'],
            self.config['params']['password']
        )

        contacts = app_instance.search_contacts(self.search_criteria)

        if contacts is None:
            self.job['state'] = JOB_STATES[2]
            self.job['state_msg'] = "No records found."
            return self.job

        if len(contacts['records']) == 1000 or len(contacts['records']) == 1:

            self.job['state'] = JOB_STATES[2]
            self.job['state_msg'] = f"Too many records found: ${len(contacts['records'])}" if len(
                contacts['records']) == 1000 else f"No duplicate contacts found."
            return self.job

        dnc_list = self.get_exact_match(
            contacts['fields'], contacts['records'], self.data_to_match, self.number_to_skip)

        if len(dnc_list) == 0:

            self.job['state'] = JOB_STATES[2]
            self.job['state_msg'] = "No match found in search result."

            return self.job

        self.add_to_dnc(dnc_list, app_instance)

        self.send_notification(dnc_list)

        self.job['state'] = JOB_STATES[1]
        self.job['state_msg'] = {
            "numbersToDnc": dnc_list,
            "skippedNumber": self.number_to_skip
        }

        return self.job

    def get_exact_match(self, fields: list, values: list, request: dict, skipped_number: str) -> list:

        dnc_list = []

        indexes = [fields.index(field) for field in request.keys()]

        for value in values:

            extracted_values = [value['values']['data'][index] if value['values']
                                ['data'][index] is not None else "" for index in indexes]

            if extracted_values.sort() == list(request.values()).sort():

                for i in range(3):

                    number_field_index = fields.index(
                        f"number{i+1}")

                    if value['values']['data'][number_field_index] is None:
                        continue

                    if value['values']['data'][number_field_index] == skipped_number:
                        continue

                    dnc_list.append(value['values']['data']
                                    [number_field_index])

        return dnc_list

    def add_to_dnc(self, numbers: list, app_instance) -> int:

        if len(numbers) == 6 or len(numbers) == 5:

            list1 = numbers[:3]
            list2 = numbers[3:]

            response1 = app_instance.configuration.addNumbersToDnc(list1)
            response2 = app_instance.configuration.addNumbersToDnc(list2)

            return response1 + response2

        return app_instance.configuration.addNumbersToDnc(numbers)

    def send_notification(self, dnc_list):

        for_markdown = {
            "lead_name": f"{self.job['request']['first_name']} {self.job['request']['last_name']}",
            "campaign": self.job['request']['campaign_name'],
            "disposition": self.job['request']['disposition_name'],
            "target_number": self.number_to_skip,
            "dnc_numbers": ",".join(dnc_list)
        }

        markdown = generate_markdown(for_markdown)

        sender = os.environ.get('SENDER', ENV_VAR_MSG)
        password = os.environ.get('PASSWORD', ENV_VAR_MSG)
        recipients = os.environ.get('RECIPIENTS', ENV_VAR_MSG).split(",")
        subject = f"AT Central Notifications | Person Of Interest Identified"
        body = f"""
            A new person of interest has been identified for campaign {for_markdown['campaign']}<br>
            All other {len(dnc_list)} numbers were added to the DNC list.<br>∫
            {markdown}
        """

        return send_email(sender, password, recipients, subject, body)
