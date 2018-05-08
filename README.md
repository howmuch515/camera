# camera
## Description
This can take pictures with PC camera.  

## Require
- Python 3.6.5+
- OpenCV 3.4.0+

## Install
```
pip3 install git+https://github.com/howmuch515/camera
```

## Usage
### take a picture
```
# save as "image.jpg"
# if not set file_name, save as "$HOME/Pictures/CAMERA/camera_picture.jpg"
camera -n ./image
```

### continuous_shoot_mode
```
# take 5 pictures
camera -c
```
### self timer
```
# countdown 10
camera -t 10
```
