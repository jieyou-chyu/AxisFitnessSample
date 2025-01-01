import os
import csv
import os
import barcode
#from barcode import EAN13
#from barcode import code128
from barcode.writer import ImageWriter

# CSV 檔案路徑
CSV_FILE = "data/products.csv"  # CSV 檔案路徑
# header category,subcategory,product,price,svgpath

# SVG 檔案存放目錄
SVG_FOLDER = "svg"             # SVG 存放資料夾

def get_existing_barcodes():
    # 如果資料夾不存在，建立資料夾
    if not os.path.exists(SVG_FOLDER):
        os.makedirs(SVG_FOLDER)
        print(f"Created folder: {SVG_FOLDER}")
    # 返回資料夾中所有的條碼名稱（移除副檔名 .svg）
    return {file.replace(".svg", "") for file in os.listdir(SVG_FOLDER) if file.endswith(".svg")}

def read_csv_barcodes(csv_file):
    with open(csv_file, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return {row['svgpath'] for row in reader}

def generate_barcodeEAN13_svg(barcode, output_folder):
    print(f"generate barcode: {barcode}")
    ean = barcode.EAN13(barcode)
    file_path = os.path.join(output_folder, f"{barcode}")
    ean.save(file_path)

def generate_barcodeCode128_svg(barcode, output_folder):
    print(f"generate barcode: {barcode}")
    code = barcode.Code128(barcode)
    file_path = os.path.join(output_folder, f"{barcode}")
    code.save(file_path)

def main():
    existing_barcodes = get_existing_barcodes()
    csv_barcodes = read_csv_barcodes(CSV_FILE)
    # 找出需要新增的條碼
    new_barcodes = csv_barcodes - existing_barcodes
    if not os.path.exists(SVG_FOLDER):
        os.makedirs(SVG_FOLDER)
    for barcode in new_barcodes:
		if len(barcode) == 13:
			generate_barcodeEAN13_svg(barcode, SVG_FOLDER)
		else:
			generate_barcodeCode128_svg(barcode, SVG_FOLDER)
    print(f"Generated {len(new_barcodes)} new SVG files.")

if __name__ == "__main__":
    main()