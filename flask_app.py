from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")

@app.route('/contact', methods=['POST'])
def contact():
    with open('my_contacts.txt', 'a') as f :
        f.write(request.form['name'] + '\n')
        f.write(request.form['phone'] + '\n')
        f.write(request.form['email'] + '\n')
        f.write(request.form['message'] + '\n'+'\n')
    return 'message sent'



if __name__ == '__main__':
    app.run()
