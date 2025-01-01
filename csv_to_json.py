import csv
import json

# 定義輸入和輸出文件名
input_csv_file = 'products.csv'
<<<<<<< HEAD
output_json_file = 'products.json'
=======
output_json_file = 'products_test.json'
>>>>>>> f8a1fe1453ed8776f17c176ad20fd691cc5dfeef

# 創建一個空字典以儲存結構化數據
data = {
    "categories": []
}

# 讀取CSV文件
with open(input_csv_file, mode='r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        category = row['category'].strip()
        subcategory = row['subcategory'].strip()
        product = row['product'].strip()
<<<<<<< HEAD
        price = row['price'].strip()
=======
>>>>>>> f8a1fe1453ed8776f17c176ad20fd691cc5dfeef
        svgpath = row['svgpath'].strip()

        # 查找或創建類別
        category_found = next((cat for cat in data["categories"] if cat["name"] == category), None)
        if not category_found:
            category_found = {"name": category, "subcategories": []}
            data["categories"].append(category_found)

        # 查找或創建子類別
        subcategory_found = next((subcat for subcat in category_found["subcategories"] if subcat["name"] == subcategory), None)
        if not subcategory_found:
            subcategory_found = {"name": subcategory, "products": []}
            category_found["subcategories"].append(subcategory_found)

        # 添加產品
<<<<<<< HEAD
        subcategory_found["products"].append({"name": product, "price": price, "svg": 'svg/'+svgpath+'.svg'})
=======
        subcategory_found["products"].append({"name": product, "svg": 'svg/'+svgpath+'.svg'})
>>>>>>> f8a1fe1453ed8776f17c176ad20fd691cc5dfeef

# 將結構化數據寫入JSON文件
with open(output_json_file, mode='w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)

print(f"Successfully converted {input_csv_file} to {output_json_file}.")
