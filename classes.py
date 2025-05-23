
class MyClass:

    def __init__(self, image):
        self.image = image

    def my_method(self):
        print(self.image)


def factorial(n):
    # 5! = 1 * 2 * 3 * 4 * 5
    if n == 1: # базовый случай
        return
    else:  #рекурсивный случай
        return factorial(n-1)*n 


if __name__ == "tictactoe":
    my_class = MyClass("1.png")
    my_class2 = MyClass("2.png")
    print(my_class.my_method())
    print(my_class2.my_method())
