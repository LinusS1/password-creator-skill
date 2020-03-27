#  Copyright 2020 Linus S.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from mycroft import MycroftSkill, intent_handler
from lingua_franca.parse import extract_number
from adapt.intent import IntentBuilder
from xkcdpass import xkcd_password as xp


class PasswordCreator(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder("CreatePassword").require("Create").require("Password").optionally("NumberOfWords").optionally("Acrostic"))
    def handle_creator_password(self, message):
        number_of_words = message.data.get("NumberOfWords")
        number_of_words = extract_number(number_of_words) if number_of_words else 6

        acrostic = message.data.get("Acrostic")
        acrostic = acrostic if acrostic else False

        wordfile = xp.locate_wordfile()
        words = xp.generate_wordlist(wordfile=wordfile)  # Can modify
        password = xp.generate_xkcdpassword(words, number_of_words, acrostic=acrostic)  # Can modify

        self.speak_dialog('creator.password', data={
            'password': password
        })


def create_skill():
    return PasswordCreator()

