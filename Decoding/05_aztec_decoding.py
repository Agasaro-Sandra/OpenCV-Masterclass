import zxing
import cv2
import numpy as np

def decode_aztec_code(image_path):
    # Initialize the ZXing barcode reader
    reader = zxing.BarCodeReader()
    
    # Decode the image
    result = reader.decode(image_path)
    
    if result:
        # Print the results
        print(f'Decoded Data: {result.parsed}')
        print(f'Barcode Type: {result.format}')
        print(f'Location: {result.points}')
        
        # Load the image with OpenCV to display the barcode location
        image = cv2.imread(image_path)
        
        # Draw a polygon around the Aztec code location (if available)
        if result.points:
            pts = np.array(result.points, dtype=np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(image, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
        
        # Show the image with the detected Aztec code
        cv2.imshow('Aztec Code', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No Aztec code detected.")

# Example usage
decode_aztec_code('image05.jpg')
