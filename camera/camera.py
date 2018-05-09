import cv2, argparse
from pathlib import Path
from time import sleep

CURRENT_PATH = str(Path.cwd())
HOME_PATH = str(Path.home())
DEFAULT_PATH = HOME_PATH + "/Pictures/CAMERA/camera_picture"


def countdown_timer(timer):
    for i in range(timer):
        last_time = timer - i
        print("{}...".format(last_time))
        sleep(1)


class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        # 初期の写真はカメラが起動してすぐは暗いので、捨てる
        for i in range(3):
            self.cap.read()

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def take(self, file_path):
        file_path += ".jpg"
        ret, im = self.cap.read()
        if ret == 0:
            print("[!] Miss...")
        else:
            print("[*] Success!")
            cv2.imwrite(file_path, im)
            print("Saved in {}".format(file_path))

    def continuous_shoot(self, file_path, number):
        for i in range(number):
            self.take(file_path + str(i))


def main():
    parser = argparse.ArgumentParser(description="Take a picture.")
    parser.add_argument('-n', '--file_path', metavar="file_path", action="store", help="picture's name",
                        default=DEFAULT_PATH)
    parser.add_argument('-c', '--continuous', action="store_true", help="continuous shooting", default=False)
    parser.add_argument('-t', '--timer', action="store", help="self timer", default=0)
    parser.add_argument('-v', '--version', action="version", version="Ver.0.0")

    args = parser.parse_args()

    # file path setting
    file_path = args.file_path
    if file_path != DEFAULT_PATH:
        file_path = CURRENT_PATH + '/' + file_path

    # camera init
    camera = Camera()

    # timer
    timer = int(args.timer)
    countdown_timer(timer)

    # take pictures
    if args.continuous:
        camera.continuous_shoot(file_path, 5)
    else:
        camera.take(file_path)

    # camera fin
    del camera


if __name__ == '__main__':
    main()
