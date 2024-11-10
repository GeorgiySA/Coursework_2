import json


def get_posts_all():  # Считывает из json файла все посты
    with open('data/posts.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_comments_all():  # Считывает из json файла все комменты
    with open('data/comments.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_posts_by_user(user_name):  # Возвращает посты определенного пользователя
    data_post = []
    for post in get_posts_all():
        if user_name.lower() == post['poster_name'].lower():
            data_post.append(post)
    if len(data_post) == 0:
        return []
    return data_post

def get_comments_by_post_id(post_id):  # Возвращает комментарии определенного поста
    allowed_posts = False
    allowed_comments = []
    for comment in get_comments_all():
        if post_id == comment['post_id']:
            allowed_comments.append(comment)
    for post in get_posts_all():
        if post_id == post['pk']:
            allowed_posts = True
    if not allowed_posts:
        raise ValueError ('Post not found')
    elif len(allowed_comments) == 0:
        return allowed_comments
    return allowed_comments

def search_for_posts(query):  # Возвращает список постов по ключевому слову
    return [i for i in get_posts_all() if query.lower() in i['content'].lower()]

def get_post_by_pk(pk):  # Возвращает один пост по его идентификатору
    return [i for i in get_posts_all() if pk == i['pk']]

# q = get_post_by_pk(1)
# print(q)