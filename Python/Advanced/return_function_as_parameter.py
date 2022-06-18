# Example 1 (simple)
def logger(msg):
    def log_message():
        print('Log:', msg)
    return log_message


log_hi = logger("Hi!")
log_hi()
print(logger)
print(log_hi)

# Example 2 (semi-practical)


def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}<{tag}>')
    return wrap_text


print_hi = html_tag('hi')
print_hi('Test Headline!')
print_hi('Another Headline!')

print_p = html_tag('p')
print_p('Test paragraph!')
print_hi('Another line!')
