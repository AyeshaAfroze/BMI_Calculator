from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)
@app.route('/about')
def aboutpage():
    return render_template("about.html")
@app.route('/', defaults = {'name':" "})
@app.route('/<name>')
def mainpage(name):
    return render_template("index.html", name=name)

@app.route('/submit', methods=['GET'])
def sub():
    print(request.method)
    if request.method == 'GET':
        sl=request.args['SL']
        sw=request.args['SW']
      #  pl=request.args['PL']
      #  pw=request.args['PW']


        height = float(sl)
        weight = float(sw)
       # unit = input("Kgs or Lbs? ")
        #pound = 2.20462
        converted_weight = float((703*weight) /(height*height))
        formatted_float = "{:.2f}".format(converted_weight)





        
        print(" "+formatted_float)
        return redirect(url_for('mainpage', name=" "+formatted_float))
      #   return redirect(url_for('mainpage', name=" "+formatted_float+" "+sw+" "+pl+" "+pw))
    else:
     return redirect(url_for('mainpage'))





if __name__=='__main__':
        app.run(debug = True)







