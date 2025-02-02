from ast import alias
import discord
from discord.ext import commands
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
import asyncio
import gc

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        #all the music related stuff
        self.is_playing = False
        self.is_paused = False

        # 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio/best'}
        self.FFMPEG_OPTIONS = {'options': '-vn'}

        self.vc = None
        self.ytdl = YoutubeDL(self.YDL_OPTIONS)

     #searching the item on youtube
    def search_yt(self, item):
        try:
            if item.startswith("https://"):
                info = self.ytdl.extract_info(item, download=False)
                return {'source': info["url"], 'title': info["title"]}
            else:
                # Use yt_dlp's ytsearch to find the video
                info = self.ytdl.extract_info(f"ytsearch:{item}", download=False)
                if 'entries' in info and len(info['entries']) > 0:
                    video = info['entries'][0]
                    return {'source': video['url'], 'title': video['title']}
                else:
                    return None
        except Exception as e:
            print(f"Error in search_yt: {e}")
            return None

    async def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            #get the first url
            m_url = self.music_queue[0][0]['source']

            #remove the first element as you are currently playing it
            
            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: self.ytdl.extract_info(m_url, download=False))
            song = data['url']
            self.vc.play(discord.FFmpegPCMAudio(song, executable= "ffmpeg.exe", **self.FFMPEG_OPTIONS), after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(), self.bot.loop))
            self.music_queue.pop(0)
        else:
            self.is_playing = False

            # Cleanup after song
        del data  # Free memory used for song data
        gc.collect()  # Force garbage collection

    # infinite loop checking 
    async def play_music(self, ctx):
        if len(self.music_queue) > 0:
            self.is_playing = True
            m_url = self.music_queue[0][0]['source']

            try:
                if self.vc is None or not self.vc.is_connected():
                    print(f"Connecting to channel: {self.music_queue[0][1].name}")
                    self.vc = await self.music_queue[0][1].connect()
                    print(f"Successfully connected to: {self.music_queue[0][1].name}")
                else:
                    print("Bot is already connected to a voice channel.")
                    await self.vc.move_to(self.music_queue[0][1])

                print(f"Attempting to play: {m_url}")
                loop = asyncio.get_event_loop()
                data = await loop.run_in_executor(None, lambda: self.ytdl.extract_info(m_url, download=False))
                song = data['url']
                print(f"Playing song: {data['title']} - URL: {song}")

                self.vc.play(
                    discord.FFmpegPCMAudio(song, executable="ffmpeg.exe", **self.FFMPEG_OPTIONS),
                    after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(), self.bot.loop)
                )
            except Exception as e:
                print(f"Error in play_music: {e}")
                await ctx.send("Failed to play the song.")
            finally:
                self.music_queue.pop(0)
                del data
                gc.collect()
        else:
            self.is_playing = False
            print("No more songs in the queue.")

    @commands.command(name="play", aliases=["p", "playing"], help="Plays a selected song from YouTube")
    async def play(self, ctx, *args):
        query = " ".join(args)
        try:
            voice_channel = ctx.author.voice.channel
        except:
            await ctx.send("```You need to connect to a voice channel first!```")
            return
        if self.is_paused:
            self.vc.resume()
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("```Could not download the song. Incorrect format try another keyword. This could be due to playlist or a livestream format.```")
            else:
                if self.is_playing:
                    await ctx.send(f"**#{len(self.music_queue)+2} -'{song['title']}'** added to the queue")  
                else:
                    await ctx.send(f"**'{song['title']}'** added to the queue")  
                self.music_queue.append([song, voice_channel])
                if self.is_playing == False:
                    await self.play_music(ctx)

    @commands.command(name="pause", help="Pauses the current song being played")
    async def pause(self, ctx, *args):
        if self.is_playing:
            self.is_playing = False
            self.is_paused = True
            self.vc.pause()
        elif self.is_paused:
            self.is_paused = False
            self.is_playing = True
            self.vc.resume()

    @commands.command(name = "resume", aliases=["r"], help="Resumes playing with the discord bot")
    async def resume(self, ctx, *args):
        if self.is_paused:
            self.is_paused = False
            self.is_playing = True
            self.vc.resume()

    @commands.command(name="skip", aliases=["s", "next"], help="Skips the current song being played")
    async def skip(self, ctx):
        if self.vc != None and self.vc:
            self.vc.stop()
            #try to play next in the queue if it exists
            await self.play_music(ctx)


    @commands.command(name="queue", aliases=["q", "cola"], help="Displays the current songs in queue")
    async def queue(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += f"#{i+1} -" + self.music_queue[i][0]['title'] + "\n"

        if retval != "":
            await ctx.send(f"```queue:\n{retval}```")
        else:
            await ctx.send("```No music in queue```")

    @commands.command(name="clear", aliases=["c", "bin"], help="Stops the music and clears the queue")
    async def clear(self, ctx):
        if self.vc != None and self.is_playing:
            self.vc.stop()
        self.music_queue = []
        await ctx.send("```Music queue cleared```")
        
        # Trigger garbage collection
        gc.collect()

    @commands.command(name="stop", aliases=["disconnect", "d"], help="Kick the bot from VC")
    async def dc(self, ctx):
        self.is_playing = False
        self.is_paused = False
        await self.vc.disconnect()
    
    @commands.command(name="remove", help="Removes last song added to queue")
    async def re(self, ctx):
        self.music_queue.pop()
        await ctx.send("```last song removed```")