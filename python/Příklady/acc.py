class Account:
    def __init__(self, username, followers):
        self.username = username
        self.followers = followers

    def add_followers(self, count):
        self.followers += count
        if self.followers < 0:
            self.followers = 0
            print ("Počet followerů nemůže být záporný.")
        print( f"self.followers")
    
    def __str__(self):
        return f"Účet {self.username} má {self.followers} followerů."
    
    def __del__(self):
        print(f"Účet {self.username} byl smazán")
        self.username = None
        self.followers = None

class VerifiedAccount(Account):

    def __init__(self, username, followers, badge_color):
        super().__init__ (username, followers)
        self.badge_color = badge_color

    def __str__(self):
        if self.followers > 10000:
            return f"Účet {self.username} má {self.followers} followerů a modrou značku ověření."
        else:
            return f"Účet {self.username} má {self.followers} followerů a šedou značku ověření."

user1 = Account("cool_student_23", 150)
user2 = VerifiedAccount("singer_official", 1050, "badge")
user3 = VerifiedAccount("singer_official", 10500, "badge")
print(user2)
print(user3)
user1.add_followers(50)
print(user1)
