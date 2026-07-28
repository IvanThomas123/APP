def login_required(func):
    def wrapper():
        if logged_in:
            func()
        else:
            print("Access denied. Please log in.")
    return wrapper

@login_required
def view_profile():
    print("Welcome to your profile")

logged_in = True
view_profile()
