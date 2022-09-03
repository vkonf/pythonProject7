from django import template

register = template.Library()



@register.filter()
def censor(value):


   # 1 вариант фильтра
   # Недостаток: не заменит со смешанным регистром - "СмЕрКалоСь"

   # badword = ['Смеркалось', 'Кирпич', 'вдруг']
   #
   # worlds=list(map(str.capitalize, badword))
   #
   # c = value
   #
   # worlds_low=list(map(str.lower, worlds))
   # worlds_upper=list(map(str.upper, worlds))
   #
   # for i in range(len(worlds)):
   #    l1 = len(worlds[i])
   #    w1 = worlds[i]
   #    w2 = worlds_low[i]
   #    w3 = worlds_upper[i]
   #
   #    a = c.replace(worlds_upper[i], w3[0] + "*" * l1)
   #    b = a.replace(worlds_low[i], w2[0] + "*" * l1)
   #    c = b.replace(worlds[i], w1[0] + "*" * l1)





   # 2 вариант фильтра
   # Заменит с любым регистром
   # Недостаток: первая буква замены будет равной из списка "cenzure"



   cenzure = ['смеркалось','кирпич', 'стульев']

   badword = list(map(str.casefold, cenzure))

   zamena = ' '.join(list(cenzure))        #преобразование списка в текст




   for i in range(0,len(cenzure)):
      l1 = len(cenzure[i])
      w1 = cenzure[i]
      v = zamena.replace(cenzure[i], w1[0] + "*" * l1)
      zamena = v
   zamena=v.split(' ')   #преобразование текста в список



   struct = ''.join(list(map(str.casefold, value)))
   # str_list = list(map(str.casefold, value))
   str_list = list(value)


   m: str
   m = ''

   i: int
   j=0
   mass = []
   g: int



   n: int
   n = 0
   p=1



   for b in range(len(zamena)):
      v = zamena[b]

      for i in range(len(value)):
         m = struct[i:i+len(badword[b])]

         if m == badword[b]:
            j += 1
            mass.insert(j,i)


      for t in range(len(mass)):
         x = 0
         for g in range(mass[t], mass[t] + len(badword[b])):
            str_list[g] = v[0 + x]

            x += 1


   value=''.join(str_list)








   return value