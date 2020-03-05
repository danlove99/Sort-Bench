from flask import Flask,render_template,request,url_for, redirect, session
import quicksort
import selectionsort
import heapsort
import bubblesort
import random
import time

app = Flask(__name__)
app.secret_key = "abc"  

@app.route("/")
def index():    
	return render_template("index.html")

@app.route("/",methods=['POST'])
def start():
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
			highest = request.form['Highest']
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
			highest = request.form['Highest']
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
			highest = request.form['Highest']
			for x in range(int(length)):
				arr.append(random.randrange(int(highest)))
			start = time.time()
			quicksort.quicksort(arr)
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
