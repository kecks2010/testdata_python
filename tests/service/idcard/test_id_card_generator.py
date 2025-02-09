import unittest

from datetime import datetime
from dateutil.relativedelta import relativedelta
from testdata.model.idcard.id_card import IdCardType, Gender
from testdata.service.idcard.id_card_generator import IdCardGenerator
from testdata.service.idcard.id_card_validator import IdCardValidator

class TestIdCardGenerator(unittest.TestCase):

    id_card_generator = IdCardGenerator()
    id_card_validator = IdCardValidator()

    def test_old_identity_card_without_birth_date(self):
        id_card = self.id_card_generator.generate_old_identity_card()

        self.assertIsNone(id_card.version)
        self.assertIsNone(id_card.gender)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.OLD_IDENTITY_CARD)

    def test_old_identity_card_with_birth_date(self):
        birth_date = datetime(1981, 12, 8)
        id_card = self.id_card_generator.generate_old_identity_card(birth_date)

        self.assertIsNone(id_card.version)
        self.assertIsNone(id_card.gender)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.OLD_IDENTITY_CARD)

    def test_old_identity_card_with_birth_date_and_expiry_date(self):
        birth_date = datetime(1981, 12, 8)
        expiry_date = datetime.now() + relativedelta(years=5)
        id_card = self.id_card_generator.generate_old_identity_card(birth_date, expiry_date)

        self.assertIsNone(id_card.version)
        self.assertIsNone(id_card.gender)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.OLD_IDENTITY_CARD)

    def test_new_identity_card_without_version_without_birth_date(self):
        id_card = self.id_card_generator.generate_new_identity_card_without_version()

        self.assertIsNone(id_card.version)
        self.assertIsNone(id_card.gender)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

    def test_new_identity_card_without_version_with_birth_date(self):
        birth_date = datetime(1981, 12, 8)
        id_card = self.id_card_generator.generate_new_identity_card_without_version(birth_date)

        self.assertIsNone(id_card.version)
        self.assertIsNone(id_card.gender)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

    def test_new_identity_card_without_versio_with_birth_date_and_expiry_date(self):
        birth_date = datetime(1981, 12, 8)
        expiry_date = datetime.now() + relativedelta(years=5)
        id_card = self.id_card_generator.generate_new_identity_card_without_version(birth_date, expiry_date)

        self.assertIsNone(id_card.version)
        self.assertIsNone(id_card.gender)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.NEW_IDENTITY_CARD_WITHOUT_VERSION)

    def test_new_identity_card_with_version_without_birth_date(self):
        id_card = self.id_card_generator.generate_new_identity_card_with_version()

        self.assertIsNotNone(id_card.version)
        self.assertIsNone(id_card.gender)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.NEW_IDENTITY_CARD_WITH_VERSION)

    def test_new_identity_card_with_version_with_birth_date(self):
        birth_date = datetime(1981, 12, 8)
        id_card = self.id_card_generator.generate_new_identity_card_with_version(birth_date)

        self.assertIsNotNone(id_card.version)
        self.assertIsNone(id_card.gender)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.NEW_IDENTITY_CARD_WITH_VERSION)

    def test_new_identity_card_with_versio_with_birth_date_and_expiry_date(self):
        birth_date = datetime(1981, 12, 8)
        expiry_date = datetime.now() + relativedelta(years=5)
        id_card = self.id_card_generator.generate_new_identity_card_with_version(birth_date, expiry_date)

        self.assertIsNotNone(id_card.version)
        self.assertIsNone(id_card.gender)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.NEW_IDENTITY_CARD_WITH_VERSION)

    def test_new_passport_without_birth_date_for_male(self):
        id_card = self.id_card_generator.generate_passport(Gender.M)

        self.assertIsNotNone(id_card.version)
        self.assertEqual(id_card.gender, Gender.M)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.PASSPORT)

    def test_new_passport_without_birth_date_for_female(self):
        id_card = self.id_card_generator.generate_passport(Gender.F)

        self.assertIsNotNone(id_card.version)
        self.assertEqual(id_card.gender, Gender.F)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.PASSPORT)

    def test_new_passport_without_birth_date_for_divers(self):
        id_card = self.id_card_generator.generate_passport(Gender.X)

        self.assertIsNotNone(id_card.version)
        self.assertEqual(id_card.gender, Gender.X)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.PASSPORT)

    def test_new_passport_with_version_with_birth_date_for_male(self):
        birth_date = datetime(1981, 12, 8)
        id_card = self.id_card_generator.generate_passport(Gender.M, birth_date)

        self.assertIsNotNone(id_card.version)
        self.assertEqual(id_card.gender, Gender.M)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.PASSPORT)

    def test_new_passport_with_versio_with_birth_date_and_expiry_date_for_male(self):
        birth_date = datetime(1981, 12, 8)
        expiry_date = datetime.now() + relativedelta(years=5)
        id_card = self.id_card_generator.generate_passport(Gender.M, birth_date, expiry_date)

        self.assertIsNotNone(id_card.version)
        self.assertEqual(id_card.gender, Gender.M)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.PASSPORT)

    def test_new_temporary_passport_without_birth_date_for_male(self):
        id_card = self.id_card_generator.generate_temporary_passport(Gender.M)

        self.assertIsNone(id_card.version)
        self.assertEqual(id_card.gender, Gender.M)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.TEMPORARY_PASSPORT)

    def test_new_temporary_passport_without_birth_date_for_female(self):
        id_card = self.id_card_generator.generate_temporary_passport(Gender.F)

        self.assertIsNone(id_card.version)
        self.assertEqual(id_card.gender, Gender.F)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.TEMPORARY_PASSPORT)

    def test_new_temporary_passport_without_birth_date_for_divers(self):
        id_card = self.id_card_generator.generate_temporary_passport(Gender.X)

        self.assertIsNone(id_card.version)
        self.assertEqual(id_card.gender, Gender.X)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.TEMPORARY_PASSPORT)

    def test_new_temporary_passport_with_version_with_birth_date_for_male(self):
        birth_date = datetime(1981, 12, 8)
        id_card = self.id_card_generator.generate_temporary_passport(Gender.M, birth_date)

        self.assertIsNone(id_card.version)
        self.assertEqual(id_card.gender, Gender.M)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.TEMPORARY_PASSPORT)

    def test_new_temporary_passport_with_versio_with_birth_date_and_expiry_date_for_male(self):
        birth_date = datetime(1981, 12, 8)
        expiry_date = datetime.now() + relativedelta(years=5)
        id_card = self.id_card_generator.generate_temporary_passport(Gender.M, birth_date, expiry_date)

        self.assertIsNone(id_card.version)
        self.assertEqual(id_card.gender, Gender.M)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.TEMPORARY_PASSPORT)

    def test_new_children_passport_without_birth_date_for_male(self):
        id_card = self.id_card_generator.generate_children_passport(Gender.M)

        self.assertIsNone(id_card.version)
        self.assertEqual(id_card.gender, Gender.M)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.CHILDREN_PASSPORT)

    def test_new_children_passport_without_birth_date_for_female(self):
        id_card = self.id_card_generator.generate_children_passport(Gender.F)

        self.assertIsNone(id_card.version)
        self.assertEqual(id_card.gender, Gender.F)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.CHILDREN_PASSPORT)

    def test_new_children_passport_without_birth_date_for_divers(self):
        id_card = self.id_card_generator.generate_children_passport(Gender.X)

        self.assertIsNone(id_card.version)
        self.assertEqual(id_card.gender, Gender.X)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.CHILDREN_PASSPORT)

    def test_new_children_passport_with_version_with_birth_date_for_male(self):
        birth_date = datetime(1981, 12, 8)
        id_card = self.id_card_generator.generate_children_passport(Gender.M, birth_date)

        self.assertIsNone(id_card.version)
        self.assertEqual(id_card.gender, Gender.M)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.CHILDREN_PASSPORT)

    def test_new_children_passport_with_versio_with_birth_date_and_expiry_date_for_male(self):
        birth_date = datetime(1981, 12, 8)
        expiry_date = datetime.now() + relativedelta(years=5)
        id_card = self.id_card_generator.generate_children_passport(Gender.M, birth_date, expiry_date)

        self.assertIsNone(id_card.version)
        self.assertEqual(id_card.gender, Gender.M)
        self.assertTrue(self.id_card_validator.is_id_card_valid(id_card))
        self.assertEqual(id_card.id_card_type, IdCardType.CHILDREN_PASSPORT)


if __name__ == '__main__':
    unittest.main()
