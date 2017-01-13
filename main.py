import praw
import datetime
import mail

reddit = praw.Reddit('bot')
input_sub = input("enter subreddit to check ")
subreddit = reddit.subreddit(input_sub)

for submission in subreddit.top(time_filter="day", limit = 5):
	if submission==0:
		print("no submissions")

	date = datetime.datetime.fromtimestamp(submission.created_utc)
	now = datetime.datetime.utcnow()
	if(date.day == now.day and date.month == now.month):
		mail.send_mail(input_sub)
	print("Title: ", submission.title)
	print("Score: ", submission.score)
	print("---------------------------------\n")
		