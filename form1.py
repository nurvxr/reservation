from PyQt5 import QtWidgets,uic

#Bouton valider
def valid() :
    global call_2
    a=call.lineEdit.text()
    b=call.lineEdit_2.text()
    c=call.lineEdit_3.text()
    d=call.lineEdit_4.text()
    m=call.radioButton.isChecked()
    n=call.radioButton_2.isChecked()
    ch=[]
    e=call.checkBox.isChecked()
    g=call.checkBox_3.isChecked()
    h=call.checkBox_2.isChecked()
    i=call.checkBox_4.isChecked()
    if e:
        ch.append("Piscine")
    if g:
        ch.append("Sport")
    if h:
        ch.append("Sortie")
    if i:
        ch.append("Disco")
    if m :
        f="Masculin"
    if n:
        f="Féminin"
    call_2.show()
    
    x=f'Nom et prénom : {a}\nAdresse e-mail : {b}\nMot de passe : {c}\nCIN : {d}\nGenre : {f}\nOptions : {ch}'
    call_2.complete.setText(x)
    
def quit_2():
    app.quit()

#Boutton annuler
def canceling():
    app.quit()


#Program principal
app=QtWidgets.QApplication([])
call=uic.loadUi("form.ui")
call_2=uic.loadUi("okform.ui")
call.pushButton.clicked.connect(valid)
call.pushButton_2.clicked.connect(canceling)
call_2.ok1.clicked.connect(quit_2)
call.show()
app.exec()
