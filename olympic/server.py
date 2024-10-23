import os
import pickle
import threading
from typing import Callable, Dict, List, Tuple


class OlympicsServer:
    def __init__(self):
        self.lock = threading.Lock()
        self.subscribers: Dict[str, List[Tuple[Callable, int]]] = {}
        self.messages: List[Tuple[str, str]] = []
        self.load_messages()

    def load_messages(self):
        if os.path.exists('messages.pkl'):
            with open('messages.pkl', 'rb') as f:
                self.messages = pickle.load(f)

    def save_messages(self):
        with open('messages.pkl', 'wb') as f:
            pickle.dump(self.messages, f)

    def publish(self, topic: str, message: str, qos: int):
        with self.lock:
            self.messages.append((topic, message))
            self.save_messages()
            self.notify_subscribers(topic, message, qos)

    def subscribe(self, topic: str, callback: Callable):
        with self.lock:
            if topic not in self.subscribers:
                self.subscribers[topic] = []
            self.subscribers[topic].append((callback, 0))  # QoS level is not implemented yet
            self.send_stored_messages(topic, callback)

    def notify_subscribers(self, topic: str, message: str, qos: int):
        for sub_topic in self.subscribers:
            if self.match_topic(topic, sub_topic):
                for callback, _ in self.subscribers[sub_topic]:
                    threading.Thread(target=callback, args=(topic, message)).start()

    def match_topic(self, topic: str, sub_topic: str) -> bool:
        pass

    def send_stored_messages(self, topic: str, callback: Callable):
        for stored_topic, message in self.messages:
            if self.match_topic(stored_topic, topic):
                callback(stored_topic, message)
