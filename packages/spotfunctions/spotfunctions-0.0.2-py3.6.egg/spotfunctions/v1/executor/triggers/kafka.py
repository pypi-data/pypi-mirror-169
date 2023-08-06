from kafka import KafkaConsumer
from spotfunctions.v1.models.triggers.kafka import KafkaTrigger
from spotfunctions.v1.executor.bindings.kafka import KafkaBindingRuntime
from importlib import import_module
class KafkaTriggerRunner:
    def __init__(self, main_file_name: str, kafka_consumer: KafkaConsumer, configs, binding: KafkaBindingRuntime = None, binding_name: str = None):
        self.kafka_consumer = kafka_consumer
        self.configs = configs
        self.binding = binding
        self.binding_name = binding_name
        self.user_main_function = getattr(import_module(main_file_name.replace(".py", "")), "main")

    def run(self):
        for message in self.kafka_consumer:
            # message value and key are raw bytes -- decode if necessary!
            # e.g., for unicode: `message.value.decode('utf-8')`
            trigger_message = KafkaTrigger(message)
            if self.binding is not None:
                self.user_main_function(**{self.config["name"]: trigger_message, self.binding_name: self.binding})
            else:
                self.user_main_function(**{self.configs["name"]: trigger_message})
