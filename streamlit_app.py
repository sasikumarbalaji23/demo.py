import streamlit as st

class Library:

    def __init__(self, *data):
        self.booklist = list(data)

    def show_books(self):
        st.write("Books available in the library:")
        for i in self.booklist:
          st.write(i)

    def lend_a_book(self, bookname):
        if bookname in self.booklist:
            self.booklist.remove(bookname)
            st.success("Your request is fulfilled. Thank you!")
        else:
            st.error("Book is not available")

    def add_a_book(self, returned_book):
        self.booklist.append(returned_book)
        st.success("Book successfully added. Thank you!")


class Customer:
    def request_a_book(self):
      self.book = st.text_input("Request a Book Name")
      return self.book

    def return_a_book(self):
      self.book = st.text_input("Enter a Book Name")
      return self.book


all_books = ['Ponniyin Selvan', 'Thiyaga Bhoomi', 'Parthiban Kanavu', 'Alai Osai', 'Sivagamiyin Sabatham']

library = Library(*all_books)
customer = Customer()

st.title("Welcome to our Library Management System")

# option = st.sidebar.selectbox("Select an Option", ["Show Books", "Lend a Book", "Return a Book"])


tab1, tab2, tab3 = st.tabs(["Show Books", "Lend a Book", "Return a Book"])





with tab1:
  if st.button("Click to see Book List"):
    library.show_books()

with tab2:
  requested_book = customer.request_a_book()
  if requested_book:
    library.lend_a_book(requested_book)
    library.show_books()

with tab3:
  returned_book = customer.return_a_book()
  if returned_book:
    library.add_a_book(returned_book)
    library.show_books()

# else:
#     st.warning("Select a valid option from the sidebar!")






















# import streamlit as st

# # Define a session state variable to store the book list
# class SessionState:
#     def __init__(self):
#         self.booklist = ['Ponniyin Selvan', 'Thiyaga Bhoomi', 'Parthiban Kanavu', 'Alai Osai', 'Sivagamiyin Sabatham']

# # Create an instance of the SessionState
# session_state = SessionState()

# class Library:

#     def show_books(self):
#         st.write("Books available in the library:")
#         for i in session_state.booklist:
#             st.write(i)

#     def lend_a_book(self, bookname):
#         if bookname in session_state.booklist:
#             session_state.booklist.remove(bookname)
#             st.success("Your request is fulfilled. Thank you!")
#         else:
#             st.error("Book is not available")

#     def add_a_book(self, returned_book):
#         session_state.booklist.append(returned_book)
#         st.success("Book successfully added. Thank you!")

# class Customer:
#     def request_a_book(self):
#         return st.text_input("Enter the book you would like to borrow:")

#     def return_a_book(self):
#         return st.text_input("Enter the book you would like to return:")

# library = Library()
# customer = Customer()

# st.title("Library Management System")

# option = st.sidebar.selectbox("Select an Option", ["Show Books", "Lend a Book", "Return a Book"])

# if option == "Show Books":
#     library.show_books()
# elif option == "Lend a Book":
#     requested_book = customer.request_a_book()
#     if requested_book:
#         library.lend_a_book(requested_book)
# elif option == "Return a Book":
#     returned_book = customer.return_a_book()
#     if returned_book:
#         library.add_a_book(returned_book)
# else:
#     st.warning("Select a valid option from the sidebar.")


