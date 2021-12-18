import random
class thermometer():
    def __init__(self):
        self.is_on=False
    def on(self):
        self.is_on=True
    def off(self):
        self.is_on=False
    def measure(self):
        if self.is_on: self.temperature=random.randrange(3400,4200,10)/100
        else: print("can't measure,thermometer is off")
    def display(self):
        if self.is_on==False: print("can't display,thermometer is off")
        else:
            try:
                if self.temperature >= 41.0: print(f"Temperature: {self.temperature} (CRITICAL TEMPERATURE!!)")
                elif self.temperature >= 37.0: print(f"Temperature: {self.temperature} (FEVER)")
                else: print(f"Temperature: {self.temperature}")
            except: print("temperature isn't measured")