#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """Sets up the resources required to run tests"""
        if os.path.isfile('file.json'):
            os.rename('file.json', 'tmp_file.json')
        self.model1 = BaseModel()

    def tearDown(self):
        """Tears down the resources that have been used to run tests"""
        if os.path.isfile('file.json'):
            os.remove('file.json')
        if os.path.isfile('tmp_file.json'):
            os.rename('tmp_file.json', 'file.json')
        del self.model1

    def test_attributes_exist(self):
        """Test that FileStorage class has required attributes and methods"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(hasattr(FileStorage, 'new'))
        self.assertTrue(hasattr(FileStorage, 'save'))
        self.assertTrue(hasattr(FileStorage, 'reload'))

    def test_attributes(self):
        """Test whether the type of FileStorage class attributes is correct"""
        self.assertEqual(storage._FileStorage__file_path, 'file.json')
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_all(self):
        """Test that the all method returns the correct dictionary"""
        my_dict = storage.all()
        my_id = 'BaseModel.' + self.model1.id
        self.assertIsInstance(my_dict, dict)

    def test_reload(self):
        """Test that the reload method actually reloads objects from file"""
        self.model1.save()
        self.assertTrue(os.path.isfile('file.json'))
        tmp_obj = BaseModel()
        tmp_id = 'BaseModel.' + tmp_obj.id
        tmp_obj.save()
        del storage._FileStorage__objects[tmp_id]
        storage.reload()
        self.assertIn(tmp_id, storage.all())

    def test_all_params(self):
        """ __objects id properly returned  """
        Mm = ['BaseModel', 'User', 'Place',
              'City', 'State', 'Review', 'Amenity']
        new = BaseModel()
        temp = storage.all(BaseModel)
        self.assertIsInstance(temp, dict)

        # Test that only specified classes are returned
        for m in Mm:
            tmp = storage.all(eval(m))
            for n in Mm:
                if n != m:
                    self.assertNotIn(n, tmp)

    def test_all_params_error(self):
        """Check that the correct error message is raised"""
        with self.assertRaises(NameError):
            tmp = storage.all(MyModel)

    def test_delete(self):
        """ Confirm delete method deletes objects """

        new = BaseModel()
        new.save()
        new_id = "BaseModel" + "." + "new.id"
        storage.delete()
        self.assertNotIn(new_id, storage.all().keys())
