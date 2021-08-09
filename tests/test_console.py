"""
   Contains the tests for the console 
"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

import sys
import os

def setUpModule():
    """Set up resources to be used in the test module"""
    if os.path.isfile("file.json"):
        os.rename("file.json", "tmp.json")


def tearDownModule():
    """Tear down resources used in the test module"""
    if os.path.isfile("file.json"):
        os.remove("file.json")
    if os.path.isfile("tmp.json"):
        os.rename("tmp.json", "file.json")


class TestHBNBCommand(unittest.TestCase):
    """Tests for the HBNBCommand prompt"""

    def test_HBNBCommand_prompt(self):
        """Test the HBNBCommand prompt"""
        self.assertEqual(HBNBCommand.prompt, '(hbnb) ')

    def test_empty_line(self):
        """Test output when an empty line is passed"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual("", f.getvalue().strip())

class TestHBNBCommand_create(unittest.TestCase):
    """Test the HBNBCommand create command"""

    def test_HBNBCommand_create_error_messages(self):
        """Test that the create comand prints the correct error messages"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create')
            self.assertEqual("** class name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create MyModel')
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_HBNBCommand_create_new_instances(self):
        """Test the creation of new instances of different classes"""

        Mm = ['BaseModel', 'User', 'Place',
              'City', 'State', 'Review', 'Amenity']
        for m in Mm:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd('create {}'.format(m))
                new_key = m + "." + f.getvalue().strip()
                self.assertIn(new_key, storage.all().keys())


