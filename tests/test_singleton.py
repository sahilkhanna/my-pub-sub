import pytest
from mypubsub.modules import SingletonBase

def test_singleton_instance_creation():
    """Test that only one instance of the singleton class is created."""
    instance1 = SingletonBase.get_instance()
    instance2 = SingletonBase.get_instance()
    
    assert instance1 is instance2, "SingletonBase should have only one instance"

def test_singleton_reset():
    """Test that resetting the singleton creates a new instance."""
    instance1 = SingletonBase.get_instance()
    SingletonBase.reset_instance()
    instance2 = SingletonBase.get_instance()
    
    assert instance1 is not instance2, "SingletonBase instance should be reset and a new instance created"
    assert SingletonBase.get_instance_count() == 1, "SingletonBase should have exactly one instance after reset"

def test_singleton_instance_count():
    """Test the number of instances created for the singleton class."""
    instance1 = SingletonBase.get_instance()
    instance2 = SingletonBase.get_instance()
    
    assert SingletonBase.get_instance_count() == 1, "SingletonBase should have exactly one instance"

def test_singleton_string_representation():
    """Test the string representation of the singleton instance."""
    instance = SingletonBase.get_instance()
    assert str(instance) == "SingletonBase singleton instance", "String representation of SingletonBase is incorrect"
