import tkinter as ttk
import pandas as pd

model = pd.read_pickle(r'C:\Users\admin\Desktop\ML training\Student_perform_project_ML\student_perform_RF2.pickle')

app = ttk.Tk()
app.geometry('400x250')
app.title('Student performance prediction')

cols = ['gender_M','Relation_Father','ParentAnsweringSurvey_No','StudentAbsenceDays_Under-7']

# Heading
ttk.Label(app, text='Choose correct data to predict the student performance', padx=15,pady=15,font=('Times New Roman', 12, 'bold')).grid(row=0, columnspan = 2)


# GENDER
ttk.Label(app, text='Student Gender :-',  padx=5,pady=5,background='White',borderwidth=1, relief="sunken").grid(row=1, column = 0)
genders = {
    'Male': 1,
    'Female': 0
}
genderVar = ttk.Variable(app)
genderVar.set(genders['Male'])
frame = ttk.Frame(app)  
frame.grid(row = 1, column = 1)
for gender, genderValue in genders.items():
    ttk.Radiobutton(frame, text = gender, variable = genderVar, value = genderValue).pack(side=ttk.LEFT)


# RELATIONSHIP
ttk.Label(app, text='Responsible Parent :-',  padx=5,pady=5,background='White',borderwidth=1, relief="sunken").grid(row=2, column = 0)
Relationship = {
    'Father': 1,
    'Mother': 0
}
RelationVar = ttk.Variable(app)
RelationVar.set(Relationship['Father'])
frame = ttk.Frame(app)  
frame.grid(row = 2, column = 1)
for Relation, RelationValue in Relationship.items():
    ttk.Radiobutton(frame, text = Relation, variable = RelationVar, value = RelationValue).pack(side=ttk.LEFT)


# PARENT SURVEY
ttk.Label(app, text='Survey Answered :-', padx=5,pady=5,background='White',borderwidth=1, relief="sunken").grid(row=3, column = 0)
Survey = {
    'Yes': 0,
    'No': 1
}
ParentAnsweringSurveyVar = ttk.Variable(app)
ParentAnsweringSurveyVar.set(Survey['Yes'])
frame = ttk.Frame(app)  
frame.grid(row = 3, column = 1)
for ParentAnsweringSurvey, ParentAnsweringSurveyValue in Survey.items():
    ttk.Radiobutton(frame, text = ParentAnsweringSurvey, variable = ParentAnsweringSurveyVar, value = ParentAnsweringSurveyValue).pack(side=ttk.LEFT)


# ABSENT DAYS
ttk.Label(app, text='Absent Days :-', padx=5,pady=5,background='White',borderwidth=1, relief="sunken").grid(row=4, column = 0)
Absence = {
    'Above 7': 0,
    'Under 7': 1
}
StudentAbsenceDaysVar = ttk.Variable(app)
StudentAbsenceDaysVar.set(Absence['Above 7'])
frame = ttk.Frame(app)  
frame.grid(row = 4, column = 1)
for StudentAbsenceDays, StudentAbsenceDaysValue in Absence.items():
    ttk.Radiobutton(frame, text = StudentAbsenceDays, variable = StudentAbsenceDaysVar, value = StudentAbsenceDaysValue).pack(side=ttk.LEFT)


# PREDICTION BUTTON
def st_performance():
    global model
    query_df = pd.DataFrame({'gender_M':[genderVar.get()], 'Relation_Father':[RelationVar.get()],'ParentAnsweringSurvey_No':[ParentAnsweringSurveyVar.get()],'StudentAbsenceDays_Under-7':[StudentAbsenceDaysVar.get()]})
    
    pred = model.predict(query_df)
    print(pred)
    if pred[0] == 1:
        resultVar.set('GOOD PERFORMER')
    elif pred[0]== 2:
        resultVar.set('AVG PERFORMER')
    else:
        resultVar.set('NEEDS IMPROVEMENT')

ttk.Button(app, text='Check Performance', command = st_performance, padx=20, pady=2,background='Yellow',fg = "black").grid(row = 5, column=0, columnspan=2)


# RESULT 
resultVar = ttk.Variable(app)
ttk.Label(app, textvariable=resultVar, font=('Times New Roman',20),background='White',borderwidth=1, relief="sunken").grid(row = 7, column=0, columnspan=2)

app.mainloop()