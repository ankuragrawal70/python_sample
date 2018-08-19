class TestNew():
    def __init__(self, a):
        self.a = a

    def __enter__(self):
        print("entering")
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def my_fun(self):
        raise Exception("invalid")


with TestNew(10) as t:
    t.my_fun()