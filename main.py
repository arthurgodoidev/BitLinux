
from libs import *

app = Tk()
app.config(bg='#074BE8')
app.geometry('1280x720')
app.title('            BitLinux v1.0 by Arthur Godoi')
app.attributes('-zoomed', True)
def Bitcoin():
    
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
    cotacoes = cotacoes.json()
    cotacoes_btc = cotacoes['BTCBRL']['bid']
    Cotacao['text'] = cotacoes_btc    
    
def Dolar():
     
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    cotacoes = cotacoes.json()
    cotacoes_dol = cotacoes['USDBRL']['bid']
    Cotacao['text'] = cotacoes_dol   

def Euro():
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL")
    cotacoes = cotacoes.json()
    cotacoes_eur = cotacoes['EURBRL']['bid']
    Cotacao['text'] = cotacoes_eur    
def Esterlina():
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/GBP-BRL")
    cotacoes = cotacoes.json()
    cotacoes_est = cotacoes['GBPBRL']['bid']
    Cotacao['text'] = cotacoes_est 
def Canadense():
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/CAD-BRL")
    cotacoes = cotacoes.json()
    cotacoes_cad = cotacoes['CADBRL']['bid']
    Cotacao['text'] = cotacoes_cad    

Cotacao = Label(app,text='Cotação',font='Arial 40',fg='white',bg='#074BE8')
Cotacao.pack(anchor=CENTER)

Data = Label(app,text=datetime.today().strftime('%d-%m'),font='Arial 40',fg='white',bg='#074BE8')
Data.pack(anchor='e')
bitbutton = Button(app,text='Bitcoin',font='Arial 40',fg='white',bg='#074BE8',command=Bitcoin)
bitbutton.pack(pady=25)

dolbutton = Button(app,text='Dólar',font='Arial 40',fg='white',bg='#074BE8',command=Dolar)
dolbutton.pack(pady=25)

eurbutton = Button(app,text='Euro',font='Arial 40',fg='white',bg='#074BE8',command=Euro)
eurbutton.pack()

estbutton = Button(app,text='Libra Esterlina',font='Arial 40',fg='white',bg='#074BE8',command=Esterlina)
estbutton.pack(pady=25)

cadbutton = Button(app,text='Dólar Canadense',font='Arial 40',fg='white',bg='#074BE8',command=Canadense)
cadbutton.pack(pady=25)
app.mainloop()