class Food:
  def __init__(self, fruit, color):
    self.fruit = fruit
    self.color = color
 
  def show(self):
    print("fruit is", self.fruit)
    print("color is", self.color)
 
apple = Food("apple", "red")
 
apple.show()
