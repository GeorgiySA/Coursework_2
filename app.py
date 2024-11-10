from flask import Flask, request, render_template, jsonify
import logging
from utils import *


logging.basicConfig(filename="api.log", level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
app = Flask(__name__, template_folder='templates')

@app.route('/')  # Эта страница выводит все посты (без комментариев)
def main_page():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)

@app.route('/posts/<int:postid>')  # Эта страница выводит один пост по соответствующему номеру
def posts_page(postid):
    posts = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template("post.html", posts=posts, comments=comments)

@app.route('/search', methods=['GET', 'POST'])
def search_page():
    query = request.args.get('s')
    posts = search_for_posts(query)
    return render_template("search.html", posts=posts)

@app.route('/users/<username>')  # Эта страница выводит посты по имени пользователя
def user_page(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts)

@app.errorhandler(404)  # Это обработчик запросов к несуществующим страницам
def page_not_found(e):
    return "<h1>Статус-код: 404</h1><p>Такой страницы не существует</p>", 404

@app.errorhandler(500)  # Это обработчик ошибок, возникших на стороне сервера
def page_not_found(e):
    return "<h1>Статус-код: 500</h1><p>Где-то в коде закралась ошибка</p>", 500

@app.route('/api/posts')  # Возвращает полный список постов в виде JSON-списка
def api_posts():
    posts = get_posts_all()
    logging.info('Запрос /api/posts')
    return jsonify(posts)

@app.route('/api/posts/<int:postid>')  # Возвращает один пост в виде JSON-словаря
def api_post(postid):
    post = get_post_by_pk(postid)
    logging.info(f'Запрос /api/posts {postid}')
    return jsonify(post)

if __name__ == "__main__":
    app.run(port=5025)