import time
class List:
    def time_it(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(func.__name__ + "took" + str((end-start)*10000))
            return result
        return wrapper

    @time_it
    def list_comprehension(self):
        a = [i for i in range (50)]
        print(a)
          
        #a = []
        #for i in range(50):
        #    a.append(i)
        #print(a)
    
    @time_it
    def generators(self,data):
        for index in range(len(data)-1, -1, -1):
            yield data[index]

if __name__ == "__main__":
    obj = List()
    obj.list_comprehension()
    rev = obj.generators("amardeep")
    for char in rev:
        print(char)
