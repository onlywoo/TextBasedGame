print('You stand in front of your house. All the memories flood your mind as they hazily replay. You watch the stillness of the once-swinging tire hung from the tree; the wooden panels of the house are so old they almost look as if they are withering away in front of your eyes. ')
print('')
print('You go up the stairs,approaching the front porch; you expect nostalgia to wash over you, but you feel nothing.')
nextLine = input('>Next')
print('You go in, pushing the heavy spruce door open as it follows its tired tracks and step in. The wallpaper curled off like the shell of a snail.')
nextLine = input('>Next')
print("You look around as you watch your childhood lie desolate in the abandoned house, covered in layers of dust. You're here for one thing, you just need to get in and out. Get the cartridge and leave.")
print('You walk upstairs following the well known path to your old room, the stairs groaning with each step. You stop at the top to the sound of a tap on the window. You look around and see nothing.')
print('')

print("Continuing down the hallway, you can't help but hear a second step behind you, almost as if they are timing it with yours. You begin to sweat.")
print("As you hurridly reach your door, running. You hear a scurried movement behind you.")
scared = input('Turn around? Yes or No')
if scared == 'yes' or scared == 'Yes' or scared == 'YES':
    print('Your spine straightens as you muster up the courage to turn. As you look back, the shriek of glass breaking stuns you, eyes widened. Relief washes over you as you look down to see your family portrait on the floor.')
    print('All this activity must have shaken all the lose things causing it to unhook. You pick up the picture through the glass and examine what used to be.')
    nextLine = input('>Next')
    print("As expected, your whole family stands with emotionless smiles and stares back into the camera. You begin to put the picture down when you see an unfamiliar figure in the back of the picture.")
    print('You chalk it up to old cameras being weird and go into your room. The door struggling to open. You push and push till you make it in.')

elif scared == 'no' or scared == 'No' or scared == 'NO':
    print("You can't. You just cannot bring yourself to turn around. Your face tingles and goosebumps cover your body, eyes darting. The floor board creaks are getting close. You lunge for the handle, the door struggling to open. You push and push till you make it in. Swinging the door open, you hurry inside, slaming it closed.")
    print('BANG. Something hit the door just as you closed it. You are NOT investigating that.')
    nextLine = input('>Next')
else:
    scared()

intoRoom = input('You walk into your room, everything still as it was.')
print('')
print('Your desk sits there littered with cartidges and disks. Your once white PC is now #c4b595. Memories rush into your mind as you think about the hours you spent in that chair swapping disks.')
print("""\
  .---------.
  |.-------.|
  ||>run#  ||
  ||       ||
  |"-------'|etf
.-^---------^-.
| ---~   AMiGA|
"-------------'

    """)
print('"For old times sake" you think to yourself as you brush the dust off everything and plug in your favourite game. Dungeons. The determined yet annoying music plays. https://tinyurl.com/2lcv548p')
print('You begin to play')
nextLine = input('>Next')
print("""\  Welcome! to Dungeon. Press Any key to Begin. It is advised to use lowercase when making choices
                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     -ART BY ZEUS-
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--` """)

intoGame = input('>Next')
name = input('Enter your name!')
print(f"Greetings {name}, You're back after all these years.")
start = input('Let the adventure begin?')

if start == 'yes' or start == 'Yes' or start == 'YES':
    print('You walk in with your sword and shield in hand, ready for whatever is to be thrown at you!')
    # setting = input('Want to go through the left corridor or the right?')
elif 'no':
    print("You get only a one more chance to change your mind...Type yes")
else:
    start

secondC = input('Would you like to enter the dungeon?')
# roomchoice = input("> ")
if secondC == 'yes' or secondC == 'Yes' or secondC == 'Yes':
    # make an array and see if valid responses are in the array
    print('There you go...Let the adventure begin...')
else:
    print('Type yes.')
nextLine = input('>Next')

setting = input('You are met with an empty dimly lit room. Moss slowly swallowing the slimly stone walls, with the faint sound of running water in the distance. You have two options. Do you want to go through the left corridor or the right?')
if setting == 'left' or setting == 'Left' or setting == 'LEFT':
    print('In the left room, you are met with... green foliage. Vines creeping on the walls and a waterfall in the corner. The vines are thick enough to break your sword.')
