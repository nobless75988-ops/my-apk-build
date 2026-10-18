import os
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
# Session စီမံဖို့ Secret Key သတ်မှတ်ခြင်း
app.secret_key = 'super_secret_key_change_this'

# စမ်းသပ်ရန် Username နဲ့ Password (စိတ်ကြိုက် ပြောင်းနိုင်ပါတယ်)
USER_DATA = {
    "admin": "password123"
}

@app.route('/')
def home():
    if 'username' in session:
        return f'''
            <h2>မင်္ဂလာပါ {session['username']}! Login အောင်မြင်ပါသည်။</h2>
            <a href="/logout"><button>Logout ထွက်ရန်</button></a>
        '''
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Username နဲ့ Password စစ်ဆေးခြင်း
        if username in USER_DATA and USER_DATA[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Username သို့မဟုတ် Password မှားယွင်းနေပါသည်။', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Cloud Platform တွေမှာ Run နိုင်ဖို့ PORT Environment variable ကို ယူသုံးပေးခြင်း
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
