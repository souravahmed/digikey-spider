import csv
import os


class FileUtil:
    
    @staticmethod
    def export_to_csv(file_name: str, data:list)->None:
        root_path = os.getcwd()
        exports_folder_path = os.path.join(root_path, "exports")
        FileUtil.create_folder(exports_folder_path)
        file_path = os.path.join(exports_folder_path, f'{file_name}')
        print(f'exporting... {file_name} file.')
        with open(file_path, 'w', newline='', encoding='UTF8') as csvfile:
            row = {}
            rows= []
            headers = ['name', 'slug', 'sku', 'description', 'price', 'quantity', 'mfr_code', 'attributes_list', 'advance_price_list', 'others', 'image', 'document', 'category']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for each_row in data:
                for index, item in enumerate(each_row):
                    row[headers[index]] = item
                rows.append(row)  
                row = {}  
            writer.writerows(rows)
        
        print('export to csv completed')    
    
    @staticmethod
    def save_image(file_name:str, image)->None:
        root_path = os.getcwd()
        image_folder_path = os.path.join(root_path, "images")
        FileUtil.create_folder(image_folder_path)
        file_path = os.path.join(image_folder_path, f'{file_name}')
        with open(file_path, 'wb') as file:
            file.write(image) 
    
    @staticmethod
    def create_folder(path:str)->None:
        if not os.path.isdir(path):
            os.mkdir(path)    
