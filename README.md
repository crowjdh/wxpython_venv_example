# wxpython_venv_example
wxPython with virtualenv setup example

# Instruction
1. Download and install repackaged wxPython from [here](https://drive.google.com/file/d/0B_pNwAeZ0TWYSG5jd2V3ck5aNmM/view?usp=sharing)
2. Clone this repo and open directory in terminal
```{r, engine='sh', count_lines}
MacBook-Pro:Python User$ git clone https://github.com/crowjdh/wxpython_venv_example.git
MacBook-Pro:Python User$ cd wxpython_venv_example/
MacBook-Pro:wxpython_venv_example User$ virtualenv venv
MacBook-Pro:wxpython_venv_example User$ source venv/bin/activate
(venv) MacBook-Pro:wxpython_venv_example User$ cat requirements.txt | xargs -n 1 pip install
(venv) MacBook-Pro:wxpython_venv_example User$ ./python test.py
```
