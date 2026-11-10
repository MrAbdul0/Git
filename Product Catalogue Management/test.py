class Twitter:
    def __init__(self, content):
        self.content = content

    def post(self):
        return f'Tweet: {self.content}'
