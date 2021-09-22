import amino
import time
from gtts import gTTS
import requests

client=amino.Client()

client.login(email="mebad17855@tst999.com",password="pagal0")

print("logged in.....")

cid="18652750"
cidy=18652750
adm=[]
##admx=["http://aminoapps.com/p/fv5iiu","http://aminoapps.com/p/7dk2zc",''http://aminoapps.com/p/2ssktow'',''http://aminoapps.com/p/eavv85'']

admx=["http://aminoapps.com/p/h9z7uj","http://aminoapps.com/p/x0ivz4"]

for i in admx:
	try:
		w=client.get_from_code(i).objectId
		adm.append(w)
	except:
		print("invalid admin links/format")
subclient=amino.SubClient(comId=cid,profile=client.profile)

print("inside community")
@client.event("on_group_member_join")
def on_group_member_join(data):
	if data.comId==cidy:
		try:
			x=data.message.author.icon
			response=requests.get(f"{x}")
			file=open("sample.png","wb")
			file.write(response.content)
			file.close()
			img=open("sample.png","rb")
			subclient.send_message(chatId=data.message.chatId,message=f"""[BC][BC]  ─━─━─━─͜͡─͜͡  ⭞ 🍮⃟⃟ૈ͙⃨ .❣️ ꪝꫀᥨᩮꪔꫀ .🍰᪶֞◞⃕  ‍  𝐭𝐨  ⏜ indian's kingdom♡࿔𝐨𝐮𝐫 𝐜𝐡𝐚𝐭 
 （„• ֊ •„)♡
 ┏━━∪∪━━━ღ❦ღ━━┓
      ✯
[BC]✾✾✾✾✾✾✾✾✾✾✾✾✾✾
 ᕼOᒪᗩ ♕ ✿
[C]༄ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ 𝔗𝔥𝔯𝔢𝔢                                                  #A𝓁𝓁✯
[C]༄ʀᴇᴀᴅ ᴀɴᴅ ғᴏʟʟᴏᴡ ᴛʜᴇ ɢᴄ ʀᴜʟᴇs
[C]༄ᴀɴᴅ ᴇɴᴊᴏʏ ʏᴏᴜʀ sᴛᴀʏ ʜᴇʀᴇ 
[C]༄ᴀɴᴅ ᴍᴀᴋᴇ ɴᴇᴡ ғʀɪᴇɴᴅs 

[BC]❃❃❃❃❃❃❃❃❃❃❃❃❃❃❃❃

                        ┗ღ❦ღ━━━━━━━━┛
                                            ヽ(‧ω‧`)ﾉ
                                                 |    |""",embedId=data.message.author.userId,embedTitle=data.message.author.nickname,embedLink=f"ndc://x{cid}/user-profile/{data.message.author.userId}",embedImage=img,mentionUserIds=[data.message.author.userId])
			print(f"\nwelcomed {data.message.author.nickname} to gc ")
		except Exception as e:
			print(e)
				
@client.event("on_group_member_leave")
def on_group_member_leave(data):
	if data.comId==cidy:
		try:
			subclient.send_message(chatId=data.message.chatId,message="""[c][BC]━━❃❃❃━━┅Rip━━━❃❃❃┅
[C]「 OH NOO !! 」
[C]Someone has left 💀 the
[C]group chat.
[BC]━━❃❃❃━━┅━Rip━━┅❃❃❃━━━━""")
			print(f"Someone left the gc")
		except Exception as e:
			print(e)

