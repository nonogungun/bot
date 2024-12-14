
#라이브러리 불러오기 
import discord, asyncio

#디코 클라이언트를 얻어오는 내장함수 
#client = discord.Client(intents=discord.Intents.default())

intents = discord.Intents.default()
intents.message_content = True 
#bot 생성 
client = discord.Client(intents=intents)


@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("봇이 온라인 전환됨")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("봇의 상태매세지"))

@client.event
async def on_message(message):

    if message.author == client.user:
        return  # 봇 자신이 보낸 메시지에는 반응하지 않도록 예외처리 


    if message.content == "테스트": # 메세지 감지
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        #await message.author.send ("{} | {}, Hello".format(message.author, message.author.mention))

    if message.content == "야":
        ch = client.get_channel(1317145624038080571)
        #await ch.send ("User, Hello")
        await ch.send ("{} | {}, User, Hello".format(message.author, message.author.mention))


#async def on_message(message):
    if message.content == "임베드": # 메세지 감지
        embed = discord.Embed(title="제목", description="부제목", color=0x79e6d9)

        embed.add_field(name="임베드 라인 1 - inline = false로 책정", value="라인 이름에 해당하는 값", inline=False)
        embed.add_field(name="임베드 라인 2 - inline = false로 책정", value="라인 이름에 해당하는 값", inline=False)

        embed.add_field(name="임베드 라인 3 - inline = true로 책정", value="라인 이름에 해당하는 값", inline=True)
        embed.add_field(name="임베드 라인 4 - inline = true로 책정", value="라인 이름에 해당하는 값", inline=True)

        await message.channel.send (embed=embed) #이렇게 메세지를 입럭한 채널에 보낼 수 있대요 

#삭제 기능 
    if message.content.startswith ("!청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다"
                                  .format(amount, message.author), color=0x000000)
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))



# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('MTMxNzE0MjI0NjQyODI1MDExMg.G-qu88.cDFY1sIUT5I3KNXhp2fUMqb_LIiIrPVzVcRhDE')































