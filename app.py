from flask import Flask, render_template, request
import spacy
nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)

@app.route('/')
def index_view():
    return render_template('index.html')
  
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        sen = request.form['sentence']
        doc=nlp(sen)
        mylist=[]
        for ent in doc.ents:
            if ent.label_ in ["ORG","PRODUCT"]:
                mylist.append((ent.text, ent.start_char, ent.end_char, ent.label_))
            else:
                continue 
            

        return render_template('predict.html', results = mylist)
    else:
        return "Unable to read the file. Please check file extension"
    
if __name__ == '__main__':
  
    app.run(debug = True,use_reloader=False, port=8000)