from subprocess import call

call(["amixer", "-D", "pulse", "sset", "Master", "0%"])

valid = False

while not False:
    volume = input("WHeat volume > ")

try:
    volume = int(volume)
    if (volume <= 100) and (volume >= 0):
        call(["amixer", "-D", "pulse", "sset", "Master", str(volume)+"%"])
        valid = True

except ValueError:
    pass
