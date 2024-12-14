
import discord, asyncio

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from youtube_dl import YoutubeDL
from discord.ext import commands
from discord import FFmpegPCMAudio
#import yt_dlp as youtube_dl

#bot 생성 
intents = discord.Intents.default()
intents.message_content = True 
intents.members = True  # 멤버 상태 추적 허용
client = discord.Client(intents=intents)

#chrome driver 생성 
#options = Options() # Chrome 옵션 설정
# 웹드라이버 자동 설치 및 설정
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#전역 변수 : List, 재생 여부, 


@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("봇이 온라인 전환됨")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("봇의 상태매세지"))


#메세지가 보내졌을때 호출되는 이벤트
@client.event
async def on_message(message):
    if message.author == client.user:
        return  # 봇 자신이 보낸 메시지에는 반응하지 않도록 예외처리 

    #메세지 보낸 사람의 채널에 연결해 
    if message.content.startswith("야"):
        global vc
        vc = await message.author.voice.channel.connect() 


    if message.content == "나가":
        await vc.disconnect()
        


    #if message.content.strip():
    if message.content.startswith("노래"):
        #await message.channel.purge(limit=1)

        start = discord.Embed(title="검색 중 : {} ".format(message.content[2:])
                              ,description="", color=0x62c1cc)
        msg = await message.channel.send(embed=start)
        
        baseUrl = "https://www.youtube.com/results?search_query="
        Url = baseUrl + message.content[2:]
        print(Url)

        #driver.get(Url)
        #info = driver.find_elements(By.XPATH,
        #'//*[@id="contents"]/ytd-video-renderer[1]')[0].text #.replace("\n", " | ")
        #await message.channel.send("{}".format(info))


        YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
                          , 'options': '-vn'}
        
        for voice_client in client.voice_clients:
            if voice_client.guild == message.guild:  # 현재 서버에서 봇의 음성 클라이언트 찾기
                # 봇이 재생 중인지 확인
                if voice_client.is_playing():
                    voice_client.stop()

                    embed = discord.Embed(title="노래 재생",
                            description = "현재 " + Url + "을(를) 재생하고 있습니다.", color = 0x00ff00)
                    await message.channel.send(embed = embed)
                    
                    #with  YoutubeDL(YDL_OPTIONS) as ydl:
                    #    info = ydl.extract_info(Url, download=False)

                    #URL = info['formats'][0]['url']
                    voice_client.play(discord.FFmpegPCMAudio(Url))


                else:
                    voice_client.stop()
                    await message.channel.send("노래가 이미 재생되고 있습니다!")
        



# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('MTMxNzE0MjI0NjQyODI1MDExMg.G-qu88.cDFY1sIUT5I3KNXhp2fUMqb_LIiIrPVzVcRhDE')
