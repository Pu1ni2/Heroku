from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def index():
    r = requests.get('https://api.thingspeak.com/channels/1136341/fields/1/last.txt')
   
    
    #temp_c_in = r.text
   # temp_c = str(round(float(temp_c_in)))+ ' C'
    #temp_f = str(round(((9.0 / 5.0) * float(temp_c_in) + 32), 1)) + ' F'
    
    #humid = a.text
    #humi = str(round(float(humid)))
    
    Level=r.text
    Le= str(Level)
    
    return render_template('index.html',Level=Le)

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    