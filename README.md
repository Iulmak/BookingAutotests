In order to run the tests, you should perform the following steps:
1.Setting up the environment: install python 3.8, pip
2.Install dependencies: run 'pip install-r requirements.txt'
3.Download and install Selenium Driver for Chrome(chromedriver) and FireFox(geckodriver). Put them to the directory specified in PATH.
4.To run the tests, run the command "python main.py"
5.The browser and the path to the directory with reports are set using environment variables: BROWSER and REPORT_DIR. 
By default, the browser is set to "CHROME" and directory with reports is current directory.