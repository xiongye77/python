[cloud_user@ip-10-0-1-90 ~]$ more streams.py
import io

def copy_book(input, output):
    """
    write the input to the output
    """
    output.write(input.read())
    pass # student code here


if __name__ == "__main__":

    # author's novel is stored in file `book.txt`
    # create a copy of the book for the editing department
    # append _text to the end of the name of the copy
    # student input needed, please use book_input and book_copy
    # as the handles to the files


    # send to function `copy_book(input, output)`
    # make sure the cursor is at the start of each file

    # to test return each file to the head of the file
    book_input = open("book.txt", "r+b")
    book_copy = open("book_edit.txt", "w+b")

    copy_book(book_input, book_copy)

    book_input.seek(0)
    book_copy.seek(0)
    # test file exists
    try:
        f = open("book_edit.txt", "r+b")
    except FileNotFoundError:
        print("book_edit.txt does not exist")
    finally:
        f.close()

    assert book_input.read() == book_copy.read()
    book_stream = io.BytesIO()


    book_input.seek(0)
    copy_book(book_input, book_stream)

    book_stream.seek(0)
    book_input.seek(0)

    # test file exists
    # send to copy function


    # to test return each file to the head of the file

    # test file exists
    if not book_stream.readable():
        print("book_stream does not exist")
        exit(1)

    # test
    assert book_input.read() == book_stream.getvalue(), f"Expected: {book_copy.read()}\nGot: {book_stream.getvalue()}"

    # close all open files
   # close all open files
    book_input.close()
    book_copy.close()
    book_stream.close()
    # test
    assert book_input.closed == True, f"Expected: True \nGot: False"
    assert book_copy.closed == True, f"Expected: True \nGot: False"
    assert book_stream.closed == True, f"Expected: True \nGot: False"


