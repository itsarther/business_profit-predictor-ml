from flask import *
from pickle import load

with open("pp.pkl","rb") as f:
	model=load(f)

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
	if request.method=="POST":
		rnd=float(request.form.get("rnd"))
		amd=float(request.form.get("amd"))
		mrk=float(request.form.get("mrk"))
		profit=model.predict([[rnd,amd,mrk]])
		profit=round(profit[0],2)
		msg="Estimated Profit: "+str(profit)
		return render_template("home.html",msg=msg)
	else:
		return render_template("home.html")

if __name__=="__main__":
	app.run(debug=True,use_reloader=True)