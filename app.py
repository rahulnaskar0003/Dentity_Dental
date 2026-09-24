from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def home():
    return render_template('index.html', title='Home - Dentity Dental')

@app.route('/services')
def services():
    return render_template('services.html', title='Our Services - Dentity Dental')

@app.route('/treatments')
def treatments():
    return render_template('treatments.html', title='Our Treatments - Dentity Dental')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us - Dentity Dental')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        service = request.form.get('service')
        date = request.form.get('date')
        
        flash(f'Thank you {name}! Your appointment for {service} on {date} has been successfully requested. We will call you at {phone} shortly.', 'success')
        return redirect(url_for('contact'))
        
    return render_template('contact.html', title='Contact Us - Dentity Dental')

if __name__ == '__main__':
    app.run(debug=True)