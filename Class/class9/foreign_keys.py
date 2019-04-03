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


class Smartphone(Phone):  # Specify that Smartphone inherit from Phone

    def __init__(self, brand, model, phone_number, nb_of_cameras):
        super().__init__(brand, model, phone_number, tactile_screen=True)  # super() is the parent function
        self.nb_of_cameras = nb_of_cameras

    def take_pic(self):
        print("Say cheese! *Click*")
        print("You took a picture with {} camers".format(self.nb_of_cameras))


class Iphone(Smartphone):

    def __init__(self, model, phone_number, nb_of_cameras, face_recognition=False):
        super().__init__(brand="apple",
                         model=model,
                         phone_number=phone_number,
                         nb_of_cameras=nb_of_cameras)

        self.face_recognition = face_recognition
        self.password = None

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


iphone = Iphone(model="X", phone_number="0586784987", nb_of_cameras=4)
iphone.change_password()
iphone.unlock()