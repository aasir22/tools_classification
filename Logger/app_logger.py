from datetime import datetime

class App_logger:

    def __init__(self):
        pass

    def log(self,file_name,log_message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.time = self.now.strftime("%H:%M:%S")
        file_name.write(str(self.date) + '\t' + str(self.time) +'\t\t' + log_message + '\n')