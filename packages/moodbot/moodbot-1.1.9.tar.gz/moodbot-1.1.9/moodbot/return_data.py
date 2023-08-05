class output:
    def __init__(self, input, output, confidence, delta, emotion):
        self.content = output
        self.match = input
        self.confidence = confidence
        self.time = delta
        self.emotion = emotion