# https://www.safaribooksonline.com/library/view/flask-framework-cookbook/9781783983407/ch01s07.html

from my_app import application

# run the app.
if __name__ == "__main__":
    # app.run(debug=True, port=5002)
    application.run()