else:
    setting
thirdchoice = input('Slash away or Look behind the waterfall?')
if thirdchoice == 'slash away' or thirdchoice == 'Slash away' or thirdchoice == 'SLASH AWAY' or thirdchoice == 'Slash Away':
    print('You sword gets to work, your arms aching from the thickness of the vines. You flinch as a piece of shiny metal flies towards you. You sword is beginning to weaken, you begin to worry but that is soon gone when you see the next room. Someones in there.')
    print('He sits in the corner of a dark wet room, the floor squelches under you. He turns to you as you make noise. Staring. You both stop moving. You are in danger')
    print('He lunges at you, you dodge the attack and swing your sword. You hit his arm. You can barely see anything with only the light from the previous room lighting a small sliver of the room.')
    print('He avoids it. The wall is cracked and weak.')

elif thirdchoice == 'Waterfall' or thirdchoice == 'behind the waterfall' or thirdchoice == 'look behind the waterfall' or thirdchoice == 'waterfall':
    print('You walk behind the waterfall, finding a passage. It looks safe enough?')
    print('go in?')

killHim = input('Break the wall or Fight?')
if killHim == 'Break the wall' or killHim == 'break the wall' or killHim == 'break' or killHim == 'Break' or killHim == 'break wall' or killHim == 'Break wall':
    print("You use what's left of your sword and start hacking away at the wall. Sparks flying, the sword begins to shorten. You turn and throw whats left of it at the man. He falls, dazed, nows your chance.")
    print('You start frantically pulling away at the wall with your fingers, blood flowing from your nails. You pull a huge brick, the wall comes crumbling down and the light brightens the whole room. He sits up and fear covers his face.')
    print('')
    print('His skin, or whats left of it, begins to tear off, falling too the group. Burning too the touch of light. His face melts before you. Nothing left but his bones and sword.')
    print("""\
                                             ____
                              __,---'     `--.__
                           ,-'                ; `.
                          ,'                  `--.`--.
                         ,'                       `._ `-.
                         ;                     ;     `-- ;
                       ,-'-_       _,-~~-.      ,--      `.
                       ;;   `-,;    ,'~`.__    ,;;;    ;  ;
                       ;;    ;,'  ,;;      `,  ;;;     `. ;
                       `:   ,'    `:;     __/  `.;      ; ;
                        ;~~^.   `.   `---'~~    ;;      ; ;
                        `,' `.   `.            .;;;     ;'
                        ,',^. `.  `._    __    `:;     ,'
                        `-' `--'    ~`--'~~`--.  ~    ,'
                       /;`-;_ ; ;. /. /   ; ~~`-.     ;
-._                   ; ;  ; `,;`-;__;---;      `----'
   `--.__             ``-`-;__;:  ;  ;__;
 ...     `--.__                `-- `-'
`--.:::...     `--.__                ____
    `--:::::--.      `--.__    __,--'    `.
        `--:::`;....       `--'       ___  `.
            `--`-:::...     __           )  ;
                  ~`-:::...   `---.      ( ,'
                      ~`-:::::::::`--.   `-.
                          ~`-::::::::`.    ;
                              ~`--:::,'   ,'
                                   ~~`--'~
""")
else:
    killHim
nextLine
if killHim == 'fight' or killHim == 'Fight':
    print('You swing your sword and slash at him. You both fight, you dodge and block his attacks. You hear a faint noise of someones voice behind you. It distracts you, leaving you open to the final blow. He pushes the blade deeper and deeper into you. Leaving you in a puddle of blood. He kneels down next to you. You watch him with your dying breath, lift your arm and tear the flesh from your bones.')
    nextLine
    print('You died.')
gameClose = input('You sit and stare at your screen as you huff at your stupid decisions. Only thing left to do is start again, right? You get ready to restart the dungeon again. Start?')
print("""\  Welcome! to Dungeon. Press Any key to Begin. It is advised to use lowercase when making choices
                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     -ART BY ZEUS-
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--` """)

