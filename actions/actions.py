import csv
from pathlib import Path

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSearchFAQ(Action):

    def name(self):
        return "action_search_faq"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: dict
    ):

        user_question = tracker.latest_message.get("text", "").lower()

        faq_path = Path("data/faq.csv")

        best_answer = None

        if faq_path.exists():

            with open(faq_path, "r", encoding="utf-8") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    question = row["question"].lower()

                    question_words = question.split()

                    matching_words = [
                        word
                        for word in question_words
                        if len(word) > 3 and word in user_question
                    ]

                    if len(matching_words) >= 2:
                        best_answer = row["answer"]
                        break

        if best_answer:

            dispatcher.utter_message(text=best_answer)

        else:

            dispatcher.utter_message(
                text="I could not find a specific answer. Please contact your internship supervisor for assistance."
            )

        return []