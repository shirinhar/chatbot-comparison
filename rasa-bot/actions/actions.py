from deeppavlov.core.data.sqlite_database import Sqlite3Database
from rasa_sdk import Action
from typing import Any, Text, Dict, List, Type
from rasa_sdk.events import SlotSet
import os, json

from deeppavlov.dataset_iterators.dialog_iterator import DialogDatasetIterator

full_results = []

def get_db():

    database = Sqlite3Database(primary_keys=["name"],
                               save_path="database/db.sqlite")

    return database

def params_dict(tracker):
    search_params = dict()

    params = ["area", "name", "pricerange", "food"]

    for param in params:
        try:
            slot = tracker.get_slot(param)
            if slot != None: 
                search_params[param] = slot
        except:
            pass

    return search_params

class ActionSuggest(Action):
    def name(self) -> Text:
        return "action_suggest"

    def run(self, dispatcher, tracker, domain):
        db = get_db()
        search_params = [params_dict(tracker)]
        full_results = db(search_params)[0]

        print(full_results)

        for r in full_results:
            dispatcher.utter_message(text="name: "+str(r['name']) + ", phone:"+ str(r['phone'])+ ", address:"+ str(r['addr']))
        
        if not full_results:
            dispatcher.utter_message(text="No matches with the given criteria were found")
        

        return [] 

class ActionRequest(Action):
    def name(self) -> Text:
        return "action_request"

    def run(self, dispatcher, tracker, domain):

        db = get_db()
        search_params = [params_dict(tracker)]
        full_results = db(search_params)[0]

        p = tracker.get_slot('slot')

        for r in full_results:
            dispatcher.utter_message(text="name: "+str(r['name']) + " -> "+ p +":"+ str(r[p]))

        
        return []
