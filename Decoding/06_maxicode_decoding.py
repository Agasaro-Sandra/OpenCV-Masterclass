import zxing
import cv2
import numpy as np  # Import numpy

def decode_maxicode(image_path):
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
        
        # Draw a polygon around the MaxiCode location (if available)
        if result.points:
            pts = np.array(result.points, dtype=np.int32)  # Convert points to numpy array
            pts = pts.reshape((-1, 1, 2))  # Reshape the points to match the expected format
            cv2.polylines(image, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
        
        # Show the image with the detected MaxiCode
        cv2.imshow('MaxiCode', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No MaxiCode detected.")

# Example usage
decode_maxicode('image06.png')
