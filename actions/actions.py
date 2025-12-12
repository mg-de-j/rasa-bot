from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


# class ActionCheckSufficientFunds(Action):
#     def name(self) -> Text:
#         return "action_check_sufficient_funds"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         # hard-coded balance for tutorial purposes. in production this
#         # would be retrieved from a database or an API
#         balance = 1000
#         transfer_amount = tracker.get_slot("amount")
#         has_sufficient_funds = transfer_amount <= balance
#         return [SlotSet("has_sufficient_funds", has_sufficient_funds)]

class ActionCalculateQuizScore(Action):
    def name(self) -> Text:
        return "action_calculate_quiz_score"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        answer_key = {
            "question_1": ["washington", "george washington"],
            "question_2": ["1945"],
            "question_3": ["roman", "rome", "roman empire"],
            "question_4": ["da vinci", "leonardo", "leonardo da vinci"],
            "question_5": ["1989"],
            "question_6": ["france"],
            "question_7": ["thatcher", "margaret thatcher"],
            "question_8": ["greece", "athens"],
            "question_9": ["egypt", "egyptians", "ancient egypt"],
            "question_10": ["1912"],
            "question_11": ["armstrong", "neil armstrong"],
            "question_12": ["churchill", "winston churchill"],
            "question_13": ["edison", "thomas edison"],
            "question_14": ["einstein", "albert einstein"],
            "question_15": ["pompeii"]
        }
        
        score = 0
        questions_asked = 0 
        
        for slot_name, valid_answers in answer_key.items():
            user_input = tracker.get_slot(slot_name)
            
            if user_input:
                questions_asked += 1
                
                cleaned_input = str(user_input).lower().strip()
                if any(ans in cleaned_input for ans in valid_answers):
                    score += 1
        
        return [
             SlotSet("quiz_score", float(score)),
             SlotSet("questions_asked", float(questions_asked))
        ]
class ActionResetEra(Action):
    def name(self) -> Text:
        return "action_reset_era"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        return [SlotSet("era", None)]