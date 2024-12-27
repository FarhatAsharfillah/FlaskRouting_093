from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')  # Render file login.html di folder templates
@app.route('/success/<name>')
def success(name):
    return f'Welcome, {name}!'
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm')  # Ambil data dari POST
        print(f"POST received: {user}")  # Debugging
    else:
        user = request.args.get('nm')  # Ambil data dari GET
        print(f"GET received: {user}")  # Debugging  
    if user:
        return redirect(url_for('success', name=user))
    else:
        return "Error: Parameter 'nm' tidak ditemukan!"
if __name__ == '__main__':
    app.run(debug=True)
