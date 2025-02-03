from flask import Flask ,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template("home.html")
    else:
        data=CustomData(
            Outlet_Size=request.form.get("Outlet_Identifier"),
            Outlet_Identifier=request.form.get("Outlet_Identifier"),
            Item_Type=request.form.get("Item_Type"),
            Item_Fat_Content=request.form.get("Item_Fat_Content"),
            Outlet_Location_Type=request.form.get("Outlet_Location_Type"),
            Outlet_Type=request.form.get("Outlet_Type"),
            Item_Weight=float(request.form.get("Item_Weight")),
            Item_Visibility=float(request.form.get("Item_Visibility")),
            Item_MRP=float(request.form.get("Item_MRP"))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template("home.html",results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)