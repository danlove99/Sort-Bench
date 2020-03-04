from flask import Flask,render_template,request,url_for, redirect
import quicksort
import selectionsort
import heapsort
import bubblesort
import random
import time

app = Flask(__name__)


@app.route("/")
def index():
    
	return render_template("index.html")

@app.route("/",methods=['POST'])
def start():
	if request.method == 'POST':
		
		if request.form['submit_button'] == 'BubbleSort':
			arr = []
			length = request.form['Length']
			highest = request.form['Highest']
			for x in range(int(length)):
				arr.append(random.randrange(int(highest)))
			


			start = time.time()
			bubblesort.bubbleSort(arr)
			end = time.time()
			Time = str((end-start)/1000)
			return render_template('results.html', result=(Time[:5]+' milliseconds'))

			
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
			return render_template('results.html', result=(Time[:5]+' milliseconds'))

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
			return render_template('results.html', result=(Time[:5]+' milliseconds'))
			
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
			return render_template('results.html', result=(Time[:5]+' milliseconds'))

		
			

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=8080,debug=True)
