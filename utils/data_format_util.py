
import json


class DataFormatUtil:
    
    @staticmethod
    def replace_dollar_sign(data:str)-> str:
        return data.replace('$','')
    
    @staticmethod
    def format_bulk_price(data: str)-> str:
        data_list = data.splitlines()
        price_list = data_list[2:]
        result = []
        price = {}
        previous_price = DataFormatUtil.format_price(data)
        for prices in price_list:
            actual_price_list = prices.split(' ')[0:2]
            current_price = float(DataFormatUtil.replace_dollar_sign(actual_price_list[1])) 
            price['min_quantity'] = actual_price_list[0]
            price['price_type'] ='FA'
            price['price'] = previous_price - current_price 
            previous_price = current_price
            result.append(price)
            price = {}
        
        return json.dumps(result)    
        
    
    @staticmethod
    def format_price(data:str) -> str:
        data_list = data.splitlines()
        return float(DataFormatUtil.replace_dollar_sign(data_list[1].split(' ')[1]))    
    
    @staticmethod
    def format_category_attr(data: str) -> str:
        categories = data.splitlines()
        return ','.join(categories)
    
    @staticmethod
    def format_product_attrs(data: str) -> str:
        data_list = data.splitlines();
        attr_list = data_list[3:]
        is_attr = True
        filter_attr_dict = {}
        previous_attr = ''
        mfr_index = attr_list.index('Mfr')
        category_index = attr_list.index('Category')
        filter_attr_dict['Category'] = attr_list[category_index+1: mfr_index]
        attr_list = attr_list[mfr_index:]
        filtered_attr_list = []
        filtered_attr_list.append(filter_attr_dict)
        filter_attr_dict = {}
        result = []
       
        for attr in attr_list:
            if is_attr:
                filter_attr_dict[attr] = ''
                is_attr = False
                previous_attr = attr
            else:
                filter_attr_dict[previous_attr] = attr.replace('"', '<double_quote>')
                filtered_attr_list.append(filter_attr_dict)
                is_attr = True
                filter_attr_dict = {}
        
        filter_attr_dict = {}
        for each_attr in filtered_attr_list:
            for attr, value in each_attr.items():
                   filter_attr_dict['attr_name'] = attr
                   filter_attr_dict['text'] = value
                   result.append(filter_attr_dict)
                   filter_attr_dict = {}
        
        return json.dumps(result)   
    
    @staticmethod
    def format_quantity(data:str)-> int:
        try:
            return int(data.split(' ')[0].replace(',',''))
        
        except ValueError:
            return int(data.split(' ').pop().replace(',', ''))
    
    @staticmethod
    def format_others(data:list)->str:
        result = {}
        result['short_description'] =  data[0]
        result['mfr_part'] =  data[1]
        result['manufacturer'] =  data[2]
        result['manufacturer_product_number'] =  data[3]
        result['manufacturer_std_lead_time'] =  data[4]
        # result['feature_image'] =  {
        #     'main_img': data[5],
        #     'thumb_img': data[5],
        #     'medium_img': data[5],
        # }
        
        return json.dumps(result)   