from flask import Flask,render_template,request,url_for, redirect, session

# Python imports
import quicksort
import selectionsort
import heapsort
import bubblesort


# Javascript imports
import jsquicksort
import jsselectionsort
import jsheapsort
import jsbubblesort



import random
import time

app = Flask(__name__)
app.secret_key = "abc"  

@app.route("/")
def index():
	return render_template("choice.html")
app.route("/", methods=['POST'])
def start():
	if request.method == 'POST':
		if request.form['submit_button'] == 'python':
			return redirect(url_for('indexPython'))
		elif request.form['submit_button'] == 'JS':
			return redirect(url_for('indexJS'))


# Python route

@app.route("/python")
def indexPython():    
	return render_template("index.html")

@app.route("/python",methods=['POST'])
def startPython():
	if request.method == 'POST':		
		if request.form['submit_button'] == 'BubbleSort':
			arr = []
			length = request.form['Length']
			if length == '':
				length = '100'
			highest = request.form['Highest']
			if highest == '':
				highest = '100'
			for x in range(int(length)):
				arr.append(random.randrange(int(highest)))
			start = time.time()
			bubblesort.bubbleSort(arr)
			end = time.time()
			Time = str((end-start)/1000)
			session['time'] = (Time[:5]+' milliseconds')
			return redirect(url_for('result'))

			
		elif request.form['submit_button'] == 'SelectionSort':
			arr = []
			length = request.form['Length']
			if length == '':
				length = '100'
			highest = request.form['Highest']                
			if highest == '':
				highest = '100'
			for x in range(int(length)):
				arr.append(random.randrange(int(highest)))
			start = time.time()
			selectionsort.selectionsort(arr)
			end = time.time()
			Time = str((end-start)/1000)
			session['time'] = (Time[:5]+' milliseconds')
			return redirect(url_for('result'))

		elif request.form['submit_button'] == 'HeapSort':
			arr = []
			length = request.form['Length']
			if length == '':
				length = '100'
			highest = request.form['Highest']                
			if highest == '':
				highest = '100'
			for x in range(int(length)):
				arr.append(random.randrange(int(highest)))
			start = time.time()
			heapsort.heapsort(arr)
			end = time.time()
			Time = str((end-start)/1000)
			session['time'] = (Time[:5]+' milliseconds')
			return redirect(url_for('result'))
			
		elif request.form['submit_button'] == 'QuickSort':
			arr = []
			length = request.form['Length']
			if length == '':
				length = '100'
			highest = request.form['Highest']                
			if highest == '':
				highest = '100'
			for x in range(int(length)):
				arr.append(random.randrange(int(highest)))
			start = time.time()
			quicksort.quicksort(arr)
			end = time.time()
			Time = str((end-start)/1000)
			session['time'] = (Time[:5]+' milliseconds')
			return redirect(url_for('result'))
	
# Javascript route	

@app.route("/JS")
def indexJS():    
	return render_template("index.html")

@app.route("/JS",methods=['POST'])
def startJS():
	if request.method == 'POST':		
		if request.form['submit_button'] == 'BubbleSort':
			arr = []
			length = request.form['Length']
			if length == '':
				length = '100'
			highest = request.form['Highest']
			if highest == '':
				highest = '100'
			for x in range(int(length)):
				arr.append(random.randrange(int(highest)))
			start = time.time()
			jsbubblesort.js2py.eval_js(arr)
			end = time.time()
			Time = str((end-start)/1000)
			session['time'] = (Time[:5]+' milliseconds')
			return redirect(url_for('result'))

			
		elif request.form['submit_button'] == 'SelectionSort':
			arr = []
			length = request.form['Length']
			if length == '':
				length = '100'
			highest = request.form['Highest']                
			if highest == '':
				highest = '100'
			for x in range(int(length)):
				arr.append(random.randrange(int(highest)))
			start = time.time()
			jsselectionsort.js2py.eval_js(arr)
			end = time.time()
			Time = str((end-start)/1000)
			session['time'] = (Time[:5]+' milliseconds')
			return redirect(url_for('result'))

		elif request.form['submit_button'] == 'HeapSort':
			arr = []
			length = request.form['Length']
			if length == '':
				length = '100'
			highest = request.form['Highest']                
			if highest == '':
				highest = '100'
			for x in range(int(length)):
				arr.append(random.randrange(int(highest)))
			start = time.time()
			jsheapsort.js2py.eval_js(arr)
			end = time.time()
			Time = str((end-start)/1000)
			session['time'] = (Time[:5]+' milliseconds')
			return redirect(url_for('result'))
			
		elif request.form['submit_button'] == 'QuickSort':
			arr = []
			length = request.form['Length']
			if length == '':
				length = '100'
			highest = request.form['Highest']                
			if highest == '':
				highest = '100'
			for x in range(int(length)):
				arr.append(random.randrange(int(highest)))
			start = time.time()
			jsquicksort.js2py.eval_js(arr)
			end = time.time()
			Time = str((end-start)/1000)
			session['time'] = (Time[:5]+' milliseconds')
			return redirect(url_for('result'))
@app.route("/result")
def result():
	Time = session['time']
	return render_template('results.html', result=Time)

@app.route("/result", methods=['POST'])	
def Back():
	if request.method == 'POST':
		if request.form['back_button'] == 'Back':
			print('Done')
			return redirect(url_for('start'))

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=8080,debug=True)
