from mycroft import MycroftSkill, intent_file_handler


class Pregonero(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pregonero.intent')
    def handle_pregonero(self, message):
        self.speak_dialog('pregonero')


def create_skill():
    return Pregonero()

