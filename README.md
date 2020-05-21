# Windows Server Drive Space Checker

This program will sends an email when the space run below than 15G! You can set another value for space checker in this program.
Also you can use windows scheduler to repeat the cycle of checking every day or hour to send you and alert email.

## How to run

```bash
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python SpaceMailer.py <example@gmail.com> <password>
```
