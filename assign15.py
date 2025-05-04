# mro.py

class A:
    def show(self):
        print("A's show method")

class B(A):
    def show(self):
        print("B's show method")

class C(A):
    def show(self):
        print("C's show method")

class D(B, C):  # D inherits from B and C
    pass

# Example usage
obj = D()
obj.show()  # Call the show method and observe the MRO
