from django.db import models
import random


class Cat(models.Model):
    objects = None
    name = models.CharField(max_length=15)
    age = models.IntegerField(default=1)
    fullness = models.IntegerField(default=40)
    happiness = models.IntegerField(default=40)
    is_sleeping = models.BooleanField(default=False)

    def feed(self):
        if not self.is_sleeping:
            self.fullness += 15
            self.happiness += 5
            if self.fullness > 100:
                self.happiness -= 30
        self.save()

    def play(self):
        if self.is_sleeping:
            self.is_sleeping = False
            self.happiness -= 5
        else:
            self.happiness += 15
            self.fullness -= 10
            if random.randint(1, 3) == 1:
                self.happiness = 0
        self.save()

    def sleep(self):
        self.is_sleeping = True
        self.save()

    def get_image(self):
        if self.happiness > 70:
            return 'images/happy.jpeg'
        elif self.happiness > 30:
            return 'images/neutral.jpeg'
        else:
            return 'images/sad.jpeg'
