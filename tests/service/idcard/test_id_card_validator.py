import unittest

from datetime import datetime
from dateutil.relativedelta import relativedelta
from testdata.model.idcard.id_card import IdCard
from testdata.model.idcard.id_card import IdCardType
from testdata.model.idcard.id_card import Gender
from testdata.service.idcard.id_card_generator import IdCardGenerator
from testdata.service.idcard.id_card_validator import IdCardValidator


class MyTestCase(unittest.TestCase):

    id_card_validator = IdCardValidator()
    id_card_generator = IdCardGenerator()

    def test_is_old_identity_card_valid(self):
        old_identity_card = IdCard.create_identity_card_without_version("7403318053", "4201115",
                                                                        "4201115","8",
                                                                        IdCardType.OLD_IDENTITY_CARD)

        self.assertTrue(self.id_card_validator.is_id_card_valid(old_identity_card))

    def test_is_new_identity_card_valid(self):
        new_identity_card = IdCard.create_identity_card_without_version("RPKV2X4VT0",
                                                                                  "9901122",
                                                                        "3501106","2",
                                                                        IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

        self.assertTrue(self.id_card_validator.is_id_card_valid(new_identity_card))

    def test_is_new_identity_card_with_version_valid(self):
        new_identity_card_with_version = IdCard.create_identity_card_with_version("RN5878VMK1",
                                                                                  "7801125",
                                                                        "3501128","2501", "6",
                                                                        IdCardType.NEW_IDENTITY_CARD_WITH_VERSION)

        self.assertTrue(self.id_card_validator.is_id_card_valid(new_identity_card_with_version))

    def test_is_passport_valid(self):
        passport = IdCard.create_passport("KXYZ2N11N0","7301120", Gender.M,
                                          "3501128","2501", "8",
                                          IdCardType.PASSPORT)

        self.assertTrue(self.id_card_validator.is_id_card_valid(passport))

    def test_is_temporary_passport_valid(self):
        temporary_passport = IdCard.create_temporary_or_children_passport("B<37962198","6101149",
                                                                          Gender.M,"3501140", "0",
                                                                          IdCardType.TEMPORARY_PASSPORT)

        self.assertTrue(self.id_card_validator.is_id_card_valid(temporary_passport))

    def test_is_children_passport_valid(self):
        children_passport = IdCard.create_temporary_or_children_passport("G<40134435","7101146",
                                                                          Gender.M,"3501140", "0",
                                                                          IdCardType.CHILDREN_PASSPORT)

        self.assertTrue(self.id_card_validator.is_id_card_valid(children_passport))

    def test_is_documentnumber_for_old_identity_card_valid(self):
        old_identity_card = IdCard.create_identity_card_without_version("7403318053","4201115",
                                                                          "4201115", "8",
                                                                          IdCardType.OLD_IDENTITY_CARD)

        self.assertTrue(self.id_card_validator.is_id_card_valid(old_identity_card))
        self.assertTrue(self.id_card_validator.is_documentnumber_valid(old_identity_card.documentnumber,
                                                                       IdCardType.OLD_IDENTITY_CARD))

    def test_is_documentnumber_for_old_identity_card_with_invalid_check_digit_in_documentnumber_valid(self):
        old_identity_card = IdCard.create_identity_card_without_version("3272983754","4201115",
                                                                          "3501117", "4",
                                                                          IdCardType.OLD_IDENTITY_CARD)

        self.assertFalse(self.id_card_validator.is_id_card_valid(old_identity_card))
        self.assertFalse(self.id_card_validator.is_documentnumber_valid(old_identity_card.documentnumber,
                                                                       IdCardType.OLD_IDENTITY_CARD))

    def test_is_documentnumber_for_old_identity_card_with_to_short_documentnumber_valid(self):
        old_identity_card = IdCard.create_identity_card_without_version("778781837","8401108",
                                                                          "3501106", "4",
                                                                          IdCardType.OLD_IDENTITY_CARD)

        self.assertFalse(self.id_card_validator.is_id_card_valid(old_identity_card))
        self.assertFalse(self.id_card_validator.is_documentnumber_valid(old_identity_card.documentnumber,
                                                                       IdCardType.OLD_IDENTITY_CARD))

    def test_is_documentnumber_for_old_identity_card_with_to_long_documentnumber_valid(self):
        old_identity_card = IdCard.create_identity_card_without_version("77878183526","8401108",
                                                                          "3501106", "4",
                                                                          IdCardType.OLD_IDENTITY_CARD)

        self.assertFalse(self.id_card_validator.is_id_card_valid(old_identity_card))
        self.assertFalse(self.id_card_validator.is_documentnumber_valid(old_identity_card.documentnumber,
                                                                       IdCardType.OLD_IDENTITY_CARD))

    def test_is_documentnumber_for_old_identity_card_with_letter_in_documentnumber_valid(self):
        old_identity_card = IdCard.create_identity_card_without_version("7787818N52","8401108",
                                                                          "3501106", "4",
                                                                          IdCardType.OLD_IDENTITY_CARD)

        self.assertFalse(self.id_card_validator.is_id_card_valid(old_identity_card))
        self.assertFalse(self.id_card_validator.is_documentnumber_valid(old_identity_card.documentnumber,
                                                                       IdCardType.OLD_IDENTITY_CARD))

    def test_is_documentnumber_for_old_identity_card_with_letter_as_first_element_in_documentnumber_valid(self):
        old_identity_card = IdCard.create_identity_card_without_version("N697121869","3101115",
                                                                          "3501117", "4",
                                                                          IdCardType.OLD_IDENTITY_CARD)

        self.assertFalse(self.id_card_validator.is_id_card_valid(old_identity_card))
        self.assertFalse(self.id_card_validator.is_documentnumber_valid(old_identity_card.documentnumber,
                                                                       IdCardType.OLD_IDENTITY_CARD))

    def test_is_documentnumber_for_new_identity_card_valid(self):
        new_identity_card = IdCard.create_identity_card_without_version("RPKV2X4VT0","9901122",
                                                                          "3501106", "2",
                                                                          IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

        self.assertTrue(self.id_card_validator.is_id_card_valid(new_identity_card))
        self.assertTrue(self.id_card_validator.is_documentnumber_valid(new_identity_card.documentnumber,
                                                                       IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION))

    def test_is_documentnumber_for_new_identity_card_with_illegal_first_character_in_documentnumber_valid(self):
        new_identity_card = IdCard.create_identity_card_without_version("12NCGFGGL4","3901108",
                                                                          "3501106", "0",
                                                                          IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

        self.assertFalse(self.id_card_validator.is_id_card_valid(new_identity_card))
        self.assertFalse(self.id_card_validator.is_documentnumber_valid(new_identity_card.documentnumber,
                                                                       IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION))

    def test_is_documentnumber_for_new_identity_card_with_illegal_character_in_documentnumber_valid(self):
        new_identity_card = IdCard.create_identity_card_without_version("MNROYGHF77","9501108",
                                                                          "3501106", "8",
                                                                          IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

        self.assertFalse(self.id_card_validator.is_id_card_valid(new_identity_card))
        self.assertFalse(self.id_card_validator.is_documentnumber_valid(new_identity_card.documentnumber,
                                                                       IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION))

    def test_is_documentnumber_for_new_identity_card_with_version_valid(self):
        new_identity_card_with_version = IdCard.create_identity_card_with_version("RN5878VMK1",
                                                                                  "7801125","3501128",
                                                                                  "2501", "6",
                                                                                  IdCardType.NEW_IDENTITY_CARD_WITH_VERSION)

        self.assertTrue(self.id_card_validator.is_id_card_valid(new_identity_card_with_version))
        self.assertTrue(self.id_card_validator.is_documentnumber_valid(new_identity_card_with_version.documentnumber,
                                                                       IdCardType.NEW_IDENTITY_CARD_WITH_VERSION))

    def test_is_documentnumber_for_passport_valid(self):
        passport = IdCard.create_passport("KXYZ2N11N0","7301120", Gender.M,"3501128",
                                          "2501<<<<<<<<<<6", "4", IdCardType.PASSPORT)

        self.assertTrue(self.id_card_validator.is_id_card_valid(passport))
        self.assertTrue(self.id_card_validator.is_documentnumber_valid(passport.documentnumber, IdCardType.PASSPORT))

    def test_is_documentnumber_for_passport_with_illegal_first_character_in_documentnumber_valid(self):
        passport = IdCard.create_passport("LN8Z7CPCY7","9301124", Gender.M,"3501128",
                                          "2501<<<<<<<<<<6", "2", IdCardType.PASSPORT)

        self.assertFalse(self.id_card_validator.is_id_card_valid(passport))
        self.assertFalse(self.id_card_validator.is_documentnumber_valid(passport.documentnumber, IdCardType.PASSPORT))

    def test_is_documentnumber_for_passport_with_illegal_character_in_documentnumber_valid(self):
        passport = IdCard.create_passport("FX1AGML4R1","8001128", Gender.M,"3501128",
                                          "2501<<<<<<<<<<6", "0", IdCardType.PASSPORT)

        self.assertFalse(self.id_card_validator.is_id_card_valid(passport))
        self.assertFalse(self.id_card_validator.is_documentnumber_valid(passport.documentnumber, IdCardType.PASSPORT))

    def test_is_documentnumber_for_temporary_passport_valid(self):
        temporary_passport = IdCard.create_temporary_or_children_passport("B<37962198","6101149",
                                                                          Gender.M, "3501140", "0",
                                                                          IdCardType.TEMPORARY_PASSPORT)

        self.assertTrue(self.id_card_validator.is_id_card_valid(temporary_passport))
        self.assertTrue(self.id_card_validator.is_documentnumber_valid(temporary_passport.documentnumber,
                                                                       IdCardType.TEMPORARY_PASSPORT))

    def test_is_documentnumber_for_temporary_passport_with_to_short_documentnumber_valid(self):
        temporary_passport = IdCard.create_temporary_or_children_passport("B<3796219","6101149",
                                                                          Gender.M,"3501140", "6",
                                                                          IdCardType.TEMPORARY_PASSPORT)

        self.assertFalse(self.id_card_validator.is_id_card_valid(temporary_passport))
        self.assertFalse(self.id_card_validator.is_documentnumber_valid(temporary_passport.documentnumber,
                                                                        IdCardType.TEMPORARY_PASSPORT))

    def test_is_documentnumber_for_temporary_passport_with_to_long_documentnumber_valid(self):
        temporary_passport = IdCard.create_temporary_or_children_passport("B<379621984","6101149",
                                                                          Gender.M, "3501140", "8",
                                                                          IdCardType.TEMPORARY_PASSPORT)

        self.assertFalse(self.id_card_validator.is_id_card_valid(temporary_passport))
        self.assertFalse(self.id_card_validator.is_documentnumber_valid(temporary_passport.documentnumber,
                                                                        IdCardType.TEMPORARY_PASSPORT))

    def test_is_documentnumber_for_temporary_passport_with_illegal_first_character_in_documentnumber_valid(self):
        temporary_passport = IdCard.create_temporary_or_children_passport("F<37962196","6101149",
                                                                          Gender.M, "3501140", "4",
                                                                          IdCardType.TEMPORARY_PASSPORT)

        self.assertFalse(self.id_card_validator.is_id_card_valid(temporary_passport))
        self.assertFalse(self.id_card_validator.is_documentnumber_valid(temporary_passport.documentnumber,
                                                                        IdCardType.TEMPORARY_PASSPORT))

    def test_is_documentnumber_for_children_passport_valid(self):
        children_passport = IdCard.create_temporary_or_children_passport("G<40134435","7101146",
                                                                          Gender.M, "3501140", "0",
                                                                          IdCardType.CHILDREN_PASSPORT)

        self.assertTrue(self.id_card_validator.is_id_card_valid(children_passport))
        self.assertTrue(self.id_card_validator.is_documentnumber_valid(children_passport.documentnumber,
                                                                       IdCardType.CHILDREN_PASSPORT))

    def test_is_documentnumber_for_children_passport_with_illegal_first_character_in_documentnumber_valid(self):
        children_passport = IdCard.create_temporary_or_children_passport("C<40134435","7101146",
                                                                          Gender.M, "3501140", "2",
                                                                          IdCardType.CHILDREN_PASSPORT)

        self.assertFalse(self.id_card_validator.is_id_card_valid(children_passport))
        self.assertFalse(self.id_card_validator.is_documentnumber_valid(children_passport.documentnumber,
                                                                        IdCardType.CHILDREN_PASSPORT))

    def test_is_birth_date_valid(self):
        new_identity_card = IdCard.create_identity_card_without_version("RPKV2X4VT0","9901122",
                                                                        "3501106", "2",
                                                                        IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

        self.assertTrue(self.id_card_validator.is_id_card_valid(new_identity_card))
        self.assertTrue(self.id_card_validator.is_birthday_date_valid(new_identity_card.birth_date))

    def test_is_birth_date_with_invalid_check_digit_valid(self):
        new_identity_card = IdCard.create_identity_card_without_version("RPKV2X4VT0","9901123",
                                                                        "3501106", "5",
                                                                        IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

        self.assertFalse(self.id_card_validator.is_id_card_valid(new_identity_card))
        self.assertFalse(self.id_card_validator.is_birthday_date_valid(new_identity_card.birth_date))

    def test_is_birth_date_without_check_digit_valid(self):
        new_identity_card = IdCard.create_identity_card_without_version("RPKV2X4VT0","990112",
                                                                        "3501106", "0",
                                                                        IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

        self.assertFalse(self.id_card_validator.is_id_card_valid(new_identity_card))
        self.assertFalse(self.id_card_validator.is_birthday_date_valid(new_identity_card.birth_date))

    def test_is_birth_date_younger_than_16_year_valid(self):
        birth_date = datetime.strftime(datetime.now() - relativedelta(years=16) + relativedelta(days=1), '%y%m%d')
        birth_date_with_check_digit = birth_date + self.id_card_generator.generate_check_digit(birth_date)
        check_digit = self.id_card_generator.generate_check_digit("RPKV2X4VT0" + birth_date_with_check_digit + "3501106")
        new_identity_card = IdCard.create_identity_card_without_version("RPKV2X4VT0",
                                                                        birth_date_with_check_digit, "3501106",
                                                                        check_digit,
                                                                        IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

        self.assertFalse(self.id_card_validator.is_id_card_valid(new_identity_card))
        self.assertFalse(self.id_card_validator.is_birthday_date_valid(new_identity_card.birth_date))

    def test_is_birth_date_16_year_valid(self):
        birth_date = datetime.strftime(datetime.now() - relativedelta(years=16) - relativedelta(days=1), '%y%m%d')
        birth_date_with_check_digit = birth_date + self.id_card_generator.generate_check_digit(birth_date)
        check_digit = self.id_card_generator.generate_check_digit("RPKV2X4VT0" + birth_date_with_check_digit + "3501106")
        new_identity_card = IdCard.create_identity_card_without_version("RPKV2X4VT0",
                                                                        birth_date_with_check_digit, "3501106",
                                                                        check_digit,
                                                                        IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

        self.assertTrue(self.id_card_validator.is_id_card_valid(new_identity_card))
        self.assertTrue(self.id_card_validator.is_birthday_date_valid(new_identity_card.birth_date))

    def test_is_birth_date_older_than_16_year_valid(self):
        birth_date = datetime.strftime(datetime.now() - relativedelta(years=16), '%y%m%d')
        birth_date_with_check_digit = birth_date + self.id_card_generator.generate_check_digit(birth_date)
        check_digit = self.id_card_generator.generate_check_digit("RPKV2X4VT0" + birth_date_with_check_digit + "3501106")
        new_identity_card = IdCard.create_identity_card_without_version("RPKV2X4VT0",
                                                                        birth_date_with_check_digit, "3501106",
                                                                        check_digit,
                                                                        IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

        self.assertTrue(self.id_card_validator.is_id_card_valid(new_identity_card))
        self.assertTrue(self.id_card_validator.is_birthday_date_valid(new_identity_card.birth_date))

    def test_is_expiry_date_valid(self):
        new_identity_card = IdCard.create_identity_card_without_version("RPKV2X4VT0","9901122",
                                                                        "3501106", "2",
                                                                        IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

        self.assertTrue(self.id_card_validator.is_id_card_valid(new_identity_card))
        self.assertTrue(self.id_card_validator.is_expiry_date_valid(new_identity_card.expiry_date))

    def test_is_expiry_date_without_check_digit_valid(self):
        check_digit = self.id_card_generator.generate_check_digit("RPKV2X4VT0" + "9901122" + "350110")
        new_identity_card = IdCard.create_identity_card_without_version("RPKV2X4VT0","9901122",
                                                                        "350110", check_digit,
                                                                        IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

        self.assertFalse(self.id_card_validator.is_id_card_valid(new_identity_card))
        self.assertFalse(self.id_card_validator.is_expiry_date_valid(new_identity_card.expiry_date))

    def test_is_expired_expiry_date_valid(self):
        expiry_date = datetime.strftime(datetime.now() - relativedelta(days=1), '%y%m%d')
        expiry_date_with_check_digit = expiry_date + self.id_card_generator.generate_check_digit(expiry_date)
        check_digit = self.id_card_generator.generate_check_digit("RPKV2X4VT0" + "9901122" + expiry_date_with_check_digit)
        new_identity_card = IdCard.create_identity_card_without_version("RPKV2X4VT0", "9901122",
                                                                        expiry_date_with_check_digit, check_digit,
                                                                        IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

        self.assertFalse(self.id_card_validator.is_id_card_valid(new_identity_card))
        self.assertFalse(self.id_card_validator.is_expiry_date_valid(new_identity_card.expiry_date))

    def test_is_expiry_date_expires_today_valid(self):
        expiry_date = datetime.strftime(datetime.now(), '%y%m%d')
        expiry_date_with_check_digit = expiry_date + self.id_card_generator.generate_check_digit(expiry_date)
        check_digit = self.id_card_generator.generate_check_digit("RPKV2X4VT0" + "9901122" + expiry_date_with_check_digit)
        new_identity_card = IdCard.create_identity_card_without_version("RPKV2X4VT0", "9901122",
                                                                        expiry_date_with_check_digit, check_digit,
                                                                        IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

        self.assertTrue(self.id_card_validator.is_id_card_valid(new_identity_card))
        self.assertTrue(self.id_card_validator.is_expiry_date_valid(new_identity_card.expiry_date))



if __name__ == '__main__':
    unittest.main()
