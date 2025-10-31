

Encoding (encoder.py)
I first create a QR code from the secret message using the qrcode library.
Then I place that QR image on every frame of the video, mostly at the bottom-right corner.
OpenCV reads each frame, adds the QR, and saves it into a new video file.
The final output video looks normal but has a small QR watermark that holds the hidden message.

Why QR Code
I used a QR code instead of normal steganography because QR has error correction.
That means even if the video loses some quality or is re-recorded from a mobile, the QR can still be read.

Decoding (decoder.py)
The decoder reads the video frame by frame using OpenCV.
It checks only the part of the frame where the QR code was added.
To make sure it works for blurred or zoomed videos, it tries different scales (like 2x, 3x, and 4x).
The built-in QRCodeDetector from OpenCV finds and decodes the QR message.
Once it finds the secret message, it prints it and stops.

Example Output
Frame 219, Scale 2: The password is blueberry42

<img width="1162" height="393" alt="Screenshot result" src="https://github.com/user-attachments/assets/42f57c2a-3c92-4cba-bf64-85c656e8ab99" />

Why This Method
I checked other methods like hiding data inside pixels (LSB or frequency-based steganography), but they fail after video re-recording.
So I used QR because it is simple, strong against quality loss, and easy to decode even after compression or recording.









