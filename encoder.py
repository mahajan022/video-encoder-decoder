import cv2
import qrcode
import numpy as np

def encode_qr_watermark(input_video, output_video, secret_message):
 
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,  
    )
    qr.add_data(secret_message)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    qr_img = np.array(qr_img)
    qr_img = cv2.cvtColor(qr_img, cv2.COLOR_RGB2BGR)


    cap = cv2.VideoCapture(input_video)
    if not cap.isOpened():
        print(f"Could not open video: {input_video}")
        return

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

   
    qr_size = min(width, height) // 4  
    qr_img = cv2.resize(qr_img, (qr_size, qr_size))


    margin = 50
    x_offset = width - qr_size - margin
    y_offset = height - qr_size - margin

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        
        frame[y_offset:y_offset+qr_size, x_offset:x_offset+qr_size] = 255
        frame[y_offset:y_offset+qr_size, x_offset:x_offset+qr_size] = qr_img

        out.write(frame)

    cap.release()
    out.release()
    print(f"Video encoded with QR watermark: {output_video}")



encode_qr_watermark(
    "testvideo.mov",
    "encoded_video.mov",
    "The password is blueberry42"
)
