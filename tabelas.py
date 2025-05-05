import discord
import os
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


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
@bot.tree.command(name="blox_fruits", description="Tabela com preços de Gamepasses e Frutas Permanentes")
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
            "**Dragon:** R$ 125,00 | **Gas:** R$ 62,50 | **Yeti:** R$ 75,00\n"
            "Eagle:** R$ 24,80 | **Creation:** R$ 43,75 |" 
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
            "**Roupas de despertar:** R$ 3,75\n"
            "**Emoções de anime:** R$ 10,00\n"
            "**Som de gol:** R$ 3,75\n"
            "**Som de quebrador de tornozelo:** R$ 3,75\n" 
            "**Pulo de giro:** R$ 2,50\n"
            "**Servidor Privado+:** R$ 2,50"
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

# Tabela de bobux
@bot.tree.command(name="bobux", description="Tabela de preço de bobux")
async def bobux(interaction: discord.Interaction):

    embed = discord.Embed(
        title="💳 Tabela de bobux",
        description="Lista dos preços de bobux",
        color=discord.Color.purple()
    )

    embed.add_field(
        name="💵 Valores de bobux",
        value=(
            "**50 bobux:** R$ 1,25\n"
            "**100 bobux:** R$ 2,50\n"
            "**400 bobux:** R$ 10,00\n"
            "**500 bobux:** R$ 12,50\n"
            "**1000 bobux:** R$ 25,00"
        )
    )
    

    await interaction.response.send_message(embed=embed, ephemeral=True)


# Verificador de admin
def eh_adm(Interaction: discord.Interaction) -> bool:
    return Interaction.user.guild_permissions.administrator

# Comando de Bobux
@app_commands.check(eh_adm)
@bot.tree.command(name="admbobux", description="ADM") #calcula a quantidade de bobux a ser enviado
@app_commands.describe(bobux="Digite quantos bobux:")
async def bobuxADM(interaction: discord.Interaction, bobux: int):
    valorPagar = (bobux/100) * 2.5
    await interaction.response.send_message(f"💰 **{bobux}** bobux por apenas **R$ {valorPagar:.2f}**", ephemeral=True)

# Mensagem de erro para quem não tem permissão
@bobuxADM.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CheckFailure):
        await interaction.response.send_message("🚫 Você não tem permissão para usar esse comando!", ephemeral=True)
    else:
        await interaction.response.send_message("⚠️ Ocorreu um erro ao executar o comando.", ephemeral=True)

bot.tree.on_error = on_app_command_error

bot.run(TOKEN)