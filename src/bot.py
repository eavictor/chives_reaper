import time
from discord.ext.commands import Bot, bot_has_permissions


bot = Bot(command_prefix="!")


@bot.command(name="公告")
@bot_has_permissions(manage_messages=True)
async def announce(ctx, message):
    # Owner Check: 確定只有乾太可以發公告
    if not message.author.id == ctx.guild.owner.id:
        await ctx.send(f"{ctx.message.author.display_name} 這個87嘗試偷發公告，當BOT是塑膠做的嗎？")
        await ctx.message.delete()
        return None

    await ctx.send(" ".join(["@everyone", message]))
    await ctx.message.delete()
    return None


@bot.command(name="割韭菜")
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
        for user in reaction.users().flatten():
            active_members.add(user.id)  # 只加入user id節省記憶體空間

    # 3. 找出全部伺服器的members，過濾掉以下：
    #    (1) 有身份組的大佬們(everyone除外)
    #    (2) BOT們
    #    (3) 有按emoji的村民們
    members = bot.get_all_members()
    chives = set()  # 要被割掉的韭菜們的名字會在這邊
    for member in members:
        if not member.bot and len(member.roles) <= 1 and member.id not in active_members:
            chives.add(member.display_name)
            # await ctx.guild.kick(member.id, reason=kick_reason)  # TODO: 這行取消註解才會踢人！

    # 4. 唱名被割掉的韭菜，我們懷念他們
    await ctx.send("開始唱名被割掉的韭菜喔喔喔喔喔！")
    # 這次要報的韭菜名單
    kick_report = ""
    for chive in chives:
        # 還沒有2000字元，繼續寫韭菜名單！
        if 2000 - len(kick_report) > chive:
            kick_report = " ".join([kick_report, chive])
        # 要頂到2000字元了，唱名唱起來！
        else:
            await ctx.send(kick_report)
            kick_report = chive
            time.sleep(0.01)  # 防止頂到Discord API rate limit用的，有自信不會頂到肺的話可以把這行砍掉喔 :)
    if len(kick_report) > 0:
        await ctx.send(kick_report)
    return


if __name__ == "__main__":
    bot.run("token")
