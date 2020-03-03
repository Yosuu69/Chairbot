import praw

# reddit api login
reddit = praw.Reddit(client_id='lWCCgPYpUWPE9A', client_secret='cDwYFiOoMubsM9rj-eOFPhkihHU',
                     username='ChairBot_', password='chairbot69', user_agent='ChairBot by u/EvilTacoMan7533')
isComment = True

# subreddits
subreddit = reddit.subreddit('dankmemes+memes+pewdiepiesubmissions+antimeme')

# keyphrase
keyphrase = '!DankChair'

# look for phrase and reply appropriately
for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        word = comment.body.replace(keyphrase, '')
        try:
            if isComment:
                reply = 'https://imgur.com/gallery/n1UDyJp                                     Beep Boop, I was created by u/EvilTacoMan7533'
                comment.reply(reply)
                print('posted')
            else:
                print('postedno')
        except:
            print('to frequent')
