import concurrent.futures
from threading import Lock


a = 0
threadLock = Lock()


def function(arg):
    global a
    for _ in range(arg):
        with threadLock:
            a += 1


def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(5):
            executor.submit(function, 1000000)
    print("----------------------", a)  # ???


main()