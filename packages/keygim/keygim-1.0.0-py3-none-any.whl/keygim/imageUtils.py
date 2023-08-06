import itertools
import pyautogui
import threading
import datetime
import skimage
import random
import pynput
import urllib
import numpy
import time
import copy
import cv2
import sys
import os
from keyscraper.utils import TimeName, FileName

class BasicUtils:
    def help():
        print("BasicUtils:")
        print("\t[1] verify_type(variable, typeList)")
        print("\t\t#returns variable if verified else raises an exception")
        print("\t[2] length_of(iterable)")
        print("\t\t#returns length if is iterable else 0")
        print("\t[3] verify_channels(channels, expected, operand = 0)")
        print("\t\t#operand(0, 1, 2) = (==, >=, <=)")
        print("\t[4] verify_tuples(tuple1, tuple2)")
        print("\t[5] verify_mode(mode, modeList)")
        print("\t[6] RandomObject")
        print("\t[7] verify_filename(filename, overwrite = True)")
        print("\t[8] verify_folder(folderName, create = False)")
        print("\t[9] format_length(string, length)")
        print("\t[10] char_padding(string, length, padding)")
        print("\t\t#length is integer")
        print("\t[11] countdown(seconds, verbose = False)")
        print("\t[12] MouseController")
        print("\t[a] NUMPY_IMAGE #numpy.ndarray")
        print("\t[b] PYNPUT_TYPE #list of pynput key types")
        print("")
    def verify_type(variable, typeList):
        if (any([ isinstance(variable,type) for type in typeList ])):
            return variable
        raise Exception(f"Type Error: expected type {typeList} but got [{type(variable)}]\n")
    def length_of(iterable):
        try: return len(iterable)
        except: return 0
    def verify_channels(channels, expected, operand = 0):
        if (((operand == 0) and (channels == expected)) or 
            ((operand == 1) and (channels >= expected)) or 
            ((operand == 2) and (channels <= expected))
        ): return channels
        elif (operand not in [ 0, 1, 2 ]):
            raise Exception(f"Operand Error: expected operand to be [ 0, 1, 2 ] but got {operand}\n")
        else:
            raise Exception(f"Channel Error: expected {expected} color channels but got {channels}\n")
    def verify_tuples(tuple1, tuple2):
        if (tuple1 == tuple2): return (tuple1, tuple2)
        raise Exception(f"Value Error: {tuple1} is not the same as {tuple2}\n")
    def verify_mode(mode, modeList):
        if (mode in modeList): return mode
        raise Exception(f"Value Error: expected mode {modeList} but got {mode}\n")
    class RandomObject:
        def help():
            print("BasicUtils.RandomObject:")
            print("\t[1] randint(start, end)")
            print("\t[2] uniform(start, end)")
            print("\t[3] shuffle(targetList)")
            print("")
        def randint(start, end):
            return numpy.random.randint(start, end + 1)
        def uniform(start, end):
            return numpy.random.uniform(start, end)
        def shuffle(targetList):
            numpy.random.shuffle(targetList)
    def verify_filename(filename, overwrite = True):
        (filename, overwrite) = (
            BasicUtils.verify_type(filename, [str]),
            BasicUtils.verify_type(overwrite, [bool,int])
        )
        if ((overwrite) or (not os.path.isfile(filename))):
            return filename
        __filename = FileName(filename)
        for index in itertools.count(start = 1):
            _filename = "".join([
                __filename["folder"], 
                __filename["name"],
                f" ({index})",
                __filename["extension"]
            ])
            if not (os.path.isfile(_filename)):
                return _filename
    def verify_folder(folderName, create = False):
        (folderName, create) = (
            BasicUtils.verify_type(folderName, [str]),
            BasicUtils.verify_type(create, [bool,int])
        )
        if ((create) and (not (os.path.exists(folderName)))):
            os.mkdir(folderName)
        return ((folderName) if (folderName[-1] == "/") else (folderName + "/"))
    def format_length(string, length):
        (string, length) = (
            BasicUtils.verify_type(string, [str]),
            max(0, BasicUtils.verify_type(length, [int]))
        )
        offset = length - len(string)
        if (offset >= 0):
            return string + " " * offset
        front = round(length / 2)
        return string[:front] + " ... " + string[front:]
    NUMPY_IMAGE = numpy.ndarray
    PYNPUT_TYPE = [type(pynput.keyboard.Key.esc),type(pynput.keyboard.KeyCode(char = 'a'))]
    def char_padding(string, length, padding = "-"):
        (string, length, padding) = (
            BasicUtils.verify_type(string, [str]),
            max(1, BasicUtils.verify_type(length, [int])),
            BasicUtils.verify_type(padding, [str])
        )
        paddingLen = length - len(string)
        if (paddingLen <= 0):
            return string
        return string + padding * paddingLen
    def countdown(seconds, verbose = False):
        (seconds, verbose) = (
            max(0, BasicUtils.verify_type(seconds, [float,int])),
            bool(BasicUtils.verify_type(verbose, [int,bool]))
        )
        sot = datetime.datetime.now()
        if (verbose):
            print("")
            _seconds = seconds
        while ((datetime.datetime.now() - sot).total_seconds() <= seconds):
            if (verbose):
                sys.stdout.write(f"\rStarting in {int(_seconds)} seconds...")
                sys.stdout.flush()
                _seconds = max(0, _seconds - 1)
            time.sleep(1)
        if (verbose):
            sys.stdout.write("\rStarted!                      ")
            sys.stdout.flush()
            print("")
    class MouseController:
        def help():
            print("BasicUtils.MouseController:")
            print("\t[1] move(x, y, t_ms = 1000)")
            print("\t[2] click(x, y, t = 0.25)")
            print("")
        def move(x, y, t_ms = 1000):
            t_ms = max(1, BasicUtils.verify_type(t_ms, [int,float]))
            cur_pos = pynput.mouse.Controller().position
            (dx, dy) = (
                numpy.linspace(cur_pos[0], x, t_ms).tolist(),
                numpy.linspace(cur_pos[1], y, t_ms).tolist()
            )
            for i, _ in enumerate(dx):
                pynput.mouse.Controller().position = (dx[i], dy[i])
                time.sleep(0.001)
        def click(x, y, t = 0.25):
            t = BasicUtils.verify_type(t, [float, int])
            BasicUtils.MouseController.move(x, y, round(t * 1000.0))
            time.sleep(0.5)
            pynput.mouse.Controller().press(pynput.mouse.Button.left)
            time.sleep(0.25)
            pynput.mouse.Controller().release(pynput.mouse.Button.left)
