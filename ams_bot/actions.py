from rasa_sdk import Action
from typing import Dict, Text, Any, List, Union
from rasa_sdk import Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
import requests
import json
from db_connect import insert_ticket
from Similarity import get_most_similar_sent

class ActionFaqResponse(Action):
    def name(self):
        return 'action_faq_response'

    def run(self, dispatcher, tracker, domain):
        print("Action FAQ") 
        message = tracker.latest_message.get('text')
        print("Input Message:",message)
        response=get_most_similar_sent(message)
        print(response)
        dispatcher.utter_message(response)

class ActionWebSense(Action):
    def name(self):
        return 'action_web_sense'

    def run(self, dispatcher, tracker, domain):
        message = tracker.latest_message.get('text')
        address = tracker.get_slot('description')
        print("Ticket Description",message)
        print("slots",address)
        text_=insert_ticket('WebSense',message)
        print(text_)
        dispatcher.utter_message(str(text_))
        return []


class ActionSoftwareInstallation(Action):
    def name(self):
        return 'action_software_installation'

    def run(self, dispatcher, tracker, domain):
        message = tracker.latest_message.get('text')
        address = tracker.get_slot('description')
        print("Ticket Description",message)
        print("slots",address)
        text_=insert_ticket('Software Installation',message)
        print(text_)
        dispatcher.utter_message(str(text_))
        return []

class ActionAdminAccess(Action):
    def name(self):
        return 'action_admin_access'

    def run(self, dispatcher, tracker, domain):
        message = tracker.latest_message.get('text')
        address = tracker.get_slot('description')
        print("Ticket Description",message)
        print("slots",address)
        text_=insert_ticket('Admin Access',message)
        print(text_)
        dispatcher.utter_message(str(text_))
        return []

class ActionRequestForLaptop(Action):
    def name(self):
        return 'action_request_for_laptop'

    def run(self, dispatcher, tracker, domain):
        message = tracker.latest_message.get('text')
        address = tracker.get_slot('description')
        print("Ticket Description",message)
        print("slots",address)
        text_=insert_ticket('Laptop Issue',message)
        print(text_)
        dispatcher.utter_message(str(text_))
        return []

class ActionHardwareIssue(Action):
    def name(self):
        return 'action_hardware_issue'

    def run(self, dispatcher, tracker, domain):
        message = tracker.latest_message.get('text')
        address = tracker.get_slot('description')
        print("Ticket Description",message)
        print("slots",address)
        text_=insert_ticket('Hardware Issue',message)
        print(text_)
        dispatcher.utter_message(str(text_))
        return []

class TicketForm(FormAction):
    def name(self):
        """Unique identifier of the form"""
        return "ticket_form"

    @staticmethod
    def required_slots(tracker):
        """A list of required slots that the form has to fill.
        Use `tracker` to request different list of slots
        depending on the state of the dialogue
        """
        # print(tracker.get_slot('description'))
        return ["description"]

    def slot_mappings(self)-> Dict[Text, Union[Dict, List[Dict]]]:
        return { "description": self.from_text(intent=None)}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
              after all required slots are filled"""
        dispatcher.utter_message(template="utter_submit")    

        return []    




 # text="Call API: http://dubal5136v/PortalWS/PortalCPWS.asmx?op=Bot_Get_ETA"
       # PARAMS={'user_id':'admin','password':'12345'}
       # req = requests.get('http://127.0.0.1:8081/', params = PARAMS)
       # req_dict = json.loads(req.text)
       # return [SlotSet('order_number',order_id)]    