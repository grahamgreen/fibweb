# fibweb
A simple web app to return the Fibonacci sequence  
###Requirements:
pip  
virtualenv  
virtualenvwrapper  


###Build:  

```
export WORKON_HOME=~/Envs  
mkdir -p $WORKON_HOME  
source /usr/local/bin/virtualenvwrapper.sh  
mkvirtualenv fib1
git clone git@github.com:grahamgreen/fibweb.git  
cd fibweb
pip install -r requirements.txt
python fib.py
```
