from http import server
import os, time, logging, glob, sys, threading, asyncio
from logging import handlers
from urllib import request
from os import path

os.popen("kill `pidof Xvnc` 2> /dev/null")


class DictClass:
    def __init__(self, name, data):
        for k, v in data.items():
            setattr(self, k, DictClass(name, v) if isinstance(v, dict) else v)


def keepAlive(bot):
    @bot.event
    async def on_ready():
        bot.info = DictClass("application", await bot.http.application_info())

        class Server(server.BaseHTTPRequestHandler):
            start = time.time()

            def log_request(self, code="", size=""):
                pass

            def do_HEAD(self):
                self.send_response(200)
                self.send_header(
                    "Content-Type",
                    "text/html;charset=utf-8",
                )
                self.send_header("Cache-Control", "no-cache")
                self.send_header("x-content-type-options", "nosniff")
                self.end_headers()

            def do_GET(self):
                self.do_HEAD()
                self.send_response(200)
                info = bot.info
                owner = info.owner
                team = info.team
                user = bot.user
                try:
                    install = f"<a href={info.custom_install_url}>Install</a>"
                except:
                    try:
                        install = f"<a href=https://discord.com/api/oauth2/authorize?client_id={bot.info.id}&scope={'+'.join(bot.info.install_params.scopes)}&permissions={int(bot.info.install_params.permissions)}>Install</a>"
                    except:
                        install = ""
                description = info.description.replace("`", "\\`")
                self.wfile.write(
                    b"\n".join([open(i, "rb").read() for i in glob.glob("logs*")])
                    if self.path == "/logs"
                    else (
                        f"<!DOCTYPE html><meta charset=utf-8><meta name=viewport content='width=device-width'><meta name=description content='{description}'><link rel='shortcut icon'href={user.avatar}><html lang=en><script src=https://cdn.jsdelivr.net/gh/adamvleggett/drawdown/drawdown.min.js></script><script>onload=()=>{{setInterval(()=>{{let u=BigInt(Math.ceil(Date.now()/1000-{self.start}))\ndocument.getElementById('u').innerText=`${{u>86400n?`${{u/86400n}}d`:''}}${{u>3600n?`${{u/3600n%60n}}h`:''}}${{u>60n?`${{u/60n%24n}}m`:''}}${{`${{u%60n}}`}}s`}},1000)\ndocument.getElementById('s').innerText=new Date({self.start*1000}).toLocaleString();document.getElementById('d').innerHTML=markdown(`{description}`)}}</script><style>*:not(code){{background-color:#FDF6E3;color:#657B83;font-family:sans-serif;text-align:center;margin:auto}}@media(prefers-color-scheme:dark){{*:not(code){{background-color:#002B36;color:#839496}}}}img{{height:1em</style><title>{user}</title><h1>{user}<img src={user.avatar} alt></h1><p id=d><table><tr><th>Servers<td>{len(bot.guilds)}<tr><th>Latency<td>{round(bot.latency*1000 if bot.latency!=float('nan') else 'Offline?')}ms<tr><th>Uptime<td id=u><tr><th>Up since<td id=s>{f'<tr><th><a href=${team.icon}>'+[f'<tr><th><a href=https://discord.com/users/{m}>Creator</a><img src={m.avatar} alt>'for m in team.members].join('')if team else f'<tr><th><a href=https://discord.com/users/{owner.id}>DM owner</a><td><img src={owner.avatar} alt>{owner}'}<tr><th>RAM used<td>{sum(map(int, os.popen('ps hx -o rss').readlines()))}B</table>{install}<br>"
                        + "<code id=l></code><button type=button onclick=\"setInterval(()=>{let x=new XMLHttpRequest();x.onload=r=>document.getElementById('l').innerText=r.srcElement.responseText;x.open('GET','logs');x.send()},1e3);scrollTo(0, document.body.scrollHeight)\">Show logs"
                        if os.path.isfile("logs")
                        else ""
                    ).encode()
                )

        threading.Thread(
            target=server.ThreadingHTTPServer(("", 80), Server).serve_forever
        ).start()
        print(
            "Server is ready! \033[4mHit enter\033[0m to update bot/owner info shown on website"
        )
        while True:
            t = threading.Thread(target=input)
            t.start()
            while t.is_alive():
                await asyncio.sleep(0)
            bot.info = DictClass("application", await bot.http.application_info())

    intents = bot.intents
    if not (intents.presences or intents.members or intents.message_content):
        logger = logging.getLogger("discord")
        logger.setLevel(logging.DEBUG)
        handler = handlers.TimedRotatingFileHandler(
            "./logs", backupCount=1, when="m", interval=30
        )
        handler.setFormatter(
            logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
        )
        logger.addHandler(handler)
    try:
        request.urlopen(
            f"https://up.repl.link/add?author={os.environ['REPL_OWNER'].lower()}&repl={os.environ['REPL_SLUG'].lower()}"
        )
    except:
        pass

    @bot.listen()
    async def on_disconnect():
        if not bot.ws or bot.is_ws_ratelimited():
            request.urlopen(
                f"https://cd594a2f-0e9f-48f1-b3eb-e7f6e8665adf.id.repl.co/{os.environ['REPL_ID']}"
            )
            os.kill(1, 1)

    try:
        bot.run(os.environ["DISCORD_TOKEN"])
    except Exception as err:
        if getattr(err, "status", 0) == 429:
            request.urlopen(
                f"https://cd594a2f-0e9f-48f1-b3eb-e7f6e8665adf.id.repl.co/{os.environ['REPL_ID']}"
            )
            os.kill(1, 1)
        print(err)