@client.event("on_avatar_chat_start")
def on_avatar_start_chat_start(data):
	if data.comId==cidy:
		if subclient.get_chat_thread(data.message.chatId).title!=None:
			try:
				subclient.send_message(chatId=data.message.chatId,message=f"Ghost message by <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
				subclient.kick(userId=data.message.author.userId,chatId=data.message.chatId,allowRejoin=True)
				print(f"Someone spamed gc")
			except Exception as e:
				print(e)
l=[]
@client.event("on_text_message")
def on_text_message(data):
	if data.comId==cidy:
		ex=data.message.content
		cd=ex.split(' ')
		x=cd[0]
		c=cd[1:]
		#print(c)
		adx=[]
		for w in cd:
			adx.append(w)
		print(adx)
		#m=data.message.messageType
		if ex:
			for i in adx:
				if len(i)<=50:
					if i[:23]=="http://aminoapps.com/p/" or i[:23]=="http://aminoapps.com/c/":
						fok=client.get_from_code(i)
						cidx=fok.path[1:fok.path.index("/")]
						if cidx!=cid:
							try:
								subclient.delete_message(chatId=data.message.chatId,messageId=data.message.messageId,asStaff=False)
								#subclient.kick(chatId=data.message.chatId,userId=data.message.author.userId,allowRejoin=True)
								s=subclient.get_chat_thread(data.message.chatId).title
								subclient.start_chat(userId=adm,message=f"ndc://x{cid}/user-profile/{data.message.author.userId} was advertisng in {s}")
								
								subclient.send_message(chatId=data.message.chatId,message="[c]No advertising here !!")
								print("spotted advertiser")
							except Exception as e:
								print(e)
			if x.lower()=="*info" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="[ci]Hey there i m a bot, I can welcome newbies and also tell them bye when they leave")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*global":
				try:
					for i in c:
						d=client.get_from_code(i).objectId
					subclient.send_message(chatId=data.message.chatId,message=f"""Global id :- 
ndc://g/user_nickname/tag/{d}""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*clear":
				if x.lower() not in l:
					try:
						for i in c:
							d=int(i)
						a=subclient.get_chat_messages(chatId=data.message.chatId,size=d)
						if d<=5:
							for i in a.messageId:
								subclient.delete_message(chatId=data.message.chatId,messageId=i,asStaff=True,reason="clear")
							subclient.send_message(chatId=data.message.chatId,message="[ci]Cleared")
							print(f"Info requested by {data.message.author.nickname}")
						else:
							subclient.send_message(chatId=data.message.chatId,message="[ci]Can't clear more than 5")
					except Exception as e:
						print(e)
				else:
					subclient.send_message(chatId=data.message.chatId,message="Clear command is locked")
			if x.lower()=="*lock command" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"Locked commands {l}")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*alock":
				if data.message.author.userId in adm:
					try:
						for i in c:
							l.append(i)
							subclient.send_message(chatId=data.message.chatId,message=f"locked {i} command")
							print(l)
							print(f"Info requested by {data.message.author.nickname}")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="This command is only accessible to admin")
					except Exception as e:
						print(e)
			if x.lower()=="*rlock":
				if data.message.author.userId in adm:
					try:
						for i in c:
							l.remove(i)
							subclient.send_message(chatId=data.message.chatId,message=f"unlocked {i} command")
							print(l)
							print(f"Info requested by {data.message.author.nickname}")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="This command is only accessible to admin")
					except Exception as e:
						print(e)
			if x.lower()=="*say":
				if x.lower() not in l:
					if c==[]:
						try:
							subclient.send_message(chatId=data.message.chatId,message=f"{data.message.author.nickname}, i can't talk unless you write something after say !")
						except:
							pass
					else:
						try:
							t=''
							lx='en'
							for i in c:
								t=t+i
							out=gTTS(text=t,lang=lx,slow=False)
							out.save("soundfx.mp3")
							with open("soundfx.mp3","rb") as f:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="audio")
							f.close()
							print(f"Info requested by {data.message.author.nickname}")
						except Exception as e:
							print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="say command is locked")
					except:
						pass
			if x.lower()=="*join":
				if c==[]:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"{data.message.author.nickname}, you have to paste the link after join, dumb !")
					except:
						pass
				else:
					try:
						for i in c:
							try:
								d=client.get_from_code(i).objectId
								subclient.join_chat(chatId=d)
								subclient.send_message(chatId=data.message.chatId,message="Joined !!")
							except Exception as e:
								print(e)
						print(f"Info requested by {data.message.author.nickname}")
					except Exception as e:
						print(e)
			if x.lower()=="*invitevc" and c==[]:
				try:
					subclient.invite_to_vc(userId=data.message.author.userId,chatId=data.message.chatId)
					print(f"invited {data.message.author.nickname} to vc")
				except Exception as e:
					print(e)
					subclient.send_message(chatId=data.message.chatId,message=f"[ic]I dont have co-host/host/staff id to invite u to vc, <$@{data.message.author.nickname}$>")
			if x.lower()=="*inviteall" and c==[]:
				if x.lower() not in l:
					try:
						h=subclient.get_online_users(start=0,size=1000)
						for u in h.profile.userId:
							try:
								subclient.invite_to_vc(userId=u,chatId=data.message.chatId)
							except Exception as e:
								print(e)
								pass
						subclient.send_message(chatId=data.message.chatId,message=f"[ic]Invited all online Users in cm")
						print(f"invited {data.message.author.nickname} to vc")
					except Exception as e:
						print(e)
						subclient.send_message(chatId=data.message.chatId,message=f"[ic]I dont have co-host/host/staff id to invite u to vc, <$@{data.message.author.nickname}$>")
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Inviteall command is locked")
					except:
						pass
			if x.lower()=="*prank" and c==[]:
				try:
					subclient.delete_message(messageId=data.message.messageId,chatId=data.message.chatId,asStaff=True,reason="clear")
					subclient.send_message(chatId=data.message.chatId,message=f"You have been fooled by {data.message.author.nickname}",messageType=107)
					print("deleted a message")
				except Exception as e:
					print(e)
					subclient.send_message(chatId=data.message.chatId,message=f"[ic]I dont have staff id to run that command, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
			if x.lower()=="*pm" and c==[]:
				if x.lower() not in l:
					try:
						subclient.start_chat(userId=data.message.author.userId,message="Hey Bot here !")
						subclient.send_message(chatId=data.message.chatId,message=f"Check your pm <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
						print(f"invite {data.message.author.nickname} to pm")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"Pm command is locked <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					except:
						pass
			if x.lower()=="*startvc" and c==[]:
				if x.lower() not in l:
					try:
						client.start_vc(comId=cid,chatId=data.message.chatId,joinType=1)
						subclient.send_message(chatId=data.message.chatId,message=f"Vc started")
						print(f"VC started")
					except Exception as e:
						print(e)
						try:
							subclient.send_message(chatId=data.message.chatId,message=f"[ic]I dont have co-host/host id to run that command, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"Start command is locked <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					except:
						pass
			if x.lower()=="*endvc" and c==[]:
				try:
					client.end_vc(comId=cid,chatId=data.message.chatId,joinType=1)
					subclient.send_message(chatId=data.message.chatId,message=f"End Vc ")
					print(f"End Vc")
				except Exception as e:
					print(e)
					subclient.send_message(chatId=data.message.chatId,message=f"[ic]I dont have co-host/host/staff id to run that command, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
			if x.lower()=="*members" and c==[]:
				if x.lower() not in l:
					try:
						o=""
						q=subclient.get_online_users(start=0,size=1000)
						for uid in q.profile.nickname:
							o=o+uid+"\n"
						subclient.send_message(chatId=data.message.chatId,message=o)
						print("done")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Members command is locked")
					except:
						pass

			if x.lower()=="*amino" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[cbu]What is amino.py
[c]Amino.py Is A Python API For Communicating With Amino Servers Whilst Pretending That You're An App User. This Is Mostly Accomplished By Spoofing Device Configuration Headers. It Is Also For Objectifying And Organizing Amino Response Data, So That Actually Doing Anything Is Easier.
do -import to find more
-source :- google""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*import" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""import amino.py
[c]This command/line imports the amino.py module which consists of 5 set of python files namely
-acm
-client
-subclient
-socket
-init""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*acm" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[cb]acm attribute
[c]To use this Acm commands, you will have to first make an object of acm
Acm=amino.ACM()
You can use this "Acm" object in commands
For eg:- if u want to create a community the line is
[c]--------------------------------

import amino
Acm=amino.ACM()
Acm.create_community(name: str, tagline: str, icon: BinaryIO, themeColor: str, joinType: int = 0, primaryLanguage: str = 'en')

[c]--------------------------------
Ps:-
str denotes string which means text in qoutes
Eg:- "uchiha clan"
BinaryIO denotes binary file... Which means the icon/image must be in binary format (wil deal about binary stuff later)
int denotes integer which means numbers... There is different type of int for joinType ....like 1,2,3....
en denotes english""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*help" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[BC]~~BoT Command Menu~~

[C]Don't forget to put (*) Before each command

➼ help           ➼ quote
➼ check        ➼ join
➼ startvc      ➼ leave
➼ endvc        ➼ joinall
➼ joinvc        ➼ leaveall
➼ startsc      ➼ follow
➼ endsc        ➼ unfollow
➼ joinsc        ➼ global
➼ inviteall     ➼ joinall
➼ ghost         ➼ mention
➼ say             ➼ mentionco
➼ spam         ➼ bg
➼ prank         ➼ pvp
➼ gif              ➼ cb
➼ tr                ➼ accept
➼ dice           ➼ ask
➼ msg           ➼ clear
➼ abw           ➼ lock command
➼ rbw            ➼ unlock command
➼ bwl            ➼ llock
➼ chatlist     ➼ joinamimo
➼ all              ➼ leaveamino
➼ google      ➼ restart
➼ block
➼ unblock""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*movie" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[cb]Movie Shows https://yomovies.pe/""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*tvshow" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[cb]https://www.zee5.com/tvshows""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*xxx" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[cb]Pron 20 Websites https://www.pornhub.com/
					http://www.affairhub.com/goto/filf/http://www.affairhub.com/goto/broken-teens/
					http://www.affairhub.com/go/idesires/
					https://anyxxx.com/search/indian#""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*ipl" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[cb]https://www.google.com/search?q=IPL+lesest+match&oq=IPL+lesest+match&aqs=chrome..69i57j0i13j0i22i30l3.15460j1j4&client=ms-android-xiaomi&sourceid=chrome-mobile&ie=UTF-8""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*flirt" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[i]Everytime i look at you, my heart races faster than a bullet""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*fart" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[i]Phush phush phush,Ahh!!!""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*hugme" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[i]opens my arms and hugs you gently (づ｡◕‿‿◕｡)づ
[i]I m here for you...""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*joke" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[i]1.Hindi Joke in English
   Rohan & Mohan were sitting in a kabristan &      were talking.
   Rohan: Mohan, dekho yeh murde kitne                 aaraam se apni kabron mein sote hai.
   Sare murde uth khare hue aur bole: Kyun na       soye, yeh jaga apni jaan de ke hasil kee hai..!
   
   2.Bihari Babu Aare O Doctor.
    Kaise Nasbandi Kiye Ho Hamari.
    Biwi Fir Se Maa Banne Wali Hai.
    Dr.Burbaak Hum Nasbandi Tohar Kiye Hai.
    Poore Bihar Ki N Ahi
    
    3.Guest: Beta Naam Kya Hai Aapka,
 Boy: Mintu.
    Guest: Ye Toh Ghar Ka Hai..
Wo Batao Jo School Mein Bulatey Hain                        Tumhey,
Boy: O Mintu Behan Ke Laudey.

If you need more jokes, ask your host.
               Happy And Injoy """)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*punchme" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[i]Wears My Boxing Gloves And Punches U Hard At Ur Face""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*moan" and c==[]:
				if subclient.get_chat_thread(data.message.chatId).title==None:
					if x.lower() not in l:
						sounds="moan.mp3"
						with open(sounds,"rb") as f:
							try:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="audio")
								print(f"Info requested by {data.message.author.nickname}")
							except Exception as e:
								print(e)
					else:
						try:
							subclient.send_message(chatId=data.message.chatId,message="Moan command is locked")
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Moan command works only in pm, type -pm to make the bot join pm")
					except:
						pass
			if x.lower()=="*cheerme" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[i]I have replied to many members, but when i replies u, it makes my day!""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*threeall" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""https://youtube.com/channel/UCoPoVn07TEUQydSOi_mPo3Q Three All subscribe This channel""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*cid" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"{cid}")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="*twerk" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[i]my booty hurts right now, maybe later..""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="-heicmd" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[b]Commands by Hei!!
-flirt
-punchme
-twerk
-cheerme
-moan
-hugme
-joke
-fart""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			
def socketRoot():
	j=0
	while True:
		if j>=300:
			print("Updating socket.......")
			client.close()
			client.start()
			print("Socket updated")
			j=0
		j=j+1
		time.sleep(1)
socketRoot()