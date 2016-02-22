


# My Comments for the assignment:


    The main logic of the app is working, however I am unable to pass tests beyond registration checks because the test cannot seem to find my task creation form even though I specifically gave it the class "create-task".
    I honestly have no idea how to overcome this, I've tried everything I know. But hope you accept my code as it is.
    Thanks!



#My Code Strucure

    I decided to split my apps into two, splash and tasks. splash contains the models, views and html pertaining to users, login and registration. Once logged in, it will direct the user to the html i wrote in my tasks app.
    My tasks app contains models, views and htmls of Tasks, task creation and actions you can do to tasks. It imports the user models from the splash app.
    
#Custom User Model
    

    So I stupidly created a custom user model called 'myUser' just to get my email authentication to work. That's why is specified AUTH_USER_MODEL = 'splash.myUsers' in order for my authentications to work. 



To install this on c9, clone the repository. Then, before you run it
for the first time, you'd do

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
This installs your Python dependencies. Then you need to run your database
migrations with 

```
python manage.py migrate
```

This will create a file called `db.sqlite3`, which is ignored in your
`.gitignore` file. 

Now you're ready to run the application.Then you can run it with the following

```
python manage.py runserver 0.0.0.0:$PORT
```

Then you can click "Preview" in the c9 interface to see your running application.
Off to the races.

