from mycroft import MycroftSkill, intent_file_handler


class PasswordCreator(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('creator.password.intent')
    def handle_creator_password(self, message):
        password = ''

        self.speak_dialog('creator.password', data={
            'password': password
        })


def create_skill():
    return PasswordCreator()

