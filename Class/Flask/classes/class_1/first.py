import jinja2

name = "Eyal Shukrun"
fav_languages = ['python','c++','java']
images = ['dog', 'cat', 'bird', 'reuven']


template =  """

{% if title %}
    <h1>{{ title }} </h1>
{% else %}
    <h1>Hello World!</h1>
{% endif %}

{% for img in img_list %}
    <img src="https://google.images.com/{{ img }}.png" />
{% endfor %}

<p>Hello, I am {{ username }}, here is a list of my favourite languages:</p>
<ol>
    {% for element in languages %}
        <li>{{ element }}</li>
    {% endfor %}
</ol>
<p>Thanks for visiting my site</p>
"""

html = jinja2.Template(template).render(username=name,
                                        title="Hello from eyal",
                                        languages=fav_languages,
                                        img_list = images

                                       )

print("############# MY HTML FILE ##############\n")
print(html)
print("############# END OF HTML  ##############\n")


print("Finish")








