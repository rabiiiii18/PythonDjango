#L5DJG1 - Summer django 2023 Herald College Kathmandu

To download and use this project: Follow the below-mentioned steps
# PythonDjango

## Clone the project
 to clone the project using SSH choose option bar 1 otherwise, you can go with option 2.
 - if you choose  option 1 you have to set up the SSH in your local machine and GitHub
 - Option 1
   ```
   git clone git@github.com:rabiiiii18/PythonDjango.git myproject
    ```
- Option 2
  ```
  git clone https://github.com/rabiiiii18/PythonDjango.git myproject
  ```

  ## Set the Environment
  - GO to myproject
    ```
     cd myproject
    ```
  - you can create virtual the virtualenv for the isolated environment. if you do not want to create the env you can skip the process click here here to know more details to create the virtual environment [https://github.com/rabiiiii18/PythonDjango.git](url)
  - Installing the dependency from the requirement file
    ```
    pip install -r requirements.txt
    ```
- Create the env file in the root project then populate it with the below data
- DATABASE=YOUR-DATABASE-URI
- SECRET_KEY=YOUR-SECRET-KEY
- EMAIL_BACKEND=YOUR-EMAIL-BACKEND
- EMAIL_HOST=YOUR-EMAIL-HOST
- EMAIL_HOST_USER=YOUR-EMAIL-ADDRESS
- EMAIL_HOST_PASSWORD=YOUR-EMAIL-PASSWORD
- EMAIL_PORT=YOUR-EMAIL-PORT
- EMAIL_USE_TLS=YOUR-BOOLEAN-VALUE
- DEFAULT_FROM_EMAIL=YOUR-DEFAULT-VALUE

## Run the project
  - Migrate the database
    
    ```
    python manage.py migrate
    ```
  - Run server
    
    ```
    python manage.py runserver
    ```
  - Nagivate to the localhost and enjoy 


## Main Feature
- User Management System.
- Dynamic Email Sending.
- CRUD operation for the Blog.


## Want to Collaborate
- You can add new feature, push to the new branch and send the pull request.

  
