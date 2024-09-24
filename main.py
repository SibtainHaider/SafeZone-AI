import cv2
from detectingimages import detect_objects_in_photo, detect_objects_in_video, detect_objects_and_plot

def main():
    # Test detecting objects in a single image
    image_path = "Dataset/weapon_detection/train/bazooka/Bazooka_5.jpeg"
    result_image_path = detect_objects_in_photo(image_path)
    print("Object detection result saved at:", result_image_path)

    # Test detecting objects in a video
    #video_path = "test_video.mp4"
    #result_video_path = detect_objects_in_video(video_path)
    #print("Object detection result video saved at:", result_video_path)

    # Test detecting objects in an image and displaying it
    #path_orig = "test_image.jpg"
    #detect_objects_and_plot(path_orig)

if __name__ == "__main__":
    main()