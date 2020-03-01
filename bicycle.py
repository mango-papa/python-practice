class Bicycle:
    instance_count = 0

    def __init__(self, wheel_zie=10, color='red', speed=20):
        self.speed = speed
        self.wheel_size = wheel_zie
        self.color = color
        Bicycle.instance_count = Bicycle.instance_count + 1

    @staticmethod
    def call():
        print('call')

    def move(self, speed):
        print("gogo {}".format(speed))
        Bicycle.call()

    def turn(self, direction):
        print('turn {}'.format(direction))

    def stop(self):
        print("stop {} {}".format(self.wheel_size, self.color))
        print(self.speed)



class FoldingBicycle(Bicycle):
    def __init__(self, wheel_size, color, state):
        # Bicycle.__init__(self, wheel_size, color)
        super().__init__(wheel_size, color)
        self.state = state

    def fold(self):
        self.state = 'folding'
        print('state is now {}'.format(self.state))

    def unfold(self):
        self.state = 'unfolding'
        print('state is now {}'.format(self.state))