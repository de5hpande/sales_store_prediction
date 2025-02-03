import sys
import pandas as pd
from src.exception import CustomException

from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path="artifacts\model.pkl"
            preprocessor_path="artifacts\preprocessor.pkl"
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(self,
        Outlet_Size:str, 
         Outlet_Identifier:str,
         Item_Type:str,
         Item_Fat_Content:str,
         Outlet_Location_Type:str,
         Outlet_Type:str,
         Item_Weight:float,
         Item_Visibility:float,
         Item_MRP:float ):
        self.Outlet_Size=Outlet_Size
        self.Outlet_Identifier=Outlet_Identifier
        self.Item_Type=Item_Type
        self.Item_Fat_Content=Item_Fat_Content
        self.Outlet_Location_Type=Outlet_Location_Type
        self.Outlet_Type=Outlet_Type
        self.Item_Weight=Item_Weight
        self.Item_Visibility=Item_Visibility
        self.Item_MRP=Item_MRP

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict={
                "Outlet_Size":[self.Outlet_Size],
               "Outlet_Identifier":[self.Outlet_Identifier],
                "Item_Type":[self.Item_Type],
                "Item_Fat_Content":[self.Item_Fat_Content],
                "Outlet_Location_Type":[self.Outlet_Location_Type],
                "Outlet_Type":[self.Outlet_Type],
                "Item_Weight":[self.Item_Weight],
                "Item_Visibility":[self.Item_Visibility],
                "Item_MRP":[self.Item_MRP]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)