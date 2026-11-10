import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

# 👇把下面引号里的内容换成你第一步复制的 Token
BOT_TOKEN = "你的Token填在这里"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    text = (
        "🚀 开始使用 · 查我的授权状态 /start\n\n"
        "📷 UID反 · 发收款码图片破解 /skm\n\n"
        "🛠 操作手册 · 指令格式与用法 /help\n\n"
        "📋 大厅面板 · 实时进度与队列 /mb\n\n"
        "👤 我的信息 · 到期时间与剩余次数 /info\n\n"
        "🔴 取消我当前正在跑的任务 /cancel\n\n"
        "📊 今日剩余调度量 /qq\n\n"
        "🔍 名字查询 /mz 账号或UID\n\n"
        "🔍 扫码查名 /zcm 账号或UID\n\n"
        "🔆 姓名破解 /zm 李x鲜 账号\n\n"
        "⚡ 单次支二 /z2 姓名 账号"
    )
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("❌ 菜单", callback_data="close_menu"))
    
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler(commands=['z2'])
def handle_z2(message):
    bot.reply_to(message, "⏳ 任务已接收，正在调度千线程并发队列...")
    time.sleep(1.5)
    bot.reply_to(message, "【查询结果】\n目标账号：已加密隐藏\n匹配状态：一致 (模拟成功)")

if __name__ == '__main__':
    print("Bot 正在运行...")
    bot.infinity_polling()
