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

