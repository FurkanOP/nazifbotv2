import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext, JobQueue
import time
import sys
import os

datakeyy = [
"740509944",
"149769244",
"499892225",
"692741324",
"271367195",
"358146607",
"940481039",
"018693662",
"010031780",
"006129466",
"841244057",
"601363409",
"121297099",
"451716499",
"133450574",
"914776507",
"722927267",
"979165161",
"429638262",
"043626421",
"063959255",
"982427790",
"542124402",
"434698424",
"955794211",
"212686128",
"670646913",
"636509771",
"663054151",
"356099465",
"688332788",
"832978536",
"242773299",
"318114161",
"451767024",
"368361661",
"591616516",
"723837642",
"929150872",
"713216550",
"346696160",
"453829142",
"645944798",
"695734572",
"712900098",
"022467090",
"528324370",
"569622814",
"201285468",
"917694279",
"973701843",
"758857927",
"061166425",
"227310842",
"465414583",
"259857578",
"156205117",
"490661532",
"994349790",
"591660208",
"779427978",
"526054671",
"334205141",
"525193308",
"701942172",
"604624756",
"011597167",
"874928561",
"930634318",
"912834648",
"557358143",
"047953613",
"315712228",
"499690080",
"023052910",
"353230950",
"136163078",
"420468812",
"898684364",
"696355227",
"821437872",
"972735352",
"954257782",
"088186829",
"131835287",
"095008801",
"695371443",
"199993650",
"413430079",
"780766857",
"007387312",
"697664056",
"910811903",
"590329759",
"705130816",
"505459925",
"998803206",
"471836353",
"043327842",
"542994346",
"047794040",
"530748068",
"660493905",
"906848667",
"855815867",
"564781817",
"336474575",
"740479877",
"416603760",
"971968176",
"769510479",
"745376994",
"834364405",
"332380421",
"873588146",
"903525834",
"605678340",
"064483640",
"006375134",
"788848160",
"568843904",
"548825134",
"240494134",
"106813947",
"912321424",
"892062175",
"052022898",
"258147867",
"288101979",
"062839855",
"604661037",
"228336175",
"322410622",
"651261356",
"309427229",
"055224362",
"179924073",
"711208916",
"774108945",
"529340327",
"451224825",
"819231785",
"268769103",
"001147712",
"391533273",
"244488569",
"582516857",
"836188316",
"856172710",
"327243849",
"977978185",
"935383563",
"559431148",
"852292596",
"826697018",
"076993319",
"997939239",
"615007372",
"267183489",
"105629322",
"178042078",
"205826917",
"765296991",
"430288718",
"336760985",
"738768259",
"250039677",
"514281230",
"189876081",
"344171243",
"326109269",
"638036300",
"616600242",
"544606378",
"277523126",
"506325069",
"657335674",
"427974868",
"389058276",
"204300816",
"215975549",
"784907516",
"466837664",
"774197714",
"913394044",
"184562186",
"593585743",
"190715468",
"815099434",
"710496041",
"573006338",
"381193032",
"704648605",
"376758111",
"269319356",
"314574465",
"016558118",
"589585016",
"472516992",
"055578707",
"663926751",
"477742369",
"974558308",
"878038912",
"992072673",
"825256650",
"613823559",
"076898490",
"910699698",
"837697567",
"520661399",
"096044088",
"693899002",
"337758958",
"402739065",
"426277119",
"254382594",
"981982318",
"970465877",
"479471034",
"085540397",
"796134697",
"843153410",
"640062094",
"829838763",
"907842996",
"757601176",
"218475478",
"790035173",
"307620892",
"762099226",
"683962413",
"992988228",
"459489397",
"039308604",
"129470430",
"144355615",
"214032788",
"712310001",
"357507599",
"878164605",
"204674890",
"802887264",
"052998760",
"737529213",
"961741135",
"547930234",
"799341970",
"382574337",
"452931133",
"725913783",
"625099655",
"846986599",
"790522110",
"092074693",
"262766780",
"836166533",
"994993186",
"037508617",
"762754816",
"317085530",
"945800825",
"088017279",
"994541748",
"696021968",
"986758190",
"737325004",
"518261689",
"529527874",
"030811061",
"976393651",
"305370966",
"224760251",
"763077968",
"377010893",
"019727253",
"349786004",
"470709986",
"623035454",
"489291893",
"122129940",
"532591554",
"108095736",
"781155379",
"428361614",
"991288273",
"473144907",
"642072390",
"873582451",
"828832265",
"449276786",
"632391836",
"178022888",
"317064816",
"878024943",
"795316667",
"032747166",
"935318265",
"448860215",
"269866332",
"362316180",
"617437517",
"071739302",
"863007314",
"896431394",
"640295000",
"120808922",
"829267537",
"785757091",
"902798307",
"181705060",
"549395393",
"530638381",
"040575026",
"945948419",
"825835464",
"926622570",
"947379714",
"621357917",
"027136534",
"337962624",
"300416916",
"587768661",
"601108196",
"246678788",
"846162401",
"439300765",
"952196086",
"253495399",
"810584447",
"465413202",
"625081552",
"030744934",
"929481593",
"296173913",
"365897248",
"779691685",
"563980309",
"039304431",
"769508724",
"928970148",
"945076159",
"808190913",
"308268728",
"651942703",
"442331017",
"678714491",
"548180563",
"860543778",
"604316655",
"388270955",
"037529624",
"302157282",
"055205385",
"358625570",
"478402254",
"516978315",
"114839772",
"452685144",
"825700739",
"166718577",
"231866456",
"740690195",
"998838815",
"979184638",
"213903470",
"249905916",
"639323341",
"971918031",
"476078186",
"598532721",
"793183983",
"597326001",
"772269522",
"331064403",
"698458460",
"512704740",
"481684580",
"778362326",
"663387653",
"026666438",
"376042381",
"140585407",
"971593237",
"592804687",
"944195817",
"292364247",
"839767764",
"455312403",
"561920325",
"228174753",
"636703556",
"485829555",
"795731704",
"924827575",
"876146082",
"162742932",
"358115507",
"116461011",
"528439819",
"945309817",
"269849382",
"637192753",
"481693270",
"799341970",
"382574337",
"452931133",
"725913783",
"625099655",
"846986599",
"790522110",
"092074693",
"262766780",
"836166533",
"994993186",
"037508617",
"762754816",
"317085530",
"945800825",
"088017279",
"994541748",
"696021968",
"986758190",
"737325004",
"518261689",
"529527874",
"030811061",
"976393651",
"305370966",
"224760251",
"763077968",
"377010893",
"019727253",
"349786004",
"470709986",
"623035454",
"489291893",
"122129940",
"532591554",
"108095736",
"781155379",
"428361614",
"991288273",
"473144907",
"642072390",
"873582451",
"828832265",
"449276786",
"632391836",
"178022888",
"317064816",
"878024943",
"795316667",
"032747166",
"935318265",
"448860215",
"269866332",
"362316180",
"617437517",
"071739302",
"863007314",
"896431394",
"640295000",
"120808922",
"829267537",
"785757091",
"902798307",
"181705060",
"549395393",
"530638381",
"040575026",
"945948419",
"825835464",
"926622570",
"947379714",
"621357917",
"027136534",
"337962624",
"300416916",
"587768661",
"601108196",
"246678788",
"846162401",
"439300765",
"952196086",
"253495399",
"810584447",
"465413202",
"625081552",
"030744934",
"929481593",
"296173913",
"365897248",
"779691685",
"563980309",
"039304431",
"769508724",
"928970148",
"945076159",
"808190913",
"308268728",
"651942703",
"442331017",
"678714491",
"548180563",
"860543778",
"604316655",
"388270955",
"037529624",
"302157282",
"055205385",
"358625570",
"478402254",
"516978315",
"114839772",
"452685144",
"825700739",
"166718577",
"231866456",
"740690195",
"998838815",
"979184638",
"213903470",
"249905916",
"639323341",
"971918031",
"476078186",
"598532721",
"793183983",
"597326001",
"772269522",
"331064403",
"698458460",
"512704740",
"481684580",
"778362326",
"663387653",
"026666438",
"376042381",
"140585407",
"971593237",
"592804687",
"944195817",
"292364247",
"839767764",
"455312403",
"561920325",
"228174753",
"636703556",
"485829555",
"795731704",
"924827575",
"876146082",
"162742932",
"358115507",
"116461011",
"528439819",
"945309817",
"269849382",
"637192753",
"481693270",
"799341970",
"382574337",
"452931133",
"725913783",
"625099655",
"846986599",
"790522110",
"092074693",
"262766780",
"836166533",
"994993186",
"037508617",
"762754816",
"317085530",
"945800825",
"088017279",
"994541748",
"696021968",
"986758190",
"737325004",
"518261689",
"529527874",
"030811061",
"976393651",
"305370966",
"224760251",
"763077968",
"377010893",
"019727253",
"349786004",
"470709986",
"623035454",
"489291893",
"122129940",
"532591554",
"108095736",
"781155379",
"428361614",
"991288273",
"473144907",
"642072390"]
kullanilmis = [

]
satinalanlar = []
# Telegram bot token ve chat ID
gurupchatid = -4233612402
def print_mesaj():
    mesaj = "Nazif Kara . . . . .\nanskm. . . . .\npatliom. . . . ."
    renkli_mesaj = "\033[1;32;40m" + mesaj + "\033[0m"  # Yeşil renkli metin
    for karakter in renkli_mesaj:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(0.05)  # Her karakter arasında kısa bir gecikme
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Merhaba {update.effective_user.first_name}. Nazif Kara sinyal robotunu kullanmak için bir KEY'e sahip olmanız gerekir. Eğer sahipseniz /key yazın. Satın almak için https://www.shopier.com/28289167")
async def key(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    async def finishh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        message = update.message
        mesajj = message.text
        print(mesajj)
        try:
            datakeyy.index(mesajj)
            kullanilmistext = open("kullanilmis.txt","r")
            content = kullanilmistext.read()
            if mesajj in content:
                await context.bot.forward_message(chat_id=gurupchatid, from_chat_id= message.chat_id,message_id=message.message_id)
                await update.message.reply_text(f"Bu key daha önce kullanılmış.")
                
            else:
                await context.bot.forward_message(chat_id=gurupchatid, from_chat_id= message.chat_id,message_id=message.message_id)
                await update.message.reply_text(f"Başarılı. Artık sinyaller sana yönlendirilecek. Eğer Hisse sormak istiyorsan /sor ile sorabilirsin.")
                satinalanlartext = open("musteriler.txt","a")
                satinalanlartext2 = open("musteriler2.txt","a")
                current_datetime = datetime.now()
                satinalanlartext.write(str(message.from_user['id']))
                satinalanlartext2.write(str(message.from_user['id']) + " , " + current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
                satinalanlartext.write("\n")
                satinalanlartext2.write("\n")
                satinalanlartext.close()
                satinalanlartext2.close()
            kullanilmistext.close()

            kullanilmistext = open("kullanilmis.txt","a")
            kullanilmistext.write(str(mesajj))
            kullanilmistext.write("\n")
            kullanilmistext.close()
        except ValueError:
            await update.message.reply_text(f"Böyle bir key yoktur.")   
    await update.message.reply_text(f"Sahip olduğunuz keyi mesaj olarak gönderin.")
    app.add_handler(MessageHandler(filters.TEXT ,finishh))
    
app = ApplicationBuilder().token("7334498197:AAFpv5W6XC6R44Dw_1a0sxThCux-Pt_AIw4").build()

# BIST hisse senedi listesi (örnek bir dosya)
def load_bist_stocks():
    with open("bist_stocks.txt", "r",encoding="utf-8") as file:
        stocks = file.read().splitlines()    
    return stocks

def fetch_data(ticker, start, end):
    """
    Belirli bir tarih aralığında veri çeker.
    """
    data = yf.download(ticker, start=start, end=end, interval='1h')  # Saatlik veriyi çek
    return data

def calculate_indicators(data):
    """
    Teknik analiz göstergelerini hesaplar.
    """
    data = data.copy()
    
    # EMA hesapla
    data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()
    data['EMA_50'] = data['Close'].ewm(span=50, adjust=False).mean()
    
    # MACD ve Sinyal Çizgisi hesapla
    data['MACD'] = data['Close'].ewm(span=12, adjust=False).mean() - data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD_Signal'] = data['MACD'].ewm(span=9, adjust=False).mean()
    
    # RSI hesapla
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()

    # Sıfır bölme hatası için önlem
    gain = gain.fillna(0)
    loss = loss.fillna(0)
    
    # rs hesapla
    rs = gain / loss
    rs = rs.replace([np.inf, -np.inf], 0)  # Sonsuzluk değerlerini sıfırla
    data['RSI'] = 100 - (100 / (1 + rs))
    
    return data

def check_signals(data):
    """
    Sinyalleri kontrol eder ve anlamlı olanları döndürür.
    """
    results = []
    last_signal_time = None
    min_signal_interval = timedelta(minutes=1)  # Minimum sinyal aralığı

    for i in range(1, len(data)):
        latest = data.iloc[i]
        previous = data.iloc[i - 1]

        # EMA sinyali kontrolü
        ema_signal = None
        if latest['EMA_20'] > latest['EMA_50'] and previous['EMA_20'] <= previous['EMA_50']:
            ema_signal = 'Buy'
        elif latest['EMA_20'] < latest['EMA_50'] and previous['EMA_20'] >= previous['EMA_50']:
            ema_signal = 'Sell'

        # MACD sinyali kontrolü
        macd_signal = None
        if latest['MACD'] > latest['MACD_Signal'] and previous['MACD'] <= previous['MACD_Signal']:
            macd_signal = 'Buy'
        elif latest['MACD'] < latest['MACD_Signal'] and previous['MACD'] >= previous['MACD_Signal']:
            macd_signal = 'Sell'

        # RSI sinyali kontrolü
        rsi_signal = None
        if latest['RSI'] < 30:  # RSI için genişletilmiş eşik
            rsi_signal = 'Oversold'
        elif latest['RSI'] > 70:  # RSI için genişletilmiş eşik
            rsi_signal = 'Overbought'

        # Kombine Sinyaller
        if ema_signal == 'Buy' and macd_signal == 'Buy':
            if last_signal_time is None or (latest.name - last_signal_time) > min_signal_interval:  # En az 30 dakika aralık
                results.append(f'Al Sinyali\nTarih: {latest.name.strftime("%Y-%m-%d %H:%M")}\nHisse Fiyatı: {round(latest["Close"], 2)}')
                last_signal_time = latest.name
        elif ema_signal == 'Sell' and macd_signal == 'Sell':
            if last_signal_time is None or (latest.name - last_signal_time) > min_signal_interval:  # En az 30 dakika aralık
                results.append(f'Sat Sinyali\nTarih: {latest.name.strftime("%Y-%m-%d %H:%M")}\nHisse Fiaytı: {round(latest["Close"], 2)}')
                last_signal_time = latest.name

        # RSI sinyali ile birlikte EMA ve MACD sinyalleri
        if rsi_signal == 'Oversold' and ema_signal == 'Buy' and macd_signal == 'Buy':
            if last_signal_time is None or (latest.name - last_signal_time) > min_signal_interval:  # En az 30 dakika aralık
                results.append(f'Süper Al Sinyali(RSI aşırı satım)\nTarih: {latest.name.strftime("%Y-%m-%d %H:%M")}\nHisse Fiyatı: {round(latest["Close"], 2)}')
                last_signal_time = latest.name
        elif rsi_signal == 'Overbought' and ema_signal == 'Sell' and macd_signal == 'Sell':
            if last_signal_time is None or (latest.name - last_signal_time) > min_signal_interval:  # En az 30 dakika aralık
                results.append(f'Süper Sat Sinyali(RSI aşırı alım)\nTarih: {latest.name.strftime("%Y-%m-%d %H:%M")}\nHisse Fiyatı: {round(latest["Close"], 2)}')
                last_signal_time = latest.name

    return results

last_signal_times = {}

async def check_all_stocks(context: CallbackContext):
    stocks = load_bist_stocks()
    today = datetime.now()
    start =  (today - timedelta(days=7)).strftime('%Y-%m-%d')
    end = (today + timedelta(days=365)).strftime('%Y-%m-%d')
    #today.strftime('%Y-%m-%d')
    for ticker in stocks:
        try:
            data = fetch_data(ticker, start, end)
            data = calculate_indicators(data)
            signals = check_signals(data)
            print(signals)            
            # Get the last signal time for this stock
            last_signal_time = last_signal_times.get(ticker, None)
            
            # Check if there are new signals
            for signal in signals:
                signal_time = signal.split('\n')[1].split(': ')[1]  # Extract signal time
                signal_time = datetime.strptime(signal_time, '%Y-%m-%d %H:%M')
                
                if last_signal_time is None or signal_time > last_signal_time:
                    # Send message to users
                    if signal[0:1] == "A":
                        with open("musteriler.txt", "r",encoding="utf-8") as filee:
                            users = filee.read().splitlines()
                        
                        for user_id in users:
                            try:
                                await context.bot.send_message(chat_id=user_id, text=f"{ticker}: {signal}")
                            except Exception as e:
                                await context.bot.send_message(chat_id=gurupchatid, text=f"Mesaj gönderme hatası ({user_id}): {e}")
                        
                        # Update last signal time
                        last_signal_times[ticker] = signal_time
            
        except Exception as e:
            await context.bot.send_message(chat_id=gurupchatid, text=f"{ticker} için veri alınırken hata oluştu: {e}")
async def sor(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    text = message.text
    user_id = message.from_user.id
    with open("musteriler.txt", "r") as filee:
        users = filee.read().splitlines()

    if str(user_id) in users:
        # Komut ve hisse kodunu ayır
        if text.startswith("/sor"):
            parts = text.split()
            if len(parts) == 2:
                command, ticker = parts
                ticker = ticker + ".ıs"
                start = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")  # Örneğin 7 gün önceyi başlangıç tarihi olarak alın
                end = datetime.now().strftime("%Y-%m-%d")  # Bugünün tarihini bitiş tarihi olarak alın
                try:
                    data = fetch_data(ticker, start, end)
                    data = calculate_indicators(data)
                    signals = check_signals(data)
                    if signals:
                        for signal in signals:
                            await update.message.reply_text(signal)
                    else:
                        await update.message.reply_text(f"Belirtilen tarih aralığında sinyal bulunamadı.")
                except Exception as e:
                    await update.message.reply_text(f"Veri alınırken hata oluştu: {e}")
            else:
                await update.message.reply_text("Geçersiz komut formatı. Lütfen /sor [hisse kodu] şeklinde yazınız.")
        else:
            await update.message.reply_text("Bu komut geçerli değil.")
    else:
        await update.message.reply_text("Bu kullanıcı yetkili değil.")
# Telegram bot komutları ve zamanlayıcı ayarları
async def adminn(update: Update, context: CallbackContext) -> None:
    # Mesajın geldiği yer
    chat = update.message.chat_id
    # Mesajın kanaldan gelip gelmediğini kontrol et
    with open("musteriler.txt", "r") as filee:
        users = filee.read().splitlines()
    if gurupchatid == chat:
        for user_id in users:
                await context.bot.send_message(chat_id=user_id, text=update.message.text)

def main():
    print_mesaj()
    app.add_handler(CommandHandler("sor", sor))
    app.add_handler(CommandHandler("start", hello))
    app.add_handler(CommandHandler("key", key))
    app.add_handler(CommandHandler("admin", adminn))
    
    # İşlerin zamanlamasını yapalım: Belirli aralıklarla hisse senedi sinyallerini kontrol etmek için
    job_queue = app.job_queue
    job_queue.run_repeating(check_all_stocks, interval=60*1, first=0)  # Her saat başı çalışacak şekilde ayarlandı
    
    app.run_polling()

if __name__ == "__main__":
    main()
