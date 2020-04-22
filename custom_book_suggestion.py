# import pandas as pd
#
#
# def custom_book_search(gen, lan,title):
#
#     df_custom_book = pd.read_csv("C:/Users/Nikhita/Desktop/Dataset/Final/final_book_details.csv")
#
#     if gen !="":
#         cst_book = df_custom_book[(df_custom_book['genres'] == gen) &
#                               (df_custom_book['language_code'] == lan)]
#     if title !="":
#         cst_book = df_custom_book[(df_custom_book['book_title'] == title)]
#
#
#
#     cst_book.to_csv("C:/Users/Nikhita/Desktop/Dataset/Final/custom_book.csv")
#     return cst_book
#
#
# b = custom_book_search("young adult", "eng")
