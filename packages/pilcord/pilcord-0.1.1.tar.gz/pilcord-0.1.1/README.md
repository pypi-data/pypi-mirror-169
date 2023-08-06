# pilcord

`note: since the library is still under development, the method and its parameter may change in the future, to get latest information please check the github repository`

[github](https://github.com/ResetXD/pilcord)


[ WIP ] A library rich with many image generation funcitons powered by PIL for your discord bot such as leveling, welcome card and meme generation!


## ranking card preview

`card1`

![card1](https://cdn.discordapp.com/attachments/907213435358547968/994620579816681572/unknown.png)


`card2`
![card](https://cdn.discordapp.com/attachments/907213435358547968/1020968412144480316/final.png)


`card3` *same as card2 but with background*
![card](https://cdn.discordapp.com/attachments/1018936393659076668/1022149875544113172/rank.png)


<br>

## installation

`for pypi version`
```sh
pip install pilcord
```

`for github developement version`
```sh
pip install git+https://github.com/ResetXD/pilcord
```

## How To Use

The method will return `bytes` which can directly be used in discord.py/disnake/pycord/nextcord 's `File class`.


<br>


## Rank Card Example

`It returns bytes which can directly be used in discord.py and its fork's File class.`

```py

from disnake.ext import commands
from DiscordLevelingCard import RankCard, CardSettings
import disnake

client = commands.Bot()
# define background, bar_color, text_color at one place
card_settings = CardSettings(
    background="url or path to background image",
    text_color="white",
    bar_color="#000000"
)

@client.slash_command(name="rank")
async def user_rank_card(ctx, user:disnake.Member):
    await ctx.response.defer()
    a = RankCard(
        settings=card_settings,
        avatar=user.display_avatar.url,
        level=1,
        current_exp=1,
        max_exp=1,
        username="cool username",
        rank=1
    )
    image = await a.card1()
    await ctx.edit_original_message(file=disnake.File(image, filename="rank.png")) # providing filename is very important

```

<br>

## Documentation


<details>

<summary> <span style="color:yellow">RankCard</span> class</summary>

<br>

`__init__` method

```py
RankCard(
    settings: CardSettings,
    avatar:str,
    level:int,
    current_exp:int,
    max_exp:int,
    username:str,
    rank: Optional[int] = None
)
```

- `settings` - Settings class from DiscordLevelingCard.

- `avatar` - avatar image url.

- `level` - level of the user.

- `current_exp` - current exp of the user.

- `max_exp` - max exp of the user.

- `username` - username of the user.

- `rank` - rank of the user. (optional)

</details>

<details>

<summary> <span style="color:yellow">CardSettings</span> class</summary>

<br>

`__init__` method

```py
CardSettings(
    background: Union[PathLike, BufferedIOBase, str],
    bar_color: Optional[str] = 'white',
    text_color: Optional[str] = 'white',
    background_color: Optional[str]= "#36393f"

)
```

- `background` - background image url or file-object in `rb` mode.
  - `4:1` aspect ratio recommended.

- `bar_color` - color of the bar [example: "white" or "#000000"]

- `text_color` - color of the text [example: "white" or "#000000"]

- `background_color` - color of the background [example: "white" or "#000000"]

</details>


<details>

<summary> <span style="color:yellow">card1</span> method</summary>


```py
RankCard.card1()
```

`returns` - `bytes` which can directly be used within `discord.File` class.



![card1](https://cdn.discordapp.com/attachments/907213435358547968/994620579816681572/unknown.png)

<br>

</details>


<details>

<summary> <span style="color:yellow">card2</span> method</summary>


```py
RankCard.card2()
```

`returns` - `bytes` which can directly be used within `discord.File` class.



![card](https://cdn.discordapp.com/attachments/907213435358547968/1020968412144480316/final.png)

<br>

</details>


<details>

<summary> <span style="color:yellow">card3</span> method</summary>


```py
RankCard.card3()
```

`returns` - `bytes` which can directly be used within `discord.File` class.



![card](https://cdn.discordapp.com/attachments/1018936393659076668/1022149875544113172/rank.png)

<br>

</details>
