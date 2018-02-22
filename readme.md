# Cross Browser Testing
This program starts a local server and local tunnel, executes selenium test for different browsers on the local server and assert that page title is correct or not for the particular web page.It reads JSON file containing browsers detail from the cross-browser testing site and randomly select window browser, mac browser, and mobile device browser. It will then run selenium test on these browsers and assert page title for a predefined page.

# Prerequisites
You need to first create an account in browser testing site, crossbrowsertesting.com. You will have free access to test site for 7 days for trial purpose. Also, you need to install selenium web driver to run selenium test in python on the local server.
You need to replace each "<<username>>" in code by username and "<<password>>" by password, which you used to sign up on the website.

# Running the test
Below is the order of file execution.
* Run startserver.py file. This will start the local server on port 8000.
* Run starttunnel.py file. This will start tunnel between the local server and cross-browser testing site.
* Run assertpagetitle.py file. This will run selenium test on the local server and assert page title is correct or not for the predefined web page.

# Implementation
This project is written in python version 3.4. Some libraries may not support if python in your system is less than version 3.0.

# Methods Description:
File- startserver.py
* start_local_server() - This method runs local server on port 8000 using simpleHttpServer.

File - starttunnel.py
* start_cbt_tunnel() - This method creates a tunnel between the local server and cross-browser testing site and open local connection from the cross-browser testing site. We can run the live test, screenshot test and other tests from the cross-browser site in the local server.

File - assertpagetitle.py
* fetch_all_browsers(url)- This method reads the URL and extracts data from the URL path in JSON data format.

* get_random_browsers(names, browser_name, edevice) - This method takes all parameters defined in JSON file in the crossbrowser testing site, user-defined device names and browser types as input. It will return random browsers with all fields which match user-defined device names and types.

* test_CBT() - This method finds out the browser name for all device type and asserts page title for the particular webpage on random browsers selected by the program. It will assert page title as correct or not and print the result.
