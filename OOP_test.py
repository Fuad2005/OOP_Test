# CameraSystem classinin each_camera_price adinda hidden bir propertysi olsun. Deyeri 50 verin

class CameraSystem:
    __each_camera_price = 50
    def get_camera_price(self):
        return self.__each_camera_price * self.__count

    def set_camera_count(self, count):
        self.__count = count



# MemorySystem classinin each_gb_price adinda hidden bir propertysi olsun. Deyeri 10 verin
class MemorySystem:
    __each_gb_price = 10
    def set_memory_amount(self, amount):
        self.__amount = amount

    def get_memory_price(self):
        return self.__each_gb_price * self.__amount


class SmartDevice(CameraSystem, MemorySystem):
    def __init__(self, camera_count, memory_amount):
        self.set_camera_count(camera_count)
        self.set_memory_amount(memory_amount)

    @staticmethod
    def calculate_product_prices(*args):
        price = 0
        for i in args:
            price += i.get_total_price()
        return price



class Phone(SmartDevice):

    def get_total_price(self):
        return self.get_camera_price() + self.get_memory_price()


class PremiumPhone(Phone):
    def __init__(self, charger_price, camera_count, memory_amount):
        super().__init__(camera_count, memory_amount)
        self.charger_price = charger_price

    def get_total_price(self):
        return super().get_total_price() + self.charger_price

class Laptop(SmartDevice):
    def get_total_price(self):
        return self.get_camera_price() + self.get_memory_price()

class Tablet(SmartDevice):
    def get_total_price(self):
        return self.get_camera_price() + self.get_memory_price()


samsung = Phone(4, 256)
iphone = PremiumPhone(70, 3, 128)
dell = Laptop(1, 512)
huawei = Tablet(2, 256)

def calculate_product_prices(*args):
    price = 0
    for i in args:
        price += i.get_total_price()
    return price



# print(SmartDevice.calculate_product_prices(samsung, iphone, dell, huawei))


class Question:
    def __init__(self, text, answer, *options):
        self.text = text
        self.options = options
        self.answer = answer-1

    def check(self, user_answer):
        iuanswer = ord(user_answer.lower()) - 97
        return self.answer == iuanswer

    def get_question(self):
        result = ''
        result += self.text + '\n'
        for i, o in enumerate(self.options, 65):
            result += chr(i) + ') ' + o + '\n'
        return result

    @property
    def answer_letter(self):
        return chr(self.answer + 65)

class Test:
    def __init__(self):
        self.index = 0
        self.questions = []
        self.right_answers = 0
        self.wrong_answers = 0

    @property
    def count(self):
        return len(self.questions)

    @property
    def left_count(self):
        return self.count - self.index

    def add_question(self, question):
        self.questions.append(question)

    def get_current_question(self):
        return self.questions[self.index]
        
    def pass_to_next(self):
        self.index += 1

    def finished(self):
        return self.index == self.count

    def __len__(self):
        return self.count





class UserInteraction:
    answer_input_ask = 'Cavabi girin: '
    wrong_output = 'Cavab yanlisdir, duzgun cavab: {}'
    correct_ouput = 'Cavab dogrudur!'

    def __init__(self, test):
        self.test = test

    def show_question(self):
        print(self.test.get_current_question().get_question())

    def check_answer(self):
        user_answer = input(self.answer_input_ask)
        question = self.test.get_current_question()
        if (question.check(user_answer)):
            print(self.correct_ouput, end='\n\n')
        else:
            print(self.wrong_output.format(question.answer_letter), end='\n\n')

    def start(self):
        while not self.test.finished():
            self.show_question()
            self.check_answer()
            self.test.pass_to_next()









    



sual1 = Question(
    'En boyuk qite hansidir?',
    2,
    'Antartika',
    'Amerika',
    'Avropa',
    'Asiya',
    'Avstraliya'
)
sual2 = Question(
    'Asagidakilardan hansi bitkiler alemine aiddir??',
    4,
    'Ordek',
    'Gobelek',
    'At',
    'Sam agaci',
)

sual3 = Question(
    'Bunlardan hansi saitdir',
    4,
    'b',
    'c',
    'd',
    'a',
    'g',
    'f'
)
sual4 = Question(
    'Quvvetin vahidi?',
    1,
    'Newton',
    'Volt',
    'Watt',
    'Metr',
    'Paskal'
)

sual5 = Question(
    'Asagidakilardan hansi radioaktivdir?',
    1,
    'Plutonium',
    'Cive',
    'Lithium',
    'Cupper',
    'Selenium'
)

test = Test()
test.add_question(sual1)
test.add_question(sual2)
test.add_question(sual3)
test.add_question(sual4)
test.add_question(sual5)

user_interaction = UserInteraction(test)

user_interaction.start()