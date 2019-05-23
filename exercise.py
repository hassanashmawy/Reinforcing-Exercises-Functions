def word_counter(my_string):
    my_length = 0
    my_list = my_string.split(' ')
    if my_list[0] != '':
        my_length = len(my_list)
    print(my_length)


word_counter("Hello world") 
word_counter("This is a sentence")
word_counter("")
