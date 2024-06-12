# App Users part 1

# You have the next big thing on the interwebs.  But a thing isn't anything without users.  In your application, users can sign up with all kinds of valuable personal information like `name`, `email address`, `driver's licence number`, you name it.
# requirement part 1
# 1. Write a `User` class that can handle your growing application's needs.
# 2. Create a few users.

# App User part 2

# Add a method to your User class that allows for creating a new user post.
# Add any necessary instance properties to make step 1 work. What data structure should you use?
# Add a static variable that stores the posts from every user. What data structure should you use?
# Make sure that the the information stays in sync!
# Bonus
# Add a method that allows for deleting a post. Again, make sure that your information stays in sync.

class User:
    all_posts = []  # Class variable to store all posts from all users

    def __init__(self, name, email, drivers_licence=None):
        self.Name = name
        self.Email = email
        self.Drivers_liscence = drivers_licence
        self.User_posts = []  # User’s own list of posts
        # self.posts = []

    def create_a_post(self, content=None):
        """Create a post and add to the personal and global lists."""
        post = {"Author": self.Name, "Content": content}
        self.User_posts.append(post)
        # self.posts.append(post)
        User.all_posts.append(post)

    def delete_a_post(self, content=None):
        """Delete a post by content from personal and global lists."""
        self.User_posts = [
            post for post in self.User_posts if post["Content"] != content
        ]
        User.all_posts = [post for post in User.all_posts if post["Content"] != content]

    @classmethod
    def see_all_posts(cls):
        """Static method to display all posts from all users."""
        if cls.all_posts:
            print(f"\n{'DISPLAYING ALL POSTS':-^50}\n")
            for post in cls.all_posts:
                print(f"Author:{post['Author']}\nContent: {post['Content']}\n")
        else:
            print("No posts to display.")

    def see_my_posts(self):
        print(f"\n{'DISPLAYING ALL MY INDIVIDUAL POSTS':-^50}\n")
        for i in self.User_posts:
            print(f"Author: {i['Author']}\nContent:\n\t{i['Content']}\n")


# Create users
user1 = User("Alice Smith", "alice@example.com", "B1234567")
user2 = User("Bob Johnson", "bob@example.com”, “C2345678")
user3 = User("Carol Williams", "carol@example.com", "D3456789")
# Users creating posts
user1.create_a_post("Hello, this is Alice!")
user2.create_a_post("It’s a great day, says Bob.")
user3.create_a_post("Looking forward to the weekend, Carol here.")
# Display all posts
User.see_all_posts()
# User 1 deletes a post
user1.delete_a_post("Hello, this is Alice!")
user3.create_a_post("Another post from user 3")
User.see_all_posts()
user3.see_my_posts()
