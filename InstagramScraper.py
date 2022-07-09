import instaloader
from itertools import islice
# from datetime import datetime, timedelta
# from itertools import takewhile


def insta_follower_data():
    log = instaloader.Instaloader()

    # login data
    username = "username"
    password = "password"
    # actual login
    log.login(username, password)

    # Profile data
    profile = instaloader.Profile.from_username(log.context, "account")

    # Print list of followers
    follow_list = []
    count = 0
    for followers in profile.get_followers():
        follow_list.append(followers.username)
        file = open("user_followers.txt", "a+")
        file.write(follow_list[count])
        file.write("\n")
        file.close()
        print(follow_list[count])
        count = count + 1


def insta_post_likes():
    log = instaloader.Instaloader()

    # login data
    username = "username"
    password = "password"
    # actual login
    log.login(username, password)

    profile = instaloader.Profile.from_username(log.context, "account")

    likes = set()
    print('Fetching likes of all posts of profile {}.'.format(profile.username))
    # this allows a certain timeline for a specific post
    # NOW = datetime.now()
    # for post in takewhile(lambda p: NOW - p.date < timedelta(days=7), profile.get_posts()):
    for post in islice(profile.get_posts(), 2):
        print(post)
        likes = likes | set(post.get_likes())

    # print('Storing names into a file.')
    with open('post_likes.txt', 'a+') as file:
        for liker in likes:
            file.write(liker.username)
            file.write("\n")
            # file.close()
            print(liker.username, file=file)


insta_post_likes()
insta_follower_data()
