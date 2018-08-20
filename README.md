# feature-request
A web application that allows the user to create "feature requests".

== Steps to install and run this feature request app ==

The app was developed and tested on Ubuntu 16.04.3 LTS Linux utilizing Python
virtualenv based on Python 3.5.2.  Newer versions should work just fine.
When I get a chance I'll try this on a Windows machine and update this README.

Make a new directory and clone the repository.

    ~$ mkdir fapp
    ~$ cd fapp/
    ~/fapp$ git clone git@github.com:brucev3/feature-request.git

Create a Python virtual environment at the root of the project.

    ~/fapp$ cd feature-request/
    ~/fapp/feature-request$ which virtualenv

        No virtualenv?

    ~/fapp/feature-request$  ~/fapp/feature-request$ sudo apt install virtualenv
    ~/fapp/feature-request$ which virtualenv
    /usr/local/bin/virtualenv
    ~/fapp/feature-request$ virtualenv venv
    Using base prefix '/usr'
    New python executable in /home/bdv/fapp/feature-request/venv/bin/python3.5
    Also creating executable in /home/bdv/fapp/feature-request/venv/bin/python
    Installing setuptools, pip, wheel...done.

Activate the virtual environment.

    ~/fapp/feature-request$ source venv/bin/activate
    (venv) ~/fapp/feature-request$

Install additional Python modules in the virtual environment the app needs.

    (venv) ~/fapp/feature-request$ pip install -r requirements.txt

Run the app.

    (venv) ~/fapp/feature-request$ python run.py
    /home/bdv/fapp/feature-request/venv/lib/python3.5/site-packages/flask_sqlalchemy/__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
      'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
     * Serving Flask app "my_app" (lazy loading)
     * Environment: production
       WARNING: Do not use the development server in a production environment.
       Use a production WSGI server instead.
     * Debug mode: on
     * Running on http://127.0.0.1:5002/ (Press CTRL+C to quit)
     * Restarting with stat
    /home/bdv/fapp/feature-request/venv/lib/python3.5/site-packages/flask_sqlalchemy/__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
      'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
     * Debugger is active!
     * Debugger PIN: 147-968-870

You can see app is available at http://127.0.0.1:5002/ point your browser there.

Ctrl + c will kill the app.

    ^C(venv) ~/fapp/feature-request$

Run the unit tests.

    (venv) ~/fapp/feature-request$ nosetests -v
    /home/bdv/fapp/feature-request/venv/lib/python3.5/site-packages/flask_sqlalchemy/__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
      'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
    Test Feature page ... ok
    Test Featureslist page ... ok
    Test Featureslist page one ... ok
    test_home (my_app.app_test.FeaturesTestCase) ... ok

    ----------------------------------------------------------------------
    Ran 4 tests in 0.422s

    OK
    (venv) ~/fapp/feature-request$

Deactivate the virtual environment.

    (venv) ~/fapp/feature-request$ deactivate
    ~/fapp/feature-request$

You may want to delete the database.

    ~/fapp/feature-request$ rm my_app/features.db
