from odwracacz import odwroc_zdanie

def czy_palindrom(zdanie):
    if zdanie == odwroc_zdanie(zdanie):
        return True
    else:
        return False

print(czy_palindrom('ala ma ala'))
print(czy_palindrom('ala mam ala'))

