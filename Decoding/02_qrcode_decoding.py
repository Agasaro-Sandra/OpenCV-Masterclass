import cv2
from pyzbar.pyzbar import decode
import numpy as np

def decode_qr_code(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Decode the QR code
    decoded_objects = decode(image)
    
    # Print the results
    for obj in decoded_objects:
        print(f'Decoded Data: {obj.data.decode("utf-8")}')
        print(f'Barcode Type: {obj.type}')
        print(f'Location: {obj.polygon}')
        
        # Draw a rectangle around the QR code
        if len(obj.polygon) == 4:  # Check if the QR code has 4 corners
            pts = np.array([point for point in obj.polygon], dtype=np.int32)
            pts = pts.reshape((-1, 1, 2))  # Reshape the points to match the expected format
            cv2.polylines(image, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
    
    # Show the image with the detected QR code
    cv2.imshow('QR Code', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
decode_qr_code('image04.jpg')