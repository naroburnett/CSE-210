class phone:
    def __init__(self):
        self.phone_number = int('6')
        self.text_messages = []

    def place_call(self,number_to_call):
        pass

    def place_text(self,number_to_text, message_to_send):
        pass

    def save_text(self,message_to_save):
        return self.text_messages.append(message_to_save)

    def get_texts():
        pass
    
    def get_number():
        pass

class CameraPhone(phone):
    def __init__(self):
        super().__init__()
        self.pictures = []

    def take_picture(self, picture_name):
        self.pictures.append(picture_name)

Phone = phone()
camera = CameraPhone()