nextLine
print(f"Greetings {name}, You're back after all these years.")
nextLine
print('Thats odd, you think to yourself, you never typed in your name this time...Maybe it remebered from last time.')
secondGame = input('Welcome back.')
print('You approach the porch and come face to face with a thick spruce door waiting to be dragged open.')
nextLine
print("This isn't dungeon, you think to yourself. You check if you placed the right cartridge in but the screen changes before you could do anything. You stare back at your screen as the game plays itself.")
nextLine
print('The door opens and you walk in. You look around the abandoned home and walk up the stairs. Two sets of footsteps can be heard. Suddenly glass comes crashing too the floor. Turning around to see a family protrait strewn across the floor. You pick it up and see one extra person.')
nextLine
print('The door slams. You jolt away from the screen, fear filling your entire body as the you hear those foot steps again. You stare at the door waiting for the worst.')
print('')
print('The start getting faster... and faster. Now running towards your door.')
nextLine
print('You jump fron your seat and push every fiber of your body against the door, tears welling in your eyes as the running reaches you. You look down, bracing for impact. You notice the light from under the door dancing.')
print('')
print('Someone is there.')
nextLine
print('The banging stops.')
nextLine
askName = input('You hear a familiar voice. Ask who it is?')
if askName == 'yes' or askName == 'Yes' or askName == 'YES':
    print('You yell out asking their name. All sound stops and they respond. Sounding almost shaken...')
    nextLine
    print(f"'I am {name}, who are you?' they respond.")
    nextLine
    print('You stare in shock as your knees go weak.')
    print('They push the door and it opens, you stand face to face.')
if askName == 'no' or askName == 'No' or askName == 'NO':
    print('You refuse to speak. You open the door once everything quietens down and you see nobody. You sprint out the front door and look back. Staring up at your room window. He watches you as you freeze in shock')
else:
    askName
nextLine
quitGame = input('The end')

passageChoice = input('Yes or No?')
if passageChoice == 'yes' or passageChoice == 'Yes' or passageChoice == 'YES':
    print('As you walk in to see something on the floor, a bag of fish shaped treats?')
    fishTreats = input('Take them?')
    print('Yes or no?')
if fishTreats == 'yes' or fishTreats == 'Yes' or fishTreats == 'YES':
    print('You pick them up and proceed through the passage.')
print('You are met with a feline looking animal. Parts of their body... missing? almost as if its invisible. Another one follows, standing behind it.')
nextLine
print("""\
      Art by Niki Fowler
 /\___/\
 \/   \/
  \~ ~/
 ==`^ ==
  /   \        |\___/|
 /|   |        \/- -\/ ____...,...
 || - |         \o o/             \
 ||   |        ==`^ ==   ,        /\
 ||| ||_            `.  / --- \  / \\____//
/\||_|//         ;____,'      | /   ` ---
\_____/                    ;___/
""")
peace = input('They are curiously watch you... Give peace offering?')
if peace == 'yes' or peace == 'Yes' or peace == 'YES':
    print('You remember the bag of treats... You pull them out and extend your hand while crouching, ready to pull away. They scurry towards you hesitantly stopping to stare at you. Doing a back and forth dance as they decide whether they want food or not.')
    print('They slowly take one from your hand and soon enough are laying all over you purring. You stroke your new found friends.')
    print("""\
              __..--''``---....___   _..._    __
 /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /
///_.-' _..--.'_    \                    `( ) ) // //
/ (_..-' // (< _     ;_..__               ; `' / ///
 / // // //  `-._,_)' // / ``--...____..-' /// / //
 
       Another one appears and hands you a key. You take it and look around the room, seeing a huge bejeweled door at the top of a set of broken and crumbling stairs.""")
endGame = input('Your screen goes black and you are back at the beginning of the page. You sign in disbelief but you know you are playing with decade old technology. It is a wonder it still works. You end up at the start menu again. You play again')
print("""\  Welcome! to Dungeon. Press Any key to Begin. It is advised to use lowercase when making choices
                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     -ART BY ZEUS-
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--` """)

