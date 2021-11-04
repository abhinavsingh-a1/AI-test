from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('good_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    sensor_01 = request.form['sensor_01']
    sensor_02 = request.form['sensor_02']
    sensor_03 = request.form['sensor_03']
    sensor_04 = request.form['sensor_04']
    sensor_05 = request.form['sensor_05']
    sensor_06 = request.form['sensor_06']
    sensor_07 = request.form['sensor_07']
    sensor_08 = request.form['sensor_08']
    sensor_09 = request.form['sensor_09']
    sensor_10 = request.form['sensor_10']
    sensor_11 = request.form['sensor_11']
    sensor_12 = request.form['sensor_12']
    sensor_13 = request.form['sensor_13']
    sensor_14 = request.form['sensor_14']
    sensor_15 = request.form['sensor_15']
    sensor_16 = request.form['sensor_16']
    sensor_17 = request.form['sensor_17']
    sensor_18 = request.form['sensor_18']
    sensor_19 = request.form['sensor_19']
    sensor_20 = request.form['sensor_20']
    sensor_21 = request.form['sensor_21']
    sensor_22 = request.form['sensor_22']
    sensor_23 = request.form['sensor_23']
    sensor_24 = request.form['sensor_24']
    sensor_25 = request.form['sensor_25']
    sensor_26 = request.form['sensor_26']
    sensor_27 = request.form['sensor_27']
    sensor_28 = request.form['sensor_28']
    sensor_29 = request.form['sensor_29']
    sensor_30 = request.form['sensor_30']
    sensor_31 = request.form['sensor_31']
    sensor_32 = request.form['sensor_32']
    sensor_33 = request.form['sensor_33']
    sensor_34 = request.form['sensor_34']
    sensor_35 = request.form['sensor_35']
    sensor_36 = request.form['sensor_36']
    sensor_37 = request.form['sensor_37']
    sensor_38 = request.form['sensor_38']
    sensor_39 = request.form['sensor_39']
    sensor_40 = request.form['sensor_40']
    sensor_41 = request.form['sensor_41']
    sensor_42 = request.form['sensor_42']
    sensor_43 = request.form['sensor_43']
    sensor_44 = request.form['sensor_44']
    sensor_45 = request.form['sensor_45']
    sensor_46 = request.form['sensor_46']
    sensor_47 = request.form['sensor_47']
    sensor_48 = request.form['sensor_48']
    input_variables_ = pd.DataFrame([[sensor_01, sensor_02,sensor_03,sensor_04,sensor_05,sensor_06,sensor_07,sensor_08,sensor_09,sensor_10,
                                     sensor_11,sensor_12,sensor_13,sensor_14,sensor_15,sensor_16,sensor_17,sensor_18,sensor_19,sensor_20,
                                     sensor_21,sensor_22,sensor_23,sensor_24,sensor_25,sensor_26,sensor_27,sensor_28,sensor_29,sensor_30,
                                     sensor_31,sensor_32,sensor_33,sensor_34,sensor_35,sensor_36,sensor_37,sensor_38,sensor_39,sensor_40,
                                     sensor_41,sensor_42,sensor_43,sensor_44,sensor_45,sensor_46,sensor_47,sensor_48]],
                                       columns=['sensor_01', 'sensor_02','sensor_03','sensor_04','sensor_05','sensor_06','sensor_07','sensor_08','sensor_09','sensor_10',
                                     'sensor_11','sensor_12','sensor_13','sensor_14','sensor_15','sensor_16','sensor_17','sensor_18','sensor_19','sensor_20',
                                     'sensor_21','sensor_22','sensor_23','sensor_24','sensor_25','sensor_26','sensor_27','sensor_28','sensor_29','sensor_30',
                                     'sensor_31','sensor_32','sensor_33','sensor_34','sensor_35','sensor_36','sensor_37','sensor_38','sensor_39','sensor_40',
                                     'sensor_41','sensor_42','sensor_43','sensor_44','sensor_45','sensor_46','sensor_47','sensor_48'],
                                       dtype=float)
    input_variables = pd.DataFrame([[sensor_03, sensor_04,sensor_09,sensor_10,sensor_11,sensor_27,sensor_30,sensor_39,sensor_47,sensor_48]],
                                       columns=['sensor_03', 'sensor_04','sensor_09','sensor_10','sensor_11','sensor_27','sensor_30','sensor_39','sensor_47',
                                                'sensor_48'
                                     ],
                                       dtype=float)
    prediction = model.predict(input_variables)[0]
    #output = round(prediction[0], 2)
    if prediction == 0:
        output = 'Normal'
    else:
        output = 'Broken'
    
    return render_template('index.html', prediction_text='Sensor Status is $ {}'.format(output))
    

if __name__ == "__main__":
    app.run(debug=True)


