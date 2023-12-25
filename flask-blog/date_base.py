from flask import request, Flask, render_template, redirect
import sqlite3
import os
from flask.helpers import flash, url_for
from flask_sqlalchemy import SQLAlchemy


class Db():
    def db(self):
        """_summary_
        """
        if  "mydb.db" not in os.listdir():
            conn = sqlite3.connect("mydb.db")
            db = conn.cursor()
            db.execute("CREATE TABLE posts (title TEXT, content TEXT, date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)")
            conn.commit()
            conn.close()
    
    @staticmethod
    def display_post(post_id):
        """
        получение поста по id
        Args:
            post_id (_type_): id поста
        """
        conn = sqlite3.connect("mydb.db")
        cur = conn.cursor()
        post = cur.execute("SELECT * FROM posts WHERE rowid = ?", (str(post_id))).fetchone() # Notice the fetchone() fucntion
        conn.commit()
        conn.close()
        return post
    
    def display_posts(self):
        """
        Показывает на экране все созданные посты
        """
        conn = sqlite3.connect("mydb.db")
        cur = conn.cursor()
        cur.execute("SELECT *, rowid FROM posts") # Получение всех записей из базы данных sqlite3
        posts = cur.fetchall() # извлекаем все записи из базы данных и присваиваем их переменной posts
        cur.close()
        conn.close()
        return posts
    
    def create_post(self, title, content):
        """
        Показывает один определённый пост
        Args:
            title (_type_): Заголовок
            content (_type_): Текст поста
        """
        conn = sqlite3.connect("mydb.db")
        cur = conn.cursor()
        # Adding the post to the database
        cur.execute("INSERT INTO posts (title, content) VALUES(?, ?)", (title, content))
        conn.commit()
        cur.close()
        conn.close()
    
    @staticmethod   
    def delete_post(post_id):
        """удаляет определённый пост по id

        Args:
            post_id (_type_): id поста
        """
        conn = sqlite3.connect("mydb.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM posts WHERE rowid = ?", (str(post_id)))
        conn.commit()
        cur.close()
        conn.close()
        
    @staticmethod
    def edit_post(title, content, post_id):
        """Корректировка поста

        Args:
            title (_type_): Заголовок
            content (_type_): Текст поста
            post_id (_type_): id поста
        """
        conn = sqlite3.connect("mydb.db")
        cur = conn.cursor()
        cur.execute("UPDATE posts SET title = ?, content = ? WHERE rowid = ?", (title, content, post_id))
        conn.commit()        
        cur.close()
        conn.close()
        