class ImageUtils:
    def help():
        print("ImageUtils:")
        print("\t[1] ImageLoader")
        print("\t[2] ImageSaver")
        print("\t[3] ImageDisplayer")
        print("\t[4] SnapshotTaker")
        print("\t[5] BoundaryBoxSelector")
        print("\t[6] ImageRandomCropper")
        print("\t[7] ImageOverLayer")
        print("\t[8] convert_color(imageList, color_code)")
        print("\t\t#converts list of images using cv2 color code")
        print("\t[9] ScreenshotCropperSaver")
        print("\t[10] ImageResizer")
        print("\t[11] ImageCorruptDisposer")
        print("")
    class __ImageBaseObject:
        COLOR_MODES   = [0,1,2,3,4,5]
        COLOR_GRAY_2D = COLOR_MODES[0]
        COLOR_GRAY_3D = COLOR_MODES[1]
        COLOR_BGR_3D  = COLOR_MODES[2]
        COLOR_BGRA_3D = COLOR_MODES[3]
        COLOR_RGB_3D  = COLOR_MODES[4]
        COLOR_RGBA_3D = COLOR_MODES[5]
    class ImageLoader(__ImageBaseObject):
        __COLOR_CONVERT = [
            cv2.COLOR_BGR2GRAY,
            cv2.COLOR_BGR2GRAY,
            None,
            cv2.COLOR_BGR2BGRA,
            cv2.COLOR_BGR2RGB,
            cv2.COLOR_BGR2RGBA
        ]
        def help():
            print("ImageUtils.ImageLoader:")
            print("\tavailable modes:")
            print("\t(1) ImageUtils.ImageLoader.COLOR_GRAY_2D")
            print("\t(2) ImageUtils.ImageLoader.COLOR_GRAY_3D")
            print("\t(3) ImageUtils.ImageLoader.COLOR_BGR_3D")
            print("\t(4) ImageUtils.ImageLoader.COLOR_BGRA_3D")
            print("\t(5) ImageUtils.ImageLoader.COLOR_RGB_3D")
            print("\t(6) ImageUtils.ImageLoader.COLOR_RGBA_3D")
            print("\t[1] __init__(self, filename, mode = 2) #BGR default")
            print("\t[2] load(self)")
            print("\t[3] load_images(nameList, mode = 2)")
            print("\t[4] load_images_from_folder(folderName, quantity = \"all\", shuffle = False)")
            print("")
        def __init__(self, filename, mode = 2):
            (self.filename, self.mode) = (
                BasicUtils.verify_type(filename, [str]),
                BasicUtils.verify_mode(BasicUtils.verify_type(mode, [int]), self.COLOR_MODES)
            )
        def load(self):
            image = cv2.imread(self.filename)
            if not (isinstance(image, BasicUtils.NUMPY_IMAGE)): 
                return None
            if (self.mode == self.COLOR_BGR_3D): 
                pass
            elif (self.mode == self.COLOR_GRAY_3D):
                image = numpy.expand_dims(
                    cv2.cvtColor(image, self.__COLOR_CONVERT[self.COLOR_GRAY_3D]),
                    axis = 2
                )
            else:
                image = cv2.cvtColor(image, self.__COLOR_CONVERT[self.mode])
            return image.astype("uint8") 
        def load_images(nameList, mode = 2):
            (nameList, mode) = (
                BasicUtils.verify_type(nameList, [list]),
                BasicUtils.verify_mode(BasicUtils.verify_type(mode, [int]), ImageUtils.ImageLoader.COLOR_MODES)
            )
            return [  
                image for image in [  ImageUtils.ImageLoader(name, mode).load() for name in nameList  ]
                    if (isinstance(image, BasicUtils.NUMPY_IMAGE))
            ]
        def load_images_from_folder(folderName, quantity = "all", shuffle = False):
            quantity = (1e18 if (quantity == "all") else max(1, BasicUtils.verify_type(quantity, [int])))
            shuffle = BasicUtils.verify_type(shuffle, [bool,int])
            fileList = [  folderName + name for name in os.listdir(folderName) if os.path.isfile(folderName + name)  ]
            if (len(fileList) == 0):
                raise Exception(f"List Error: expected a minimum of 1 image(s) but got {len(fileList)}\n")
            if (shuffle):
                BasicUtils.RandomObject.shuffle(fileList)
            return ImageUtils.ImageLoader.load_images(fileList[:quantity])
                
    class ImageSaver(__ImageBaseObject):
        __COLOR_CONVERT = [
            cv2.COLOR_GRAY2BGR,
            cv2.COLOR_GRAY2BGR,
            None,
            cv2.COLOR_BGRA2BGR,
            cv2.COLOR_RGB2BGR,
            cv2.COLOR_RGBA2BGR
        ]
        def help():
            print("ImageUtils.ImageSaver:")
            print("\tavailable modes:")
            print("\t(1) ImageUtils.ImageSaver.COLOR_GRAY_2D")
            print("\t(2) ImageUtils.ImageSaver.COLOR_GRAY_3D")
            print("\t(3) ImageUtils.ImageSaver.COLOR_BGR_3D")
            print("\t(4) ImageUtils.ImageSaver.COLOR_BGRA_3D")
            print("\t(5) ImageUtils.ImageSaver.COLOR_RGB_3D")
            print("\t(6) ImageUtils.ImageSaver.COLOR_RGBA_3D")
            print("\t[1] __init__(self, filename, mode = 2) #BGR default mode")
            print("\t[2] save_image(self, image, overwrite = True)")
            print("\t[3] save_images(self, imageList, overwrite = True)")
            print("\t[4] save_image_from_url(self, link, overwrite = True)")
            print("")
        def __init__(self, filename, mode = 2):
            (self.filename, self.mode) = (
                FileName(BasicUtils.verify_type(filename, [str])),
                BasicUtils.verify_mode(BasicUtils.verify_type(mode, [int]), self.COLOR_MODES)
            )
        def __save_image(self, image, filename):
            if (self.mode == self.COLOR_BGR_3D):
                pass
            elif (self.mode == self.COLOR_GRAY_3D):
                image = numpy.reshape((len(image), len(image[0])))
            else:
                image = cv2.cvtColor(image.astype(numpy.uint8), self.__COLOR_CONVERT[self.mode])
            cv2.imwrite(filename, image)
        def __save_image_from_url(self, link, filename):
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(link, filename)
        def save_image_from_url(self, link, overwrite = True):
            (link, overwrite) = (
                BasicUtils.verify_type(link, [str]),
                BasicUtils.verify_type(overwrite, [int,bool])
            )
            if ((overwrite) or (not os.path.isfile(self.filename["all"]))):
                self.__save_image_from_url(link, self.filename["all"])
            else:
                for i in itertools.count(start = 1):
                    __filename = self.filename["folder"] + self.filename["name"] + f" ({i})" + self.filename["extension"]
                    if not (os.path.isfile(__filename)):
                        self.__save_image_from_url(link, __filename)
                        break
        def save_image(self, image, overwrite = True):
            (image, overwrite) = (
                BasicUtils.verify_type(image, [BasicUtils.NUMPY_IMAGE]),
                BasicUtils.verify_type(overwrite, [int,bool])
            )
            if ((overwrite) or (not os.path.isfile(self.filename["all"]))):
                self.__save_image(image, self.filename["all"])
            else:
                for i in itertools.count(start = 1):
                    __filename = self.filename["folder"] + self.filename["name"] + f" ({i})" + self.filename["extension"]
                    if not (os.path.isfile(__filename)):
                        self.__save_image(image, __filename)
                        break
        def save_images(self, imageList, overwrite = True):
            (imageList, overwrite) = (
                BasicUtils.verify_type(imageList, [list,BasicUtils.NUMPY_IMAGE]),
                BasicUtils.verify_type(overwrite, [int,bool])
            )
            if (overwrite):
                for i, image in enumerate(imageList):
                    if (i):
                        __filename = self.filename["folder"] + self.filename["name"] + f" ({i})" + self.filename["extension"]
                        self.__save_image(image, __filename)
                    else:
                        self.__save_image(image, self.filename["all"])
            else:
                for image in imageList:
                    self.save_image(image, overwrite = False)
    class ImageDisplayer:
        __DISPLAY_QUANTUM = 0.05
        def help():
            print("ImageUtils.ImageDisplayer:")
            print("\t[1] __init__(self, image, windowName = \"Image Preview\")")
            print("\t\t#image must be of type numpy-BGR")
            print("\t[2] start(self)")
            print("\t[3] stop(self)")
            print("\t[4] display_for(self, interval = 5)")
            print("\t[5] display_multiple_for(imageList, windowName = \"Image Preview\", interval = 1)")
            print("")
        def __init__(self, image, windowName = "Image Preview"):
            (self.image, self.windowName) = (
                BasicUtils.verify_type(image, [BasicUtils.NUMPY_IMAGE]),
                BasicUtils.verify_type(windowName, [str])
            )
            (self.__display, self.__displayer) = (
                False, threading.Thread(target = self.__display_image)
            )
        def __display_image(self):
            cv2.namedWindow(self.windowName)
            while (self.__display):
                cv2.imshow(self.windowName, self.image.astype("uint8"))
                cv2.waitKey(1)
                time.sleep(self.__DISPLAY_QUANTUM)
            cv2.destroyWindow(self.windowName)
        def start(self):
            if not (self.__display):
                self.__display = True
                self.__displayer.start()
            return self
        def stop(self):
            if (self.__display):
                self.__display = False
                self.__displayer.join()
            return self
        def display_for(self, interval = 5):
            interval = max(0, BasicUtils.verify_type(interval, [int,float]))
            sot = datetime.datetime.now()
            cv2.namedWindow(self.windowName)
            while ((datetime.datetime.now() - sot).total_seconds() <= interval):
                cv2.imshow(self.windowName, self.image.astype("uint8"))
                cv2.waitKey(1)
                time.sleep(self.__DISPLAY_QUANTUM)
            cv2.destroyWindow(self.windowName)
        def display_multiple_for(imageList, windowName = "Image Preview", interval = 1):
            for image in imageList:
                ImageUtils.ImageDisplayer(image, windowName).display_for(interval)
    class SnapshotTaker(__ImageBaseObject):
        __KEY_QUANTUM = 0.1
        __COLOR_CONVERT = [
            cv2.COLOR_RGB2GRAY,
            cv2.COLOR_RGB2GRAY,
            cv2.COLOR_RGB2BGR,
            cv2.COLOR_RGB2BGRA,
            None,
            cv2.COLOR_RGB2RGBA
        ]
        def help():
            print("ImageUtils.SnapshotTaker:")
            print("\tavailable modes:")
            print("\t(1) ImageUtils.SnapshotTaker.COLOR_GRAY_2D")
            print("\t(2) ImageUtils.SnapshotTaker.COLOR_GRAY_3D")
            print("\t(3) ImageUtils.SnapshotTaker.COLOR_BGR_3D")
            print("\t(4) ImageUtils.SnapshotTaker.COLOR_BGRA_3D")
            print("\t(5) ImageUtils.SnapshotTaker.COLOR_RGB_3D")
            print("\t(6) ImageUtils.SnapshotTaker.COLOR_RGBA_3D")
            print("\t[1] __init__(self, mode = 2) #default mode BGR")
            print("\t[2] take_screenshot(self, key = none, message = None)")
            print("\t[3] take_screenshots(self, key = None, quantity = 1, message = None)")
            print("")
        def __init__(self, mode = 2):
            (self.key, self.__running, self.mode) = (
                None, False,
                BasicUtils.verify_mode(
                    BasicUtils.verify_type(mode, [int]), 
                    self.COLOR_MODES
                )
            )
        def __screenshot_listener(self, key):
            if (key == self.key):
                self.__running = False
        def __convert_color(self, image):
            image = numpy.array(image)
            if (self.mode != self.COLOR_RGB_3D):
                image = cv2.cvtColor(image.astype("uint8"), self.__COLOR_CONVERT[self.mode])
            if (self.mode == self.COLOR_GRAY_3D):
                image = numpy.expand_dims(image, axis = 2, dtype = numpy.uint8)
            return image
        def take_screenshot(self, key = None, message = None):
            if (key != None):
                (self.key, message) = (
                    BasicUtils.verify_type(key, BasicUtils.PYNPUT_TYPE),
                    BasicUtils.verify_type(message, [str,type(None)])
                )
                if (message != None):
                    print(message)
                self.__running = True
                listener = pynput.keyboard.Listener(on_press = self.__screenshot_listener)
                listener.start()
                while (self.__running):
                    time.sleep(self.__KEY_QUANTUM)
                listener.stop()
            return self.__convert_color(pyautogui.screenshot())
        def take_screenshots(self, key = None, quantity = 1, message = None):
            quantity = max(1, BasicUtils.verify_type(quantity, [int]))
            return numpy.stack([
                self.take_screenshot(key, message) for _ in range(quantity)        
            ])
    class BoundaryBoxSelector:
        def help():
            print("ImageUtils.BoundaryBoxSelector:")
            print("\t[1] BoundaryBox")
            print("\t[2] __init__(self, image, windowName = \"Boundary Box Selector\", \n\t\tboxColor = (255, 0, 0), boxWidth = 5)")
            print("\t[3] draw(self)")
            print("\t[4] place(self, width, height)")
            print("\t[5] draw_multiple(self, quantity = 1)")
            print("\t[6] place_multiple(self, width, height, quantity = 1)")
            print("\t[7] crop_partial(image, bbox)")
            print("\t[8] crop_multiple(image, bboxes)")
            print("")
        class BoundaryBox:
            def help():
                print("ImageUtils.BoundaryBoxSelector.BoundaryBox:")
                print("\t[1] __init__(self, SX = 0, SY = 0, EX = 1, EY = 1)")
                print("\t[2] modify(self, key, value)")
                print("\t\t#keys: \"SX\", \"SY\", \"EX\", \"EY\"")
                print("\t[3] __getitem__(self, key)")
                print("\t\t#keys: \"SX\", \"SY\", \"EX\", \"EY\", \"DX\", \"DY\"")
                print("\t[4] sort(self) #sorts boundary box")
                print("")
            def __init__(self, SX = 0, SY = 0, EX = 1, EY = 1):
                (SX, SY, EX, EY) = (
                    max(0, int(BasicUtils.verify_type(SX, [int,float]))),
                    max(0, int(BasicUtils.verify_type(SY, [int,float]))),
                    max(0, int(BasicUtils.verify_type(EX, [int,float]))),
                    max(0, int(BasicUtils.verify_type(EY, [int,float])))
                )
                self.boundaryBox = {
                    "sx" : SX, "sy" : SY, "ex" : EX, "ey" : EY        
                }
            def modify(self, key, value):
                if (isinstance(key,str)):
                    key = key.lower()
                    if (key in self.boundaryBox.keys()): self.boundaryBox[key] = max(0, int(BasicUtils.verify_type(value,[int,float])))
                else: 
                    raise Exception(f'Key Error: expected key from ["SX", "SY", "EX", "EY"] but got {key}')
            def __getitem__(self, key):
                if (isinstance(key, str)):
                    key = key.lower()
                    if (key in self.boundaryBox): return self.boundaryBox[key]
                    elif (key == "tuple"): return tuple(self.boundaryBox.values())
                    elif (key == "dx"): return abs(self.boundaryBox["ex"] - self.boundaryBox["sx"])
                    elif (key == "dy"): return abs(self.boundaryBox["ey"] - self.boundaryBox["sy"])
                    elif (key == "cx"): return round((self.boundaryBox["sx"] + self.boundaryBox["ex"]) / 2)
                    elif (key == "cy"): return round((self.boundaryBox["sy"] + self.boundaryBox["ey"]) / 2)
                else: 
                    raise Exception(f'Key Error: expected key from ["SX", "SY", "EX", "EY", "tuple", "DX", "DY", "CX", "CY"] but got {key}')
            def sort(self):
                (SX, SY, EX, EY) = (
                    min(self.boundaryBox["sx"], self.boundaryBox["ex"]),
                    min(self.boundaryBox["sy"], self.boundaryBox["ey"]),
                    max(self.boundaryBox["sx"], self.boundaryBox["ex"]),
                    max(self.boundaryBox["sy"], self.boundaryBox["ey"])
                )
                (self.boundaryBox["sx"], self.boundaryBox["sy"], self.boundaryBox["ex"], self.boundaryBox["ey"]) = (
                    SX, SY, EX, EY        
                )
        __SELECT_QUANTUM = 0.01
        def __init__(self, image, windowName = "Boundary Box Selector", boxColor = (255, 0, 0), boxWidth = 5):
            (self.image, self.windowName, self.boxColor, self.boxWidth) = (
                BasicUtils.verify_type(image, [BasicUtils.NUMPY_IMAGE]),
                BasicUtils.verify_type(windowName, [str]),
                BasicUtils.verify_type(boxColor, [tuple]),
                max(1, BasicUtils.verify_type(boxWidth, [int]))
            )
            (self.__window_open, self.__draw_begin, self.__boundaryBox) = (
                False, False, ImageUtils.BoundaryBoxSelector.BoundaryBox()
            )
            (self.rows, self.cols) = (
                BasicUtils.length_of(self.image), 
                BasicUtils.length_of(self.image[0])
            )
        def __draw_mouse_callback(self, event, x, y, *args, **kwargs):
            if (self.__window_open):
                if (event == cv2.EVENT_LBUTTONDOWN):
                    self.__boundaryBox.modify("SX", x) 
                    self.__boundaryBox.modify("SY", y) 
                    self.__draw_begin = True
                elif (event == cv2.EVENT_LBUTTONUP):
                    self.__boundaryBox.modify("EX", x) 
                    self.__boundaryBox.modify("EY", y) 
                    self.__draw_begin = False
                    self.__window_open = False
                elif (event == cv2.EVENT_MOUSEMOVE):
                    self.__boundaryBox.modify("EX", x)
                    self.__boundaryBox.modify("EY", y)
        def __place_mouse_callback(self, event, x, y, *args, **kwargs):
            if (self.__window_open):
                if (event == cv2.EVENT_LBUTTONDOWN):
                    pass
                elif (event == cv2.EVENT_LBUTTONUP):
                    self.__window_open = False
                elif (event == cv2.EVENT_MOUSEMOVE):
                    if (x <= self.__place_width_front):
                        self.__boundaryBox.modify("SX", 0)
                        self.__boundaryBox.modify("EX", self.__place_width)
                    elif (x >= (self.cols - self.__place_width_rear)):
                        self.__boundaryBox.modify("SX", (self.cols - self.__place_width))
                        self.__boundaryBox.modify("EX", self.cols)
                    else: 
                        self.__boundaryBox.modify("SX", (x - self.__place_width_front))
                        self.__boundaryBox.modify("EX", (x + self.__place_width_rear))
                    if (y <= self.__place_height_front):
                        self.__boundaryBox.modify("SY", 0)
                        self.__boundaryBox.modify("EY", self.__place_height)
                    elif (y >= (self.rows - self.__place_height_rear)):
                        self.__boundaryBox.modify("SY", (self.rows - self.__place_height))
                        self.__boundaryBox.modify("EY", self.rows)
                    else:
                        self.__boundaryBox.modify("SY", (y - self.__place_height_front))
                        self.__boundaryBox.modify("EY", (y + self.__place_height_rear))
        def draw(self):
            if not (self.__window_open):
                self.__window_open = True
                cv2.namedWindow(self.windowName)
                cv2.setMouseCallback(self.windowName, self.__draw_mouse_callback)
                while (self.__window_open):
                    if (self.__draw_begin):
                        (copyImage, bbox) = (self.image.copy(), self.__boundaryBox["tuple"])
                        cv2.rectangle(copyImage, (bbox[0], bbox[1]), (bbox[2], bbox[3]), self.boxColor, self.boxWidth)
                        cv2.imshow(self.windowName, copyImage)
                    else:
                        cv2.imshow(self.windowName, self.image)
                    cv2.waitKey(1)
                    time.sleep(self.__SELECT_QUANTUM)
                cv2.destroyWindow(self.windowName)
                self.__boundaryBox.sort()
                return copy.deepcopy(self.__boundaryBox)
        def draw_multiple(self, quantity = 1):
            quantity = max(1, BasicUtils.verify_type(quantity, [int]))
            return [
                self.draw() for _ in range(quantity)
            ]
        def place(self, width, height):
            if not (self.__window_open):
                (self.__place_width, self.__place_height) = (
                    max(1, int(BasicUtils.verify_type(width, [int,float]))),
                    max(1, int(BasicUtils.verify_type(height, [int,float])))
                )
                (self.__place_width_front, self.__place_height_front) = (
                    int(self.__place_width / 2), int(self.__place_height / 2)
                )
                (self.__place_width_rear, self.__place_height_rear) = (
                    (self.__place_width - self.__place_width_front),
                    (self.__place_height - self.__place_height_front)
                )
                self.__boundaryBox.modify("SX", 0)
                self.__boundaryBox.modify("SY", 0)
                self.__boundaryBox.modify("EX", self.__place_width)
                self.__boundaryBox.modify("EY", self.__place_height)
                self.__window_open = True
                cv2.namedWindow(self.windowName)
                cv2.setMouseCallback(self.windowName, self.__place_mouse_callback)
                while (self.__window_open):
                    (copyImage, bbox) = (self.image.copy(), self.__boundaryBox["tuple"])
                    (copyImage, bbox) = (self.image.copy(), self.__boundaryBox["tuple"])
                    cv2.rectangle(copyImage, (bbox[0], bbox[1]), (bbox[2], bbox[3]), self.boxColor, self.boxWidth)
                    cv2.imshow(self.windowName, copyImage)
                    cv2.waitKey(1)
                    time.sleep(self.__SELECT_QUANTUM)
                cv2.destroyWindow(self.windowName)
                return copy.deepcopy(self.__boundaryBox)
        def place_multiple(self, width, height, quantity = 1):
            quantity = max(1, BasicUtils.verify_type(quantity, [int]))
            return [
                self.place(width, height) for _ in range(quantity)
            ]
        def crop_partial(image, bbox):
            (image, bbox) = (
                copy.deepcopy(BasicUtils.verify_type(image, [BasicUtils.NUMPY_IMAGE])),
                BasicUtils.verify_type(bbox, [ImageUtils.BoundaryBoxSelector.BoundaryBox])
            )
            return image[
                bbox["sy"] : bbox["ey"], 
                bbox["sx"] : bbox["ex"]
            ]
        def crop_multiple(image, bboxes):
            (image, bboxes) = (
                BasicUtils.verify_type(image, [BasicUtils.NUMPY_IMAGE]),
                BasicUtils.verify_type(bboxes, [list])
            )
            return [
                ImageUtils.BoundaryBoxSelector.crop_partial(image, bbox) for bbox in bboxes
            ]
    class ImageRandomCropper:
        def help():
            print("ImageUtils.ImageRandomCropper:")
            print("\t[1] __init__(self, image)")
            print("\t[2] crop(self, width, height, overflow = True) #whether to allow overflow")
            print("\t\t#cropping fails if selected region exceeds boundary of master image")
            print("\t[3] crop_multiple(self, width, height, quantity = 1, overflow = True)")
            print("")
        def __init__(self, image):
            self.image = BasicUtils.verify_type(image, [BasicUtils.NUMPY_IMAGE])
            (self.rows, self.cols) = (
                BasicUtils.length_of(self.image), 
                BasicUtils.length_of(self.image[0])
            )
        def crop(self, width, height, overflow = True):
            (width, height, overflow) = (
                max(1, int(BasicUtils.verify_type(width, [int]))),
                max(1, int(BasicUtils.verify_type(height, [int]))),
                BasicUtils.verify_type(overflow, [int,bool])
            )
            if ((overflow == False) and ((width > self.cols) or (height > self.rows))):
                raise Exception("Value Error: width or height overflows from the image\n")
            (width_start, height_start) = ((self.cols - width), (self.rows - height))
            (width_start, height_start) = (
                BasicUtils.RandomObject.randint(0, width_start),
                BasicUtils.RandomObject.randint(0, height_start)
            )
            return self.image[
                height_start : height_start + height,
                width_start : width_start + width
            ]
        def crop_multiple(self, width, height, quantity = 1, overflow = True):
            quantity = max(1, BasicUtils.verify_type(quantity, [int]))
            return numpy.stack([
                self.crop(width, height, overflow) for _ in range(quantity)        
            ])
    class ImageOverLayer:
        def help():
            print("ImageUtils.ImageOverLayer:")
            print("\t[1] __init__(self, image) #image must be numpy-BGRA")
            print("\t[2] overlay(self, background)")
            print("\t\t#width and height of background and image must match")
            print("\t[3] overlay_multiple(self, backgroundList)")
            print("")
        def __init__(self, image):
            self.image = BasicUtils.verify_type(image, [BasicUtils.NUMPY_IMAGE])
            (self.rows, self.cols, self.channels) = (
                BasicUtils.length_of(self.image),
                BasicUtils.length_of(self.image[0]),
                BasicUtils.verify_channels(BasicUtils.length_of(self.image[0][0]), 4)
            )
        def overlay(self, background):
            (background, height, width) = (
                BasicUtils.verify_type(background, [BasicUtils.NUMPY_IMAGE]),
                BasicUtils.length_of(background),
                BasicUtils.length_of(background[0])
            )
            if ((height, width) != (self.rows, self.cols)):
                raise Exception("Length Error: width or height of background doesn't match with base image\n")
            overlayed = self.image.copy()
            overlayed[:,:,:3] = numpy.where(
                (self.image[:,:,3] == 255).repeat(3, axis = 1).reshape((height, width, 3)),
                self.image[:,:,:3], background[:,:,:3]
            )
            overlayed[:,:,3] = numpy.full((height, width), 255, dtype = "uint8")
            return overlayed
        def overlay_multiple(self, backgroundList):
            backgroundList = BasicUtils.verify_type(backgroundList, [list,BasicUtils.NUMPY_IMAGE])
            return numpy.stack([
                self.overlay(background) for background in backgroundList        
            ])
    def convert_color(imageList, color_code):
        (imageList, color_code) = (
            BasicUtils.verify_type(imageList, [list,BasicUtils.NUMPY_IMAGE]),
            BasicUtils.verify_type(color_code, [int])
        )
        return numpy.stack([
            cv2.cvtColor(image, color_code).astype("uint8") for image in imageList        
        ])
    class ScreenshotCropperSaver:
        def help():
            print("ImageUtils.ScreenshotCropperSaver:")
            print("\t[1] __init__(self, filename = \"temp.png\", draw = True, save = True)")
            print("\t\t#draw = True -> draw all ; draw = False -> draw one place rest")
            print("\t[2] start(self, key = None, message = None, overwrite = True, quantity = 1)")
            print("")
        def __init__(self, filename = "temp.png", draw = True, save = True):
            (self.filename, self.draw, self.save) = (
                BasicUtils.verify_type(filename, [str]),
                BasicUtils.verify_type(draw, [bool,int]),
                BasicUtils.verify_type(save, [bool,int])
            )
        def start(self, key = None, message = None, overwrite = True, quantity = 1):
            image = ImageUtils.SnapshotTaker(ImageUtils.SnapshotTaker.COLOR_BGR_3D).take_screenshot(key, message)
            if (self.draw):
                bboxes = ImageUtils.BoundaryBoxSelector(image).draw_multiple(quantity)
            else:
                bboxes = ImageUtils.BoundaryBoxSelector(image).draw_multiple(quantity = 1)
                if (quantity > 1):
                    bboxes += ImageUtils.BoundaryBoxSelector(image).place_multiple(bboxes[0]["dx"], bboxes[0]["dy"], quantity - 1)
            images = ImageUtils.BoundaryBoxSelector.crop_multiple(image, bboxes)
            if (self.save):
                ImageUtils.ImageSaver(self.filename).save_images(images, overwrite)
            return images
    class ImageResizer:
        def help():
            print("ImageUtils.ImageResizer:")
            print("\t[1] __init__(self, image)")
            print("\t[2] resize(self, width, height)")
            print("\t\t#retains aspect ratio via zero padding")
            print("\t[3] resize_multiple(imageList, width, height)")
            print("")
        def __init__(self, image):
            self.image = BasicUtils.verify_type(image, [BasicUtils.NUMPY_IMAGE])
            (self.width, self.height, self.channels) = (
                BasicUtils.length_of(self.image[0]),
                BasicUtils.length_of(self.image),
                BasicUtils.length_of(self.image[0][0])
            )
        def __get_shape(self, height, width):
            return ((height, width, self.channels) if (self.channels) else (height, width))
        def resize(self, width, height):
            (height, width) = (
                max(1, BasicUtils.verify_type(height, [int])),
                max(1, BasicUtils.verify_type(width, [int]))
            )
            newMinAxis = (0 if (height <= width) else 1)
            (resized_height, resized_width) = (
                (height) if (newMinAxis == 0) else round(self.height * width / self.width),
                (width) if (newMinAxis == 1) else round(self.width * height / self.height)
            )
            resized = cv2.resize(self.image, (resized_width, resized_height), interpolation = cv2.INTER_AREA)
            background = numpy.zeros(shape = self.__get_shape(height, width), dtype = numpy.uint8)
            (start_height, start_width) = (
                round(abs((height - resized_height) / 2)),
                round(abs((width - resized_width) / 2))
            )
            background[start_height : start_height + resized_height, start_width : start_width + resized_width] = resized
            return background
        def resize_multiple(imageList, width, height):
            imageList = BasicUtils.verify_type(imageList, [list,BasicUtils.NUMPY_IMAGE])
            return numpy.stack([
                ImageUtils.ImageResizer(image).resize(width, height) for image in imageList        
            ])
    class ImageCorruptDisposer:
        def help():
            print("ImageAugmentor.ImageCorruptDisposer:")
            print("\t[1] __init__(self, folderName)")
            print("\t[2] parse(self, return_quantity = False)")
            print("\t\t#return_quantity = False -> returns instance self")
            print("\t[3] dispose(self, extensions = \"all\")")
            print("\t\t#extensions must be list of strings (with .)")
            print("")
        def __init__(self, folderName):
            self.folderName = BasicUtils.verify_type(folderName, [str])
            (self.allImages, self.valids, self.invalids) = (None, None, None)
        def __isvalid(self, filename):
            try:
                image = skimage.io.imread(filename)
                if not (isinstance(image, BasicUtils.NUMPY_IMAGE)):
                    raise Exception("!")
                return True
            except:
                return False
        def parse(self, return_quantity = False):
            return_quantity = bool(BasicUtils.verify_type(return_quantity, [bool,int]))
            self.allImages = [  
                (self.folderName + name) for name in os.listdir(self.folderName) \
                    if os.path.isfile(self.folderName + name)  
            ]
            (self.valids, self.invalids) = [], []
            for filename in self.allImages:
                if (self.__isvalid(filename)):
                    self.valids.append(filename)
                else:
                    self.invalids.append(filename)
            return ((len(self.valids), len(self.invalids)) if (return_quantity) else self)
        def dispose(self, extensions = "all"):
            extensions = None if (extensions == "all") else (
                BasicUtils.verify_type(extensions, [list])
            )
            counter = 0
            for filename in self.invalids:
                _filename = FileName(filename)
                if ((extensions == None) or (_filename["extension"] in extensions)):
                    os.remove(filename)
                    counter += 1
            return counter
            
