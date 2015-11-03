# fibweb
A simple web app to return the Fibonacci sequence  
###Requirements:
##### from apt-get:
git  
pip  
libffi-dev   
libssl-dev  
python-dev  
#####from pip:
virtualenv  
virtualenvwrapper  

###Build and Run with VirtualEnv:  

```
mkvirtualenv fib1
git clone https://github.com/grahamgreen/fibweb.git 
cd fibweb
pip install -r requirements.txt
nosetests -v
python fib.py
```
If you're not into virtualenvs
###Build and Run without VirtualEnv:  
```
git clone https://github.com/grahamgreen/fibweb.git 
cd fibweb
pip install -r requirements.txt
nosetests -v
python fib.py
```

###Profit:
Point your browser at `http://<your ip>:5000/<a number>  `
e.g. http://127.0.0.1:5000/10  


####Bonus Points:
Crash your box by calculating a really big int.
