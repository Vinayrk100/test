import pandas as pd


# def read_book_details(gen, cust_title, lan, title, uid):
# def read_book_details(cust_title, title, uid):
def read_book_details(title, uid):
    # df_custom_book = pd.read_csv("C:/Users/Nikhita/Desktop/Dataset/Final/final_book_details.csv")
    # df_unique_book = pd.read_csv("C:/Users/Nikhita/Desktop/Dataset/Final/unique_books.csv")
    # df_unique_user = pd.read_csv("C:/Users/Nikhita/Desktop/Dataset/Final/user_details.csv")

    df_custom_book = pd.read_csv("s3://admfinalproject/Dataset/final_book_details.csv")
    df_unique_book = pd.read_csv("s3://admfinalproject/Dataset/unique_books.csv")
    df_unique_user = pd.read_csv("s3://admfinalproject/Dataset/user_details.csv")

    lst_user = df_unique_user[df_unique_user['user_id'] == uid]

    # if gen != "" and cust_title != "" and lan != "":
    #     lst_book = df_custom_book[(df_custom_book['genres'] == gen) &
    #                               (df_custom_book['language_code'] == lan) &
    #                               (df_custom_book['book_title'] == cust_title)]

    # if cust_title != "" :
    #         # and gen == "" and lan == "":
    #     lst_book = df_unique_book[df_unique_book['book_title'] == cust_title.casefold()]

    # if cust_title == "" and gen != "" and lan != "":
    #     lst_book = df_custom_book[(df_custom_book['genres'] == gen) &
    #                               (df_custom_book['language_code'] == lan)]

    if title != "" :
            # and cust_title == "" and gen == "" and lan == "":
        lst_book = df_unique_book[df_unique_book['book_title'] == title.casefold()]
        lst_book['Price'].astype(int)

    return lst_book, lst_user
