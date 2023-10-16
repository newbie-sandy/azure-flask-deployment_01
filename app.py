from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')
 
df = pd.read_csv('/home/yeshangdan/azure-flask-deployment_01/Hospital_Cost_Report_2019 (1).csv')
@app.route('/data')
def data(data=df):
    data = data.sample(15)
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8088
    )