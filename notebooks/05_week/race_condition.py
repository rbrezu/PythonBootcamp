import threading

GLOBAL_RANGE = 100000

# lock = threading.Lock()
def increment_global():
    global x
    x += 1


def worker():
    for _ in range(GLOBAL_RANGE):
        # lock.acquire()
        increment_global()
        # lock.release()


n_threads = 2
def main():
    global x
    x = 0

    threads = []
    for _ in range(n_threads):
        th = threading.Thread(target=worker)
        th.start()

        threads.append(th)

    [th.join() for th in threads]


if __name__ == "__main__":
    for i in range(5):
        main()
        print("x = {1} after Iteration {0}".format(i, x))
