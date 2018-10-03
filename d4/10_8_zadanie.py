# 2. Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:
#
#   #
#  ###
# #####
#

rows = int(input("Podaj wysokosc:\n "))

for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

