import cv2
from pylibdmtx.pylibdmtx import decode

image = cv2.imread("image02.jpg", cv2.IMREAD_GRAYSCALE)

decoded_image = decode(image)

for obj in decoded_image:
    data = obj.data.decode("utf-8")
    print("Decoded Data:", data)

output_file = "decoded_datamatrix_code.png"
cv2.imwrite(output_file, image)
print(f" Annotated image saved as {output_file}")

cv2.imshow("QR Code", image)
cv2.waitKey(0)
cv2.destroyAllWindows()