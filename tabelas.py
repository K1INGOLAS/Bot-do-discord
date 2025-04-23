import discord
from discord.ext import commands

class TabelaBot(commands.Bot): 
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="$",
            intents=intents
        )
    
    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"O Bot {self.user} foi ligado com sucesso.")

bot = TabelaBot()

# Tabela do Blox Fruits
@bot.tree.command(name="blox-fruits", description="Tabela com preços de Gamepasses e Frutas Permanentes")
async def blox(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🍍 Tabela de Preços - Blox Fruits",
        description="Lista de Gamepasses e Frutas Permanentes",
        color=discord.Color.gold()
    )

    # Gamepasses
    embed.add_field(
        name="🎮 Gamepasses",
        value=(
            "**2X Drops:** R$ 8,75\n"
            "**Fast Boats:** R$ 8,75\n"
            "**+1 Storage:** R$ 10,00\n"
            "**2X Mastery:** R$ 11,25\n"
            "**2X Money:** R$ 11,25\n"
            "**Legendary Scrolls:** R$ 20,00\n"
            "**Dark Blade:** R$ 30,00\n"
            "**Mythical Scrolls:** R$ 37,50\n"
            "**Fruit Notifier:** R$ 67,50"
        ),
        inline=False
    )

    # Frutas Permanentes
    embed.add_field(
        name="🍇 Frutas Permanentes",
        value=(
            "**Light:** R$ 27,50 | **Kitsune:** R$ 100,00 | **Leopard:** R$ 75,00\n"
            "**Spirit:** R$ 63,00 | **Control:** R$ 62,50 | **Venom:** R$ 62,00\n"
            "**Shadow:** R$ 61,00 | **Dough:** R$ 60,00 | **T-Rex:** R$ 59,00\n"
            "**Mammoth:** R$ 58,75 | **Gravity:** R$ 57,50 | **Blizzard:** R$ 57,00\n"
            "**Pain:** R$ 55,00 | **Rumble:** R$ 52,50 | **Portal:** R$ 50,00\n"
            "**Phoenix:** R$ 50,00 | **Sound:** R$ 47,50 | **Spider:** R$ 45,00\n"
            "**Love:** R$ 42,50 | **Buddha:** R$ 41,50 | **Quake:** R$ 37,50\n"
            "**Magma:** R$ 32,50 | **Ghost:** R$ 31,88 | **Ice:** R$ 18,75\n"
            "**Dragon:** R$ 125,00 | **Gas:** R$ 62,50 | **Yeti:** R$ 75,00" 
        ),
        inline=False
    )

    # Frutas Adicionais
    embed.add_field(
        name="🔥 Novas Frutas",
        value=(
            "**Eagle Skin chromatic:** 12,50\n"
            "**Eagle:** R$ 24,80\n"
            "**Creation:** R$ 43,75\n"
            "**Gravity:** R$ 57,50"
        ),
        inline=False
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)

# Tabela do Blue Lock Rivals
@bot.tree.command(name="blue_lock_rivals", description="Tabela com todas as gamepass importantes")
async def blue(interaction: discord.Interaction):
    embed = discord.Embed(
        title="⚽ Tabela de Preços - Blue Lock Rivals",
        description="Lista de Gamepasses Importantes",
        color=discord.Color.blue()
    )

    # Gamepass da loja
    embed.add_field(
        name="🛍️ Loja do jogo",
        value=(
            "**Emotes toxic:** R$ 5,00\n"
            "**Vip:** R$ 12,50\n"
            "**Roupas de despertar:** R$ 2,25\n"
            "**Emoções de anime:** R$ 6,00\n"
            "**Som de gol:** R$ 2,25\n"
            "**Som de quebrador de ankle:** R$ 2,25\n" 
            "**Pulo de giro:** R$ 2,50\n"
            "**Servidor Privado+:** R$ 1,50"
        ),
        inline=False
    )

    # Slots de estilo e Flow
    embed.add_field(
        name="➕Slot de estilo",
        value=(
            "**Slot 2:** R$ 3,75\n"
            "**Slot 3:** R$ 7,50\n"
            "**Slot 4:** R$ 10,00\n"
            "**Slot 5:** R$ 12,50\n"
            "**Slot 6:** R$ 15,00"
        )
    )

    embed.add_field(
        name="⚡Slot de Flow",
        value=(
            "**Slot 2:** R$ 3,75\n"
            "**Slot 3:** R$ 7,50\n"
            "**Slot 4:** R$ 10,00\n"
            "**Slot 5:** R$ 12,50\n"
            "**Slot 6:** R$ 15,00"
        )
    )

    embed.add_field(
        name="🔄 Giro da sorte",
        value=(
            "**1 Giro:** R$ 5,00\n"
            "**5 Giros:** R$ 12,50\n"
            "**20 Giros:** R$ 40,00"
        )
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)

bot.run("TOKEN")