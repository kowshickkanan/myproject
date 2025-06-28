from serpapi import GoogleSearch
import openpyxl
workbook = openpyxl.Workbook()
sheet = workbook.active
from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        name=request.form.get("pname")
        country=request.form.get("country")
        state=request.form.get("sname")
        district=request.form.get("dname")
        print(name,country,state,district)
        location=country+","+state+","+district
        
        params = {
        "engine": "google_maps",
        "q": name,
        "location":location,
        "type": "search",
        "api_key":"09b7477a8f0e2d1b252681540b16d8d118a199d49b965d63acadb4574065a48f"

}

        search = GoogleSearch(params)
        results = search.get_dict()
        i=0
        for place in results.get("local_results", []):
            name = place.get("title")
            phone = place.get("phone")
            print(f"{name} - {phone}")
            i=i+1
            sheet["A"+str(i)]=name
            sheet["B"+str(i)]=phone

        else:
            workbook.save('output.xlsx')
        
    
    return render_template("product.html")
  

if __name__ == "__main__":
   app.run(debug=True)