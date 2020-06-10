import urllib.request
import urllib


# function to read in text from a file
def read_text():

    # open text file to check and makes it an Object
    text = open("/home/mark/GitRepos/course_udacity_prog_foundation_python/data/movie_quotes.txt")
    
    # read the text in the file
    text_contents = text.read()
    
    # close the file
    text.close()

    # check the profanoity using the function created below
    check_profanity(text_contents)


# function to check for profanity
def check_profanity(text_to_check):
    
    # pyth 3.#
    # create a connection that opens a url as an Object
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+urllib.parse.quote(text_to_check))
    
    #python 2.#
    # create a connection that opens a url as an Object
        #connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    
    # read connection out, will either be "true" or "false"
    output = connection.read()
    
    #close the connection
    connection.close()
    
    # print out result of scan. the 'b' is used becasue the open returns the text as a byte and not a string
    if b"true" in output:
        print("Warning!!! Warning!!! Profanity Alert!!!")
    elif b"false" in output:
        print("The document contains no bad words!")
    else:
        print("Couldn't scan the document properly.")
    
# run the shizzle
read_text()