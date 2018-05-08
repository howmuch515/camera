import cv2, argparse
from pathlib import Path

CURRENT_PATH = str(Path.cwd())
HOME_PATH = str(Path.home())
DEFAULT_PATH = HOME_PATH + "/Pictures/CAMERA/camera_picture.jpg"

def main():
    parser = argparse.ArgumentParser(description="Take a picture.")
    parser.add_argument('-n', '--file_name', metavar="FILE_NAME", action="store", help="picture's name", default=DEFAULT_PATH)
    parser.add_argument('-v', '--version', action="version", version="Ver.0.0")

    args = parser.parse_args()

    # init
    FILE_NAME = args.file_name
    if FILE_NAME != DEFAULT_PATH:
        FILE_NAME = CURRENT_PATH + '/' + FILE_NAME + ".jpg"

    cap = cv2.VideoCapture(0)
    for i in range(3):
        cap.read() # 初期の写真はカメラが起動して間もないため暗いので、捨てる

    # main
    ret, im = cap.read()
    if ret == 0:
        print("[!] Miss...")
    else:
        print("[*] Success!")
        cv2.imwrite(FILE_NAME, im)
        print("Saved in {}".format(FILE_NAME))

    # fini
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
