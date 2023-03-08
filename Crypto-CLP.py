from requests import get,post
from rich.console import Console;from rich.table import Table
from time import sleep
import os,re

console=Console()
_Set_Currency='USD'


    
def Head():
    os.system('cls' if os.name=='nt' else 'clear')
    console.print(f"""
 ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗        ██████╗██╗     ██████╗ 
██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗      ██╔════╝██║     ██╔══██╗
██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║█████╗██║     ██║     ██████╔╝
██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║╚════╝██║     ██║     ██╔═══╝ 
╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝      ╚██████╗███████╗██║     
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝        ╚═════╝╚══════╝╚═╝ 
                   [bold white] By @TweakPY - @vv1ck [/bold white]                                         
""",style='bold red',justify='left')

def Starter():
    console.log('Started CryptoCurrency Live Price [bold orange]...[/bold orange]')
    try:CryptoCLP_Core()
    except KeyboardInterrupt:Head();console.log('-- USER Interrupt\n\n');exit()
    
def SAR_Converter(buff):
    try:
        e=post('https://fcsapi.com/converter/converter_total_val',headers={'Host': 'fcsapi.com','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Te': 'trailers','Connection': 'close'},data=f'from=usd&to=sar&amount={buff}').json()["total"]
        return e
    except:
        return 0
    
def Currency(Currency_price,set_sleep):
    if set_sleep==3:set_sleep="3 Sec"
    elif set_sleep==60*2:set_sleep="120 Sec"
    console.print("[bold magenta]Crypto Currency [/bold magenta]!",":coffee:",'\n')
    table=Table(show_header=True,header_style="bold blue")
    table.add_column("ID",style="bold dim",width=6)
    table.add_column("CryptoCurrency Name",style="bold red",min_width=20)
    table.add_column("Price USD",style="bold Yellow",min_width=12,justify="right")
    table.add_column("Price SAR",style="Yellow",min_width=12,justify="right")
    table.add_column("Refresh Rate",style="bold green",min_width=12,justify="left")
    for id,operation in enumerate(Currency_price,start=1):
        Currency_Name=str(operation).split(":")[0]
        PriceUSD=str(operation).split(":")[1]
        PriceSAR=str(operation).split(":")[2]
        table.add_row(f'{id}',f'{str(Currency_Name)}',f"{str(PriceUSD)}",f"{str(PriceSAR)}",f'{str(set_sleep)}')
    console.print(table)
    
def CryptoCLP_Core():
    _Max_Calls=7574
    set_sleep=3
    i=0
    Currency_price=list()
    while i != _Max_Calls: 
        sleep(set_sleep)
        BTC=get(f'https://min-api.cryptocompare.com/data/price?fsym=btc&tsyms={_Set_Currency}').json()
        ETH=get(f'https://min-api.cryptocompare.com/data/price?fsym=eth&tsyms={_Set_Currency}').json()
        LTC=get(f'https://min-api.cryptocompare.com/data/price?fsym=ltc&tsyms={_Set_Currency}').json()
        BNB=get(f'https://min-api.cryptocompare.com/data/price?fsym=bnb&tsyms={_Set_Currency}').json()
        if "You are over your rate limit please upgrade your account!" in BTC:
            set_sleep=60*2
            try:err_msg=BTC['Message']
            except:err_msg=0
        else:
            Currency_price.append('Bitcoin:'+str(BTC[_Set_Currency])+f":{SAR_Converter(BTC[_Set_Currency])}")
            Currency_price.append('Ethereum:'+str(ETH[_Set_Currency])+f":{SAR_Converter(ETH[_Set_Currency])}")
            Currency_price.append('Litecoin:'+str(LTC[_Set_Currency])+f":{SAR_Converter(LTC[_Set_Currency])}")
            Currency_price.append('Binance:'+str(BNB[_Set_Currency])+f":{SAR_Converter(BNB[_Set_Currency])}")
            Head()
            Currency(Currency_price,set_sleep)
            Currency_price.clear()
        i+=1
    Head()
    console.print(f'''
[!] Error, I think we mistakenly do a ddos instead of fetching cryptocurrency prices\n
Error Message: {err_msg}
\n\n[!] Try again after 5 minutes to run the tool''')
        
        
        
        
Head();Starter()
