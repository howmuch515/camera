import cv2, argparse
from pathlib import Path
from time import sleep

CURRENT_PATH = str(Path.cwd())
HOME_PATH = str(Path.home())
DEFAULT_PATH = HOME_PATH + "/Pictures/CAMERA/camera_picture"

def take(file_name):
    file_name += ".jpg"
    cap = cv2.VideoCapture(0)
    for i in range(3):
        cap.read() # 初期の写真はカメラが起動してすぐは暗いので、捨てる

    ret, im = cap.read()
    if ret == 0:
        print("[!] Miss...")
    else:
        print("[*] Success!")
        print(file_name)
        cv2.imwrite(file_name, im)
        print("Saved in {}".format(file_name))

    # fini
    cap.release()
    cv2.destroyAllWindows()


def continuous_shoot(file_name, number):
    for i in range(number):
        take(file_name + str(i))

def timer(t):
    timer_count = int(t)
    for i in range(timer_count):
        last_time = timer_count - i
        print("{}...".format(last_time))
        sleep(1)

def main():
    parser = argparse.ArgumentParser(description="Take a picture.")
    parser.add_argument('-n', '--file_name', metavar="FILE_NAME", action="store", help="picture's name", default=DEFAULT_PATH)
    parser.add_argument('-c', '--continuous', action="store_true", help="continuous shooting", default=False)
    parser.add_argument('-t', '--timer', action="store", help="self timer", default=0)
    parser.add_argument('-v', '--version', action="version", version="Ver.0.0")

    args = parser.parse_args()

    # init
    FILE_NAME = args.file_name
    if FILE_NAME != DEFAULT_PATH:
        FILE_NAME = CURRENT_PATH + '/' + FILE_NAME

    # timer
    timer(args.timer)

    if args.continuous:
        continuous_shoot(FILE_NAME, 5)
    else:
        take(FILE_NAME)

if __name__ == '__main__':
    main()
