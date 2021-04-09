meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
date = input("escriba la fecha en formato dd/mm/aaaa por favor ")
date = date.split("/")
print(date[0], " de ", meses[int(date[1])], " del ", date[2])