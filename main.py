
from flask import Flask, render_template
import feedparser

app = Flask(__name__)

@app.route('/')
def index():
    krebs_news = feedparser.parse("https://krebsonsecurity.com/feed/")
    krebs_entry = krebs_news.entries[0:4]

    thn_news = feedparser.parse("https://feeds.feedburner.com/TheHackersNews")  
    thn_entry = thn_news.entries[0:4]

    darkr_news = feedparser.parse("https://www.darkreading.com/rss_simple.asp")  
    darkr_entry = darkr_news.entries[0:4]

    talos_news = feedparser.parse("http://feeds.feedburner.com/Talos")  
    talos_entry = talos_news.entries[0:4]

    nakedsec_news = feedparser.parse("http://feeds.feedburner.com/NakedSecurity")  
    nakedsec_entry = nakedsec_news.entries[0:4]

    mandiant_news = feedparser.parse("https://www.mandiant.com/resources/rss.xml?type=article_blog")  
    mandiant_entry = mandiant_news.entries[0:4]

    bleeping_news = feedparser.parse("https://www.bleepingcomputer.com/feed/")  
    bleeping_entry = bleeping_news.entries[0:4]

    kaspersky_news = feedparser.parse("https://threatpost.com/feed/")  
    kaspersky_entry = kaspersky_news.entries[0:4]

    cisa_alerts = feedparser.parse("https://www.cisa.gov/uscert/ncas/all.xml")
    cisa_entry = cisa_alerts.entries[0:5]

    return render_template("index.html",krebs_entry = krebs_entry,
                                        thn_entry = thn_entry,
                                        darkr_entry = darkr_entry,
                                        talos_entry = talos_entry,
                                        nakedsec_entry = nakedsec_entry,
                                        mandiant_entry = mandiant_entry,
                                        bleeping_entry = bleeping_entry,
                                        kaspersky_entry = kaspersky_entry,
                                        cisa_entry = cisa_entry)

if __name__ == '__main__':
   app.run(host="0.0.0.0")