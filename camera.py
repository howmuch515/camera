import cv2, argparse
from pathlib import Path

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


def main():
    parser = argparse.ArgumentParser(description="Take a picture.")
    parser.add_argument('-n', '--file_name', metavar="FILE_NAME", action="store", help="picture's name", default=DEFAULT_PATH)
    parser.add_argument('-c', '--continuous', action="store_true", help="continuous shooting", default=False)
    parser.add_argument('-v', '--version', action="version", version="Ver.0.0")

    args = parser.parse_args()

    # init
    FILE_NAME = args.file_name
    if FILE_NAME != DEFAULT_PATH:
        FILE_NAME = CURRENT_PATH + '/' + FILE_NAME

    b = args.continuous
    print("c -> {}".format(b))
    if args.continuous:
        continuous_shoot(FILE_NAME, 0x10)
    else:
        take(FILE_NAME)

if __name__ == '__main__':
    main()