nextLine
print(f"Greetings {name}, You're back after all these years.")
nextLine
print('Thats odd, you think to yourself, you never typed in your name this time...Maybe it remebered from last time.')
secondGame = input('Welcome back.')
print('')
print('You approach the porch and come face to face with a thick spruce door waiting to be dragged open.')
nextLine
print("This isn't dungeon, you think to yourself. You check if you placed the right cartridge in but the screen changes before you could do anything. You stare back at your screen as the game plays itself.")
nextLine
print('The door opens and you walk in. You look around the abandoned home and walk up the stairs. Two sets of footsteps can be heard. Suddenly glass comes crashing too the floor. Turning around to see a family protrait strewn across the floor. You pick it up and see one extra person.')
nextLine
print('The door slams. You jolt away from the screen, fear filling your entire body as the you hear those foot steps again. You stare at the door waiting for the worst.')
print('')
print('The start getting faster... and faster. Now running towards your door.')
nextLine
print('You jump fron your seat and push every fiber of your body against the door, tears welling in your eyes as the running reaches you. You look down, bracing for impact. You notice the light from under the door dancing.')
print('')
print('Someone is there.')
nextLine
print('The banging stops.')
nextLine
askName
if askName == 'yes' or askName == 'Yes' or askName == 'YES':
    print('You yell out asking their name. All sound stops and they respond. Sounding almost shaken...')
    nextLine
    print(f"'I am {name}, who are you?' they respond.")
    nextLine
    print('You stare in shock as your knees go weak.')
    print('They push the door and it opens, you stand face to face.')
elif askName == 'no' or askName == 'No' or askName == 'NO':
    print('You refuse to speak. You open the door once everything quietens down and you see nobody. You sprint out the front door and look back. Staring up at your room window. He watches you as you freeze in shock')
nextLine
quitGame = input('The end')


if peace == 'no' or peace == 'No' or peace == 'NO':
    print('Oh no. They stare at you, eyes sharp, predicting your every move, you try to run but they are just too quick. Before you can even scream, 3 sets of claws dig deep into your flesh, pulling. Leaving nothing left but pieces of you. You lie in a pools of blood as your remains cover the their pretty delicate paws and the walls.')
    print('You died')

else:
    peace

if fishTreats == 'no' or fishTreats == 'No' or fishTreats == 'NO':
    print("You can't help but feel like this is a misatke...")
    print('You proceed through the passage.')
    print('You are met with a feline looking animal. Parts of their body... missing? almost as if its invisible. Another one follows, standing behind it.')
else:
    fishTreats
noTreats = input('They are curiously watch you... Give peace offering?')
if noTreats == 'no' or noTreats == 'No' or noTreats == 'NOs':
    print('You remember the bag of treats...')
    print('Oh no. They star at you, eyes sharp, predicting your every move, you try to run but they are just too quick. Before you can even scream, 3 sets of claws dig deep into your flesh, pulling. Leaving nothing left but pieces of you. You lie in a pools of blood as your remains cover the their pretty delicate paws and the walls.')
    print("""\
            _.------.                        .----.__
           /         \_.       ._           /---.__  \
          |  O    O   |\\___  //|          /       `\ |
          |  .vvvvv.  | )   `(/ |         | o     o  \|
          /  |     |  |/      \ |  /|   ./| .vvvvv.  |\
         /   `^^^^^'  / _   _  `|_ ||  / /| |     |  | \
       ./  /|         | O)  O   ) \|| //' | `^vvvv'  |/\\
      /   / |         \        /  | | ~   \          |  \\
      \  /  |        / \ Y   /'   | \     |          |   ~
       `'   |  _     |  `._/' |   |  \     7        /
         _.-'-' `-'-'|  |`-._/   /    \ _ /    .    |
    __.-'            \  \   .   / \_.  \ -|_/\/ `--.|_
 --'                  \  \ |   /    |  |              `-
""")
    print('You died')
else:
    noTreats
nextLine
gameClose
print("""\  Welcome! to Dungeon. Press Any key to Begin. It is advised to use lowercase when making choices
                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     -ART BY ZEUS-
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--` """)

