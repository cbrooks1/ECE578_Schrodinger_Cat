#!/usr/bin/env python3
''
# This program makes the Pi speak aloud the text

from num2words import num2words
from subprocess import call


cmd_beg= 'espeak -ven+m1 -s200 -g10 '
cmd_end= ' 2>/dev/null' 

#Beginning script
text = 'Hi my name is schrodinger cat'
text2 = 'It is such a purrrrrr fect day'
text3 = 'Today I was spending time with my human and we'
text4 = 'MOUSE'
text5 = 'Oh sorry i thought i saw a mouse'
text6 = 'As i was saying i was spending time with my human and we napped all day meow'

#Replacing ' ' with '_' to identify words in the text entered
text = text.replace(' ', '_')
text2 = text2.replace(' ', '_')
text3 = text3.replace(' ', '_')
text4 = text4.replace(' ', '_')
text5 = text5.replace(' ', '_')
text6 = text6.replace(' ', '_')

call([cmd_beg+text+cmd_end], shell=True)
call([cmd_beg+text2+cmd_end], shell=True)
call([cmd_beg+text3+cmd_end], shell=True)
call([cmd_beg+text4+cmd_end], shell=True)
call([cmd_beg+text5+cmd_end], shell=True)
call([cmd_beg+text6+cmd_end], shell=True)
#End of script

#first time seeing human face detection code
face = 'Look Theres my human meow Hi human'
face = face.replace(' ', '_')
call([cmd_beg+face+cmd_end], shell=True)

#after a couple of seconds of not seeing human
whereishuman = 'Where did my human go'
whereishuman = whereishuman.replace(' ', '_')
call([cmd_beg+whereishuman+cmd_end], shell=True)

#red box detection
mouse = 'I found a mouse over meow'
mouse = mouse.replace(' ', '_')
call([cmd_beg+mouse+cmd_end], shell=True)

#after a couple of seconds of not seeing mouse
whereismouse = 'I have not seen a mouse in awhile'
atemouse = 'I must have ate all the mice yummmmmmmm'

whereismouse = whereismouse.replace(' ', '_')
atemouse = atemouse.replace(' ', '_')

call([cmd_beg+whereismouse+cmd_end], shell=True)
call([cmd_beg+atemouse+cmd_end], shell=True)
