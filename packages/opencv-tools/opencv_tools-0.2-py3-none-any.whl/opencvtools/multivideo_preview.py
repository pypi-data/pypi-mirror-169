import logging
from time import sleep

import cv2
import numpy as np

from sync import ts_s
from temp_utils import ImageMaker
from utils.general import threaded


class VideoPreview:
    def __init__(self, yolo, cams):
        LOGGER.info('init')
        self.yolo = yolo
        self.cams = cams

        self.cam_ids = []
        self.positions = []
        self.frame_res = (1080, 1920)

        self.fullscreen = False

    def update_layout(self, cam_ids, layout=None):
        LOGGER.info('update layout')
        if layout is None:
            n = int(np.ceil(np.sqrt(len(cam_ids))))
            layout = [n] * (n - 1) + [len(cam_ids) - n * (n - 1)]
        self.cam_ids = cam_ids

        # TODO: kamer layout lepszy

        # 1. grid
        self.positions = [[j, i, 1, 1] for j, row in enumerate(layout) for i in range(row)]

        # 2. scale each cam
        self.positions = [[x * 1.778, y, w * 1.778, h] for (x, y, w, h) in self.positions]

        # 3. center rows

        # 4. scale whole
        w = max([pos[0] + pos[2] for pos in self.positions])
        h = max([pos[1] + pos[3] for pos in self.positions])
        scale = min(self.frame_res[0] / h, self.frame_res[1] / w)

        self.positions = [[scale * p for p in pts] for pts in self.positions]

        # 5. enlarge to margins

        self.positions = [[int(p) for p in pts] for pts in self.positions]

    @threaded
    def play(self, window_name="Video", framerate=60):
        LOGGER.info("playing")
        delay = 1 / framerate
        cv2.namedWindow(window_name, cv2.WINDOW_KEEPRATIO)
        while True:
            start = ts_s()

            cv2.imshow(window_name, self._construct_frame())
            key = cv2.waitKey(1) & 0x7F
            if key == ord('q'):
                LOGGER.info("quit playing")
                break

            if key == ord('f'):
                LOGGER.info("toggle fullscreen")
                cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                                      cv2.WINDOW_FULLSCREEN if not self.fullscreen else cv2.WINDOW_NORMAL)
                self.fullscreen = not self.fullscreen

            sleep(max(start + delay - ts_s(), 0))

    def _construct_frame(self):
        frame = np.zeros(shape=(*self.frame_res, 3), dtype=np.uint8)
        for pos, cam_id in zip(self.positions, self.cam_ids):
            x, y, w, h = pos

            dets = self.cams[cam_id].get_last()
            img = self.yolo.frames[cam_id]
            if img is not None and img != []:
                im = ImageMaker(self.yolo.frames[cam_id].copy())
                im.resize(w, h).draw_3_part_boxes(*dets)
                frame[y:y + h, x:x + w] = im.get()
            else:
                cv2.putText(frame, 'no video', (x + 15, y + 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,) * 3, thickness=3)
                cv2.rectangle(frame, (x + 10, y + 10), (x + w - 10, y + h - 10), (255, 0, 0), 3)

        return frame
