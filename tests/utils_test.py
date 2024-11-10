from coursework2_source.utils import *
import pytest


def test_get_posts_all():
    assert type(get_posts_all()) == list
    assert type(get_posts_all()[0]) == dict

def test_get_comments_all():
    assert type(get_comments_all()) == list
    assert type(get_comments_all()[0]) == dict

def test_get_posts_by_user():
    assert len(get_posts_by_user('leo')) == 2
    assert type(get_posts_by_user('leo')) == list
    assert type(get_posts_by_user('leo')[0]) == dict

def test_get_comments_by_post_id():
    assert type(get_comments_by_post_id(1)) == list
    assert type(get_comments_by_post_id(1)[0]) == dict
    assert len(get_comments_by_post_id(1)) == 4
    assert get_comments_by_post_id(8) == []
    with pytest.raises(ValueError):
        get_comments_by_post_id(11)

def test_search_for_posts():
    assert type(search_for_posts('д')) == list
    assert type(search_for_posts('д')[0]) == dict
    assert len(search_for_posts('очень')) == 3

def test_get_post_by_pk():
    assert type(get_post_by_pk(3)) == list
    assert type(get_post_by_pk(3)[0]) == dict
    assert len(get_post_by_pk(3)) == 1

