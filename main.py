import instaloader

def insta_collector(request):
    L = instaloader.Instaloader()

    if request_args and 'handle' in request_args and 'lastname' in request_args:
        handle = request_args['handle']
    PROFILE = handle
    profile = instaloader.Profile.from_username(L.context, PROFILE)

    posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes, reverse=True)

    for post in posts_sorted_by_likes:
        L.download_post(post, PROFILE)