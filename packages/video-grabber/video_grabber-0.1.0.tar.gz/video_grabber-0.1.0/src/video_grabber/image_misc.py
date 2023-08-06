import cv2
import numpy as np
import logging


def cv_show_images(KVS, shape=(600, 400, 3), first_point=None):
    n_images = float(len(KVS))

    i = 0
    if shape is not None:
        width, height, n_per_line = shape
        _r, _c = [np.ceil(n_images / n_per_line).astype(int), n_per_line]
        m = np.moveaxis(np.squeeze(np.meshgrid(np.arange(_c), np.arange(_r))), 0, -1)
        pos_m = m * np.array(shape[:2])
        pos = pos_m.reshape(-1, 2).astype(int)
        # logging.debug(f"{n_images=},{_r=},{_c=},{m=},{pos_m=},{pos=}")
    else:
        width, height = (800, 600)
        # pos = first_point 
    for wind, frame in KVS.items():
        if frame is not None:
            cv2.namedWindow(wind, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
            if shape is not None:
                cv2.resizeWindow(wind, width, height)
            if first_point is not None:
                cv2.moveWindow(wind, pos[i][0], pos[i][1])
            i += 1
            cv2.imshow(wind, frame)


# get video infomation
def cv_get_video_info(video):
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frames_per_second = video.get(cv2.CAP_PROP_FPS)
    num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    return width, height, frames_per_second, num_frames


def mask_image(input_img, array_mask=None, type_of_array="box"):
    if array_mask is None:
        return input_img

    if type_of_array == "mask":
        return cv2.bitwise_and(input_img, input_img, mask=array_mask)

    len_shape = len(input_img.shape)
    if len_shape == 3:
        h, w, c = input_img.shape
    elif len_shape == 2:
        h, w = input_img.shape
    else:
        return input_img

    mask = np.zeros((h, w), dtype=np.uint8)
    for mask_points in array_mask:
        if type_of_array == "box":
            cv2.rectangle(mask, mask_points[0], mask_points[1], (255), -1)
        elif type_of_array == "polygon":
            cv2.fillPoly(mask, [mask_points], (255))
        else:
            logging.warning("Wrong value of parameter type_of_array")
            return input_img
    img = cv2.bitwise_and(input_img, input_img, mask=mask)
    return img


def cuda_calculate_iou(bin_frames):
    areas = []
    intersection = cv2.cuda_GpuMat()
    union = cv2.cuda_GpuMat()
    frame = cv2.cuda_GpuMat()

    for i, c in enumerate(bin_frames):
        frame.upload(c)
        if i == 0:
            intersection = frame
            union = frame
        else:
            try:
                intersection = cv2.cuda.bitwise_and(intersection, frame)
                union = cv2.cuda.bitwise_or(union, frame)
            except:
                pass
    # for i, item in enumerate([intersection, union]):
    # contours, _ = cv2.findContours(item, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # areas.append(np.sum([cv2.contourArea(cnt) for cnt in contours]))
    areas = [cv2.cuda.countNonZero(item) for item in [intersection, union]]
    iou = areas[0] / areas[1]
    # logging.debug({f"{areas=}"})
    return iou


def calculate_iou(bin_frames):
    intersection = union = None
    areas = []
    for i, c in enumerate(bin_frames):
        if i == 0:
            intersection = c
            union = c
        else:
            try:
                intersection = cv2.bitwise_and(intersection, c)
                union = cv2.bitwise_or(union, c)
            except:
                pass
    for i, item in enumerate([intersection, union]):
        contours, _ = cv2.findContours(item, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        areas.append(np.sum([cv2.contourArea(cnt) for cnt in contours]))
    iou = areas[0] / areas[1]
    # logging.debug({f"{areas=}"})
    return iou


def Img_Outline(
    input_img,
    mask=None,
    blur_kenel=(3, 3),
    morphology_kernel=(3, 3),
    threshold=-1,
):
    # original_img = cv2.imread(input_dir)

    if mask is not None:
        masked_image = cv2.bitwise_and(input_img, input_img, mask=mask)
    else:
        masked_image = input_img.copy()

    # cv2.imwrite("target.png", target)

    gray_img = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray_img, blur_kenel, 0)  # 高斯模糊去噪（设定卷积核大小影响效果）
    if threshold > 0:
        _, threshed = cv2.threshold(blurred, threshold, 255, cv2.THRESH_BINARY)  # 设定阈值165（阈值影响开闭运算效果）
    else:
        threshed = cv2.adaptiveThreshold(
            blurred,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            55,
            0,
        )
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, morphology_kernel)  # 定义矩形结构元素
    closed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)  # 闭运算（链接块）
    opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)  # 开运算（去噪点）

    return gray_img, threshed, closed, opened


def findContours_Rect(input_img, masked):
    """
    find rectangle contour in input_img masked by masked
    """
    contours, hierarchy = cv2.findContours(masked, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # draw_img = input_img.copy()
    # cv2.drawContours(draw_img, contours, -1, (255, 0, 0), 2)

    cnt = sorted(contours, key=cv2.contourArea, reverse=True)[0]  # 计算最大轮廓的旋转包围盒
    # rect = cv2.minAreaRect(c)                                    # 获取包围盒（中心点，宽高，旋转角度）
    # box = np.int0(cv2.boxPoints(rect))                           # box
    # box[]
    # draw_img = cv2.drawContours(original_img.copy(), [box], -1, (0, 0, 255), 3)

    # 拟合四边形
    # cnt_len = cv2.arcLength(contours[0], True)
    cnt_len = cv2.arcLength(cnt, True)
    cnt = cv2.approxPolyDP(cnt, 0.02 * cnt_len, True)

    # if len(cnt) == 4:
    if len(cnt) == 4 and cv2.contourArea(cnt) > 1000 and cv2.isContourConvex(cnt):
        # cv2.drawContours(draw_img, [cnt], -1, (255, 255, 0), 3)
        # logging.debug(f"{cnt=}")

        return cnt
    else:
        return None


def findContours_by_area(mask, mini_area=300):
    """
    find foot in input_img
    """
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    _found = [cnt for cnt in contours if cv2.contourArea(cnt) > mini_area]
    return _found


def sort_rect_point(box):
    """
    sorting 4 points of a rectangle to up-left, up-right, down-right, down-left
    """
    # pts1 = np.float32([box[0], box[1], box[2], box[3]])

    # s = np.sum(box, axis=2)
    # shift = -list(np.argsort(s, axis=0)).index(0)
    # pts1 = np.roll(box, shift=shift, axis=0)

    # logging.debug(f"box={box}")
    shift = -np.lexsort(box.T).tolist()[0][0]
    pts1 = np.roll(box, shift=shift, axis=0)

    # logging.debug(f"pts1={pts1}")
    return np.float32(pts1)


def Perspective_transform(box, shape_t):
    pts1 = sort_rect_point(box)

    # 变换后矩阵位置
    pts2 = np.float32(
        [
            [0, 0],
            [0, shape_t[1]],
            [shape_t[0], shape_t[1]],
            [shape_t[0], 0],
        ]
    )
    # 生成透视变换矩阵；进行透视变换
    M = cv2.getPerspectiveTransform(pts1, pts2)
    return M
