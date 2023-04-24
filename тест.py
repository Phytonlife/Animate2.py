class PhoneBook:
    phonelst = []

    def add_phone(self, phone):
        if isinstance(phone.number, int) and len(str(phone.number)) == 11 and isinstance(phone.fio, str):
            self.phonelst.append(phone)

    def remove_phone(self, indx):
        self.phonelst.pop(indx)

    def get_phone_list(self):
        numberlst = [i.number for i in self.phonelst]

        return numberlst


class PhoneNumber:
    number = None
    fio = None

    def __init__(self, number, fio):
        self.number = number

        self.fio = fio


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678905, "Панда"))

print(p.get_phone_list())