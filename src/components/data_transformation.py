import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function si responsible for data trnasformation
        '''
        try:
            numerical_columns=['Item_Weight', 'Item_Visibility', 'Item_MRP',]
            categorical_columns=['Item_Fat_Content', 'Item_Type', 'Outlet_Identifier', 'Outlet_Size',
            'Outlet_Location_Type', 'Outlet_Type']

            num_pipeline=Pipeline(

                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )

            cat_pipeline=Pipeline(

                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder(handle_unknown='ignore')),
                    ("scaler",StandardScaler(with_mean=False))


                ]
            )
            logging.info(f"Categorical Column :{categorical_columns}")
            logging.info(f"Numerical Column :{numerical_columns}")

            preprocessor=ColumnTransformer(

                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipeline",cat_pipeline,categorical_columns)
                 ]
            )
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
    

    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()
            target_column_name="Item_Outlet_Sales"
            

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            # print(input_feature_train_arr.shape)
            # print(np.array(target_feature_train_df).shape)
            
            # print(input_feature_test_arr.shape)
            # print(np.array(target_feature_test_df).shape)

            print("Train features shape:", input_feature_train_arr.shape)  # Expected: (6818, 1600)
            print("Train target shape before reshape:", target_feature_train_df.shape)  # Expected: (6818,)
            print("Train target shape after reshape:", target_feature_train_df.to_numpy().reshape(-1, 1).shape)  # Expected: (6818, 1)

            print("Test features shape:", input_feature_test_arr.shape)  # Expected: (1705, 1600)
            print("Test target shape before reshape:", target_feature_test_df.shape)  # Expected: (1705,)
            print("Test target shape after reshape:", target_feature_test_df.to_numpy().reshape(-1, 1).shape)  # Expected: (1705, 1))

            

            # train_arr=np.c_[
            #     input_feature_train_arr,np.array(target_feature_train_df)
            # ]
            # test_arr=np.c_[
            #     input_feature_test_arr,np.array(target_feature_test_df)
            # ]

            train_arr = np.hstack((input_feature_train_arr.toarray(), target_feature_train_df.values.reshape(-1, 1)))
            test_arr = np.hstack((input_feature_test_arr.toarray(), target_feature_test_df.values.reshape(-1, 1)))



            print(train_arr)
            print(test_arr)

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path

            )
        except Exception as e:
            raise CustomException(e,sys)