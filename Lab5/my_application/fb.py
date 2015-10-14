from flask import Flask
app = Flask(__name__)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    value1 = 3
	value2 = 5
	counter = 0
	allValues = []
	newValue = 0

	while newValue < post_id:
		counter = counter + 1
		newValue = value1 * counter
		allValues.append(newValue)
		if counter / 3 == 0:
			newValue = value2 * counter
			allValues.append(newValue)

print (allValues)
print ("Sum of all Values is:", newValue)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
