from flask import request, Flask, render_template, redirect
import sqlite3
import os
from flask.helpers import flash, url_for


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
        """получение поста по id

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
        conn = sqlite3.connect("mydb.db")
        cur = conn.cursor()
        cur.execute("SELECT *, rowid FROM posts") # Getting all the posts from the sqlite3 database
        posts = cur.fetchall() # fetching all the posts from the database and assigning them to the posts variable
        cur.close()
        conn.close()
        return posts
    
    def create_post(self, title, content):
        conn = sqlite3.connect("mydb.db")
        cur = conn.cursor()
        # Adding the post to the database
        cur.execute("INSERT INTO posts (title, content) VALUES(?, ?)", (title, content))
        conn.commit()
        cur.close()
        conn.close()
    
    @staticmethod   
    def delete_post(post_id):
        conn = sqlite3.connect("mydb.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM posts WHERE rowid = ?", (str(post_id)))
        conn.commit()
        cur.close()
        conn.close()
        
    @staticmethod
    def edit_post(title, content, post_id):
        conn = sqlite3.connect("mydb.db")
        cur = conn.cursor()
        cur.execute("UPDATE posts SET title = ?, content = ? WHERE rowid = ?", (title, content, post_id))
        conn.commit()
        
        cur.close()
        conn.close()