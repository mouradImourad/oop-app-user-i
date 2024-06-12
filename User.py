# App Users

# You have the next big thing on the interwebs.  But a thing isn't anything without users.  In your application, users can sign up with all kinds of valuable personal information like `name`, `email address`, `driver's licence number`, you name it.
# requirement part 1
# 1. Write a `User` class that can handle your growing application's needs.
# 2. Create a few users.


class User:

    all_posts = [] 
    print(all_posts)

    def __init__(self, name, email, drivers_licence=None):
        self.name = name
        self.email = email
        self.drivers_license = drivers_licence
        self.posts = [] # add new propetry to the object "its own list" to add post

    def create_post(self,content):  # we will define instance method to create the post
        post = { 
            "Author" : self.name,
            "content" : content 
        }
        self.posts.append(post)
        User.all_posts.append(post) # add to the global variable
    
    # @staticmethod
    # def create_all_posts():
    #     if len(User.all_posts) > 0:
    #         for post in User.all_posts:
    #             print(f"Author: {post['author']}, Content: {post['content']}")
    #     else:
    #         print("No posts to display.")



# Requirements part 2
# Add a method to your User class that allows for creating a new user post.
# Add any necessary instance properties to make step 1 work. What data structure should you use?
# Add a static variable that stores the posts from every user. What data structure should you use?
# Make sure that the the information stays in sync!
# Bonus
# Add a method that allows for deleting a post. Again, make sure that your information stays in sync.



user1 = User("Alice Smith", "alice@example.com", "B1234567")
user2 = User("Bob Johnson", "bob@example.com", "C2345678")
user3 = User("Carol Williams", "carol@example.com", "D3456789")

