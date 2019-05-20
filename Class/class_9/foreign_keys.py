class Message:
    def __init__(self, content, sender, date):
        self.content = content
        self.sender  = sender
        self.date    = date

    def __repr__(self):
        return "{} (from {} at {})".format(self.content,
                                         self.sender,
                                         self.date)

class Phone:

    def __init__(self, brand, model, phone_number, tactile_screen=False):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number
        self.tactile_screen = tactile_screen

    def call(self, number_to_call):
        print("Calling to {}...".format(number_to_call))

    def txt_message(self, number, message):
        print("Sending to {}: {}".format(number, message))

    def __repr__(self):
        return self.phone_number

class Smartphone(Phone):  # Specify that Smartphone inherit from Phone

    def __init__(self, brand, model, phone_number, nb_of_cameras):
        super().__init__(brand, model, phone_number, tactile_screen=True)  # super() is the parent function
        self.nb_of_cameras = nb_of_cameras

    def take_pic(self):
        print("Say cheese! *Click*")
        print("You took a picture with {} cameras".format(self.nb_of_cameras))


class Iphone(Smartphone):

    nb_of_iphones = 0
    number_to_obj    = {}

    def __init__(self, model, phone_number, nb_of_cameras, face_recognition=False):

        Iphone.nb_of_iphones += 1
        self.id = Iphone.nb_of_iphones

        Iphone.number_to_obj[phone_number] = self

        super().__init__(brand="apple",
                         model=model,
                         phone_number=phone_number,
                         nb_of_cameras=nb_of_cameras)

        self.face_recognition = face_recognition
        self.password = None
        self.msg_box  = []

    def query_number(self, phone_number):
        if phone_number not in Iphone.number_to_obj:
            print("Incorrect number")
            return False
        return Iphone.number_to_obj[phone_number]

    def send_message(self, content, date, dst_number):
        receiver_phone = self.query_number(dst_number)
        msg = Message(content=content, date=date, sender=self)

        receiver_phone.receive_message(msg)

    def receive_message(self, msg):
        self.msg_box.append(msg)

    def unlock(self):
        if not self.password:  # NO PASSWORD
            print("Phone unlocked. Welcome :)")
            return

        if self.face_recognition:
            print("Recognized you. Welcome :)")
            return

        if self.password:
            if self.check_password():
                print("Phone unlocked, Welcome :)")
            else:
                print("Don't touch my phone ! >:(")

            return

    def change_password(self):
        if self.password and self.check_password() == False:
            print("Sorry, wrong password.")
            return False

        while True:
            new_password = input("Please input 4 digits\n$ ")
            if len(new_password) != 4 or new_password.isnumeric() == False:  # if wrong password
                print("Bad input")
                continue
            else:
                break
        self.password = new_password

    def check_password(self):
        userinput = input("Password?...\n$ ")
        if userinput == self.password:
            return True
        return False


reuven_iphone = Iphone(model="7", phone_number="0527313370", nb_of_cameras=4)
eyal_iphone   = Iphone(model="Android", phone_number="0586878399", nb_of_cameras=2)

reuven_iphone.send_message("Hello, I love your classes", "03/04/2019", "0586878399")
print(str(eyal_iphone.msg_box))
print(str(reuven_iphone))

reuven_iphone.send_message("Hello", 0xf444837deff)
