from django.shortcuts import render
import cv2
from django.http import StreamingHttpResponse
from threading import Thread

#-----------------------------views for option 2-------------------------------

class WebcamStream:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.stopped = False

    def __del__(self):
        self.cam.release()

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        frame1 = None
        while not self.stopped:
            ret, frame2 = self.cam.read()
            if not ret:
                break
            
            if frame1 is None:
                frame1 = frame2
                continue

            diff = cv2.absdiff(frame1, frame2)
            frame1 = frame2

            ret, buffer = cv2.imencode('.jpg', diff)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    def stop(self):
        self.stopped = True

def option2(request):
    stream = WebcamStream().start()

    def generate_frames():
        for frame in stream.update():
            yield frame
            if cv2.waitKey(10) == ord('q'):
                break

        stream.stop()
        cv2.destroyAllWindows()

    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

#------------------------------views for option 1------------------------------------------------------------------------

def option1(request):
    cam = cv2.VideoCapture(0)
    
    def generate_frames():
        while True:
            ret, frame1 = cam.read()
            if not ret:
                break
            
            ret, buffer = cv2.imencode('.jpg', frame1)
            frame = buffer.tobytes()
            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
            
            if cv2.waitKey(10) == ord('q'):
                break
        
        cam.release()
        cv2.destroyAllWindows()
    
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

def welcome(request):
    return render(request, 'welcome.html')
