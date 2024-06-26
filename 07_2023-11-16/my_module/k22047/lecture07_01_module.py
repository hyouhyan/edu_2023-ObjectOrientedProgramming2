import numpy as np
import cv2

REGION_WIDTH=16
REGION_HIGH=16

fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)

def get_masked_image(img : cv2.Mat) -> cv2.Mat:
    red_mask = np.full((1, 1, 3), (0,0,255), dtype=np.uint8)
    white_mask = np.full((REGION_HIGH, REGION_WIDTH, 3), (255,255,255), dtype=np.uint8)

    rows, cols, channels = img.shape
    laplacian_mask = np.zeros((rows, cols, channels), dtype=np.uint8)
    fgmask_mask = np.zeros((rows, cols, channels), dtype=np.uint8)

    frame_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(frame_gray, cv2.CV_64F)
    for y in range(rows):
        for x in range(cols):
            if laplacian[y,x] > 10:
                laplacian_mask[y,x] = np.copy(red_mask)

    # for debug
    # cv2.imshow('frame',laplacian, cmap='gray')
    # cv2.imshow('frame',laplacian_mask)

    fgmask = fgbg.apply(img)
    fgmask_sum = [[np.sum(fgmask[REGION_HIGH*y:REGION_HIGH*(y+1), REGION_WIDTH*x:REGION_WIDTH*(x+1)]) for x in range(int(cols/REGION_WIDTH))] for y in range(int(rows/REGION_HIGH))]
    
    fgmask_mean = np.mean(fgmask_sum)
    for y in range(int(rows/REGION_HIGH)):
        for x in range(int(cols/REGION_WIDTH)):
            if fgmask_sum[y][x] > fgmask_mean:
                fgmask_mask[REGION_HIGH*y:REGION_HIGH*(y+1),REGION_WIDTH*x:REGION_WIDTH*(x+1)] = np.copy(white_mask)

    # for debug
    #cv2.imshow('frame',fgmask)
    #cv2.imshow('frame',fgmask_mask)

    mask_or = cv2.bitwise_or(laplacian_mask, fgmask_mask)
    masked_frame = cv2.bitwise_and(img, mask_or)

    return masked_frame

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while(True):
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (640,480))
        masked_frame = get_masked_image(resized_frame)

        cv2.imshow('frame', masked_frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()