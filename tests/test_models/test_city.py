#!/usr/bin/pethon3
"""
    This is the test module for base_model
"""
from models.city import City
import unittest
import datetime
import time
import os
import json
from models import storage


class TestCity(unittest.TestCase):
    """
        The tests for model
    """

    '''def setUp(self):
        """ Sets up """
        setattr(storage, "_FileStorage__objects", dict())'''

    def test_doc(self):
        """ Tests for docs """
        self.assertIsNotNone(("models.base_model".__doc__))
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)

    def test_attr(self):
        """ Tests creation of new attributes """
        m1 = City()
        m1.name = "John"
        self.assertAlmostEqual(m1.name, "John")
        m1.number = 123
        self.assertAlmostEqual(m1.number, 123)
        self.assertEqual(type(m1.id), str)
        self.assertEqual(type(m1.created_at), datetime.datetime)
        self.assertEqual(type(m1.updated_at), datetime.datetime)
        m1.state_id = "123"
        self.assertEqual(type(m1.state_id), str)

    def test_class_type(self):
        """ This makes sure we're making a base model """
        m1 = City()
        self.assertAlmostEqual(type(m1), City)

    def test_updated_at(self):
        """
            Makes sure that the class is properly
            updated and make sure created does not change
        """
        m1 = City()
        create = str(m1.created_at)
        start = str(m1.updated_at)
        m1.name = "John"
        time.sleep(1)
        m1.save()
        self.assertNotEqual(str(m1.updated_at), start)
        self.assertEqual(str(m1.created_at), create)

    def test_to_dict(self):
        """ Tests the dictionary """
        m1 = City()
        m2 = m1.to_dict()
        self.assertEqual(m2["updated_at"], m1.updated_at.isoformat())
        self.assertEqual(m2["__class__"], "City")
        self.assertNotIn("__class__", m1.__dict__)

    def test_save(self):
        """ Tests the save method """
        m1 = City()
        m1.save()
        with open("file.json", mode="r", encoding="UTF-8") as f:
            d = json.load(f)
        for item in d:
            if m1.id in item:
                d = d[item]
        self.assertDictEqual(d, m1.to_dict())

    def test_new_model_from_dict(self):
        """ Tests createion of new model with dictionary """
        m1 = City()
        m1_dict = m1.to_dict()
        m2 = City(**m1_dict)
        self.assertFalse(m1 is m2)
        self.assertDictEqual(m1.to_dict(), m2.to_dict())

    '''def tearDown(self):
        """ Tear that shit down homie """
        os.remove('file.json')'''
