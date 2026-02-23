import cv2
import os

def extract_frames(video_path, output_folder="frames"):
    # Video dosyasını aç
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Video dosyası açılamadı.")
        return

    # Çıktı klasörü oluştur
    os.makedirs(output_folder, exist_ok=True)

    frame_number = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_number += 1
        frame_filename = os.path.join(
            output_folder,
            f"frame_{frame_number:04d}.jpg"
        )

        cv2.imwrite(frame_filename, frame)
        print(f"Frame {frame_number} kaydedildi.")

    cap.release()
    print("Frameler başarıyla kaydedildi.")

if __name__ == "__main__":
    video_path = "video.mp4"  # Buraya video adını yaz
    extract_frames(video_path)