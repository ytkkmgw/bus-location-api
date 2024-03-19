import os


class ODPTApiKey:
    def __init__(self):
       self.value= os.environ.get("ODPT_API_KEY")
