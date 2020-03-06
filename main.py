from flask import Flask,render_template,request,url_for, redirect, session
import quicksort
import selectionsort
import heapsort
import bubblesort
import random
import time
import statistics

app = Flask(__name__)
app.secret_key = "abc"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/",methods=['POST'])
def start():
	if request.method == 'POST':
		if request.form['submit_button'] == 'BubbleSort':
			session['chosen'] = 'Bubble Sort'
			length = request.form['Length']
			if length == '':
				length = '100'
			highest = request.form['Highest']
			if highest == '':
				highest = '100'
			results = []
			for x in range(1001):
				arr = []
				for x in range(int(length)):
					arr.append(random.randrange(int(highest)))
				start = time.time()
				bubblesort.bubbleSort(arr)
				end = time.time()
				Time = (end-start)/1000
				results.append(Time)
			meanTime = statistics.mean(results)
			session['time'] = ((str(meanTime)[:5]) + ' Milliseconds')
			return redirect(url_for('result'))


		elif request.form['submit_button'] == 'SelectionSort':
			session['chosen'] = 'Selection Sort'
			length = request.form['Length']
			if length == '':
				length = '100'
			highest = request.form['Highest']
			if highest == '':
				highest = '100'
			results = []
			for x in range(1001):
				arr = []
				for x in range(int(length)):
					arr.append(random.randrange(int(highest)))
				start = time.time()
				selectionsort.selectionsort(arr)
				end = time.time()
				Time = (end-start)/1000
				results.append(Time)
			meanTime = statistics.mean(results)
			session['time'] = ((str(meanTime)[:5]) + ' Milliseconds')
			return redirect(url_for('result'))

		elif request.form['submit_button'] == 'HeapSort':
			session['chosen'] = 'Heap Sort'
			length = request.form['Length']
			if length == '':
				length = '100'
			highest = request.form['Highest']
			if highest == '':
				highest = '100'
			results = []
			for x in range(1001):
				arr = []
				for x in range(int(length)):
					arr.append(random.randrange(int(highest)))
				start = time.time()
				heapsort.heapsort(arr)
				end = time.time()
				Time = (end-start)/1000
				results.append(Time)
			meanTime = statistics.mean(results)
			session['time'] = ((str(meanTime)[:5]) + ' Milliseconds')
			return redirect(url_for('result'))

		elif request.form['submit_button'] == 'QuickSort':
			session['chosen'] = 'Quick Sort'
			length = request.form['Length']
			if length == '':
				length = '100'
			highest = request.form['Highest']
			if highest == '':
				highest = '100'
			results = []
			for x in range(1001):
				arr = []
				for x in range(int(length)):
					arr.append(random.randrange(int(highest)))
				start = time.time()
				quicksort.quicksort(arr)
				end = time.time()
				Time = (end-start)/1000
				results.append(Time)
			meanTime = statistics.mean(results)
			session['time'] = ((str(meanTime)[:5]) + ' Milliseconds')
			return redirect(url_for('result'))


@app.route("/result")
def result():
	Time = session['time']
	chosen = session['chosen']
	return render_template('results.html', result=Time, chosen=chosen)

@app.route("/result", methods=['POST'])
def Back():
	if request.method == 'POST':
		if request.form['back_button'] == 'Back':
			print('Done')
			return redirect(url_for('start'))

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=8080,debug=True)
