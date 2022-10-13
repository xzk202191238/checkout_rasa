# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
import re
import sqlite3
from sqlite3.dbapi2 import Error
import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.types import DomainDict
import logging

# 初始化logger
logger = logging.getLogger(__name__)
logging.basicConfig(level="DEBUG")

# 创建ecommerce.db的表  每次使用都要用另一个终端rasa run actions   ctrl+c停止
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()
cursor.execute('create table if not exists membership(ID integer primary key autoincrement, EmailAddress text, PhoneNumber int )')
logger.info("table1 create successfully")
cursor2 = conn.cursor()
cursor2.execute('create table if not exists membership2(ID integer primary key autoincrement ,PhoneNumber int )')
logger.info("table2 create successfully")
cursor3 = conn.cursor()
cursor3.execute('''create table if not exists orders(ID integer primary key autoincrement, order_number int );''')
logger.info("table orders create successfully")

conn.commit()
conn.close()


class ValidateOrderNumber(Action):
    def name(self) -> Text:
        return "action_ValidateOrderNumber"  # 返回的值就是我需要用到的action

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain):
        order_number = tracker.get_slot("order_number")
        logger.debug(order_number)
        connQ = sqlite3.connect('ecommerce.db')
        cursorQ = connQ.cursor()
        tracker.get_slot("order_number")
        row = cursorQ.execute("SELECT order_number from orders where order_number = " + order_number)
        if len(list(row)) != 0:
            logger.debug("order number exist")
            dispatcher.utter_message(text="order number exist")
        else:
            logger.debug("order number not exist")
            dispatcher.utter_message(text="order number not exist")
        return [SlotSet('order_number', None)]


class AddCustomEmailAddress(Action):
    def name(self) -> Text:
        return "action_AddCustomEmailAddress"  # 返回的值就是我需要用到的action

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        logger.debug("successfully AddCustomerEmailAddress")
        emailaddress = tracker.get_slot("email_address")
        logger.debug(emailaddress)

        conn = sqlite3.connect('ecommerce.db')
        cursorCEA = conn.cursor()
        cursorCEA.execute('INSERT INTO membership(EmailAddress) values(\'' + emailaddress +'\')')
        logger.debug('INSERT INTO membership(EmailAddress) values(\'' + emailaddress +'\')')
        conn.commit()

        return [SlotSet('email_address', None)]


class AddPhoneNumber(Action):
    def name(self) -> Text:
        return "action_AddPhoneNumber"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        logger.debug("successfully AddPhoneNumber")
        phonenumber = tracker.get_slot("phone_number")
        logger.debug(phonenumber)

        conn = sqlite3.connect('ecommerce.db')
        cursorB = conn.cursor()
        cursorB.execute('INSERT INTO membership2(PhoneNumber) values("'+ phonenumber +'")')
        logger.debug('INSERT INTO membership2(PhoneNumber) values("'+ phonenumber +'")')
        conn.commit()

        return [SlotSet('phone_number', None)]











