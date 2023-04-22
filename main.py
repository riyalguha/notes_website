# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from website.__init__ import create_app
import secrets
app=create_app()

if __name__=='__main__':
    # app.secret_key = secrets.token_hex(16)
    app.run(debug=True)


# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
