#!/usr/bin/python3
from flask import Flask, request, redirect, render_template, url_for, make_response
import praw
from datetime import datetime
import time
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Get client ID and secret from environment variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
user_agent = "CleanSlate"
redirect_uri = "http://localhost:8080/reddit_callback"
all_scopes = ['creddits', 'edit', 'flair', 'history', 'identity', 'modconfig',
              'modcontributors', 'modflair', 'modlog', 'modothers', 'modposts',
              'modself', 'modwiki', 'mysubreddits', 'privatemessages', 'read',
              'report', 'save', 'submit', 'subscribe', 'vote', 'wikiedit',
              'wikiread']

# Initialize Reddit instance with environment variables
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    redirect_uri=redirect_uri
)

preview = {'reddit': {'comment': [], 'post': []},
           'discord': None,
           'twitter': None}


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
    # handle GET method
    code = request.args.get('code')
    if code:
        try:
            reddit.auth.authorize(code)
            user = reddit.user.me()
            return render_template('select_date.html', user=user.name)
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "Authorization failed. No code found."


@app.route('/preview_<platform>', methods=['POST'])
def preview_platform(platform):
    if platform == 'reddit':
        preview['reddit']['comment'] = []
        preview['reddit']['post'] = []
        selected_date = request.form['selected_date']
        # todo: add dates with the preview
        selected_datetime = datetime.strptime(selected_date, '%Y-%m-%d')
        selected_timestamp = time.mktime(selected_datetime.timetuple())
        user = reddit.user.me()
        comments = user.comments.new(limit=None)
        submissions = user.submissions.new(limit=None)
        for comment in comments:
            if comment.created_utc < selected_timestamp:
                preview['reddit']['comment'].append(comment)
        for submission in submissions:
            if submission.created_utc < selected_timestamp:
                preview['reddit']['post'].append(submission)
        return render_template('preview.html',
                               preview_reddit=preview['reddit'])
    else:
        return make_response("Platform doesn't exist", 404)


@app.route('/delete_<platform>', methods=['POST'])
def delete_platform(platform):
    # todo: hanldle errors
    # handle GET method (using browser)
    if (platform == 'reddit'):
        for comment in preview['reddit']['comment']:
            comment.delete()
        for submission in preview['reddit']['post']:
            submission.delete()
        preview['reddit']['comment'] = []
        preview['reddit']['post'] = []
        return render_template('deletion_completed.html')
    else:
        return make_response("Platform doesn't exist", 404)


if __name__ == '__main__':
    app.run(port=8080)
