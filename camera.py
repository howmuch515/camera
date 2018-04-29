import cv2, argparse

def main():
    parser = argparse.ArgumentParser(description="Take a picture.")
    parser.add_argument('file_name', metavar="FILE_NAME",
                        help="picture's name")
    parser.add_argument('-v', '--version', action="version", version="Ver.0.0")

    args = parser.parse_args()
    FILE_NAME = args.file_name

    # init
    FILE_PATH = "/tmp/" + FILE_NAME
    cap = cv2.VideoCapture(0)
    cap.read() # 1枚目は真っ暗な写真になるので捨てる

    # main
    ret, im = cap.read()
    if ret == 0:
        print("[!] Miss...")
    else:
        print("[*] Success!")
        cv2.imwrite(FILE_PATH, im)

    # fini
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
