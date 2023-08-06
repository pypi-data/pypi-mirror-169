from pp_ocr import pp_det
from pp_ocr import pp_rec
import cv2
import numpy as np
import time

# 初始化模型
pp_detor = pp_det.DBNET()
pp_recor = pp_rec.PPrecPredictor()


short_size = 960


def predict(img_path,use_mp = True ,process_num = 10):
    print("start...")
    img = cv2.imdecode(np.fromfile(img_path,dtype=np.uint8),-1)
    if img is None:
        return 
    if len(img.shape) == 3 and img.shape[2] > 3:
        img = img[:,:,:3]
     
    start_time = time.time()
    boxes_list, score_list = pp_detor.process(np.asarray(img).astype(np.uint8),short_size=short_size)
    print("det nums:{} cost time: {:.4f}".format(len(boxes_list),time.time()-start_time))

    start_time = time.time()
    result = pp_recor(np.array(img), boxes_list,use_mp= use_mp,process_num= process_num)
    print("rec nums:{} cost time: {:.4f}".format(len(result),time.time()-start_time))
    print("end...")
    return result
