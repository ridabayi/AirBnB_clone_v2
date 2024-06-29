#!/usr/bin/python3
"""
Test cases for State class and its documentation
"""

import unittest
from datetime import datetime
import inspect
import pep8
from models.state import State
from models.base_model import BaseModel

class TestStateDocs(unittest.TestCase):
    """Tests for State class documentation and style"""
    
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.state_functions = inspect.getmembers(State, inspect.isfunction)
    
    def test_pep8_conformance_state(self):
        """Test that models/state.py conforms to PEP8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style errors found in models/state.py")
    
    def test_pep8_conformance_test_state(self):
        """Test that tests/test_models/test_state.py conforms to PEP8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style errors found in tests/test_models/test_state.py")
    
    def test_state_module_docstring(self):
        """Test for presence and length of docstring in state module"""
        self.assertTrue(len(State.__doc__) > 0,
                        "State module docstring is missing or empty")
    
    def test_state_class_docstring(self):
        """Test for presence and length of docstring in State class"""
        self.assertTrue(len(State.__doc__) > 0,
                        "State class docstring is missing or empty")
    
    def test_state_functions_docstrings(self):
        """Test for presence and length of docstrings in State methods"""
        for func_name, func in self.state_functions:
            self.assertTrue(func.__doc__ is not None and len(func.__doc__) > 0,
                            f"Docstring is missing or empty for method: {func_name}")

class TestState(unittest.TestCase):
    """Tests for State class functionality"""
    
    def setUp(self):
        """Set up each test case"""
        self.state = State()
    
    def test_is_subclass_of_base_model(self):
        """Test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.state, BaseModel)
    
    def test_name_attribute(self):
        """Test existence and default value of 'name' attribute"""
        self.assertTrue(hasattr(self.state, 'name'))
        if type(models.storage_t) == 'db':
            self.assertIsNone(self.state.name)
        else:
            self.assertEqual(self.state.name, "")
    
    def test_to_dict_method(self):
        """Test the to_dict method of State class"""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertNotIn('_sa_instance_state', state_dict)
        for attr in self.state.__dict__.keys():
            self.assertIn(attr, state_dict)
        self.assertIn('__class__', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')
    
    def test_to_dict_values(self):
        """Test values in the dictionary returned by to_dict method"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)
        self.assertEqual(state_dict['created_at'], self.state.created_at.strftime(t_format))
        self.assertEqual(state_dict['updated_at'], self.state.updated_at.strftime(t_format))
    
    def test_str_method(self):
        """Test the __str__ method of State class"""
        string = str(self.state)
        self.assertEqual(string, f"[State] ({self.state.id}) {self.state.__dict__}")

if __name__ == '__main__':
    unittest.main()
