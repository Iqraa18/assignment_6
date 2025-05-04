class Counter:
    object_count = 0  # class variable to track the number of objects

    def __init__(self):
        Counter.object_count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.object_count}")

c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()

Counter.show_count()
