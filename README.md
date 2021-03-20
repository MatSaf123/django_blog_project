# Django Blog

Blog web application powered by Django, created in group as a final project for Web Technologies course on University of Economics in Katowice.

To install required dependencies navigate to project's directory and run:

```cmd
pip install -r requirements.txt
```

To start up the server run:

```cmd
python manage.py runserver
```

# Functionality

- ##### User-side:
    - Creating account
    - Logging in/logging out
    - Resetting password if forgot (via mail)
    - Adding posts
    - Editing posts
    - Deleting posts
    - Adding/changing personal information on profile
    - Adding/changing profile photo
    
- ##### Admin-side:
    - All of above
    - Admin panel (allows managing database)
    - Export database to:
        - JSON
        - CSV
    
# Screenshots/GIFS

### Creating account
<div style="text-align:center">
    <img src="media/readme/register_1.png" width="450" height="400"/>
</div>

### Logging in
<div style="text-align:center">
    <img src="media/readme/login.gif" width="500" height="300"/>
</div>

### Main feed
<div style="text-align:center">
    <img src="media/readme/main_feed.png" width="500" height="250"/>
</div>

### Dark mode
<div style="text-align:center">
    <img src="media/readme/responsive_css.gif" width="500" height="300"/>
</div>

### Updated user profile
<div style="text-align:center">
    <img src="media/readme/photo_profile_updated.png" width="470" height="460"/>
</div>

### Creating and updating a post
<div style="text-align:center">
    <img src="media/readme/creating_updating_post.gif" width="600" height="370"/>
</div>

# Knows issues

- Sometimes CSS won't load and app will look all messed up. To fix it, delete browser cache or open blog in a new, private session/tab.