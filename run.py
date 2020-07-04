from app import create_app

config_name = 'development'
app = create_app(config_name)

@app.route('/')
def home():
    return 'Hi'

if __name__=='main':
    app.run()