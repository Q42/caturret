import imutils
import numpy
import time
import cv2


def monitor(callback, w, h):

    camera = cv2.VideoCapture(0)
    time.sleep(0.25)
    first_frame = None
    width = w
    height = h

    while True:
        (grabbed, frame) = camera.read()

        if not grabbed:
            break

        frame = imutils.resize(frame, width)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if first_frame is None:
            first_frame = gray
            continue

        frame_delta = cv2.absdiff(first_frame, gray)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        (_, contours, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        max_area, max_x, max_y, max_h, max_w = 0, 0, 0, 0, 0

        for contour in contours:
            if cv2.contourArea(contour) < 500:
                continue

            (x, y, w, h) = cv2.boundingRect(contour)
            area = x * h

            if area > max_area:
                max_area, max_x, max_y, max_h, max_w = area, x, y, w, h

        if max_area > 100:
            # cv2.rectangle(frame, (max_x, max_y), (max_x + max_w, max_y + max_h), (0, 0, 255), 2)
            target = [max_x + (max_w / 2), max_y + (max_h / 2)]
            cv2.circle(frame, target, 10, (0, 0, 255), 2)
            callback(target)

        cv2.imshow("caturret", frame)

        frame_delta = cv2.merge([frame_delta, frame_delta, frame_delta])
        thresh = cv2.merge([thresh, thresh, thresh])
        gray = cv2.merge([gray, gray, gray])

        output = numpy.zeros((height * 2, width * 2, 3), dtype="uint8")
        output[0:height, 0:width] = gray
        output[0:height, width:width * 2] = frame_delta
        output[height:height * 2, 0:width] = thresh
        output[height:height * 2, width:width * 2] = frame

        cv2.waitKey(1)

    camera.release()
    cv2.destroyAllWindows()
