import concurrent.futures
from threading import Lock



class Solution:
    def __init__(self):
        self.a = 0
        self.threadLock = Lock()


    def function(self, arg):
        for _ in range(arg):
            with self.threadLock:
                self.a += 1


    def main(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for _ in range(5):
                executor.submit(self.function, 1000000)
        print("----------------------", self.a)  # ???


if __name__ == '__main__':
    cls = Solution()
    cls.main()