from django.test import TestCase
from todolist.models import Person, Car

class PersonTestCase(TestCase):
    def setUp(self):
        Person.object.create(first_name="Yarik", last_name = "Chumak", age="21")
        Person.object.create(first_name="Yaroslav", last_name = "Chumachenko", age="22")
    
    def test_creation(self):
        person1 = Person.object.get(first_name = "Yarik")
        person2 = Person.object.get()
        self.assertEqual(person1.first_name, "Yarik")
        self.assertEqual(person2.first_name, "Yaroslav")
        self.assertEqual(person1.age, "21")
        self.assertEqual(person2.age, "22")

class CarTestCase(TestCase):
    pass