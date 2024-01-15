# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pytz import timezone
from datetime import datetime

class ActionShowTimeZone(Action):

    def name(self) -> Text:
        return "action_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")
        # get timezone for city
        try:
            city_timezone = timezone(city)
            current_time = datetime.now(city_timezone)
            dispatcher.utter_message(text=f"The current time in {city} is {current_time}")
        except Exception:
            dispatcher.utter_message(text=f"I'm sorry, I couldn't find the timezone for {city}")

        return []
