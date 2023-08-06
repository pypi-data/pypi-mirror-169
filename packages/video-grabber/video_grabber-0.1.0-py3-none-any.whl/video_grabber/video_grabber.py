from ast import literal_eval
import logging
import time
from collections import deque
from queue import Empty
from threading import Lock, Thread
from time import sleep

import cv2
from .FPS import FPS
from .image_misc import cv_get_video_info, cv_show_images

from video_grabber import __version__

__author__ = "arcayi"
__copyright__ = "arcayi"
__license__ = "CC0-1.0"


class Queue(deque):
    def __init__(self, maxsize=128):
        super().__init__(maxlen=maxsize)
        self.is_full = False
        self.empty = True
        self.status_lock = Lock()

    def full(self):
        return self.is_full

    def put(self, item):
        # logging.debug("Put")
        with self.status_lock:
            while self.is_full:
                sleep(0.0001)
            self.appendleft(item)
            self.refresh()

    def get(self):
        # logging.debug("Get")
        with self.status_lock:
            item = self.pop()
            self.refresh()
        return item

    def refresh(self):
        # self.status_lock.acquire()
        self.empty = not self
        self.is_full = len(self) >= self.maxlen
        # logging.debug(f"{self.empty=}, {self.is_full=}")
        # self.status_lock.release()


