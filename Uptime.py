import sys
import requests
import datetime
from time import sleep, time
import matplotlib.pyplot as plt


def seconds_to_str(elapsed: datetime) -> str:
    return str(datetime.timedelta(seconds=int(elapsed)))


def microseconds_to_str(elapsed: datetime) -> str:
    return str(datetime.timedelta(microseconds=elapsed))


def request(url: str) -> tuple:
    try:
        response = requests.get(url)
        return response.status_code, response.elapsed.microseconds
    except requests.exceptions.ConnectionError:
        return 0, 0


def main(argv: list) -> None:
    if len(argv) < 2:  # if no url is specified, exit with usage
        print("Usage : Uptaime.py url")
        exit()

    url = argv[1]  # store the url to watch

    res_status = []  # stores all the response codes
    res_time = []  # stores all the response times

    start = time()  # start timer

    try:
        while True:
            status, times = request(url)
            res_status.append(status)
            res_time.append(times)
            sleep(1)
    except KeyboardInterrupt:
        stop = time()  # end timer
        interval = stop - start  # calculate elapsed time

        t = [t for t in range(len(res_time))]  # time array
        x = list(map(lambda res: res // 1000, res_time))  # response time array
        y = [sum(res_time) // len(res_time) // 1000] * len(x)  # response time's mean

        percent_up = (res_status.count(200) // len(res_status)) * 100  # percentage of time when site was up

        print("{0}% up time during {1}".format(percent_up, seconds_to_str(interval)))
        print("Minimum response time: {0}ms\nMaximum response time : {1}ms\nMean response time : {2}ms"
              .format(min(x), max(x), y[0]))
        plt.plot(t, x, label="Response time")  # plot the response times
        plt.plot(t, y, label="Mean response time", linestyle="--")  # plot the response time's mean
        plt.legend(loc='upper right')
        plt.show()


if __name__ == "__main__":
    main(sys.argv)
