from mycroft import MycroftSkill, intent_file_handler


class FindBattery(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('battery.find.intent')
    def handle_battery_find(self, message):
        self.speak_dialog('battery.find')


def create_skill():
    return FindBattery()

