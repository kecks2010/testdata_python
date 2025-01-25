from dateutil.relativedelta import relativedelta

from testdata.model.idcard import IdCard
from testdata.model.idcard.IdCard import IdCardType
from testdata.service.idcard.IdCardGenerator import IdCardGenerator
from datetime import datetime
import re

class IdCardValidator:
    """
        This class provides methods to validate the id cards and id card information.

        Author:
            Mirko Werner
    """
    _instance = None
    __id_card_generator = IdCardGenerator()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(IdCardValidator, cls).__new__(cls)
        return cls._instance

    def is_id_card_valid(self, id_card : IdCard) -> bool:
        valid = self.is_documentnumber_valid(id_card.documentnumber, id_card.id_card_type) and \
                self.is_birthday_date_valid(id_card.birth_date) and self.is_expiry_date_valid(id_card.expiry_date)
        match id_card.id_card_type:
            case "OLD_IDENTITY_CARD" | "NEW_IDENTITY_CARD_WITHOUT_VERSION" | "CHILDREN_PASSPORT" | "TEMPORARY_PASSPORT":
                return valid and self.__check_check_digit_id_card_without_version(id_card)
            case "NEW_IDENTITY_CARD_WITH_VERSION" | "PASSPORT":
                return valid and self.__check_check_digit_id_card_with_version(id_card)
            case _:
                raise ValueError("Unexpected IdCardType: " + id_card.id_card_type)

    def is_documentnumber_valid(self, documentnumber : str, id_card_type : IdCardType):
        return self.__id_card_generator.generate_check_digit(documentnumber[0:len(documentnumber) - 1]) == \
            documentnumber[len(documentnumber) - 1:] and len(documentnumber) == 10 and \
            self.__not_contains_illegal_characters(documentnumber, id_card_type) and \
            self.__check_first_digit(documentnumber, id_card_type)

    def is_birthday_date_valid(self, birthday : str) -> bool:
        if len(birthday) != 7:
            return False
        birthday_without_check_digit = birthday[0:len(birthday)-1]
        if int(birthday[0:2]) > datetime.now().year % 100:
            birthday_without_check_digit = str(19) + birthday_without_check_digit
        else:
            birthday_without_check_digit = str(20) + birthday_without_check_digit
        birthday_datetime = datetime.strptime(birthday_without_check_digit, '%Y%m%d').date()

        return birthday_datetime < (datetime.now() - relativedelta(years=16) + relativedelta(days=1)).date() and \
            self.__id_card_generator.generate_check_digit(birthday[0:len(birthday) - 1]) == \
                birthday[len(birthday) - 1:]

    def is_expiry_date_valid(self, expiry_date : str) -> bool:
        if len(expiry_date) != 7:
            return False
        expiry_date_without_check_digit = expiry_date[0:len(expiry_date)-1]
        expiry_date_without_check_digit = str(20) + expiry_date_without_check_digit
        expiry_date_datetime = datetime.strptime(expiry_date_without_check_digit, '%Y%m%d').date()

        return expiry_date_datetime > (datetime.now() - relativedelta(days=1)).date() and \
            self.__id_card_generator.generate_check_digit(expiry_date[0:len(expiry_date) - 1]) == \
                expiry_date[len(expiry_date) - 1:]

    @staticmethod
    def __not_contains_illegal_characters(documentnumber : str, id_card_type : IdCardType) -> bool:
        match id_card_type:
            case "OLD_IDENTITY_CARD" | "TEMPORARY_PASSPORT" | "CHILDREN_PASSPORT":
                return documentnumber[2:] . isdigit()
            case "NEW_IDENTITY_CARD_WITHOUT_VERSION" | "NEW_IDENTITY_CARD_WITH_VERSION" | "PASSPORT":
                return not bool(re.search("[AEIOUBDQS]+", documentnumber[1:]))
            case _:
                raise ValueError("Unexpected IdCardType: " + id_card_type)

    @staticmethod
    def __check_first_digit(documentnumber : str, id_card_type : IdCardType) -> bool:
        match id_card_type:
            case "OLD_IDENTITY_CARD":
                return documentnumber[0].isdigit()
            case "NEW_IDENTITY_CARD_WITHOUT_VERSION" | "NEW_IDENTITY_CARD_WITH_VERSION":
                return bool(re.search(r'[LMNPRTVWXY]', documentnumber[0]))
            case "CHILDREN_PASSPORT":
                return bool(re.search(r'[EFG]', documentnumber[0]))
            case "TEMPORARY_PASSPORT":
                return bool(re.search(r'[AB]', documentnumber[0]))
            case "PASSPORT":
                return bool(re.search(r'[CFGHJK]', documentnumber[0]))
            case _:
                raise ValueError("Unexpected IdCardType: " + id_card_type)

    def __check_check_digit_id_card_without_version(self, id_card : IdCard) -> bool:
        return self.__id_card_generator.generate_check_digit(id_card.documentnumber + id_card.birth_date + \
                                                             id_card.expiry_date) == id_card.check_digit

    def __check_check_digit_id_card_with_version(self, id_card : IdCard) -> bool:
        return self.__id_card_generator.generate_check_digit(id_card.documentnumber + id_card.birth_date + \
                                                             id_card.expiry_date + id_card.version) == id_card.check_digit
