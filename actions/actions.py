
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
 
 
class ActionReadSelectedOptionDescription(Action):
    """
    handler for the option selection action
    """
   
    def name(self) -> Text:
        return "read_selected_option_description"
  
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
 
        """
        selects the option to describe depending on user choice
        """

        selected_option = tracker.get_slot("option")

        if selected_option == "one":
            dispatcher.utter_message(response="utter_option_one")
        elif selected_option == "two":
            dispatcher.utter_message(response="utter_option_two")
        elif selected_option == "three":
            dispatcher.utter_message(response="utter_option_three")
        elif selected_option == "four":
            dispatcher.utter_message(response="utter_option_four")
        else:
            dispatcher.utter_message(response="utter_option_invalid")
 
        return [AllSlotsReset()]
