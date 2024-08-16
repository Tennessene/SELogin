StackAutoLogin
==========
Automatically log in to your Stack Exchange sites every day!
--------------------------------------------------

StackAutoLogin (SAL) is a Python script that in combination with a GitHub workflow, allows you to log in to your Stack Exchange sites every day. This allows you to continue your consecutive visited days no matter what happens.

SAL uses the Python [selenium webDriver](https://www.selenium.dev/documentation/webdriver/) and [ChromeDriver](https://developer.chrome.com/docs/chromedriver) to browse the web without a human! First, it logs into the Stack Exchange website. Then, it goes to the Meta Stack Exchange website. It will visit any other SE websites you put in the `SITES` repository secret along with their Meta sites!

Setup
------

**NOTE**: If you log in using Google, that won't work with SAL. You can easily configure your account to be able to log in without Google (in addition to logging in with Google) by making a password for normal login. Put in your email and click "Forgot Password." Remember the password for setting SAL up.

### Providing Information

You must provide your credentials by putting your email and password into [actions repository secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository).

Put your email into a secret with the name `EMAIL`

![Email Secret](https://i.sstatic.net/515cluLH.png)

And your password into a secret named `PASSWORD`

![Password Secret](https://i.sstatic.net/518N2atH.png)

Any other sites you would like SAL to log in to you must put into a secret named `SITES`. They must be the domain of the site without ".com". For example, for Ask Ubuntu, it's domain is `askubuntu.com`. Use `askubuntu`. Or for Apple Stack Exchange, its domain is `apple.stackexchange.com`. Use `apple.stackexchange`.

Your final `SITES` secret may look something like this:

![Sites Secret](https://i.sstatic.net/JfIQkLF2.png)

Your secrets list should look like this:

![Repository Secrets](https://i.sstatic.net/f8izJw6t.png)

### Watch it Work
After this, you can sit back and relax as it logs in at 00:00 UTC every day.

Running Locally
------
If you would like to try it out on your computer, you must create a virtual Python environment and install the selenium (just like the Action does every time it runs).

### Creating Environment on Linux
**NOTE**: You may need the `python3-venv` package before being able to create a virtual environment. 
```bash
sudo apt update && sudo apt install python3-venv
```
Create the virtual environment. Try `python3` instead of `python` if it doesn't work
```bash
python -m venv venv
```

Activate the environment
```bash
source ./venv/bin/activate
```

Edit environment file
```bash
sudo nano /etc/environment
```

Add environment variables to file
```bash
EMAIL=myemail@example.com
PASSWORD=mypassword
SITES="stackoverflow, superuser, serverfault, gaming.stackexchange, gamedev.stackexchange, apple.stackexchange, security.stackexchange, askubuntu, english.stackexchange, unix.stackexchange, raspberrypi.stackexchange, diy.stackexchange, photo.stackexchange"
```

When you're finished press `CTRL + X` and then `Y`.

### Creating Environment on Windows
Create the virtual environment
```bash
python -m venv venv
```

Activate the environment
```bash
.\venv\Scripts\activate
```

Set environment variables
```bash
setx EMAIL myemail@example.com /m
```

```bash
setx PASSWORD mypassword /m
```

```bash
setx SITES "stackoverflow, superuser, serverfault, gaming.stackexchange, gamedev.stackexchange, apple.stackexchange, security.stackexchange, askubuntu, english.stackexchange, unix.stackexchange, raspberrypi.stackexchange, diy.stackexchange, photo.stackexchange" /m
```

### Running
Install selenium
```bash
pip install -r requirements.txt
```
Run SAL with the unbuffered option. It makes it so the log outputs things right away
```bash
python -u main.py
```

### Debugging

You can see SAL working in your browser

Go to chrome://inspect, click `Configure`, add `127.0.0.1:9222`, and click done. A "remote target" should pop up. When it does, click `Inspect`.

Now you can watch SAL browse the web live!

SAL also saves a screenshot as `stackexchange.png` so you can see right away if it successfully logged in or not.

(c) 2024 Anston Sorensen
