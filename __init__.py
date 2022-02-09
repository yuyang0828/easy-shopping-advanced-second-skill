from mycroft import MycroftSkill, intent_file_handler


class EasyShoppingAdvancedSecond(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('second.advanced.shopping.easy.intent')
    def handle_second_advanced_shopping_easy(self, message):
        self.speak_dialog('second.advanced.shopping.easy')


def create_skill():
    return EasyShoppingAdvancedSecond()

