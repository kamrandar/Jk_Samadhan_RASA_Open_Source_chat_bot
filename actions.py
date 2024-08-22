# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction

# Choose between whether you want to Track or Lodge a Grievance #

class ActionPromptChoice(Action):
    def name(self) -> Text:
        return "action_prompt_choice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_grievance_prompt")
        return []

class ActionTrackIssue(Action):
    def name(self) -> Text:
        return "action_track_issue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="The grievance may be tracked on the Web Portal (https://jkgrievance.in) using Track Grievance link.")
        return []

class ActionLodgeGrievance(Action):
    def name(self) -> Text:
        return "action_lodge_grievance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="The grievances can be lodged online on Web Portal (https://jkgrievance.in)In cases where internet facility is not available or even otherwise, the citizen is free to send her/his grievance by Post. There is no prescribed format. However the application must clearly mention the Name, Complete Address and Contact No of the Applicant. The grievance may be written on any plain sheet of paper and addressed to Department of Public Grievances. The grievance can also be filled through the Toll Free Call Centers.")
        return []


# Providing Contact details of Office of DOPG

class ActionHandleOptions(Action):

    def name(self) -> Text:
        return "action_handle_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # The default value is main
        submenu = tracker.get_slot("submenu")
        option2action_name =   {"main": {
                                    1: "action_show_contact_details_of_kashmir",
                                    2: "action_show_contact_details_of_Jammu"}
                               }
        try:
            option = int(tracker.get_slot("option"))
        except ValueError:
            dispatcher.utter_message(text=f"Please enter a number!")
            return [SlotSet('option', None)]
        try:
            next_action = option2action_name[submenu][option]
        except KeyError:
            dispatcher.utter_message(text=f"This option is not available!")
            return [SlotSet('option', None)]

        dispatcher.utter_message(text=f"You've choosen option {option} !")

        if type(next_action) is tuple:
            return [SlotSet('option', None),
                    SlotSet('suboption', next_action[1]),
                    FollowupAction(name=next_action[0])]
        else:
            return [SlotSet('option', None),
                    FollowupAction(name=next_action)]

# source of framework descriptions: https://marutitech.com/top-8-deep-learning-frameworks/

class ActionHandleTensorflow(Action):

    def name(self) -> Text:
        return "action_show_contact_details_of_kashmir"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """|DIVISION|                |KASHMIR|
             |Office Address|          |Department of Public Grievances Church Lane, Sonwar, Srinagar -190001|
             |Contact Nos|             |0194-2502596, 2502910, 2483236|
             |Fax|                     |0194-2501262|
             |Toll Free Call Centre|   |18005722328|
             |e-Mail|                  |jk-grievance@jk.gov.in|"""
        dispatcher.utter_message(text=message)

        return []

class ActionHandleDeepLearning4J(Action):

    def name(self) -> Text:
        return "action_show_contact_details_of_Jammu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """|DIVISION|                |JAMMU|
             |Office Address|          |Department of Public GrievancesCivil Secretariat, Jammu|
             |Contact Nos|             |0191 - 2560109, 2560265, 2560266|
             |Fax|                     |0191-2566182|
             |Toll Free Call Centre|   |18005722327|
             |e-Mail|                  |jk-grievance@jk.gov.in|"""
        dispatcher.utter_message(text=message)

        return []



class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_template("utter_default", tracker)
        return []
    


    ###################################HINDI##########################################

    # Choose between whether you want to Track or Lodge a Grievance #

class ActionPromptChoice(Action):
    def name(self) -> Text:
        return "action_prompt_choice_hindi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_grievance_prompt_hindi")
        return []

class ActionTrackIssue(Action):
    def name(self) -> Text:
        return "action_track_issue_hindi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="The grievance may be tracked on the Web Portal (https://jkgrievance.in) using Track Grievance link.")
        return []

class ActionLodgeGrievance(Action):
    def name(self) -> Text:
        return "action_lodge_grievance_hindi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="The grievances can be lodged online on Web Portal (https://jkgrievance.in)In cases where internet facility is not available or even otherwise, the citizen is free to send her/his grievance by Post. There is no prescribed format. However the application must clearly mention the Name, Complete Address and Contact No of the Applicant. The grievance may be written on any plain sheet of paper and addressed to Department of Public Grievances. The grievance can also be filled through the Toll Free Call Centers.")
        return []


# Providing Contact details of Office of DOPG

class ActionHandleOptions(Action):

    def name(self) -> Text:
        return "action_handle_options_hindi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # The default value is main
        submenu = tracker.get_slot("submenu")
        option2action_name =   {"main": {
                                    1: "action_show_contact_details_of_kashmir_hindi",
                                    2: "action_show_contact_details_of_Jammu_urdu"}
                               }
        try:
            option = int(tracker.get_slot("option"))
        except ValueError:
            dispatcher.utter_message(text=f"कृपया एक संख्या दर्ज करें!")
            return [SlotSet('option', None)]
        try:
            next_action = option2action_name[submenu][option]
        except KeyError:
            dispatcher.utter_message(text=f"यह विकल्प उपलब्ध नहीं है!")
            return [SlotSet('option', None)]

        dispatcher.utter_message(text=f"आपने विकल्प चुना है {option} !")

        if type(next_action) is tuple:
            return [SlotSet('option', None),
                    SlotSet('suboption', next_action[1]),
                    FollowupAction(name=next_action[0])]
        else:
            return [SlotSet('option', None),
                    FollowupAction(name=next_action)]

# source of framework descriptions: https://marutitech.com/top-8-deep-learning-frameworks/

class ActionHandleTensorflow(Action):

    def name(self) -> Text:
        return "action_show_contact_details_of_kashmir_hindi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """|DIVISION|                |KASHMIR|
             |Office Address|          |Department of Public Grievances Church Lane, Sonwar, Srinagar -190001|
             |Contact Nos|             |0194-2502596, 2502910, 2483236|
             |Fax|                     |0194-2501262|
             |Toll Free Call Centre|   |18005722328|
             |e-Mail|                  |jk-grievance@jk.gov.in|"""
        dispatcher.utter_message(text=message)

        return []

class ActionHandleDeepLearning4J(Action):

    def name(self) -> Text:
        return "action_show_contact_details_of_Jammu_hindi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """|DIVISION|                |JAMMU|
             |Office Address|          |Department of Public GrievancesCivil Secretariat, Jammu|
             |Contact Nos|             |0191 - 2560109, 2560265, 2560266|
             |Fax|                     |0191-2566182|
             |Toll Free Call Centre|   |18005722327|
             |e-Mail|                  |jk-grievance@jk.gov.in|"""
        dispatcher.utter_message(text=message)

        return []





###################################URDU##########################################

    # Choose between whether you want to Track or Lodge a Grievance #

class ActionPromptChoice(Action):
    def name(self) -> Text:
        return "action_prompt_choice_urdu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_grievance_prompt_urdu")
        return []

class ActionTrackIssue(Action):
    def name(self) -> Text:
        return "action_track_issue_urdu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="The grievance may be tracked on the Web Portal (https://jkgrievance.in) using Track Grievance link.")
        return []

class ActionLodgeGrievance(Action):
    def name(self) -> Text:
        return "action_lodge_grievance_urdu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="The grievances can be lodged online on Web Portal (https://jkgrievance.in)In cases where internet facility is not available or even otherwise, the citizen is free to send her/his grievance by Post. There is no prescribed format. However the application must clearly mention the Name, Complete Address and Contact No of the Applicant. The grievance may be written on any plain sheet of paper and addressed to Department of Public Grievances. The grievance can also be filled through the Toll Free Call Centers.")
        return []


# Providing Contact details of Office of DOPG

class ActionHandleOptions(Action):

    def name(self) -> Text:
        return "action_handle_options_urdu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # The default value is main
        submenu = tracker.get_slot("submenu")
        option2action_name =   {"main": {
                                    1: "action_show_contact_details_of_kashmir_urdu",
                                    2: "action_show_contact_details_of_Jammu_urdu"}
                               }
        try:
            option = int(tracker.get_slot("option"))
        except ValueError:
            dispatcher.utter_message(text=f"براہ کرم ایک نمبر درج کریں!")
            return [SlotSet('option', None)]
        try:
            next_action = option2action_name[submenu][option]
        except KeyError:
            dispatcher.utter_message(text=f"یہ اختیار دستیاب نہیں ہے")
            return [SlotSet('option', None)]

        dispatcher.utter_message(text=f"آپ نے اختیار منتخب کیا ہے! {option} !")

        if type(next_action) is tuple:
            return [SlotSet('option', None),
                    SlotSet('suboption', next_action[1]),
                    FollowupAction(name=next_action[0])]
        else:
            return [SlotSet('option', None),
                    FollowupAction(name=next_action)]

# source of framework descriptions: https://marutitech.com/top-8-deep-learning-frameworks/

class ActionHandleTensorflow(Action):

    def name(self) -> Text:
        return "action_show_contact_details_of_kashmir_urdu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """|DIVISION|                |KASHMIR|
             |Office Address|          |Department of Public Grievances Church Lane, Sonwar, Srinagar -190001|
             |Contact Nos|             |0194-2502596, 2502910, 2483236|
             |Fax|                     |0194-2501262|
             |Toll Free Call Centre|   |18005722328|
             |e-Mail|                  |jk-grievance@jk.gov.in|"""
        dispatcher.utter_message(text=message)

        return []

class ActionHandleDeepLearning4J(Action):

    def name(self) -> Text:
        return "action_show_contact_details_of_Jammu_urdu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """|DIVISION|                |JAMMU|
             |Office Address|          |Department of Public GrievancesCivil Secretariat, Jammu|
             |Contact Nos|             |0191 - 2560109, 2560265, 2560266|
             |Fax|                     |0191-2566182|
             |Toll Free Call Centre|   |18005722327|
             |e-Mail|                  |jk-grievance@jk.gov.in|"""
        dispatcher.utter_message(text=message)

        return []


