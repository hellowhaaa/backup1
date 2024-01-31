import threading
from time import sleep


def do_job(number):
    sleep(3)
    print(f"Job {number} finished")


def main():
    # treads = []
    for i in range(5):
        threading.Thread(target=do_job, args=[i]).start()

        # t1 = threading.Thread(target=do_job, args=[1.5])
        # t1.start()
        # treads.append(t1)
    # for thread in treads:
    #     thread.join()


    # threading.Thread(target=do_job(i + 2)).start()
    # threading.Thread(target=do_job(i + 3)).start()
    # threading.Thread(target=do_job(i + 4)).start()







main()