class ImageAugmentor:
    def help():
        print("ImageAugmentor:")
        print("\t[1] PlainImageGenerator")
        print("\t[2] NoiseImageGenerator")
        print("\t[3] MapGenerator")
        print("\t[4] PositionShifter")
        print("\t[5] BrightnessShifter")
        print("\t[6] ImageZoomer")
        print("\t[7] ImageGenerator")
        print("")
    class __ImageBaseObject:
        def __init__(self, width, height, channels):
            (self.width, self.height, self.channels) = (
                max(1, BasicUtils.verify_type(width, [int])),
                max(1, BasicUtils.verify_type(height, [int])),
                max(0, BasicUtils.verify_type(channels, [int]))
            )
            self.channels_3D = True
            if (self.channels == 0):
                self.channels_3D = False
                self.channels = 1
        def format_grayscale(self, image):
            return (image if (self.channels_3D) else image.reshape((self.height, self.width)))                
    class PlainImageGenerator(__ImageBaseObject):
        def help():
            print("ImageAugmentor.PlainImageGenerator:")
            print("\t[1] __init__(self, width, height, channels)")
            print("\t[2] generate(self, quantity = 1)")
            print("")
        def __init__(self, width, height, channels):
            super(ImageAugmentor.PlainImageGenerator, self).__init__(width, height, channels)
        def __generate_pixel(self):
            return numpy.random.randint(0, 256, self.channels)
        def __generate_frame(self):
            return self.__generate_pixel().reshape((1, self.channels)).repeat(self.width, axis = 0).reshape((1, self.width, self.channels)).repeat(self.height, axis = 0)
        def generate(self, quantity = 1):
            quantity = max(1, BasicUtils.verify_type(quantity, [int]))
            return (
                self.format_grayscale(self.__generate_frame()).astype("uint8") if (quantity == 1) else \
                    numpy.stack([
                        self.format_grayscale(self.__generate_frame()).astype("uint8") for _ in range(quantity)        
                    ])
            )   
    class NoiseImageGenerator(__ImageBaseObject):
        def help():
            print("ImageAugmentor.NoiseImageGenerator:")
            print("\t[1] __init__(self, width, height, channels)")
            print("\t[2] generate(self, quantity = 1)")
            print("")
        def __init__(self, width, height, channels):
            super(ImageAugmentor.NoiseImageGenerator, self).__init__(width, height, channels)
        def __generate_frame(self):
            return numpy.random.randint(0, 256, (self.height, self.width, self.channels))
        def generate(self, quantity = 1):
            quantity = max(1, BasicUtils.verify_type(quantity, [int]))
            return (
                self.format_grayscale(self.__generate_frame()).astype("uint8") if (quantity == 1) else \
                    numpy.stack([
                        self.format_grayscale(self.__generate_frame()).astype("uint8") for _ in range(quantity)        
                    ])
            ) 
    class MapGenerator:
        def help():
            print("ImageAugmentor.MapGenerator:")
            print("\t[1] __init__(self, image1, image2)")
            print("\t[2] get(self)")
            print("")
        def __init__(self, image1, image2):
            (self.image1, self.image2) = (
                BasicUtils.verify_type(image1, [BasicUtils.NUMPY_IMAGE]),
                BasicUtils.verify_type(image2, [BasicUtils.NUMPY_IMAGE])
            )
            (self.rows, self.cols, self.channels) = (
                BasicUtils.length_of(self.image1),
                BasicUtils.length_of(self.image1[0]),
                BasicUtils.verify_channels(
                    BasicUtils.verify_channels(BasicUtils.length_of(self.image1[0][0]), 3, operand = 1),
                    4, operand = 2
                )
            )
            (rows, cols, channels) = (
                BasicUtils.length_of(self.image2),
                BasicUtils.length_of(self.image2[0]),
                BasicUtils.verify_channels(
                    BasicUtils.verify_channels(BasicUtils.length_of(self.image2[0][0]), 3, operand = 1),
                    4, operand = 2
                )
            )
            BasicUtils.verify_tuples((self.rows, self.cols, self.channels), (rows, cols, channels))
        def get(self):
            image = self.image1.copy()
            if (self.channels != 4):
                image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
            reference = (self.image1[:,:,:3] == self.image2[:,:,:3]).all(axis = 2)
            image[:,:,3] = numpy.where(
                reference, 
                numpy.full((self.rows, self.cols), 255, dtype = numpy.uint8),
                numpy.zeros(shape = (self.rows, self.cols), dtype = numpy.uint8)
            )
            return image
    class PositionShifter:
        def help():
            print("ImageAugmentor.PositionShifter:")
            print("\t[1] __init__(self, image, safeMode = True)")
            print("\t\t#disabling safe mode may be faster but less safe")
            print("\t[2] shift(self, width_offset_range, height_offset_range, quantity = 1, rate = 1)")
            print("\t\t#rate = 1 -> always augment ; rate = 0 -> never augment")
            print("")
        def __init__(self, image, safeMode = True):
            self.safeMode = bool(BasicUtils.verify_type(safeMode, [bool,int]))
            self.image = (
                BasicUtils.verify_type(image, [BasicUtils.NUMPY_IMAGE]) \
                    if (self.safeMode) else image        
            )
            (self.rows, self.cols, self.channels) = (
                BasicUtils.length_of(self.image), 
                BasicUtils.length_of(self.image[0]),
                BasicUtils.verify_channels(BasicUtils.length_of(self.image[0][0]), 4, operand = 0)
            )
        def __neg_pos(self, number, boolean):
            return (number if (boolean) else -1)
        def __zero_pos(self, number, boolean):
            return (number * boolean)
        def __shift(self, width_offset, height_offset):
            (void_width, void_height) = (
                numpy.zeros(shape = (self.rows, abs(width_offset), self.channels), dtype = numpy.uint8),
                numpy.zeros(shape = (abs(height_offset), self.cols + abs(width_offset), self.channels), dtype = numpy.uint8)
            )
            (width_negative, height_negative) = (width_offset < 0, height_offset < 0)
            width = [  void_width, self.image  ]
            image = numpy.concatenate((width[width_negative], width[1 - width_negative]), axis = 1)
            height = [  void_height, image  ]
            image = numpy.concatenate((height[height_negative], height[1 - height_negative]), axis = 0)
            return image[
                self.__zero_pos(abs(height_offset) - 1, height_negative) : self.__neg_pos(self.rows, not height_negative),
                self.__zero_pos(abs(width_offset) - 1, width_negative) : self.__neg_pos(self.cols, not width_negative)
            ]
        def shift(self, width_offset_range, height_offset_range, quantity = 1, rate = 1):
            (width_offset_range, height_offset_range, quantity, rate) = (
                BasicUtils.verify_type(width_offset_range, [tuple]),
                BasicUtils.verify_type(height_offset_range, [tuple]),
                max(1, BasicUtils.verify_type(quantity, [int])),
                min(1, max(0, BasicUtils.verify_type(rate, [int,float])))
            )  if (self.safeMode) else (
                width_offset_range, height_offset_range, quantity, rate        
            )
            return (
                (
                    self.__shift(
                        BasicUtils.RandomObject.randint(width_offset_range[0], width_offset_range[1]),
                        BasicUtils.RandomObject.randint(width_offset_range[0], width_offset_range[1])
                    )  if (BasicUtils.RandomObject.uniform(0, 1) <= rate) else (self.image.copy())
                )  if (quantity == 1) else numpy.stack([
                    (
                        self.__shift(
                            BasicUtils.RandomObject.randint(width_offset_range[0], width_offset_range[1]),
                            BasicUtils.RandomObject.randint(width_offset_range[0], width_offset_range[1])
                        )  if (BasicUtils.RandomObject.uniform(0, 1) <= rate) else (self.image.copy()) 
                    )  for _ in range(quantity)
                ])
            )        
    class BrightnessShifter:
        def help():
            print("ImageAugmentor.BrightnessShifter:")
            print("\t[1] __init__(self, image, safeMode = True)")
            print("\t\t#disabling safe mode may be faster but less safe")
            print("\t[2] shift(self, brightness_shift_range, quantity = 1, rate = 1)")
            print("\t\t#rate = 1 -> always augment ; rate = 0 -> never augment")
            print("")
        def __init__(self, image, safeMode = True):
            self.safeMode = bool(BasicUtils.verify_type(safeMode, [bool,int]))
            self.image = (
                BasicUtils.verify_type(image, [BasicUtils.NUMPY_IMAGE]) \
                    if (self.safeMode) else image
            )
            (self.rows, self.cols, self.channels) = (
                BasicUtils.length_of(self.image),
                BasicUtils.length_of(self.image[0]),
                BasicUtils.length_of(self.image[0][0])
            )
        def __random_brightness(self, brightness_shift_range):
            return min(1, max(0, BasicUtils.RandomObject.uniform(brightness_shift_range[0], brightness_shift_range[1])))
        def __modify_brightness(self, image, brightness):
            image = image.copy()
            if (self.channels == 4):
                image[:,:,:3] = image[:,:,:3] * brightness
            else:
                image = image * brightness
            return image
        def __modify_image(self, brightness_weight, rate):
            return (
                self.__modify_brightness(self.image, brightness_weight).astype("uint8") \
                    if (BasicUtils.RandomObject.uniform(0, 1) <= rate) else self.image.copy()
            )
        def shift(self, brightness_shift_range, quantity = 1, rate = 1):
            (brightness_shift_range, quantity, rate) = (
                BasicUtils.verify_type(brightness_shift_range, [tuple]),
                max(1, BasicUtils.verify_type(quantity, [int])),
                min(1, max(0, BasicUtils.verify_type(rate, [int,float])))
            ) if (self.safeMode) else (
                brightness_shift_range, quantity, rate        
            )
            return (
                self.__modify_image(self.__random_brightness(brightness_shift_range), rate) if (quantity == 1) else (
                    numpy.stack([
                        self.__modify_image(self.__random_brightness(brightness_shift_range), rate) for _ in range(quantity)        
                    ])        
                )
            )      
    class ImageZoomer:
        def help():
            print("ImageAugmentor.ImageZoomer:")
            print("\t[1] __init__(self, image, safeMode = True)")
            print("\t\t#disabling safe mode may be faster but less safe")
            print("\t[2] zoom(self, zoom_value)")
            print("\t\t#(0, 1) -> zoom out ; (1, inf) -> zoom in")
            print("\t[3] random_zoom(self, zoom_range, quantity = 1, rate = 1)")
            print("\t\t#rate = 1 -> always augment ; rate = 0 -> never augment")
            print("")
        def __init__(self, image, safeMode = True):
            self.safeMode = bool(BasicUtils.verify_type(safeMode, [int,bool]))
            self.image = (
                BasicUtils.verify_type(image, [BasicUtils.NUMPY_IMAGE]) 
                    if (safeMode) else image
            )
            (self.rows, self.cols, self.channels) = (
                BasicUtils.length_of(self.image),
                BasicUtils.length_of(self.image[0]),
                BasicUtils.length_of(self.image[0][0])
            )
        def zoom(self, zoom_value):
            if (self.safeMode):
                zoom_value = max(0, BasicUtils.verify_type(zoom_value, [float,int]))
            (new_height, new_width) = (
                round(self.rows * zoom_value), 
                round(self.cols * zoom_value)
            )
            resized = cv2.resize(self.image, (new_width, new_height), interpolation = cv2.INTER_AREA)
            (height_start, width_start) = (
                round(abs(new_height - self.rows) / 2.0), 
                round(abs(new_width - self.cols) / 2.0)
            )
            if (zoom_value >= 1):
                resized = resized[  height_start : height_start + self.rows, width_start : width_start + self.cols  ]
            else:
                void = numpy.zeros(shape = (self.rows, self.cols, self.channels), dtype = numpy.uint8)
                void[  height_start : height_start + new_height, width_start : width_start + new_width  ] = resized
                resized = void
            return resized
        def __get_zoom(self, zoom_range, rate):
            return (
                self.zoom(BasicUtils.RandomObject.uniform(zoom_range[0], zoom_range[1])) \
                   if (BasicUtils.RandomObject.uniform(0, 1) <= rate) else self.image.copy()
            )
        def random_zoom(self, zoom_range, quantity = 1, rate = 1):
            (zoom_range, quantity, rate) = (
                BasicUtils.verify_type(zoom_range, [tuple]),
                max(1, BasicUtils.verify_type(quantity, [int])),
                min(1, max(0, BasicUtils.verify_type(rate, [int,float])))
            )  if (self.safeMode) else (
                zoom_range, quantity, rate        
            )
            return (
                self.__get_zoom(zoom_range, rate) if (quantity == 1) else numpy.stack([
                    self.__get_zoom(zoom_range, rate) for _ in range(quantity)
                ])
            )
    class ImageGenerator:
        class ImageGenerator:
            def help():
                print("ImageAugmentor.ImageGenerator:")
                print("\t[1] __init__(self, image1, image2)")
                print("\t[2] configure(self, **kwargs)")
                print("\t\tparameters:")
                print("\t\t(1)  \"position_shift_range\"")
                print("\t\t(2)  \"zoom_range\"")
                print("\t\t(3)  \"brightness_range\"")
                print("\t\t(4)  \"position_shift_rate\"")
                print("\t\t(5)  \"brightness_rate\"")
                print("\t\t(6)  \"zoom_rate\"")
                print("\t\t(7)  \"plain_quantity\"")
                print("\t\t(8)  \"noise_quantity\"")
                print("\t\t(9)  \"background_quantity\"")
                print("\t\t(10) \"region_quantity\"")
                print("\t\t(11) \"background_folder\"")
                print("\t[3] generate(self)")
                print("")
            def __init__(self, image1, image2, safeMode = True):
                self.safeMode = bool(BasicUtils.verify_type(safeMode, [bool,int]))
                (self.image1, self.image2) = (
                    BasicUtils.verify_type(image1, [BasicUtils.NUMPY_IMAGE]),
                    BasicUtils.verify_type(image2, [BasicUtils.NUMPY_IMAGE])
                )  if (self.safeMode) else (image1, image2)
                self.mapImage = ImageAugmentor.MapGenerator(self.image1, self.image2).get()
                (self.rows, self.cols, self.channels) = (
                    BasicUtils.length_of(self.image1),
                    BasicUtils.length_of(self.image1[0]),
                    BasicUtils.verify_channels(BasicUtils.length_of(self.image1[0][0]), 3)
                )
                self.parameters = {
                    "position_shift_range" : ((-1, 1), (-1, 1)),
                    "zoom_range" : (1.0, 1.0),
                    "brightness_range" : (1.0, 1.0),
                    "position_shift_rate" : 1,
                    "brightness_rate" : 1,
                    "zoom_rate" : 1,
                    "plain_quantity" : 1,
                    "noise_quantity" : 0,
                    "background_quantity" : 1,
                    "region_quantity" : 0,
                    "background_folder" : None
                }
            def __modify(self, key, value, verbose):
                if (key[-5:] == "range"):
                    self.parameters[key] = BasicUtils.verify_type(value, [tuple])
                elif ((key[:3] == "num") or (key[-8:] == "quantity")):
                    self.parameters[key] = max(0, BasicUtils.verify_type(value, [int]))
                elif (key[-4:] == "rate"):
                    self.parameters[key] = min(1, max(0, BasicUtils.verify_type(value, [int,float])))
                elif (key == "background_folder"):
                    self.parameters[key] = BasicUtils.verify_type(value, [str])
                elif (verbose):
                    print(f"Warning: {value} is an invalid value for key {key}.\n")
            def configure(self, verbose, **kwargs):
                keys = list(self.parameters.keys())
                for key, value in kwargs.items():
                    if (isinstance(key, str)):
                        key = key.lower()
                        if (key in keys):
                            self.__modify(key, value, verbose)
                        elif (verbose):
                            print(f"Warning: {key} is an invalid key.\n")
                    elif (verbose):
                        print(f"Warning: {key} is not a string key.\n")
            def print_parameters(self):
                maxKeyLength = max([  len(x) for x in list(self.parameters.keys())  ])
                print("===============================================")
                print("Parameters: ")
                for key, value in self.parameters.items():
                    print(f"{BasicUtils.format_length(key, maxKeyLength)} : {value}")
                print("===============================================")
                print("")
            def generate_backgrounds(self, verbose, safeMode, debug = False):
                if (debug):
                    print("===============================================")
                    print("Before Backgrounds Generation:")
                    print("===============================================")
                backgrounds = []
                if (self.parameters["plain_quantity"] > 1):
                    backgrounds = ImageAugmentor.PlainImageGenerator(self.cols, self.rows, self.channels).generate(
                        quantity = self.parameters["plain_quantity"]
                    )
                elif (self.parameters["plain_quantity"] > 0):
                    backgrounds = numpy.stack([
                        ImageAugmentor.PlainImageGenerator(self.cols, self.rows, self.channels).generate(
                            quantity = self.parameters["plain_quantity"]
                        )
                    ])
                if (self.parameters["noise_quantity"] > 1):
                    __backgrounds = ImageAugmentor.NoiseImageGenerator(self.cols, self.rows, self.channels).generate(
                        quantity = self.parameters["noise_quantity"]        
                    )
                    backgrounds = numpy.stack([
                        *[background for background in backgrounds],
                        *[_background for _background in __backgrounds]
                    ])
                elif (self.parameters["noise_quantity"] > 0):
                    __backgrounds = numpy.stack([
                        ImageAugmentor.NoiseImageGenerator(self.cols, self.rows, self.channels).generate(
                            quantity = self.parameters["noise_quantity"]        
                        )
                    ])
                    backgrounds = numpy.stack([
                        *[background for background in backgrounds],
                        *[_background for _background in __backgrounds]
                    ])
                if (self.parameters["background_folder"] != None):
                    __backgrounds = numpy.concatenate(tuple([
                        ImageUtils.ImageRandomCropper(image).crop_multiple(self.cols, self.rows, self.parameters["region_quantity"]) \
                            for image in ImageUtils.ImageLoader.load_images_from_folder(
                                self.parameters["background_folder"], shuffle = True,
                                quantity = self.parameters["background_quantity"]
                            )
                    ]))
                    backgrounds = numpy.stack([
                        *[background for background in backgrounds],
                        *[_background for _background in __backgrounds]
                    ])
                if (debug):
                    print("===============================================")
                    print("After Backgrounds Generation:")
                    print("===============================================")
                if ((verbose) and (not debug)):
                    print(f"Generated {len(backgrounds)} negative image data.")
                return backgrounds
            def generate(self, verbose, safeMode, debug = False, return_backgrounds = False):
                backgrounds = self.generate_backgrounds(verbose, safeMode, debug)
                num_backgrounds = BasicUtils.length_of(backgrounds)
                if (num_backgrounds < 1):
                    raise Exception(f"Quantity Error: expected a minimum of 1 background image(s) but found {num_backgrounds}.\n")
                elif (debug):
                    print("===============================================")
                    print(f"Background Quantity: { num_backgrounds }")
                    print("===============================================")
                images = numpy.stack([  copy.deepcopy(self.mapImage) for _ in range(num_backgrounds)  ])
                if (self.parameters["zoom_rate"] > 1e-4):
                    images = numpy.stack([
                        ImageAugmentor.ImageZoomer(image, safeMode = safeMode).random_zoom(
                            self.parameters["zoom_range"],
                            quantity = 1,
                            rate = self.parameters["zoom_rate"]
                        )  for image in images
                    ])
                if (self.parameters["position_shift_rate"] > 1e-4):
                    images = numpy.stack([
                        ImageAugmentor.PositionShifter(image, safeMode = safeMode).shift(
                            self.parameters["position_shift_range"][0],
                            self.parameters["position_shift_range"][1],
                            quantity = 1,
                            rate = self.parameters["position_shift_rate"]
                        ) for image in images
                    ])
                if (debug):                    
                    print("===============================================")
                    print("Before Overlaying:")
                    print(f"\tImages Shape: { images.shape }")
                    print(f"\tBackgrounds Shape: { backgrounds.shape }")
                    print("===============================================")
                images = numpy.stack([  
                    ImageUtils.ImageOverLayer(images[index]).overlay(backgrounds[index]) \
                        for index in range(len(images)) 
                ])
                if (debug):
                    print("===============================================")
                    print("After Overlaying:")
                    print(f"\tImages Shape: { images.shape }")
                    print("===============================================")
                if (self.parameters["brightness_rate"] > 1e-4):
                    images = numpy.stack([
                        ImageAugmentor.BrightnessShifter(image, safeMode = safeMode).shift(
                            self.parameters["brightness_range"],
                            quantity = 1,
                            rate = self.parameters["brightness_rate"]
                        )  for image in images
                    ])
                if (debug):
                    print("===============================================")
                    print("After Brightness Adjustment:")
                    print(f"\tImages Shape: { images.shape }")
                    print("===============================================")
                    print("Pausing for 5 Seconds...")
                    SOT = datetime.datetime.now()
                    while ((datetime.datetime.now() - SOT).total_seconds() < 5): time.sleep(0.5)
                    print("===============================================")
                    print("===============================================")
                    print("")
                if ((verbose) and (not debug)):
                    print(f"Generated {len(images)} positive image data.")
                images = ImageUtils.convert_color(images, cv2.COLOR_BGRA2BGR)
                return ((images, backgrounds) if (return_backgrounds) else images)
        def help():
            print("ImageAugmentor.ImageGenerator:")
            print("\t[1] __init__(self, image1, image2)")
            print("\t[2] configure(self, verbose = True, **kwargs)")
            print("\t[3] generate(self, return_backgrounds = False, verbose = True)")
            print("\t[4] summary(self)")
            print("\t[5] generate_backgrounds(self, verbose = True)")
            print("\t[6] ImageGenerator")
            print("")
        def __init__(self, image1, image2):
            self.generator = ImageAugmentor.ImageGenerator.ImageGenerator(image1, image2) 
        def configure(self, verbose = True, **kwargs):
            self.generator.configure(verbose = verbose, **kwargs)
        def summary(self):
            self.generator.print_parameters()
        def generate(self, return_backgrounds = False, verbose = True):
            return self.generator.generate(
                verbose = verbose, safeMode = True, debug = False, 
                return_backgrounds = return_backgrounds
            )
        def generate_backgrounds(self, verbose = True):
            return self.generator.generate_backgrounds(verbose = verbose, safeMode = False, debug = False)
            
if (__name__ == "__main__"):
    """
    folderName = "./background_templates/"
    imageDisposer = ImageUtils.ImageCorruptDisposer(folderName)
    num_valids, num_invalids = imageDisposer.parse(True)
    print(f"Valid: {num_valids}, Invalid: {num_invalids}\n")
    for index, filename in enumerate(imageDisposer.invalids):
        print(f"({index + 1}): {filename}")
    numDisposed = imageDisposer.dispose()
    print("Disposed: {} images".format(numDisposed))
    """