nextLine
print(f"Greetings {name}, You're back after all these years.")
nextLine
print('Thats odd, you think to yourself, you never typed in your name this time...Maybe it remebered from last time.')
secondGame = input('Welcome back.')
print('')
print('You approach the porch and come face to face with a thick spruce door waiting to be dragged open.')
nextLine
print("This isn't dungeon, you think to yourself. You check if you placed the right cartridge in but the screen changes before you could do anything. You stare back at your screen as the game plays itself.")
nextLine
print('The door opens and you walk in. You look around the abandoned home and walk up the stairs. Two sets of footsteps can be heard. Suddenly glass comes crashing too the floor. Turning around to see a family protrait strewn across the floor. You pick it up and see one extra person.')
nextLine
print('The door slams. You jolt away from the screen, fear filling your entire body as the you hear those foot steps again. You stare at the door waiting for the worst.')
print('')
print('The start getting faster... and faster. Now running towards your door.')
nextLine
print('You jump fron your seat and push every fiber of your body against the door, tears welling in your eyes as the running reaches you. You look down, bracing for impact. You notice the light from under the door dancing.')
print('')
print('Someone is there.')
nextLine
print('The banging stops.')
nextLine
askName
if askName == 'yes' or askName == 'Yes' or askName == 'YES':
    print('You yell out asking their name. All sound stops and they respond. Sounding almost shaken...')
    nextLine
    print(f"'I am {name}, who are you?' they respond.")
    nextLine
    print('You stare in shock as your knees go weak.')
    print('They push the door and it opens, you stand face to face.')
elif askName == 'no' or askName == 'No' or askName == 'NO':
    print('You refuse to speak. You open the door once everything quietens down and you see nobody. You sprint out the front door and look back. Staring up at your room window. He watches you as you freeze in shock')
nextLine
quitGame = input('The end')

# Second room
if setting == 'Right' or setting == 'right' or setting == 'RIGHT':
    print('You are met with a flowing body of water, the room lit up with a bright light, almost like the sun, and a welcoming beach waiting for you...and someone screaming for help. ')
    waterChoice = input('Save them or leave it be')
if waterChoice == 'Save them' or waterChoice == "save them" or waterChoice == "Save" or waterChoice == 'save':
    print(
        f"You throw your sword and shield to the ground, bravely diving in to save them. You get a closer look. The most beautiful woman infront of you, yelling {name}. You wonder how she knows your name. You swim up behind her, grabbing her under the arms and swim.")
    print('Something is off...You see no legs. You notice a glint of light in the water following her. She has a tail')
    print('')
    print('The water stands still. Everything falls silent. She stares at you with an evil grin on her face as you float in her arms.')
    nextLine
    print('Before you can react, she drags you down and everything around you darkens and you are swallowed by the dark blue abyss. Leaving you helpless.')
    gameClose

print("""\  Welcome! to Dungeon. Press Any key to Begin. It is advised to use lowercase when making choices
                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     -ART BY ZEUS-
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--` """)

nextLine
print(f"Greetings {name}, You're back after all these years.")
nextLine
print('Thats odd, you think to yourself, you never typed in your name this time...Maybe it remebered from last time.')
secondGame = input('Welcome back.')
print('')
print('You approach the porch and come face to face with a thick spruce door waiting to be dragged open.')
nextLine
print("This isn't dungeon, you think to yourself. You check if you placed the right cartridge in but the screen changes before you could do anything. You stare back at your screen as the game plays itself.")
nextLine
print('The door opens and you walk in. You look around the abandoned home and walk up the stairs. Two sets of footsteps can be heard. Suddenly glass comes crashing too the floor. Turning around to see a family protrait strewn across the floor. You pick it up and see one extra person.')
nextLine
print('The door slams. You jolt away from the screen, fear filling your entire body as the you hear those foot steps again. You stare at the door waiting for the worst.')
print('')
print('The start getting faster... and faster. Now running towards your door.')
nextLine
print('You jump fron your seat and push every fiber of your body against the door, tears welling in your eyes as the running reaches you. You look down, bracing for impact. You notice the light from under the door dancing.')
print('')
print('Someone is there.')
nextLine
print('The banging stops.')
nextLine
askName
if askName == 'yes' or askName == 'Yes' or askName == 'YES':
    print('You yell out asking their name. All sound stops and they respond. Sounding almost shaken...')
    nextLine
    print(f"'I am {name}, who are you?' they respond.")
    nextLine
    print('You stare in shock as your knees go weak.')
    print('They push the door and it opens, you stand face to face.')
