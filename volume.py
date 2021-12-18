class tv():
     
    def __init__(self):
       self.is_on = False
       self.channel_no = 1
       self.volume=0
    def volume_increase(self):
        if self.volume<10: self.volume+=1
    def volume_decrease(self):
        if self.volume>0: self.volume-=1
    def turn_on(self):
       self.is_on = True
    def turn_off(self):
       self.is_on = False
    def show_status(self):
        if self.is_on == False : print("TV is off")
        else: 
            try:
                if self.channel_no<= len(self.channels_list):
                    print(f"TV is on, channel: { self.channels_list[self.channel_no-1]}, current volume level: {self.volume}")
                else: print(f"TV is on, channel: {self.channel_no}, current volume level: {self.volume}")
            except: print(f"TV is on, channel: {self.channel_no}, current volume level: {self.volume}")
    def set_channel(self,new_channel_no):
       self.channel_no = new_channel_no
    def set_channels(self,channel_list):
        self.channels_list=channel_list
    def show_channels(self):
        try:
            print('Channel list:')
            for i in range(len(self.channels_list)):
                print(f"{i+1}. {self.channels_list[i]}")
        except: print('No channels')
            
channels=['TVP1','TVP2','Polsat','TVN','Filmbox','Discovery']

q=tv()
q.show_status()
q.set_channels(channels)
q.show_channels()
q.turn_on()
q.show_status()
q.volume_increase()
q.volume_increase()
q.show_status()
q.volume_increase()
q.volume_increase()
q.volume_increase()
q.volume_increase()
q.volume_increase()
q.volume_increase()
q.volume_increase()
q.volume_increase()
q.volume_increase()
q.volume_increase()
q.volume_increase()
q.volume_increase()
q.volume_increase()
q.volume_increase()
q.volume_increase()
q.show_status()
q.volume_decrease()
q.show_status()
q.turn_off()
q.show_status()

