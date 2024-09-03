from . import modules
from typing import Callable

class MyPubSub(modules.SingletonBase):
    """A Pub Sub Singleton Class"""
    def __init__(self):
        if not hasattr(self, 'initialized'):  # Prevent re-initialization
            self.initialized = True
            self._subscribers = {}
    
    def subscribe(self, topic:str, callback:Callable):
        """Subscribe to a topic with a callback function."""
        if topic not in self._subscribers:
            self._subscribers[topic] = []
        self._subscribers[topic].append(callback)

    def unsubscribe(self, topic:str, callback:Callable):
        """Unsubscribe a callback function from a topic."""
        if topic in self._subscribers:
            self._subscribers[topic].remove(callback)
            if not self._subscribers[topic]:
                del self._subscribers[topic]

    def publish(self, topic:str, message):
        """Publish a message to all subscribers of a topic."""
        if topic in self._subscribers:
            for callback in self._subscribers[topic]:
                callback(message)