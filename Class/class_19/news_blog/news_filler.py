import GoogleNews

def fill_html(html_file, news):
    html_code = open(html_file, 'r').readlines()

    # Find the ul
    matched = False

    for ix, line in enumerate(html_code):
        line = line.strip()
        if line == '<ul class="newslist">':
            ul_start_ix = ix
            matched = True

        if matched and line == "</ul>":
            ul_stop_ix = ix

    # Clean it
    html_code = html_code[:ul_start_ix+1] + html_code[ul_stop_ix:]

    # Add my own news
    ul_indent = 0
    ul_line = html_code[ul_start_ix]

    for char in ul_line:
        if char.isspace():
            ul_indent += 1
        else:
            break

    li_indent = " "*ul_indent + "\t"
    for new in news[::-1]:
        title, link = new
        html_new = "{}<li><a href={}>{}</a></li>\n".format(li_indent,link,
                                                           title)
        html_code.insert(ul_start_ix+1, html_new)

    # Put the new html code in the file
    with open(html_file,'w') as f:
        for line in html_code:
            f.write(line)

html_file = r'/home/pi/Documents/work/dev_institute/Courses/2python/Class/class_19/news_blog/homepage.html'

searched_word = "business"

news_wrapper = GoogleNews.GoogleNews()
news_wrapper.search(searched_word)

for page_ix in range(2,10):
    news_wrapper.getpage(page_ix)
    print("Fetched page", page_ix)

search_result = news_wrapper.result()
news_wrapper.clear()

news = []

for news_dict in search_result:
    title = news_dict['title']
    link  = news_dict['link']
    news.append((title, link))

fill_html(html_file, news)















