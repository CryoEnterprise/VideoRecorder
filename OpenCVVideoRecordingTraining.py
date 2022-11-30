import cv2
import datetime
import os
import numpy as np


def Video_Capture():
    # Assign opencv to default camera:
    webcam = cv2.VideoCapture(0)

    # Update to the Youtube Video Code.
    # This code will allow you to create the video path directories.
    # Check and create the video output path:
    VideoOutPutPath = "Output/Videos/"
    if os.path.isdir(VideoOutPutPath) is False:
        os.makedirs(VideoOutPutPath)

    camera1_frame_height = 480
    camera1_frame_width = 640
    camera1_recoder_time_stamp = datetime.datetime.now()
    camera1_recorder_fileName = "{}.avi".format(camera1_recoder_time_stamp.strftime("%Y-%m-%d_%H-%M-%S"))
    camera1_recorder_video_codex = cv2.VideoWriter_fourcc(*'XVID')
    camera1_recorder_video_path = os.path.sep.join((VideoOutPutPath, camera1_recorder_fileName))
    camera1_video_recorder_output = cv2.VideoWriter(camera1_recorder_video_path,
                                                    camera1_recorder_video_codex, 30,
                                                    (camera1_frame_width, camera1_frame_height))

    print("Recording...")
    while True:

        camera_status, frame_captured = webcam.read()

        camera1_video_recorder_output.write(frame_captured)

        cv2.imshow("OpenCV Video Recording Training", frame_captured)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Recording Complete")
            break

    webcam.release()
    camera1_video_recorder_output.release()
    print("Video Saved")
    cv2.destroyAllWindows()

    pass


if __name__ == '__main__':
    Video_Capture()
