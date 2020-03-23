from mycroft import MycroftSkill, intent_file_handler
from xkcdpass import xkcd_password as xp


class PasswordCreator(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('creator.password.intent')
    def handle_creator_password(self, message):
        wordfile = xp.locate_wordfile()
        words = xp.generate_wordlist(wordfile=wordfile)  # Can modify
        password = xp.generate_xkcdpassword(words)  # Can modify

        self.speak_dialog('creator.password', data={
            'password': password
        })


def create_skill():
    return PasswordCreator()

