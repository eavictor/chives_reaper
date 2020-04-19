import json
from discord.ext.commands import Bot, bot_has_permissions


with open("settings.json", "r", encoding="utf-8") as file:
    settings = json.loads(file.read())


bot = Bot(command_prefix=settings.get("command_prefix", "!"))


@bot.command(name=settings.get("announce", "公告"))
@bot_has_permissions(manage_messages=True)
async def announce(ctx, message):
    # Owner Check: 確定只有乾太可以發公告
    if not ctx.message.author.id == ctx.guild.owner.id:
        await ctx.send(f"{ctx.message.author.display_name} 這個87嘗試偷發公告，當BOT是塑膠做的嗎？")
        await ctx.message.delete()
        return None

    await ctx.send(" ".join(["@everyone", message]))
    await ctx.message.delete()
    return None


@bot.command(name=settings.get("harvest", "割韭菜"))
@bot_has_permissions(kick_members=True)
async def rip(ctx, message_id=None, kick_reason=None):
    # Owner Check: 確定只有乾太可以割韭菜
    if not ctx.message.author.id == ctx.guild.owner.id:
        await ctx.send(f"ㄟㄟ，{ctx.message.author.display_name} 這個韭菜竟然想要割自己耶！")
        return None
    # Format Check: 確定有輸入 message_id 給BOT撈
    if not message_id:
        await ctx.send("海濤法師說我的眼睛業障hen重，才會看不到 message_id。")
        return None
    else:
        try:
            int(message_id)
        except ValueError:
            await ctx.send(f"{message_id} 看起來不像「半形阿拉伯數字」R")
            return None
    # Format Check: 確定乾太有輸入 踢人的理由
    if not kick_reason:
        await ctx.send("seafood忘記說踢人的理由惹歐")
        return None

    # 1. 撈特定的message
    message = await ctx.fetch_message(message_id)

    # 2. 找出有回應的user
    active_members = set()  # 有回應的member
    for reaction in message.reactions:
        for user in await reaction.users().flatten():
            active_members.add(user.id)  # 只加入user id節省記憶體空間

    # 3. 找出全部伺服器的members，過濾掉以下：
    #    (1) 有身份組的大佬們(everyone除外)
    #    (2) BOT們
    #    (3) 有按emoji的村民們
    #    然後踢掉不符合上面條件的村民
    members = bot.get_all_members()
    chives = ""  # 被割掉的韭菜名單
    for member in members:
        # 如果這個人是「有身份組的人」、「BOT」或「有回應的村民」就略過
        if not member.bot and len(member.roles) <= 1 and member.id not in active_members:
            # 判斷會不會超過2000字元上限，不會超過的話名單繼續加
            if (2000 - len(chives)) > (len(member.display_name) + 1):
                chives = " ".join([chives, member.display_name])
            # 這個名字加上去以後會頂到兩千字元的時候就給他用力唱出去，接著再建立新名單
            else:
                await ctx.send(chives)
                chives = member.display_name
            # 割韭菜
            # await ctx.guild.kick(member.id, reason=kick_reason)
    # 檢察名單還有沒有沒上報的，有的話就說出去
    if len(chives) > 0:
        await ctx.send(chives)
    return None


def main():
    token = settings.get("token", None)
    if not token:
        raise ValueError("沒有Token，記得到這邊拿 https://discordapp.com/developers/applications/")
    bot.run(token)


if __name__ == "__main__":
    main()
