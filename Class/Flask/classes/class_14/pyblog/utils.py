def cowsay(message):
    max_len = 40
    msg_list = []
    line = ""

    messages_as_list = message.split(' ')

    for word in messages_as_list:
        if len(line) + len(word) > max_len:
            msg_list.append(line)
            line = ""
        line += word + " "

    msg_list.append(line)

    wrapped_msg = '\n'.join(msg_list)

    lines_nb = len(msg_list)
    line_len = len(msg_list[0])

    cow_msg = ""
    cow_msg += " "+"-"*(line_len+1)+" "+"\n"

    # Case 1: The message is only one line
    if lines_nb == 1:
        cow_msg += "< {} >\n".format(msg_list[0])

    # Case 2: The message is only two lines
    elif lines_nb == 2:
        cow_msg += "/ {}{} \\".format(msg_list[0], ' '*(max_len-len(msg_list[1]))) + "\n"
        cow_msg += "\ {}{} /".format(msg_list[1], ' '*(max_len-len(msg_list[1]))) + "\n"

    # Case 3: The message is more than two lines
    elif lines_nb > 2:
        cow_msg += "/ {}{} \\".format(msg_list[0], ' '*(max_len-len(msg_list[1]))) + "\n"
        for msg in msg_list[1:-1]:
            cow_msg += "| {}{} |".format(msg, ' '*(max_len-len(msg_list[1]))) + '\n'

        cow_msg += "\ {}{} /".format(msg_list[-1], ' '*(max_len-len(msg_list[-1]))) + "\n"
    # Add the underline
    cow_msg += " "+"-"*(line_len+1)+" "+"\n"

    cow_msg += r"       \   ^__^" + "\n"
    cow_msg += r"        \  (oo)\_______" + "\n"
    cow_msg += "           (__)\       )\/\\" + "\n"
    cow_msg += r"                ||----w |" + "\n"
    cow_msg += r"                ||     ||" + "\n"

    return cow_msg 

print(cowsay("Helloworld i am eyal and i love python, i also like greta but micheal doesn't"))

#  _____________
# < Hello world >
#  -------------
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||
