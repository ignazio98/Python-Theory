first_name = 'Christopher'
last_name = 'Harrison'

print(first_name + ' ' + last_name + '\n')

#output format

#output = 'Hello, ' + first_name + ' ' + last_name
#output = 'Hello, {} {}'.format(first_name, last_name)
output = 'Hello, {1} {0}'.format(first_name, last_name)

#output = f'Hello, {first_name} {last_name}'

print(output)