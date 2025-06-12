#!/usr/bin/python3
"""
Task 2: Consume and process API data using Python's requests module.
Fetches posts from JSONPlaceholder, prints titles, and saves to CSV.
"""

import requests
import csv

def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    Fetches posts and saves them as a CSV file (posts.csv).
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        structured_data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_data)

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
"""
Task 2: Consume and process API data using Python's requests module.
"""

import requests
import csv

def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints their titles.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    Fetches posts and saves them as a CSV file.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if response.status_code == 200:
        posts = response.json()
        structured_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]
        
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(structured_data)
