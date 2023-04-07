"""
MIT License

Copyright (c) 2022 Arsh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import asyncio
import io
import os
import sys
import traceback

from pyrogram import filters
from pyrogram.types import Message

from samurai.database import client
from samurai import DEV_USERS, ubot


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.id

    elif not message.from_user.is_self:
        reply_id = message.id

    return reply_id


@ubot.on_message(
    filters.command("eval", ".")
    & ~filters.forwarded
    & ~filters.via_bot
)
async def eval_func_init(bot, message):
    await evaluation_func(bot, message)


@ubot.on_edited_message(
    filters.command("eval", ".")
    & ~filters.forwarded
    & ~filters.via_bot
)
async def eval_func_edited(bot, message):
    await evaluation_func(bot, message)


async def evaluation_func(bot: ubot, message: Message):
    status_message = await message.reply_text("Processing ...")
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_id = message.id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.id

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        reply = message.reply_to_message or None
        await aexec(cmd, bot, message, reply, client)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = "<b>Expression</b>:\n<code>{}</code>\n\n<b>Result</b>:\n<code>{}</code> \n".format(
        cmd, evaluation.strip()
    )

    if len(final_output) > 4096:
        with open("eval.txt", "w", encoding="utf8") as out_file:
            out_file.write(str(final_output))

        await message.reply_document(
            "eval.txt",
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=ReplyCheck(message),
        )
        os.remove("eval.txt")
        await status_message.delete()
    else:
        await status_message.edit(final_output)


async def aexec(code, b, m, r, d):
    sys.tracebacklimit = 0
    exec(
        "async def __aexec(b, m, r, d): "
        + "".join(f"\n {line}" for line in code.split("\n"))
    )
    return await locals()["__aexec"](b, m, r, d)


@ubot.on_edited_message(
    filters.command("exec", ".")
    & ~filters.forwarded
    & ~filters.via_bot
)
async def execution_func_edited(bot, message):
    await execution(bot, message)


@ubot.on_message(
    filters.command("exec", ".")
    & ~filters.forwarded
    & ~filters.via_bot
)
async def execution_func(bot, message):
    await execution(bot, message)


async def execution(bot: ubot, message: Message):
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_id = message.id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.id

    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "No errors"
    o = stdout.decode()
    if not o:
        o = "No output"

    OUTPUT = ""
    OUTPUT += f"<b>Command:</b>\n<code>{cmd}</code>\n\n"
    OUTPUT += f"<b>Output</b>: \n<code>{o}</code>\n"
    OUTPUT += f"<b>Errors</b>: \n<code>{e}</code>"

    if len(OUTPUT) > 4096:
        with open("exec.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(OUTPUT))
        await message.reply_document(
            document="exec.text",
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=ReplyCheck(message),
        )
        os.remove("exec.text")
    else:
        await message.reply_text(OUTPUT)