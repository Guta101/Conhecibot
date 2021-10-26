# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import psycopg2

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionProcurarArtigo(Action):

    def name(self) -> Text:
        return "action_procurar_artigo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        materia = tracker.get_slot("materias")
        try:
            connection = psycopg2.connect(user="admin",
                                          password="password",
                                          host="0.0.0.0",
                                          port="5432",
                                          database="postgres_db")
            cursor = connection.cursor()
            postgreSQL_select_Query = "select * from mobile"

            cursor.execute(postgreSQL_select_Query)
            print("Selecting rows from mobile table using cursor.fetchall")
            mobile_records = cursor.fetchall()

            print("Print each row and it's columns values")
            for row in mobile_records:
                print("Id = ", row[0], )
                print("Model = ", row[1])
                print("Price  = ", row[2], "\n")

        except (Exception, psycopg2.Error) as error:
            print("Erro ao procurar dados na tabela", error)

        return []
