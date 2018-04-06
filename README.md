
# Password Strength Calculator  
  
CLI for checking password strength.
It utilizes an algorithm described on [wiki](https://en.wikipedia.org/wiki/Password_strength) based on calculation of information entropy.
# Usage
It should be run on python 3.5. 
```bash
$ python3 password_strength.py -p easypass

Your password: easypass 
is weak and has score: 3 
out of 10


$ python3 password_strength.py --password Very_st0ng_pa$$w0rd_%$!_Really_strong!

Your password: Very_st0ng_pa9718w0rd_%_Really_strong! 
is very strong and has score: 10 
out of 10

```
  
# Project Goals  
  
The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)