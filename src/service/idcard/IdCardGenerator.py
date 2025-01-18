from src.model.idcard import IdCard
from random import randrange
from random import random
from datetime import datetime
from dateutil.relativedelta import relativedelta

class IdCardGenerator:
    _instance = None
    id_card_type = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def generate_old_identity_card(self, birth_date : datetime=None, expiry_date : datetime=None) -> IdCard.IdCard:
        if birth_date is None:
            birth_date = self.__generate_birth_date()
        if expiry_date is None:
            expiry_date = datetime.now() + relativedelta(years=10)
        self.id_card_type = IdCard.IdCardType.OLD_IDENTITY_CARD
        return self.__generate_id_card(birth_date, expiry_date, IdCard.Gender.NOT_SPECIFIED)

    def generate_new_identity_card_without_version(self, birth_date : datetime=None, expiry_date : datetime=None)\
            -> IdCard.IdCard:
        if birth_date is None:
            birth_date = self.__generate_birth_date()
        if expiry_date is None:
            expiry_date = datetime.now() + relativedelta(years=10)
        self.id_card_type = IdCard.IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION
        return self.__generate_id_card(birth_date, expiry_date, IdCard.Gender.NOT_SPECIFIED)

    def generate_new_identity_card_with_version(self, birth_date : datetime=None, expiry_date : datetime=None)\
            -> IdCard.IdCard:
        if birth_date is None:
            birth_date = self.__generate_birth_date()
        if expiry_date is None:
            expiry_date = datetime.now() + relativedelta(years=10)
        self.id_card_type = IdCard.IdCardType.NEW_IDENTITY_CARD_WITH_VERSION
        return self.__generate_id_card(birth_date, expiry_date, IdCard.Gender.NOT_SPECIFIED)

    def generate_passport(self, gender: IdCard.Gender = IdCard.Gender.M, birth_date: datetime=None,
                                   expiry_date: datetime=None) -> IdCard.IdCard:
        if birth_date is None:
            birth_date = self.__generate_birth_date()
        if expiry_date is None:
            expiry_date = datetime.now() + relativedelta(years=10)
        self.id_card_type = IdCard.IdCardType.PASSPORT
        return self.__generate_id_card(birth_date, expiry_date, gender)

    def generate_temporary_passport(self, gender: IdCard.Gender = IdCard.Gender.M, birth_date: datetime=None,
                                   expiry_date: datetime=None) -> IdCard.IdCard:
        if birth_date is None:
            birth_date = self.__generate_birth_date()
        if expiry_date is None:
            expiry_date = datetime.now() + relativedelta(years=10)
        self.id_card_type = IdCard.IdCardType.TEMPORARY_PASSPORT
        return self.__generate_id_card(birth_date, expiry_date, gender)

    def generate_children_passport(self, gender: IdCard.Gender = IdCard.Gender.M, birth_date: datetime=None,
                                   expiry_date: datetime=None)-> IdCard.IdCard:
        if birth_date is None:
            birth_date = self.__generate_birth_date()
        if expiry_date is None:
            expiry_date = datetime.now() + relativedelta(years=10)
        self.id_card_type = IdCard.IdCardType.CHILDREN_PASSPORT
        return self.__generate_id_card(birth_date, expiry_date, gender)

    def __generate_id_card(self, birth_date : datetime, expiry_date : datetime, gender : IdCard.Gender) -> IdCard.IdCard:
        if self.id_card_type is None or not isinstance(self.id_card_type, IdCard.IdCardType):
            raise ValueError("IdCardType not defined")
        temp_documentnumber = self.__generate_temp_documentnumber()
        documentnumber = temp_documentnumber + self.generate_check_digit(temp_documentnumber)
        birth_date_with_check_digit = datetime.strftime(birth_date, '%y%m%d') + \
                                      self.generate_check_digit(datetime.strftime(birth_date, '%y%m%d'))
        expiry_date_with_check_digit = datetime.strftime(expiry_date, '%y%m%d') + \
                                       self.generate_check_digit(datetime.strftime(expiry_date, '%y%m%d'))
        check_digit = self.generate_check_digit(documentnumber + birth_date_with_check_digit + \
                                                expiry_date_with_check_digit)

        if self.id_card_type == IdCard.IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION or self.id_card_type == \
            IdCard.IdCardType.OLD_IDENTITY_CARD:
            return IdCard.IdCard.create_identity_card_without_version(documentnumber, birth_date_with_check_digit,
                                                                      expiry_date_with_check_digit, check_digit,
                                                                      self.id_card_type)
        if self.id_card_type == IdCard.IdCardType.TEMPORARY_PASSPORT or self.id_card_type == \
                IdCard.IdCardType.CHILDREN_PASSPORT:
            return IdCard.IdCard.create_temporary_or_children_passport(documentnumber, birth_date_with_check_digit,
                                                                       gender, expiry_date_with_check_digit,
                                                                       check_digit, self.id_card_type)
        version = self.__generate_version()
        check_digit = self.generate_check_digit(documentnumber + birth_date_with_check_digit + \
                                                expiry_date_with_check_digit + version)
        if self.id_card_type == IdCard.IdCardType.NEW_IDENTITY_CARD_WITH_VERSION:
            return IdCard.IdCard.create_identity_card_with_version(documentnumber, birth_date_with_check_digit,
                                                                   expiry_date_with_check_digit, version, check_digit,
                                                                   self.id_card_type)
        if self.id_card_type == IdCard.IdCardType.PASSPORT:
            return IdCard.IdCard.create_passport(documentnumber, birth_date_with_check_digit, gender,
                                                 expiry_date_with_check_digit, version, check_digit, self.id_card_type)
        raise ValueError("Unexpected IdCardType: " + self.id_card_type)


    def __generate_temp_documentnumber(self) -> str:
        if self.id_card_type == IdCard.IdCardType.OLD_IDENTITY_CARD:
            return self.__generate_authority_code() + self.__generate_id_number()
        if self.id_card_type == IdCard.IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION or \
            self.id_card_type == IdCard.IdCardType.NEW_IDENTITY_CARD_WITH_VERSION:
            return self.__generate_letter_identity_card() + self.__generate_documentnumber()
        if self.id_card_type == IdCard.IdCardType.PASSPORT:
            return self.__generate_letter_passport() + self.__generate_documentnumber()
        if self.id_card_type == IdCard.IdCardType.TEMPORARY_PASSPORT:
            return self.__generate_letter_temporary_passport() + "<" + self.__generate_authority_code() + \
                self.__generate_id_number()[0:3]
        if self.id_card_type == IdCard.IdCardType.CHILDREN_PASSPORT:
            return self.__generate_letter_children_passport() + "<" + self.__generate_authority_code() + \
                self.__generate_id_number()[0:3]
        raise ValueError("Unexpected IdCardType: " + self.id_card_type)

    @staticmethod
    def __generate_birth_date() -> datetime:
        lower_age = 15
        upper_age = 99

        age = int(random() * (upper_age - lower_age) + lower_age)

        return datetime.now() - relativedelta(years=age)

    @staticmethod
    def __generate_letter_identity_card() -> str:
        letters = ['L','M','N','P','R','T','V','W','X','Y']

        position = int(random() * len(letters))

        return letters[position]

    @staticmethod
    def __generate_letter_passport() -> str:
        letters = ['C','F','G','H','J','K']

        position = int(random() * len(letters))

        return letters[position]

    @staticmethod
    def __generate_letter_temporary_passport() -> str:
        letters = ['A','B']

        position = int(random() * len(letters))

        return letters[position]

    @staticmethod
    def __generate_letter_children_passport() -> str:
        letters = ['E','F','G']

        position = int(random() * len(letters))

        return letters[position]

    @staticmethod
    def __generate_authority_code() -> str:
        lower_limit = 10000
        upper_limit = 19999

        authority_code = int(random() * (upper_limit - lower_limit)) + lower_limit

        return str(authority_code)[1:]

    @staticmethod
    def __generate_id_number() -> str:
        lower_limit = 100000
        upper_limit = 199999

        authority_code = int(random() * (upper_limit - lower_limit)) + lower_limit

        return str(authority_code)[1:]

    @staticmethod
    def __generate_documentnumber() -> str:
        letters = ['C', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'T', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
                   '4', '5', '6', '7', '8', '9']
        documentnumber = ''
        for counter in range(8):
            position = randrange(len(letters))
            documentnumber += letters[position]
        return documentnumber

    def __generate_version(self) -> str:
        version = datetime.now().strftime("%y%m")

        if self.id_card_type == IdCard.IdCardType.PASSPORT:
            return version + "<<<<<<<<<<" + self.generate_check_digit(version + "<<<<<<<<<<")
        else:
            return version

    @staticmethod
    def generate_check_digit(value: str) -> str:
        weight = [7,3,1]
        check_digit = 0

        for position in range(len(value)):
            if (ord(value[position]) - 64) > 0:
                check_digit += ((ord(value[position]) - 55) * weight[position % 3]) % 10
            elif value[position] != "<":
                check_digit += (int(value[position]) * weight[position % 3]) % 10
        return str(check_digit % 10)