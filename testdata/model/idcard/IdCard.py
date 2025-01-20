from enum import StrEnum
from typing import Optional

class IdCardType(StrEnum):
    OLD_IDENTITY_CARD = "OLD_IDENTITY_CARD"
    NEW_IDENTITY_CARD_WITHOUT_VERSION = "NEW_IDENTITY_CARD_WITHOUT_VERSION"
    NEW_IDENTITY_CARD_WITH_VERSION = "NEW_IDENTITY_CARD_WITH_VERSION"
    PASSPORT = "PASSPORT"
    TEMPORARY_PASSPORT = "TEMPORARY_PASSPORT"
    CHILDREN_PASSPORT = "CHILDREN_PASSPORT"

class Gender(StrEnum):
    M = "M"
    F = "F"
    X = "X"
    NOT_SPECIFIED = "NOT_SPECIFIED"

class IdCard(object):

    nationality = "D"
    gender = None
    version = None

    def __init__(self, documentnumber, birth_date : str, gender : Optional[Gender], expiry_date : str,
                 version : Optional[str], check_digit : str, id_card_type : IdCardType):
        if not isinstance(id_card_type, IdCardType):
            raise TypeError ("id_card_type must be of type IdCardType")
        if gender is not None and not isinstance(gender, Gender):
            raise TypeError ("gender must be of type Gender")
        self.documentnumber = documentnumber
        self.birth_date = birth_date
        self.gender = gender
        self.expiry_date = expiry_date
        self.version = version
        self.check_digit = check_digit
        self.id_card_type = id_card_type

    @classmethod
    def create_identity_card_without_version(cls, documentnumber : str, birth_date : str, expiry_date : str,
                                             check_digit : str, id_card_type):
        return cls(documentnumber, birth_date, None, expiry_date, None, check_digit, id_card_type)

    @classmethod
    def create_temporary_or_children_passport(cls, documentnumber : str, birth_date : str, gender : Gender,
                                              expiry_date : str, check_digit : str, id_card_type):
        if not isinstance(gender, Gender):
            raise TypeError ("gender must be of type Gender")
        if not isinstance(id_card_type, IdCardType):
            raise TypeError ("id_card_type must be of type IdCardType")
        if id_card_type != IdCardType.TEMPORARY_PASSPORT and id_card_type != IdCardType.CHILDREN_PASSPORT:
            raise ValueError("id_card_type must be TEMPORARY_PASSPORT or CHILDREN_PASSPORT")
        cls.gender = gender
        return cls(documentnumber, birth_date, gender, expiry_date, None, check_digit, id_card_type)

    @classmethod
    def create_identity_card_with_version(cls, documentnumber : str, birth_date : str, expiry_date : str, version,
                                          check_digit : str, id_card_type : IdCardType):
        if not isinstance(id_card_type, IdCardType):
            raise TypeError ("id_card_type must be of type IdCardType")
        if id_card_type != IdCardType.NEW_IDENTITY_CARD_WITH_VERSION:
            raise ValueError("id_card_type must be NEW_IDENTITY_CARD_WITH_VERSION")
        cls.version = version
        return cls(documentnumber, birth_date, None, expiry_date, version, check_digit, id_card_type)

    @classmethod
    def create_passport(cls, documentnumber : str, birth_date : str, gender : Gender, expiry_date : str, version : str,
                        check_digit : str, id_card_type : IdCardType):
        if not isinstance(gender, Gender):
            raise TypeError ("gender must be of type Gender")
        if not isinstance(id_card_type, IdCardType):
            raise TypeError ("id_card_type must be of type IdCardType")
        if (id_card_type != IdCardType.PASSPORT and id_card_type != IdCardType.CHILDREN_PASSPORT and
                id_card_type != IdCardType.TEMPORARY_PASSPORT):
            raise ValueError("id_card_type must be PASSPORT_WITH_VERSION or CHILDREN_PASSPORT or TEMPORARY_PASSPORT")
        cls.gender = gender
        cls.version = version
        return cls(documentnumber, birth_date, gender, expiry_date, version, check_digit, id_card_type)

    def to_string(self):
        match self.id_card_type:
            case "OLD_IDENTITY_CARD":
                return self.documentnumber + self.nationality + "<<" + self.birth_date + "<" + self.expiry_date +\
                    "<<<<<<<" + self.check_digit
            case "NEW_IDENTITY_CARD_WITHOUT_VERSION":
                return "IDD<<" + self.documentnumber + "<<<<<<<<<<<<<<<\n" + self.birth_date + "<" +\
                    self.expiry_date + self.nationality + "<<<<<<<<<<<<<" + self.check_digit
            case "NEW_IDENTITY_CARD_WITH_VERSION":
                return "IDD<<" + self.documentnumber + "<<<<<<<<<<<<<<<\n" + self.birth_date + "<" +\
                    self.expiry_date + self.nationality + "<<" + self.version + "<<<<<<<" + self.check_digit
            case "PASSPORT":
                return self.documentnumber + self.nationality + "<<" + self.birth_date + self.gender + self.expiry_date +\
                    self.version + self.check_digit
            case "TEMPORARY_PASSPORT" | "CHILDREN_PASSPORT":
                return self.documentnumber + self.nationality + "<<" + self.birth_date + self.gender + self.expiry_date +\
                    "<<<<<<<<<<<<<<<" + self.check_digit
            case _:
                raise ValueError("Unexpected IdCardType: " + self.id_card_type)