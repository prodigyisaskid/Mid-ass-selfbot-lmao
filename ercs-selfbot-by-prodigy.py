import discord
import random
import asyncio


client = discord.Client(intents=discord.Intents.default())
token = 'token here'
version = 2.4
reacting = False
custom_emoji = None
chatpack_active = False
target_user = None
mass_dm_active = False
streaming_active = False
speed = 0.1  # Adjust typing speed as needed (in seconds)
sentences = [
    '# ur ass kid stop trying', '# ur my bitch', '# nigga built like edp455', '# u ass as fuck nigga come here',
    '# nigga built like a deformed squirtle', '# nigga lost a slapbox to a handicapped bear',
    '# you built like a asian q tip', '# built like a sumo wreslting airplane', '# you built like a fortnite battle bus',
    '# that nigga whitebeard threw a pocket knife at yo tooth ', '# built like a tap dancing motor scooter',
    '# you built like a fighter jet with plot armor on', '# that nigga luigi threw a twinkie at this nigga nose, this nigga nose flew away',
    '# rip me out the plastic i been acting brand new bitch ass nigga', '# you look like an iguana with a rocket boot on',
    '# you look like a jay walking panda tooth', '# edp 445 in diguise', '# indian school buss', '# thirsty demagorgan',
    '# belly flopping dishrag', '# sexy beer cap', '# u jumped up and nothing happend', '# kayflock with a grinch costume on',
    '# white boead with 2 dreads on his ass cheaks', '# cricket on ripcord', '# credit card with the power of flight',
    '# railgun with mouse fingers', '# vampire shoe with a nose rings', '# ginger crane fly with back problems',
    '# evil keyboard with shoes', '# forbidem cucumber with a face mask on', '# indian lobster with a icey hat on',
    '# gay mafia boss with a dorito hair', '# jumping spider with a wife beater on', '# trash bag with a gucchi robe',
    '# bruh this nigga auntie got clifford the big red dog eyebrows on her kneecaps', '# bruh this nigga grandma looks like a bootyclappin brazilin xbox controller with a missing eyebrow',
    '# bruh this nigga looks like a hobbit with downsindrome ', '# bruh this nigga looks like a roblox avatar with angry eyebrows and a vecna nose',
    '# bruh this nigga said "a whole new world" and got punched in the face by dwayne the rock johnson with marry poppin eyebrows and noclipin abilities',
    '# bruh this nigga said "sofia the first" and got knocked out by a pansexual among us character',
    '# bruh this nigga granny levetaties when she clicks her ankles',
    '# bruh that nigga ceez walked into this nigga room and threw a toaster over with a unibrow at this nigga forehead and his ass fell out',
    '# bruh this nigga mom got knocked out by harry potter playing ragdoll simulator with a missing asscheek',
    '# bruh this nigga auntie got 720 noskoped by kevin heart so his nipples fell off',
    '# bruh this nigga be slapboxin jamacian doorags with extention cords in his back pocket',
    '# bruh this nigga built like a disabled superhero with missing toenails',
    '# bruh this nigga got robbed by a ps5 controller with mussle man arms ', '# bruh this nigga built like a disabled spider with dreads',
    '# yo mom got popicle stick elbows',
    '# nigga ya mom got joxx eyebrows on her pussy lips',
    '# like that nigga percy jackson threw a bannanna peel at yo forehead and your ankles fell off',
    '# ya mom got missing booty syndrome',
    '# like this nigga nostroil built like a disobedient tape measure with a missing eyebrow',
    '# NIGGA GOT A OXX CONTRACT FOR ESEXING JOXX INA MEEP CITY LOBBY',
    '# NIGGA FELL ASLEEP AND SAID SHAZAM!',
    '# THAT NIGGA HAD THE FIRST BEST MEAL AND OVERDOSED',
    '# YOU THOUGHT DONALD TRUMP WAS A DISCORD SERVER',
    '# shower patch kid with an zkis curly ass hair', '# frog with vampire teeth that runs away from humans',
    '# anime dish washer with kneecaps', '# broken minecraft dell computer', '# nigga parents gave him away because he dosent support lgbtq',
    '# nigga looks like a skinny shoelace with a waterbottle nose', '# nigga got a death sentence for being gay',
    '# UR FAMILY PLAYS CONNECT 4 WITH YOUR EYEBROWS', '# YOU SHOT A HOMELESS MAN FOR SELLING CANDY',
    '# YOU THOUGHT A DISCORD TOKEN WAS AN ONLYFANS MANAGER', '# you looked in the mirror and said "man, i wish i never had mkis shitty haircut"'
]


