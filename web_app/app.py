#!/usr/bin/python3
from flask import Flask, request, redirect, render_template, url_for
import praw
from datetime import datetime
import time

app = Flask(__name__)


# todo: secure way to handle client id & secret
client_id = "-9mNQLNIHMFPHlR1mqOomQ"
client_secret = "CiaI_lwcRdSPTEi7JMsf4sRtilby1Q"
user_agent = "CleanSlate"
redirect_uri = "http://localhost:8080/reddit_callback"
all_scopes = ['creddits', 'edit', 'flair', 'history', 'identity', 'modconfig',
              'modcontributors', 'modflair', 'modlog', 'modothers', 'modposts',
              'modself', 'modwiki', 'mysubreddits', 'privatemessages', 'read',
              'report', 'save', 'submit', 'subscribe', 'vote', 'wikiedit',
              'wikiread']

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    redirect_uri=redirect_uri,
)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/reddit_auth')
def reddit_auth():
    auth_url = reddit.auth.url(scopes=all_scopes,
                               state="random_state", duration="permanent")
    return redirect(auth_url)


@app.route('/reddit_callback')
def reddit_callback():
    code = request.args.get('code')
    if code:
        try:
            reddit.auth.authorize(code)
            user = reddit.user.me()
            return render_template('reddit_select_date.html', user=user.name)
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "Authorization failed. No code found."


@app.route('/reddit_delete', methods=['POST'])
def reddit_delete():
    # todo: hanldle errors
    selected_date = request.form['selected_date']
    selected_datetime = datetime.strptime(selected_date, '%Y-%m-%d')
    selected_timestamp = time.mktime(selected_datetime.timetuple())
    user = reddit.user.me()
    comments = user.comments.new(limit=None)
    submissions = user.submissions.new(limit=None)
    for comment in comments:
        if comment.created_utc < selected_timestamp:
            comment.delete()
    for submission in submissions:
        if submission.created_utc < selected_timestamp:
            submission.delete()
    # todo: preview of comments before deletion
    return f"Deleted comments and posts before {selected_date} for user {user.name}."


if __name__ == '__main__':
    app.run(port=8080)
