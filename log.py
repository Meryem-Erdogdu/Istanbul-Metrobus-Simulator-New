from datetime import datetime

class LogManager:
    def __init__(self, kaynak):
        self.kaynak = kaynak

    def info(self, mesaj):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [INFO][{self.kaynak}] {mesaj}")

    def warning(self, mesaj):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [WARNING][{self.kaynak}] {mesaj}")

    def error(self, mesaj):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [ERROR][{self.kaynak}] {mesaj}")

    def success(self, mesaj):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [SUCCESS][{self.kaynak}] {mesaj}")

    def alert(self, mesaj):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [ALERT][{self.kaynak}] {mesaj}")
