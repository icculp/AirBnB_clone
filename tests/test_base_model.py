#!/usr/bin/python3
"""
    This is the test module for base_model
"""
import unittest
from models.base_model import BaseModel



class test_base_model(unittest.TestCase):
    """
        The tests for model
    """

    def test_doc(self):
        """Tests for docs"""
        self.assertIsNotNone(("models.base_model".__doc__))
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def test_attr(self):
        """Tests creation of new attributes"""
        m1 = BaseModel()
        m1.name = "John"
        self.assertAlmostEqual(m1.name, "John")
        m1.number = 123
        self.assertAlmostEqual(m1.number, 123)

    def test_class_type(self):
        """This makes sure we're making a base model"""
        m1 = BaseModel()
        self.assertAlmostEqual(type(m1), BaseModel)

    def test_updated_at(self):
        """Makes sure that the class is properly updated"""
        m1 = BaseModel()
        create = str(m1.created_at)
        start = str(m1.updated_at)
        m1.name = "John"
        m1.save()
        self.assertNotEqual(str(m1.updated_at), start)
        self.assertEqual(str(m1.created_at), create)
