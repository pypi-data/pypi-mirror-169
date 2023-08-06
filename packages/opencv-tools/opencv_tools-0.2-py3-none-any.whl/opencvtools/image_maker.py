class ImageMaker:
    """Pipeline tool to resize/crop/annotate/convert images."""

    def __init__(self, img, lw=2, pts_scale=(640, 360)):  # pts scale - original scale for points (ex in bbox)
        if img is None or img == []:
            raise ValueError('Image is None')
        self.img = img
        self.lw = lw
        self.pts_scale = pts_scale

    def box(self, bbox, color=(0, 0, 255), lw=None):
        """Draws box."""
        if bbox is None:
            return self
        lw = self.lw if lw is None else lw
        p1, p2 = self.point_scale(*bbox[[0, 1]]), self.point_scale(*bbox[[2, 3]])

        cv2.rectangle(self.img, p1, p2, (120, 120, 120), thickness=lw + 1, lineType=cv2.LINE_4)
        cv2.rectangle(self.img, p1, p2, color, thickness=lw, lineType=cv2.LINE_AA)

        return self

    def label(self, label, bbox, color, lw=None):
        """Draws label"""
        lw = self.lw if lw is None else lw

        p1, p2 = (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3]))
        w, h = cv2.getTextSize(label, 0, fontScale=lw / 3, thickness=1)[0]  # text width, height
        outside = p1[1] - h >= 3
        p2 = p1[0] + w, p1[1] - h - 3 if outside else p1[1] + h + 3
        cv2.rectangle(self.img, p1, p2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(self.img, label,
                    (p1[0], p1[1] - 2 if outside else p1[1] + h + 2),
                    0,
                    lw / 3,
                    (255, 255, 255),
                    thickness=1,
                    lineType=cv2.LINE_AA)

        return self

    def resize(self, width=None, height=None, inter=cv2.INTER_AREA):
        """Resizes image."""
        (h, w) = self.img.shape[:2]
        if (not w or not h) or (width is None and height is None):
            return self

        height = height or int(h * width / w)
        width = width or int(w * height / h)
        self.img = cv2.resize(self.img, (width, height), interpolation=inter)
        return self

    def center_crop(self, center, to_size):
        """
        Crops image to size centering it to passed center point.

        Args:
            center (x, y) - point to center to
            to_size (width, height) - size to crop to
        """
        if to_size[0] > self.img.shape[1] or to_size[1] > self.img.shape[0]:
            return self

        center = self.point_scale(*center)

        a0, a1 = center[0] - to_size[0] / 2, center[1] - to_size[1] / 2
        b0, b1 = center[0] + to_size[0] / 2, center[1] + to_size[1] / 2

        x_shift = -a0 if a0 < 0 else self.img.shape[0] - 1 - b0 if b0 > self.img.shape[0] - 1 else 0
        y_shift = -a1 if a1 < 0 else self.img.shape[1] - 1 - b1 if b1 > self.img.shape[1] - 1 else 0

        a0, b0 = int(a0 + x_shift), int(b0 + x_shift)
        a1, b1 = int(a1 + y_shift), int(b1 + y_shift)

        self.img = self.img[a1:b1, a0:b0]

        return self

    def get_jpg_base64(self):
        """Returns image as base64 encoded jpg."""
        try:
            ret, buffer = cv2.imencode('.jpg', self.img)
        except cv2.error:
            ret, buffer = cv2.imencode('.jpg', np.zeros((360, 640, 3)))
            LOGGER.warning('Image is None, returning empty image')
        return "data:image/jpeg;base64," + base64.b64encode(buffer).decode('ascii')

    def get(self):
        """Returns image as numpy array."""
        return self.img

    def point_scale(self, x, y, scale=None):  # scale - original scale for points (ex in bbox)
        """Returns point scaled by scale."""
        scale = self.pts_scale if scale is None else scale
        return int(x * self.img.shape[1] / scale[0]), int(y * self.img.shape[0] / scale[1])
