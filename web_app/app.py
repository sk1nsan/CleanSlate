#!/usr/bin/python3
from flask import Flask, request, redirect, render_template, url_for
import praw

app = Flask(__name__)

# todo: secure way to handle client id & secret
client_id="-9mNQLNIHMFPHlR1mqOomQ"
client_secret="CiaI_lwcRdSPTEi7JMsf4sRtilby1Q"
user_agent = "CleanSlate"
redirect_uri = "http://localhost:8080/reddit_callback"

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    redirect_uri=redirect_uri,
)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reddit_auth')
def reddit_auth():
    auth_url = reddit.auth.url(scopes=["identity"], state="random_state", duration="permanent")
    return redirect(auth_url)

@app.route('/reddit_callback')
def reddit_callback():
    code = request.args.get('code')
    if code:
        try:
            access_token = reddit.auth.authorize(code)
            user = reddit.user.me()
            return f"Authenticated as: {user.name}"
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "Authorization failed. No code found."

if __name__ == '__main__':
    app.run(port=8080)