@client.event
async def on_ready():
    print("error checks...completed bot successful")
    print(f'logged in as  --> {client.user}')


@client.event
async def on_message(message):
    global reacting, custom_emoji, chatpack_active, target_user, mass_dm_active, streaming_active


    if message.author == client.user:
        parts = message.content.split()
       
        if len(parts) >= 1 and parts[0] == ',help':
            help_message = (
            "`join ercs / made by prodigy / skid and ur gay`\n"
            "```,reaction on - auto reaction\n"
            ",reaction off - turns off auto reactions\n"
            ",emoji <emoji> - sets a reaction emoji\n"
            ",chatpack <mentioneduser> - autoresponds to the desired user\n"
            ",endchatpack - stops chatpack\n"
            ",massdm <message> - sends message to all friends\n"
            ",stopdm - stops process\n"
            ",streaming <message> - sets a desired streaming presence\n"
            ",stopstreaming - removes your streaming presence\n"
            ",help - shows kurona help menu\n"
            ",gc <name> - automatically changes gc name\n"
            ",gc off - stop changing the gc name\n"
            ",777 - sends info\n"
            ",spam <msg>- spams message\n"
            ",massremover - (work in progress) removes all friends added\n"
            ",afkcheck <message> - starts and afk countdown from 15 with a custom message\n"
            ",attack <user.mention> - automatically spams chat with insults\n"
            ",stopattack - stops the attack command\n"
            ",credits - credits lmfao\n"
            ",server - sends W server\n"
            ">purge - purge messages (different prefix)\n"
            ",ver - shows version```\n"
            )
            await message.channel.send(help_message)
            await message.channel.send("discord.gg/Backwood")
            await message.add_reaction('â ï¸')
       
        elif len(parts) >= 2 and parts[0] == ',reaction':
            if parts[1].lower() == 'on':
                reacting = True
                print("yuh ts on")
                await message.channel.send("`reactions on type ,e (emoji) to selection your reaction`")
                await message.add_reaction('â ï¸')
            elif parts[1].lower() == 'clear':
                reacting = False
                print("ts off")
                await message.channel.send("`successfully turned off reactions`")
                await message.add_reaction('âï¸')
            else:
                await message.channel.send("`use ,r to turn reactions on/off`")
       
        elif len(parts) >= 2 and parts[0] == ',emoji':
            custom_emoji = parts[1]
            print(f"reaction set too --> {custom_emoji}")
            await message.add_reaction('â ï¸')
            await message.channel.send("reaction set too {custom_emoji}")
       
        elif len(parts) >= 1 and parts[0] == ',chatpack':
            if len(message.mentions) > 0:
                target_user = message.mentions[0].id
                chatpack_active = True
                await message.channel.send("# try me fag")
                await message.add_reaction('â ï¸')
            else:
                await message.channel.send("`mention a user to autorespond`")
                await message.add_reaction('âï¸')
       
        elif len(parts) >= 1 and parts[0] == ',endchatpack':
            chatpack_active = False
            await message.channel.send("`chatpacking disabled`")
            await message.add_reaction('âï¸')


        elif len(parts) >= 2 and parts[0] == ',massdm':
            custom_message = message.content[len(parts[0]) + 1:]
            mass_dm_active = True
            await message.channel.send("`mass dming in`")
            await message.channel.send("`5 (say ,stopdm to cancel mass dm)`")
            await message.channel.send("`4 (say ,stopdm to cancel mass dm)`")
            await message.channel.send("`3 (say ,stopdm to cancel mass dm)`")
            await message.channel.send("`2 (say ,stopdm to cancel mass dm)`")
            await message.channel.send("`1 (say ,stopdm to cancel mass dm)`")
            await message.channel.send("` mass dming emabled `")
            await message.add_reaction('âï¸')
            await mass_dm(custom_message)
       
        elif len(parts) >= 1 and parts[0] == ',stopdm':
            mass_dm_active = False
            await message.channel.send("`massdm cancelled`")
            mass_dm_active = False
            await message.add_reaction('âï¸')


        elif len(parts) >= 1 and parts[0] == ',server':
            custom_message = message.content[len(parts[0]) + 1:]
            await message.channel.send("discord.gg/5Q9UjAPh")
            await message.add_reaction('â ï¸')


        elif len(parts) >= 1 and parts[0] == ',afkcheck':
            custom_message = message.content[len(parts[0]) + 1:]
            await message.channel.send("15")
            await message.channel.send("14")
            await message.channel.send("13")
            await message.channel.send("12")
            await message.channel.send("11")
            await message.channel.send("10")
            await message.channel.send("9")
            await message.channel.send("8")
            await message.channel.send("7")
            await message.channel.send("6")
            await message.channel.send("5")
            await message.channel.send("4")
            await message.channel.send("3")
            await message.channel.send("2")
            await message.channel.send("1")
            await message.channel.send("0")
            await message.add_reaction('â ï¸')
            print(f"afk check completed {client.user}")
        elif len(parts) >= 1 and parts[0] == ',stopafk':
            await message.channel.send("`afk check canceled`")
            await message.add_reaction('âï¸')
       
        elif len(parts) >= 1 and parts[0] == ',credits':
            await message.channel.send("` ! credits ! `")
            await message.channel.send("` owner - Prodigy says join discord.gg/5Q9UjAPh `")
            await message.channel.send("https://tenor.com/view/mori-saru-gif-22237564")
           
            await message.add_reaction('âï¸')
            print(f"sent credits {client.user}")
       
        elif len(parts) >= 1 and parts[0] == ',stopdm':
            mass_dm_active = False
            await message.channel.send("`massdm canceled`")
            mass_dm_active = False
            await message.add_reaction('âï¸')


        elif len(parts) >= 1 and parts[0] == ',attack':
            if len(message.mentions) > 0:
                target_user = message.mentions[0].id
            await message.channel.send("# ur a cum guzzler")
            await message.channel.send("# aerodynamic dickbouncer")
            await message.channel.send("# ur a fembot shut the fuck up")
            await message.channel.send("# i don't recognize you son")
            await message.channel.send("# ill acknowledge you one day kiddo")
            await message.channel.send("# lol ur ass?")
            await message.channel.send("# slow cuck")
            await message.channel.send("# ur unloved")
            await message.channel.send("# poor ass loser")
            await message.channel.send("# show me a father figure?")
            await message.channel.send("# you esex in vrc nigga shut the fuck up?")
            await message.channel.send("# professional dick drainer")
            await message.channel.send("# LMFAOAO UR SHITTY BITCH")
            await message.channel.send("# your knees weak from all that dick riding yet ?")
            await message.channel.send("# hit the weight room weak fuck")
            await message.channel.send("# your underdeveloped")
            await message.channel.send("# elon musk reptile hybrid")
            await message.channel.send("# your a discord cuck i don't take you serious")
            await message.channel.send("# RIP ME OUT THE PLASTIC I BEEN ACTING BRAND NEW FACE ASS NIGGA")
            await message.channel.send("# UR A FUCKING FEMBOT LMFAO")
            await message.channel.send("# try this LOL https://cdn.discordapp.com/attachments/1253160491811999796/1260018304509018113/noose-png-3.png?ex=668dcafd&is=668c797d&hm=904531ffb275cd7c6f027158d253cb16f8640ba929e342a35251a60e0c5adb4c&")
            await message.channel.send("# ur nervous aren't you")
            await message.channel.send("# weak fuck died before we even started")
            await message.channel.send("# you sweat cheese nigga")
            await message.channel.send("# you have under titty sweat man boobed fuck")
            await message.channel.send("# 24.1 bmi btw LMFAOOAOAOA")
            await message.channel.send("# you talk to the voices in your head when your lonely https://tenor.com/view/no-gif-23548728")
            await message.channel.send("# TRYNA STRIKE A CORD AND ITS PROBABLY A MINORRRRRRRRRRRRRRRR")
            await message.channel.send("# you finger yourself when no ones around")
            await message.channel.send("# your a undercover booty bandit bitch")
            await message.channel.send("# I can tell you eat ass wipe the shitstains off ur lips nasty fuck")
            await message.channel.send("# you get dominated through a screen LMFAO")
            await message.channel.send("# you chatpack on a motorola dork")
            await message.channel.send("# show some cash poor bitch LFMAO")
            await message.channel.send("# you eat toothpaste on a hotdog bun")
            await message.channel.send("# nigga eats struggle meals")
            await message.channel.send("# Toothpick built ass nigga LMFAOAO")
            await message.channel.send("# wait")
            await message.channel.send("# yo...")
            await message.channel.send("# i think ik u")
            await message.channel.send("# sike loser ass nigga ur a random nb knows u ")
            await message.channel.send("# You store sandwiches under your stomach rolls freakishly fat fuck")
            await message.channel.send("# your mother gives blow jobs in 7/11 restrooms let that sink in")
            await message.channel.send("# you might not believe what im about to tell you but.")
            await message.channel.send("# you were left on some random niggas doorstep your parents didn't want you")
            await message.channel.send("# retarded slug with shotgun nostrils")
            await message.channel.send("# you chatpack on a orb keyboard nigga https://cdn.discordapp.com/attachments/1253160491811999796/1260020704229724231/f2e6538a8f522aa21cc11aadd6fea4fa--computer-keyboard-be-awesome.png?ex=668dcd39&is=668c7bb9&hm=b26d2c7e658c8ed9836823bfc5cd03f749045849197970a22bf8008e6073dad2&")
            await message.add_reaction('â ï¸')
            print(f"stopped attacking {client.user}")
        elif len(parts) >= 1 and parts[0] == ',stopattack':
            await message.channel.send("`stopped attacking`")
            await message.add_reaction('âï¸')
           
        elif len(parts) >= 2 and parts[0] == ',streaming':
            streaming_message = message.content[len(parts[0]) + 1:]
            await client.change_presence(activity=discord.Streaming(name=streaming_message, url="https://www.twitch.tv/idk"))
            await message.channel.send(f"`streaming presence set too: {message.content}`")
            await message.add_reaction('âï¸')
            streaming_active = True
           
        elif len(parts) >= 1 and parts[0] == ',stopstreaming':
            streaming_active = False
            await client.change_presence(activity=None)
            await message.channel.send("`stopped streaming status`")
            await message.add_reaction('âï¸')


        elif len(parts) >= 2 and parts[0] == ',gc':
            await message.channel.send("# ur ass lmao")
            global toggle_groupchat, groupchat_name, number
            channel_id = message.channel.id
            groupchat_name = ' '.join(parts[1:])
            toggle_groupchat = True
            number = 1
            await update_channel_name(message.channel)
            await message.add_reaction('âï¸')
       
        elif len(parts) >= 1 and parts[0] == ',gcoff':
            await message.channel.send("# quit trying skid")
            toggle_groupchat = False
            await message.add_reaction('âï¸')


        elif len(parts) >= 1 and parts[0] == ',777':
            await message.channel.send("https://tenor.com/view/mori-saru-gif-22237564")
            await message.add_reaction('âï¸')
            await message.channel.send("` 777 is in development and made by /Prodigy`")
            await message.add_reaction('âï¸')


        elif len(parts) >= 1 and parts[0] == ',massremover':
            await message.channel.send("```removing all friends```")
            await mass_remover(message)


        elif len(parts) >= 2 and parts[0] == ',spam':
            if len(parts) >= 2:
                spam_message = ' '.join(parts[1:])
                await spam_messages(message.channel, spam_message)
                await message.add_reaction('âï¸')
                await message.channel.send("```ez spam son```")


        elif len(parts) >= 2 and parts[0] == '>purge':
            try:
                num_messages = int(parts[1])
                deleted = await message.channel.purge(limit=num_messages + 1)
                await message.channel.send(f"```deleted {len(deleted) - 1} messages.```", delete_after=5)
            except ValueError:
                await message.channel.send("```prove a number of msgs nga```")
            except Exception as e:
                await message.channel.send(f"```error: {str(e)}```")
                print(f"error: {str(e)}")
           
        elif len(parts) >= 1 and parts[0] == ',ver':
            await message.channel.send("``` VERSION 0.0.1```")
            await message.add_reaction('â ï¸')


    if chatpack_active and message.author.id == target_user:
        current_sentence = random.choice(sentences)
        await message.reply(current_sentence)
        await asyncio.sleep(speed)
   
    if reacting and message.author == client.user:
        if custom_emoji is not None:
            await message.add_reaction(custom_emoji)
        else:
            await message.add_reaction('â ï¸')


async def update_channel_name(channel):
    global toggle_groupchat, groupchat_name, number


    while toggle_groupchat:
        await channel.edit(name=f'{groupchat_name} {number}')
        number += 1
        await asyncio.sleep(0)


async def mass_dm(custom_message):
    global mass_dm_active
    for user in client.user.friends:
        if not mass_dm_active:
            break
        try:
            await user.send(custom_message)
            await asyncio.sleep(speed)
        except Exception as e:
            print(f"failed to send to {user.name}: {e}")


async def mass_remover(message):
    try:
        # Fetch the client user object to access friends
        await client.user.fetch_self()
        for friend in client.user.friends:
            await friend.remove_friend()
            print(f"removed this random: {friend.name}")
        await message.channel.send("Removed all friends.")
    except Exception as e:
        print(f"Failed to remove friends: {e}")
        await message.channel.send("Failed to remove friends.")


async def spam_messages(channel, spam_message):
    num_messages = 50
    for _ in range(num_messages):
        await channel.send(spam_message)
        await asyncio.sleep(speed)


client.run(token, bot=False)
