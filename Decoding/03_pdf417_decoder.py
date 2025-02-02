from aspose.barcode import barcoderecognition

reader = barcoderecognition.BarCodeReader("image01.png", barcoderecognition.DecodeType.AllSupportedTypes)
recognized_results = reader.read_bar_codes()
for barcode in recognized_results:
    print(barcode.code_text)