class VideoGrabber:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

    def __init__(self, video_path=0, queue_size=128, simulate_fps=False):
        self.simulate_fps = simulate_fps
        self._fps = FPS()
        self.video_path = video_path
        # Check source
        # if isinstance(self.video_path, int) or is_int(self.video_path):
        if isinstance(self.video_path, int):
            self.video_path = int(self.video_path)
            self.source = "webcam"
        elif self.video_path.startswith("http") or self.video_path.startswith("rtsp"):
            self.source = "webcam"
        else:
            self.source = "video_file"

        # set status
        self.grabbed = False
        self.stopped = True
        self.read_lock = Lock()
        self.is_file = self.source == "video_file"
        if self.is_file:
            self.Q = Queue(maxsize=queue_size)
        self.open_stream()

    def start(self):
        # t = Thread(target=self.read_stream, args=())
        # t.daemon = True
        # t.start()
        self.thread = Thread(target=self.read_stream, args=())
        self.thread.daemon = True
        self.thread.start()
        return self

    def open_stream(self):
        # open stream and check
        # self.stream = cv2.VideoCapture(self.video_path)
        self.stream = cv2.VideoCapture(self.video_path, cv2.CAP_FFMPEG)
        # self.stream = cv2.VideoCapture(self.video_path, cv2.CAP_FFMPEG, (cv2.CAP_PROP_HW_ACCELERATION, cv2.VIDEO_ACCELERATION_ANY))
        if not self.stream.isOpened():
            # messagebox.showerror("Error", "Could not read from source: {}".format(self.video_path))
            logging.error("Could not read from source: {}".format(self.video_path))
            exit()

        # if self.is_file:
        #     self.fps = self.stream.get(cv2.CAP_PROP_FPS)
        #     self.spf = 1 / self.fps
        #     # todo: move to read stage
        #     self.last_frame_time = time.time()

        self.width, self.height, self.fps, self.nframes = cv_get_video_info(self.stream)
        self.spf = 1.0 / self.fps
        logging.debug(f"{self.width=}, {self.height=}, {self.fps=}, {self.nframes=}, {self.spf=}")
        if self.is_file:
            self.first_frame_time = self.last_frame_time = time.time()

        # set status
        self.grabbed = True
        self.stopped = False

    # def choose_new_file(self):
    #     file_path = filedialog.askopenfilename()
    #     if file_path != "":
    #         self.open_stream(file_path)

    # def open_camera(self):
    #     answer = simpledialog.askstring("Input", "Please input camera source. Put 0 for the default webcam.", parent=root,
    #         initialvalue="http://192.168.43.1:8080/video")
    #     if answer != "":
    #         self.open_stream(answer)

    def read_stream(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                # return  # if cam
                break  # if file

            if self.is_file:
                if not self.Q.full():
                    # read the next frame from the file
                    (grabbed, frame) = self.stream.read()
                    # grabbed = self.stream.grab()
                    # frame = []

                    # if the `grabbed` boolean is `False`, then we have
                    # reached the end of the video file
                    if not grabbed:
                        self.stopped = True
                    else:
                        self.Q.put(frame)

                else:
                    time.sleep(0.1)  # Rest for 10ms, we have a full queue
            else:
                (grabbed, frame) = self.stream.read()

            # self.read_lock.acquire()
            self.grabbed = grabbed
            self.frame = frame
            # self.read_lock.release()

        # while True:
        #     if self.stopped:
        #         time.sleep(1)
        #         continue
        #     frame = None
        #     grabbed = False
        #     if self.source == "video_file":
        #         if time.time() - self.last_frame_time > self.spf:
        #             grabbed, frame = self.stream.read()
        #             self.last_frame_time = time.time()
        #         else:
        #             continue
        #     else:
        #         grabbed, frame = self.stream.read()

        #     self.read_lock.acquire()
        #     self.grabbed = grabbed
        #     self.read_lock.release()
        #     if frame is not None:
        #         if self.max_width is not None:
        #             frame = imutils.resize(frame, width=self.max_width)
        #         self.read_lock.acquire()
        #         self.frame = frame
        #         self.read_lock.release()

    def get_frame(self):
        frame = None
        if self.is_file:
            if self.simulate_fps:
                # if time.time() - self.last_frame_time < self.spf:
                if time.time() - self.first_frame_time < self.spf * self._fps.nbf:
                    return None
                # self.last_frame_time = time.time()
            try:
                if not self.Q.empty:
                    frame = self.Q.get()
                else:
                    frame = None
                # frame = self.Q.get(False)
            except (Empty, IndexError):
                frame = None
            except BaseException:
                frame = None
        else:
            # self.read_lock.acquire()
            frame = self.frame.copy() if self.frame is not None else self.default_frame
            # self.read_lock.release()
        if frame is not None:
            self._fps.update()
        return frame

    def stop(self):
        # if file?
        self.stream.release()
        self.stopped = True
        self.thread.join()

    def has_frames(self):
        status = (not self.Q.empty) if self.is_file else (self.grabbed)
        return status

    def is_stopped(self):
        return self.stopped


def main(args):
    vg = VideoGrabber(video_path=args.video_source, simulate_fps=False)
    # start = perf_counter()
    # w, h, fps, nframes = cv_get_video_info(vg.stream)
    vg.start()
    fps = FPS()
    fps.update()
    # nframes_done = 0
    while True:
        if not vg.has_frames():
            if vg.stopped:
                break
            sleep(0.00001)
            continue
        frame = vg.get_frame()
        if frame is None:
            sleep(0.00001)
            continue
        # nframes_done += 1
        fps.update()

        if args.display:
            kvs = {"frame": frame}
            cv_show_images(kvs, args.draw_shape)

            key = cv2.pollKey()
            if key == ord("q") or key == 27:
                # is_break = True
                break
            elif key == 32:
                # Pause on space bar
                cv2.waitKey(0)
            elif key > 0:
                key = chr(key)
                logging.debug(f"{key=}")
                # if okv.toggle_by_key(key):
                #     logging.debug(f"{okv.kos[key]=},{okv.value_by_key(key)=}")
                #     if okv.kos[key] == "show_segmentation":
                #         bp_rt.postprocess_segmentation = okv.value_by_option("show_segmentation")
    # vg.thread.join()
    # end = perf_counter()
    global_fps, nb_frames = fps.get_global()
    logging.info(f"FPS : {global_fps:.1f} f/s (# frames = {nb_frames} @ {fps.timestamps[-1]-fps.start} s)")
    cv2.destroyAllWindows()
    vg.stop()


def draw_shape_t(str_input):
    try:
        t = literal_eval(str_input)
        if isinstance(t, tuple) and len(t) == 3:
            return t
        else:
            raise TypeError("should be (width, height)")
    except:
        raise TypeError("should be (width, height)")
    # return t


def run():
    import argparse

    parser = argparse.ArgumentParser(description="Just a video_grabber demonstration")
    parser.add_argument("-V", "--version", action="version", version="video_grabber {ver}".format(ver=__version__))
    parser.add_argument("-v", "--verbose", dest="loglevel", help="set loglevel to DEBUG", action="store_const", const=logging.DEBUG, default=logging.INFO)
    parser.add_argument(
        "-s", "--video_source", help="Video source, it may be camera id(0,1...), web camera URL(rtsp://, http://), or video file path.", required=True
    )
    parser.add_argument(
        "-d", "--display", action="store_true", default=False, help="Should frames be displayed, and how many kinds of informaion should be plotted"
    )
    parser.add_argument("--draw_shape", type=draw_shape_t, default=None, help="(width, height) to plot")
    args = parser.parse_args()

    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=args.loglevel, format=logformat, datefmt="%Y-%m-%d %H:%M:%S")

    main(args)


if __name__ == "__main__":
    run()
