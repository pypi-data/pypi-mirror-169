import onnxruntime as rt
import numpy as np
import time
import traceback
from multiprocessing.dummy import Pool as ThreadPool
import cv2
import os
from pp_ocr.decode import SegDetectorRepresenter

cur_path = os.path.dirname(os.path.abspath(__file__))

class SingletonType(type):
    def __init__(cls, *args, **kwargs):
        super(SingletonType, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        cls.__init__(obj, *args, **kwargs)
        return obj


class DBNET(metaclass=SingletonType):
    def __init__(self, MODEL_PATH = os.path.join(cur_path,"models/pp_det.onnx")):
        self.sess = rt.InferenceSession(MODEL_PATH)
        self.decode_handel = SegDetectorRepresenter()
        self.mean = (0.485, 0.456, 0.406)
        self.std = (0.229, 0.224, 0.225)


    def process(self, img, short_size):
        t1 = time.time()
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w = img.shape[:2]
        if h > w:
            scale_h = short_size / h
            tar_w = w * scale_h
            tar_w = max(int(round(tar_w / 32) * 32), 32)
            scale_w = tar_w / w

        else:
            scale_w = short_size / w
            tar_h = h * scale_w
            tar_h = max(int(round(tar_h / 32) * 32), 32)
            scale_h = tar_h / h

        img = cv2.resize(img, None, fx=scale_w, fy=scale_h)
        # img = cv2.resize(img,(320,320))

        img = img.astype(np.float32)

        img /= 255.0
        img -= self.mean
        img /= self.std
        img = img.transpose(2, 0, 1)
        transformed_image = np.expand_dims(img, axis=0)
        print("transforme cost: ",time.time()- t1)

        t1 = time.time()
        # dbnet推理
        # out = self.sess.run(["out"], {"input": transformed_image.astype(np.float32)})
        # PPOCR_det推理
        out = self.sess.run(["sigmoid_0.tmp_0"], {"x": transformed_image.astype(np.float32)})
        print("run cost: ",time.time()- t1)

        t1 = time.time()
        box_list, score_list = self.decode_handel(out[0][0], h, w)
        print("decode cost: ",time.time()- t1)
        if len(box_list) > 0:
            idx = box_list.reshape(box_list.shape[0], -1).sum(axis=1) > 0  # 去掉全为0的框
            box_list, score_list = box_list[idx], score_list[idx]
        else:
            box_list, score_list = [], []
        return box_list, score_list