from linepy import *
from akad.ttypes import *

print('[DEBUG] Memulai Bot')
#uchull = LineClient()
uchull = LineClient(authToken='ISITOKENLU')
uchull.log("Auth Token : " + str(uchull.authToken))
channel = LineChannel(uchull)
#objek = LineObject(uchull) #this is for trial :v
uchull.log("Channel Access Token : " + str(channel.channelAccessToken))

poll = LinePoll(uchull)

print('[DEBUG] Bot Started ^_^')

print("*************Welcome*************")
print('Bot Name: SB CVP')
print('Version: TKJ')
print('Codename: Uchull TKJ')
print('Creator-ID.LINE: uchull.tkj') #HARGAI CREATOR

while True:
	try:
		ops = poll.singleTrace(count=50)
		print("=-=-=-=-=-=-=-=-=---=-=-=-=-=-=-=-=-=\n")
		print(ops)
		print("=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		if ops != None:
			for op in ops:
				if op.type == 25 or op.type == 25: #BEBAS MAU BERAPA AJA , BISA [26.26],[25.26],[25.25]
					msg = op.message
					text = str(msg.text)
					msg_id = msg.id
					if msg.toType == 0: #bkn room
						receiver = msg._from
						sender = msg.to
					else:
						receiver = msg.to #room
						sender = msg._from
					try:
						if msg.contentType == 0:
							if msg.toType == 2 or 1 or 0:
								uchull.sendChatChecked(receiver, msg_id)
								contact = uchull.getContact(sender)
								if text.lower() == '.update':
									uchull.sendMessage(receiver, "wait foor upload")
									uchull.updateProfileVideoPicture('image2.png','demo.mp4',fap=0) 
									#SIMAK BAIK-BAIK( KLO LU MAU GANTI FTO SAMA VIDEO LU, HAPUS TUH FTO SAMA VIDEONYA YG DI SC, TERUS LU MASUKIN FTO N VIDEO SESUKA HATI LO) 
									#fap = 0 artinya anda sudah punya screenshot untuk videonya yg bakal di upload ke line
									#fap = 1 artinya anda blm punya screenshot untuk diupload dan bakal digenerate langsung oleh bot :3
									client.sendMessage(receiver,"sukses uploads")
					except Exception as d:
						print('[ERROR] You Got Error On Chat Bot Command Section :p')
						print(str(d))
				poll.setRevision(op.revision)
	except Exception as e:
		print('[ERROR] Well You Got Error On Your Bot -,-')
		print(str(e))
