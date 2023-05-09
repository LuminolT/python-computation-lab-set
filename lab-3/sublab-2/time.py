# Time class

class Time(object):
    def __init__(self, h=0, m=0, s=0) -> None:
        self.hour = h
        self.minute = m
        self.second = s
        if not self.isvalid():
            raise ValueError("Invalid time value!")
    
    def __str__(self) -> str:
        return f"{self.hour:02}:{self.minute:02}:{self.second}"
    
    def __add__(self, timep):
        total_seconds = self.time2int() + timep.time2int()
        return self.int2time(total_seconds)

    def time2int(self):
        return self.hour * 3600 + self.minute * 60 + self.second
    
    @classmethod
    def int2time(cls, seconds):
        mins, sec = divmod(seconds, 60)
        h, min = divmod(mins, 60)
        if h >= 24:
            h = 0
        return cls(h, min, sec) 
    
    def printtime(self):
        print(str(self))

    def isafter(self, timep):
        return self.time2int() > timep.time2int()
    
    def increment(self, n):
        total_secs = self.time2int() + n
        return self.int2time(total_secs)
    
    def isvalid(self):
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

def main():
    t1 = Time(7,15,30)
    t2 = Time(16,45,50)

    # Test __str__ and __add__
    print("Test __str__ and __add__: ")
    print(t1)
    print(t1 + t2)
    
    # Test time2int() and int2time()
    print("\nTest time2int() and int2time(): ")
    print(t1.time2int())
    print(Time.int2time(26130))

    # Test printtime()
    print("\nTest printtime(): ")
    t1.printtime()

    # Test isafter()
    print("\nTest isafter(): ")
    print(t1.isafter(t2))
    print(t2.isafter(t1))

    # Test increment()
    print("\nTest increment(): ")
    print(t1.increment(40))

    # Test isvalid()
    try:
        print("\nTest isvalid(): ")
        print(t1.isvalid())
        t3 = Time(13,60,10)
        print(t3.isvalid())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
