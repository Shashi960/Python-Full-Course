#Currency Converrter
#Basic Example
from currency_converter import CurrencyConverter
c = CurrencyConverter()
print(c.convert(1 , 'USD', 'INR'))

#Dynamic Example
from currency_converter import CurrencyConverter

amt = float(input("Enter amt in USD: "))
c = CurrencyConverter()
inr=c.convert(amt,'USD','INR')
print(f"Amount in INR: {inr}")

#Qr Code Generator
import qrcode
img = qrcode.make("https://github.com/Shashi960/Python-Full-Course")
img.save("MY GIT REPO QR.png")

#Qr Code Generator with color
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.instagram.com/anjani_putra81/')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("insta Handle.png")



#Text To Speech
import pyttsx3

engine = pyttsx3.init()
text = input("Enter text to convert into speech: ")
engine.say(text)
engine.runAndWait()
engine.save_to_file(text, "output.mp3")
print("Speech generated and saved as output.mp3")



#YT video Downloader
import yt_dlp

url = input("Enter YouTube video URL: ")


ydl_opts = {'format': 'best','outtmpl': '%(title)s.%(ext)s'}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)
    print("Download Completed!")
    print("Title:", info.get('title'))
    print("Views:", info.get('view_count'))
    print("Duration (sec):", info.get('duration'))



