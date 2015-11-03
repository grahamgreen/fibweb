from flask import Flask
app = Flask(__name__)

def fib(n):
    if n == 0:
        return "fail"
    elif n == 1:
        return "0"
    elif n == 2:
        return "0 1"
    else:
        fib_list = [0, 1]
        for i in range(2,n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return ' '.join(map(str, fib_list))




@app.route('/<int:num>')
def fibMain(num):
    return fib(num)

if __name__== "__main__":
    app.run(debug=True)
