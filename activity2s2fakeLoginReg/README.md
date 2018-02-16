Activity for this week - Create a fake login page that registers user data or "logs" users in. Data wil be stored in session 

Should have 4 routes - 
"/" -> 
    Checks if a user has "logged on", if they have redirect to "/home" otherwise render html for login and registration
"/process_form/<action>" ->
    Either checks user info is in session or creates a new user. 

    Registration should check to see if information is a duplicate or not.

    Login should check that email and password match then store email in session data for later retrieval. Upon loggin in, should redirect to "/home"

"/registered" -> 
    renders html to displays all registered users

"/home" -> 
    renders html that uses stored data in session to grab full data from