elif askName == 'no' or askName == 'No' or askName == 'NO':
    print('You refuse to speak. You open the door once everything quietens down and you see nobody. You sprint out the front door and look back. Staring up at your room window. He watches you as you freeze in shock')
nextLine
quitGame = input('The end')
if waterChoice == 'Leave' or waterChoice == 'leave' or waterChoice == 'Leave it be' or waterChoice == 'leave it be':
    print('You walk by and watch her struggle. increasingly getting more frustrated as she watches you stand there. You catch a glimps of pink in the water. She has a tail, its a Siren.')
    nextLine
    print("""\
            __
      /( `
      | `.      __
      \   \__    )\
       \  /  `--' /
        )  ____,-'
      ,' ,'                   __      ____
     /  /        _,---.  ,-,_/_ \    /,.  \__
     |  \_____,-'      `///'/    \__/ e \    `-._
     \                  . - >--<   _\'_e/_,_     \____,
   gnv`-..__________________\__,___________)\_______,-'
 """)
endGame
print("""\  Welcome! to Dungeon. Press Any key to Begin. It is advised to use lowercase when making choices
                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     -ART BY ZEUS-
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--` """)

nextLine
print(f"Greetings {name}, You're back after all these years.")
nextLine
print('Thats odd, you think to yourself, you never typed in your name this time...Maybe it remebered from last time.')
secondGame = input('Welcome back.')
print('')
print('You approach the porch and come face to face with a thick spruce door waiting to be dragged open.')
nextLine
print("This isn't dungeon, you think to yourself. You check if you placed the right cartridge in but the screen changes before you could do anything. You stare back at your screen as the game plays itself.")
nextLine
print('The door opens and you walk in. You look around the abandoned home and walk up the stairs. Two sets of footsteps can be heard. Suddenly glass comes crashing too the floor. Turning around to see a family protrait strewn across the floor. You pick it up and see one extra person.')
nextLine
print('The door slams. You jolt away from the screen, fear filling your entire body as the you hear those foot steps again. You stare at the door waiting for the worst.')
print('')
print('The start getting faster... and faster. Now running towards your door.')
nextLine
print('You jump fron your seat and push every fiber of your body against the door, tears welling in your eyes as the running reaches you. You look down, bracing for impact. You notice the light from under the door dancing.')
print('')
print('Someone is there.')
nextLine
print('The banging stops.')
nextLine
askName
if askName == 'yes' or askName == 'Yes' or askName == 'YES':
    print('You yell out asking their name. All sound stops and they respond. Sounding almost shaken...')
    nextLine
    print(f"'I am {name}, who are you?' they respond.")
    nextLine
    print('You stare in shock as your knees go weak.')
    print('They push the door and it opens, you stand face to face.')
elif askName == 'no' or askName == 'No' or askName == 'NO':
    print('You refuse to speak. You open the door once everything quietens down and you see nobody. You sprint out the front door and look back. Staring up at your room window. He watches you as you freeze in shock')
nextLine
quitGame = input('The end')

# Second room
if setting == 'Right' or setting == 'right' or setting == 'RIGHT':
    print('You are met with a flowing body of water, the room lit up with a bright light, almost like the sun, and a welcoming beach waiting for you...and someone screaming for help. ')
    waterChoice = input('Save them or leave it be')
if waterChoice == 'Save them' or waterChoice == "save them" or waterChoice == "Save" or waterChoice == 'save':
    print(
        f"You throw your sword and shield to the ground, bravely diving in to save them. You get a closer look. The most beautiful woman infront of you, yelling {name}. You wonder how she knows your name. You swim up behind her, grabbing her under the arms and swim.")
    print('Something is off...You see no legs. You notice a glint of light in the water following her. She has a tail')
    print('')
    print('The water stands still. Everything falls silent. She stares at you with an evil grin on her face as you float in her arms.')
    nextLine
    print('Before you can react, she drags you down and everything around you darkens and you are swallowed by the dark blue abyss. Leaving you helpless.')
    gameClose
