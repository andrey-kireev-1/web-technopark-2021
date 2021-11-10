from django import template

register = template.Library()

tags_names_test = {'first_line': ['perl', 'Python', 'TechnoPark'],
                    'second_line': ['MySQL', 'django'],
                    'third_line': ['Mail.Ru', 'Voloshin', 'Firefox']
                    }

best_user_names_test = ['Mr.Freeman', 'Dr.House', 'Bender', 'Queen Victoria', 'V.Pupkin']

@register.simple_tag()
def show_tags():
    tags = tags_names_test
    return tags

@register.simple_tag()
def show_best_users():
    usnames = best_user_names_test
    return usnames