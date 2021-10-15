from flask import Flask,render_template,request
import pickle
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
model=pickle.load(open('model_pickle.pkl','rb'))

app=Flask(__name__)


@app.route('/analysis')
def analysis():
    return render_template('stroke.html')

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        gender=request.form['gender']
        age=int(request.form['age'])
        hypertension=int(request.form['hypertension'])
        disease=request.form['disease']
        married=request.form['married']
        work=request.form['work']
        residence=request.form['residence']
        glucose=float(request.form['glucose'])
        bmi=float(request.form['bmi'])
        smoking=request.form['smoking']

        if (gender=="Male"):
            gender_male=1
            gender_other=0
        elif(gender=="Female"):
            gender_male=0
            gender_other=1
        else:
            gender_male=0
            gender_other=0

        if (married=='Yes'):
            married_yes=1
        else:
            married_yes=0
        
        if (work=="Self-employed"):
            work_type_Never_worked=0
            work_type_Private=0
            work_type_Self_employed=1
            work_type_children=0
        elif(work=='Private'):
            work_type_Never_worked=0
            work_type_Private=1
            work_type_Self_employed=0
            work_type_children=0 
        elif(work=='children'):
            work_type_Never_worked=0
            work_type_Private=0
            work_type_Self_employed=0
            work_type_children=1
        elif(work=='Never_worked'):
            work_type_Never_worked=1
            work_type_Private=0
            work_type_Self_employed=0
            work_type_children=0
        else:
            work_type_Never_worked=0
            work_type_Private=0
            work_type_Self_employed=0
            work_type_children=0

        if(residence=='Urban'):
            Residence_type_urban=1
        else:
            Residence_type_urban=0

        if(smoking=='formerly smoked'):
            smoking_status_formerly_smoked=1
            smoking_status_never_smoked=0
            smoking_status_smokes=0
        elif(smoking=='smokes'):
            smoking_status_formerly_smoked=0
            smoking_status_never_smoked=0
            smoking_status_smokes=1
        elif(smoking=='never smoked'):
            smoking_status_formerly_smoked=0
            smoking_status_never_smoked=1
            smoking_status_smokes=0
        else:
            smoking_status_formerly_smoked=0
            smoking_status_never_smoked=0
            smoking_status_smokes=0
        
        feature=sc.fit_transform([[age,hypertension,disease,glucose,bmi,gender_male,gender_other,married_yes,work_type_Never_worked,work_type_Private,work_type_children,work_type_Self_employed,Residence_type_urban,smoking_status_formerly_smoked,smoking_status_never_smoked,smoking_status_smokes]])
        prediction=model.predict(feature)
        print(prediction)

        return render_template('index.html',prediction_text="prediction is: {}".format(prediction))
    
    
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)