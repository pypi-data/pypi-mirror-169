
class KafkaHeader:
    def __init__(self, key: str, value: bytearray):
        self.key = key
        self.value = value
