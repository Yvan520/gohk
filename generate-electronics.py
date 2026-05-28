import os

OUTPUT_DIR = "/Users/admin/Documents/test/sunnyhk"

SITE_HEAD = '''<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="index, follow">
<link rel="manifest" href="/manifest.json">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-L9RMXXLKYK"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-L9RMXXLKYK');
</script>
<link rel="canonical" href="https://gohk.gamewayz.com/{FILENAME}">
<meta name="baidu-site-verification" content="codeva-6fKr2IJVp7" />
<meta property="og:type" content="article">
<meta property="og:locale" content="zh_HK">
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;700;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="css/style.css">
'''

NAVBAR = '''<nav class="navbar">
  <div class="inner">
    <a href="index.html" class="logo">
      <div class="sun"><i class="fas fa-sun"></i></div> Sunny<span>HK</span>
    </a>
    <div class="nav-links">
      <a href="index.html" data-i18n="nav-home">首頁</a>
      <div class="nav-dropdown">
        <a href="explore.html" data-i18n="nav-explore">探索指南</a>
        <div class="nav-dropdown-menu">
          <a href="explore.html" data-i18n="nav-explore-all">🌟 人群指南</a>
          <a href="hiking.html" data-i18n="nav-hiking">🥾 行山路線</a>
          <a href="snorkeling.html" data-i18n="nav-snorkeling">🤿 浮潛攻略</a>
          <a href="swimming.html" data-i18n="nav-swimming">🏊 游水指南</a>
        </div>
      </div>
      <a href="food.html" data-i18n="nav-food">美食地圖</a>
      <div class="nav-dropdown active">
        <a href="tips.html" data-i18n="nav-tips">實用資訊</a>
        <div class="nav-dropdown-menu">
          <a href="tips.html" data-i18n="nav-tips-all">💡 實用貼士</a>
          <a href="electronics.html" class="active" data-i18n="nav-electronics">💻 電子產品</a>
        </div>
      </div>
      <a href="map.html" data-i18n="nav-map">🗺️ 地圖</a>
      <a href="stories.html" data-i18n="nav-stories">香港故事</a>
      <a href="about.html" data-i18n="nav-about">關於</a>
    </div>
    <div class="nav-actions">
      <div class="lang-group">
        <button class="lang-btn" data-lang="trad">繁</button>
        <button class="lang-btn" data-lang="simp">简</button>
        <button class="lang-btn" data-lang="en">EN</button>
      </div>
      <button class="theme-toggle" id="themeToggle" aria-label="切換主題"><i class="fas fa-moon"></i></button>
      <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="選單">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</nav>'''

MOBILE_DRAWER = '''<div class="mobile-overlay" id="mobileOverlay"></div>
<div class="mobile-drawer" id="mobileDrawer">
  <a href="index.html" data-i18n="nav-mobile-home">首頁</a>
  <a href="explore.html" data-i18n="nav-mobile-explore">🌟 人群指南</a>
  <a href="hiking.html" data-i18n="nav-mobile-hiking">🥾 行山路線</a>
  <a href="snorkeling.html" data-i18n="nav-mobile-snorkeling">🤿 浮潛攻略</a>
  <a href="swimming.html" data-i18n="nav-mobile-swimming">🏊 游水指南</a>
  <a href="food.html" data-i18n="nav-mobile-food">美食地圖</a>
  <a href="tips.html" data-i18n="nav-mobile-tips">💡 實用貼士</a>
  <a href="electronics.html" data-i18n="nav-mobile-electronics">💻 電子產品</a>
  <a href="map.html" data-i18n="nav-mobile-map">🗺️ 地圖</a>
  <a href="stories.html" data-i18n="nav-mobile-stories">香港故事</a>
  <a href="about.html" data-i18n="nav-mobile-about">關於</a>
  <div class="lang-group">
    <button class="lang-btn" data-lang="trad">繁</button>
    <button class="lang-btn" data-lang="simp">简</button>
    <button class="lang-btn" data-lang="en">EN</button>
  </div>
  <button class="theme-toggle" id="themeToggleMobile" aria-label="切換主題" style="margin-top:8px;align-self:flex-start;"><i class="fas fa-moon"></i></button>
</div>'''

FOOTER = '''<footer class="footer">
  <div class="inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="logo-text"><div class="sun"><i class="fas fa-sun"></i></div> SunnyHK</div>
        <p data-i18n="footer-tagline">一個年輕、陽光、真實嘅香港旅行靈感平台。</p>
      </div>
      <div class="footer-col">
        <h4 data-i18n="footer-explore">探索</h4>
        <a href="explore.html" data-i18n="footer-guide">人群指南</a>
        <a href="hiking.html" data-i18n="footer-hiking">🥾 行山路線</a>
        <a href="snorkeling.html" data-i18n="footer-snorkeling">🤿 浮潛攻略</a>
        <a href="tips.html" data-i18n="footer-tips">實用資訊</a>
        <a href="stories.html" data-i18n="footer-stories">香港故事</a>
      </div>
      <div class="footer-col">
        <h4 data-i18n="footer-about">關於</h4>
        <a href="about.html" data-i18n="footer-about-us">關於 SunnyHK</a>
        <a href="about.html#faq" data-i18n="footer-faq">常見問題</a>
      </div>
      <div class="footer-col">
        <h4 data-i18n="footer-follow">關注我哋</h4>
        <div class="footer-social">
          <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
          <a href="#" aria-label="小紅書"><i class="fab fa-xiaohongshu"></i></a>
          <a href="#" aria-label="微博"><i class="fab fa-weibo"></i></a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 SunnyHK · Discover Your Own Hong Kong</span>
    </div>
  </div>
</footer>'''

SCRIPTS = '''<script src="js/lang.js"></script>
<script src="js/main.js"></script>
<script>navigator.serviceWorker?.register("/sw.js");</script>'''

def generate_page(item):
    slug = item["slug"]
    filename = f"{slug}.html"
    emoji = item["emoji"]
    name = item["name"]
    name_full = item["name_full"]
    page_title = item["page_title"]
    og_title = item["og_title"]
    meta_desc = item["meta_desc"]
    desc = item["desc"]
    tags = item["tags"]
    traffic = item["traffic"]
    hours = item["hours"]
    highlights = item["highlights"]
    shops = item["shops"]
    tips = item["tips"]
    foods = item["foods"]
    image = item["image"]

    head = SITE_HEAD.replace("{FILENAME}", filename)
    head = head + f'\n<meta name="description" content="{meta_desc}">\n' + \
        f'<meta property="og:title" content="{og_title}">\n' + \
        f'<meta property="og:description" content="{meta_desc}">\n' + \
        f'<meta property="og:url" content="https://gohk.gamewayz.com/{filename}">\n' + \
        f'<meta property="og:image" content="{image}">\n' + \
        f'<title>{page_title}</title>\n'

    tags_html = "".join(f'<span>{t}</span>' for t in tags)

    highlights_html = ""
    for h in highlights:
        highlights_html += f'''<div class="step-card">
  <h3>{h["title"]}</h3>
  <p>{h["desc"]}</p>
</div>
'''

    shops_html = ""
    for s in shops:
        shops_html += f'''<div class="step-card" style="border-left-color:#8b5cf6;">
  <h3>{s[0]}</h3>
  <p>{s[1]}</p>
</div>
'''

    tips_html = "".join(f'<li>{t}</li>\n' for t in tips)

    foods_html = ""
    for f_item in foods:
        foods_html += f'''<div class="step-card" style="border-left-color:#06b6d4;">
  <h3>{f_item[0]}</h3>
  <p>{f_item[1]}</p>
</div>
'''

    html = f'''{head}
</head>
<body>

{NAVBAR}

{MOBILE_DRAWER}

<div class="trail-hero" style="background:linear-gradient(135deg,#1e293b 0%,#0f172a 100%);min-height:40vh;">
  <img src="{image}" alt="{name}" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0.5;">
  <div class="overlay" style="background:linear-gradient(transparent 30%,rgba(0,0,0,0.85));"></div>
  <div class="inner">
    <a href="electronics.html" class="back-link" style="color:rgba(255,255,255,0.7);margin-bottom:16px;">← 返回電子產品攻略</a>
    <h1 style="font-size:2.4rem;font-weight:900;color:white;font-family:var(--font-serif);margin-bottom:8px;">{emoji} {name}</h1>
    <div class="meta">
      {tags_html}
    </div>
  </div>
</div>

<div class="trail-content">
  <p class="trail-intro">{desc}</p>

  <h2 style="margin-bottom:20px;">🛍️ 購物特色</h2>
{highlights_html}

  <h2 style="margin:40px 0 20px;">🚌 交通詳情</h2>
  <div class="step-card" style="border-left-color:#3b82f6;">
    <p style="color:var(--text-light);font-size:0.95rem;">{traffic}。營業時間：{hours}。</p>
  </div>

  <h2 style="margin:40px 0 20px;">🏪 推薦店舖</h2>
{shops_html}

  <h2 style="margin:40px 0 20px;">💡 貼士</h2>
  <ul class="trail-tips">
    {tips_html}
  </ul>

  <h2 style="margin:40px 0 20px;">🍜 附近美食</h2>
{foods_html}

  <div style="text-align:center;margin:48px 0;">
    <a href="electronics.html" class="submit-btn" style="display:inline-block;width:auto;padding:14px 36px;border-radius:100px;text-decoration:none;">
      ← 返回電子產品攻略
    </a>
  </div>
</div>

{FOOTER}

{SCRIPTS}
</body>
</html>'''

    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: {filename}")


ITEMS = [
    {
        "slug": "electronics-golden-arcade",
        "emoji": "🖥️",
        "name": "黃金電腦商場",
        "name_full": "黃金電腦商場（Golden Computer Arcade）",
        "page_title": "黃金電腦商場 Golden Computer Arcade | SunnyHK 電子產品攻略",
        "og_title": "黃金電腦商場｜SunnyHK 電子產品攻略",
        "meta_desc": "深水埗黃金電腦商場攻略 — 電腦硬件、砌機零件、手提電腦、格價攻略，香港電子產品購物指南。",
        "desc": "深水埗地標！黃金電腦商場係香港最大型嘅電腦商場之一，地庫同地下主要係電腦硬件、砌機零件、手提電腦。價格比連鎖店平10-20%，行多幾間格價先買。記得帶現金，好多舖買電子產品用現金有額外折扣。",
        "tags": ["砌機", "電腦硬件", "格價"],
        "traffic": "港鐵深水埗站D2出口，行2分鐘",
        "hours": "11:00-20:30（大部分舖）",
        "image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1200&q=80",
        "highlights": [
            {"title": "💻 地庫：砌機天堂", "desc": "地庫層係全場最熱鬧嘅地方，正都、Centralfield、Jumbo等大型電腦舖都喺呢度。砌機 list 拎去報價，行幾間格價最少慳$200-500。RAM、SSD、CPU、顯卡應有盡有。"},
            {"title": "🖱️ 地面：電腦周邊", "desc": "地面層主要賣電腦周邊：monitor、keyboard、mouse、router、外置硬碟等。價錢同樣有競爭力，行貨水貨都有得揀。"},
            {"title": "💰 格價攻略", "desc": "同一件產品喺黃金可以相差$100以上。建議用手機記低價錢，至少行3間先決定。地庫鋪租平啲，價格通常更抵。"},
        ],
        "shops": [
            ("正都電腦", "黃金地庫，砌機專家，價格透明，好多網上報價都係參考佢。"),
            ("Centralfield", "老字號電腦舖，服務好，適合砌機新手，售後有保障。"),
            ("Jumbo", "硬件齊全，價錢有競爭力，佢哋網站報價睇得清楚。"),
            ("SE Computer", "手提電腦專門店，型號多，行貨水貨都有，店員專業。"),
        ],
        "tips": [
            "格價至少行3間，同一產品差價可達$100+",
            "現金付款通常比信用卡平2-3%，帶多啲錢",
            "地庫鋪租平啲，價格通常更抵",
            "平日下晝2-4點最少人，週末迫到行唔到",
            "買貴嘢建議用信用卡有保障，細件用現金",
        ],
        "foods": [
            ("維記咖啡粉麵", "深水埗名物！豬潤麵（豬肝麵）聞名全港，仲有咖央西多士，平民價錢星級味道。行完黃金行過來5分鐘。"),
            ("合益泰小食", "米芝蓮推薦腸粉王！滑溜腸粉加甜醬麻醬，$10就有一份。深水埗掃街必食。"),
            ("劉森記麵家", "竹昇麵專家，傳統好味道。雲吞麵同撈麵都出色，老字號有信心保證。"),
        ],
    },
    {
        "slug": "electronics-golden-centre",
        "emoji": "💾",
        "name": "高登電腦中心",
        "name_full": "高登電腦中心（Golden Computer Centre）",
        "page_title": "高登電腦中心 Golden Computer Centre | SunnyHK 電子產品攻略",
        "og_title": "高登電腦中心｜SunnyHK 電子產品攻略",
        "meta_desc": "高登電腦中心攻略 — 電腦遊戲、電競產品、二手電腦、維修服務，香港電子產品購物指南。",
        "desc": "黃金隔離嘅高登電腦中心，以電腦遊戲、電競產品同二手電腦為主。上層有大量電腦遊戲碟（PC / Switch / PS5），價錢比官方平好多。下層賣電腦零件同維修服務。高登嘅電腦遊戲係全港最齊全，鍾意打機嘅必到。",
        "tags": ["遊戲", "電競", "二手"],
        "traffic": "港鐵深水埗站D2出口，黃金電腦商場隔離",
        "hours": "11:30-20:00",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=80",
        "highlights": [
            {"title": "🎮 上層：遊戲天堂", "desc": "上層係全港最齊全嘅電腦遊戲集中地！PC game碟、Steam Wallet code、點數卡，應有盡有。新game一出就有水貨，平官方$50-100。經典舊game、絕版game都仲搵到。"},
            {"title": "🖥️ 下層：電腦零件&維修", "desc": "下層有好多電腦舖同維修檔口，專幫人整電腦、換零件、upgrade硬件。價錢公道，好多街坊幫襯開。"},
            {"title": "🎧 電競產品", "desc": "高登嘅電競產品選擇多，gaming keyboard、mouse、headset、chair等，價錢比大型連鎖店平。仲有好多display可以試手感。"},
        ],
        "shops": [
            ("電氣良品", "高登上層，遊戲碟最齊全，水貨行貨都有，老細好熟行情。"),
            ("Gamer's Zone", "電競產品專門店，可以試keyboard手感，mouse握感先買。"),
            ("電腦維修站", "高登下層多間維修舖，整機前先報價，一般檢查唔收錢。"),
        ],
        "tips": [
            "PC遊戲碟高登最齊全，經典舊game都搵到",
            "Steam Wallet code喺度買平過官方",
            "買二手嘢記得試清楚先俾錢",
            "下層維修舖整機前先報價，格多間比較",
            "週末好迫，平日下晝去最好",
        ],
        "foods": [
            ("維記咖啡粉麵", "深水埗名物豬潤麵，黃金、高登行完行過來5分鐘，必食。"),
            ("新香園（堅記）", "蛋牛治烘底聞名，深水埗經典美食，腿蛋治都好正。"),
            ("蘇記茶檔", "傳統鐵皮茶檔，煎蛋豬扒飯係招牌，街坊味道。"),
        ],
    },
    {
        "slug": "electronics-new-golden",
        "emoji": "🔧",
        "name": "新高登電腦廣場",
        "name_full": "新高登電腦廣場（New Golden Computer Arcade）",
        "page_title": "新高登電腦廣場 New Golden Computer Arcade | SunnyHK 電子產品攻略",
        "og_title": "新高登電腦廣場｜SunnyHK 電子產品攻略",
        "meta_desc": "新高登電腦廣場攻略 — 二手電腦零件、水貨電子產品、古董電子產品、尋寶地，香港電子產品購物指南。",
        "desc": "專賣二手電腦零件、水貨同古董電子產品。識貨之人嘅尋寶地！好多絕版硬件、舊款顯示卡、二手伺服器零件、古董音響器材，價錢平到你唔信。唔熟行情嘅話建議帶個識電腦嘅朋友一齊去。",
        "tags": ["二手", "尋寶", "識貨"],
        "traffic": "黃金電腦商場旁邊，同一條街",
        "hours": "12:00-19:00",
        "image": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=1200&q=80",
        "highlights": [
            {"title": "🔄 二手電腦零件", "desc": "新高登最出名就係二手電腦零件！舊款CPU、顯卡、RAM、底板，好多已經停產嘅嘢呢度都搵到。價錢係原價嘅3-5折，砌 budget 機一流。"},
            {"title": "📼 古董電子產品", "desc": "經典遊戲機、舊款相機、古董音響、黑膠唱盤，呢度係 collectors' paradise！好多絕版電子產品，見到鍾意就要快手。"},
            {"title": "🔍 尋寶攻略", "desc": "新高登嘅貨品日日唔同，要慢慢行慢慢睇。入面啲舖頭仔密密麻麻，好多好嘢隱藏喺角落頭。建議預至少1-2小時慢慢尋寶。"},
        ],
        "shops": [
            ("二手硬件店", "多間舖頭集中喺下層，專賣二手電腦零件，格價一定要行勻全場。"),
            ("古董電子", "專賣經典電子產品，舊game機、舊相機、舊音響，識貨之人必到。"),
            ("水貨特賣", "有啲舖專賣水貨電子產品，平過行貨好多，但冇保養要留意。"),
        ],
        "tips": [
            "買二手嘢記得試清楚先俾錢，最好帶朋友一齊去",
            "格價行勻全場先決定，同一件貨可以差好遠",
            "舊款顯卡、CPU呢度好抵玩",
            "帶現金，好多舖冇電子支付",
            "古董音響器材好抵玩，識玩嘅有驚喜",
        ],
        "foods": [
            ("合益泰小食", "深水埗腸粉王，行完新高登行過嚟食份腸粉，$10就滿足。"),
            ("公和荳品廠", "百年老字號豆腐花店，淺嚐一碗熱豆腐花，加薑糖水，正！"),
            ("文記車仔麵", "深水埗車仔麵之王，餸菜選擇超多，湯底濃郁，必試。"),
        ],
    },
    {
        "slug": "electronics-wan-chai",
        "emoji": "🏢",
        "name": "灣仔電腦城",
        "name_full": "灣仔電腦城（Wan Chai Computer Centre）",
        "page_title": "灣仔電腦城 Wan Chai Computer Centre | SunnyHK 電子產品攻略",
        "og_title": "灣仔電腦城｜SunnyHK 電子產品攻略",
        "meta_desc": "灣仔電腦城攻略 — 電腦硬件、手提電腦、手機配件、遊戲產品，港島區電子產品購物指南。",
        "desc": "港島區最大型電腦商場，同樣有大量電腦硬件、手提電腦、手機配件同遊戲產品。比黃金細啲，但勝在近地鐵站，港島友唔使過海。價錢同黃金差唔多，部分舖頭仲會有特別優惠。",
        "tags": ["港島", "電腦", "手機配件"],
        "traffic": "港鐵灣仔站A4出口，行3分鐘",
        "hours": "11:00-20:00",
        "image": "https://images.unsplash.com/photo-1531297484001-80022131f5a1?auto=format&fit=crop&w=1200&q=80",
        "highlights": [
            {"title": "💻 電腦硬件齊全", "desc": "灣仔電腦城雖然比黃金細，但電腦硬件同樣齊全。砌機零件、手提電腦、monitor等乜都有。港島區想買電腦首選呢度，唔使專程過海。"},
            {"title": "📱 手機配件集中", "desc": "手機殼、保護貼、充電器、行動電源，款式多價錢平。好多舖頭專賣手機配件，行一圈就可以買齊。"},
            {"title": "🛍️ 格價攻略", "desc": "同一件產品喺灣仔電腦城可以差價$100+，一定要格價。一樓同二樓嘅舖頭可以互相參考價錢。"},
        ],
        "shops": [
            ("電腦中心一樓店", "多間電腦舖集中喺一樓，砌機、手提電腦、硬件齊全。"),
            ("手機配件店", "二樓有多間手機配件舖，殼、貼、充電器款式多。"),
            ("遊戲舖", "有幾間game舖，PS5、Switch碟都有，價錢合理。"),
        ],
        "tips": [
            "格價都係必要，同一件產品可以差$100+",
            "港島友唔使過海，近地鐵站好方便",
            "附近有檀島咖啡餅店，買完嘢食個蛋撻",
            "平日去人少啲，行得舒服",
            "一樓2樓都要行，唔同舖頭賣嘅嘢唔同",
        ],
        "foods": [
            ("檀島咖啡餅店", "灣仔地標！蛋撻同奶茶聞名，酥皮蛋撻超好食。行完電腦城行過來5分鐘。"),
            ("華嫂冰室", "余文樂最愛嘅冰室，招牌菠蘿油同番茄湯通粉必試。"),
            ("強記美食", "臘味糯米飯同喳咋糖水馳名，港島老字號平民美食。"),
        ],
    },
    {
        "slug": "electronics-oriental-188",
        "emoji": "🎮",
        "name": "東方188商場",
        "name_full": "東方188商場（灣仔）",
        "page_title": "東方188商場（灣仔） | SunnyHK 電子產品攻略",
        "og_title": "東方188商場｜SunnyHK 電子產品攻略",
        "meta_desc": "東方188商場攻略 — 遊戲機集中地、PS5、Switch遊戲碟、水貨遊戲、絕版遊戲，香港遊戲購物指南。",
        "desc": "灣仔嘅遊戲機集中地！細細個商場但係game舖密度超高，專賣PS5、Switch、Xbox遊戲碟同主機。水貨行貨都有，價錢有競爭力。好多絕版game喺度都搵到，遊戲收藏家必到。",
        "tags": ["遊戲機", "水貨", "絕版"],
        "traffic": "港鐵灣仔站A3出口，行5分鐘",
        "hours": "12:00-20:00",
        "image": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=1200&q=80",
        "highlights": [
            {"title": "🎯 遊戲碟集中地", "desc": "商場內有超過10間game舖，PS5、Switch、Xbox遊戲碟齊全。新game一出就有水貨，比官方平$30-80。二手game亦可以買賣，換game玩好抵。"},
            {"title": "💿 絕版game尋寶", "desc": "想搵絕版game嚟東方188就啱！好多已經停產嘅經典遊戲，呢度嘅老舖仲有存貨。遊戲收藏家必到之地。"},
            {"title": "🎮 主機&配件", "desc": "除咗遊戲碟，主機（水貨行貨都有）、手掣、耳機等配件亦齊全。限定版主機有時呢度仲有貨。"},
        ],
        "shops": [
            ("188 Game Shop", "地庫入口位，game碟最齊全，新game返貨快，老細熟悉行情。"),
            ("經典遊戲店", "專賣二手同絕版game，收藏家必到，好多市面搵唔到嘅game。"),
            ("主機專門店", "專賣PS5、Switch、Xbox主機，水貨行貨都有，價格透明。"),
        ],
        "tips": [
            "搵絕版game嚟呢度就啱，好多市面已停售",
            "新game建議等1-2星期，水貨價會回落",
            "格價都係必要，同一隻game可以差幾十蚊",
            "帶現金，有啲舖現金價平啲",
            "可以帶舊game去Trade-in，補錢換新game",
        ],
        "foods": [
            ("檀島咖啡餅店", "灣仔經典蛋撻奶茶店，行完東方188行過嚟食個tea。"),
            ("華嫂冰室", "人氣冰室，番茄湯通粉同菠蘿油最出名，假日排隊好長。"),
            ("利強記北角雞蛋仔", "馳名雞蛋仔，外脆內軟，行完商場行過嚟買份小食。"),
        ],
    },
    {
        "slug": "electronics-sino-centre",
        "emoji": "🎯",
        "name": "信和中心",
        "name_full": "信和中心（旺角）",
        "page_title": "信和中心（旺角） | SunnyHK 電子產品攻略",
        "og_title": "信和中心｜SunnyHK 電子產品攻略",
        "meta_desc": "旺角信和中心攻略 — 遊戲機集中地、PS5、Switch、水貨遊戲、Figure模型，香港遊戲購物指南。",
        "desc": "旺角最強遊戲機集中地！地庫同地下有十幾間game舖，PS5、Switch、XBOX game碟齊全。水貨game平過官方幾十蚊，新game一出就有。二樓仲有Figure、動漫精品同模型，打機迷行到唔願走。",
        "tags": ["旺角", "遊戲", "Figure"],
        "traffic": "港鐵旺角站E2出口，行3分鐘",
        "hours": "12:00-21:00",
        "image": "https://images.unsplash.com/photo-1493711662062-fa541adb3fc8?auto=format&fit=crop&w=1200&q=80",
        "highlights": [
            {"title": "🎮 地庫&地下：game舖集中地", "desc": "十幾間game舖密密麻麻，新game水貨第一時間到貨。PS5、Switch、XBOX碟齊全，水貨平官方$30-80。店舖之間競爭大，格價有著數。"},
            {"title": "🧸 二樓：Figure迷天堂", "desc": "二樓全部係Figure舖、動漫精品、模型。限定版Figure、hot toys、日本動漫周邊，應有盡有。即使唔買，行一圈都大開眼界。"},
            {"title": "📀 動漫CD&精品", "desc": "同層仲有動漫CD、日本雜誌、海報等精品。日本同步嘅動漫周邊，呢度第一時間有。"},
        ],
        "shops": [
            ("地庫Game舖", "落電梯就見到，game碟最齊全，水貨返貨最快，價錢有競爭力。"),
            ("二樓Figure舖", "多間Figure專門店，限定版、二手Figure都有，動漫迷必到。"),
            ("動漫精品店", "日本同步動漫周邊，CD、海報、襟章、Figure，應有盡有。"),
        ],
        "tips": [
            "水貨game平$30-80，留意行保問題",
            "二樓Figure舖值得行，好多限定版",
            "格價行勻地庫同地下先決定",
            "新game一出就去信和，水貨最快",
            "附近仲有好多商場行，順便行埋瓊華中心",
        ],
        "foods": [
            ("沙嗲王", "旺角經典餐廳，沙嗲牛肉粉絲煲同蟹粉豆腐飯必食。喺信和旁邊。"),
            ("十八座狗仔粉", "馳名狗仔粉，米芝蓮街頭小食。行完信和行過嚟食碗粉。"),
            ("佳佳甜品", "米芝蓮九年甜品店，芝麻糊同合桃露超好食。"),
        ],
    },
    {
        "slug": "electronics-golden-gaming",
        "emoji": "🕹️",
        "name": "黃金/高登（遊戲）",
        "name_full": "黃金電腦商場 & 高登電腦中心（遊戲）",
        "page_title": "黃金/高登遊戲攻略 | SunnyHK 電子產品攻略",
        "og_title": "黃金/高登遊戲攻略｜SunnyHK 電子產品攻略",
        "meta_desc": "深水埗黃金高登遊戲攻略 — PC game、Steam Wallet code、點數卡、PS5 Switch遊戲碟，香港遊戲購物指南。",
        "desc": "除咗電腦，黃金同高登都係買game嘅好地方。高登上層有大量PC game，Steam Wallet code、點數卡應有盡有。黃金地庫都有幾間game舖，主打PS5同Switch。一次過行勻黃金高登，電腦game同主機game全部買齊。",
        "tags": ["PC game", "點數卡", "Steam"],
        "traffic": "港鐵深水埗站D2出口",
        "hours": "星期一至日都開，11:00-20:00",
        "image": "https://images.unsplash.com/photo-1534423861386-85a16f5d13fd?auto=format&fit=crop&w=1200&q=80",
        "highlights": [
            {"title": "💿 高登上層：PC game大全", "desc": "高登上層係PC game天堂！實體碟、Steam Wallet code、點數卡、月卡，乜都有。新game出嗰日就有水貨，價錢比Steam store平。經典舊game、廉價版game一大堆。"},
            {"title": "🎮 黃金地庫：主機game", "desc": "黃金地庫有幾間game舖，主打PS5同Switch遊戲碟。價錢同信和差唔多，住新界西嘅人過海慳時間。二手game都有得買賣。"},
            {"title": "💳 Steam Wallet code", "desc": "呢度買Steam Wallet code平過官方！面額$100-$1000都有，用嚟買Steam game好方便。同場仲有PSN、Xbox Live、Nintendo eShop點數卡。"},
        ],
        "shops": [
            ("高登上層game舖", "PC game最齊全，Steam code、點數卡、月卡應該有盡有。"),
            ("黃金地庫game舖", "PS5、Switch遊戲碟，水貨行貨都有，二手game買賣。"),
            ("電競用品店", "高登有幾間電競用品店，gaming gear齊全，可以試手感。"),
        ],
        "tips": [
            "Steam Wallet code呢度買平過官方，差成$10-20",
            "PC game碟買之前check清楚有冇Steam key",
            "新game建議留意水貨價，有時平好多",
            "高登上層同黃金地庫都行勻，game最齊全",
            "買點數卡留意面額同匯率",
        ],
        "foods": [
            ("維記咖啡粉麵", "豬潤麵名物，行完黃金高登行過來食，$40左右就食飽。"),
            ("合益泰小食", "腸粉王，行完商場行過嚟食腸粉，快捷方便又平。"),
            ("公和荳品廠", "百年豆腐花老店，食碗豆腐花+煎釀三寶，正。"),
        ],
    },
    {
        "slug": "electronics-sim-city",
        "emoji": "📸",
        "name": "星際城市",
        "name_full": "星際城市（旺角）",
        "page_title": "星際城市（旺角）| SunnyHK 電子產品攻略",
        "og_title": "星際城市｜SunnyHK 電子產品攻略",
        "meta_desc": "旺角星際城市攻略 — 相機、鏡頭、水貨攝影器材、二手相機，香港攝影器材購物指南。",
        "desc": "旺角山東街嘅星際城市係香港攝影器材集中地！全港最多相機舖嘅商場，Canon、Nikon、Sony、Fujifilm等各大品牌水貨行貨都有。鏡頭、配件、三腳架、相機袋，應有盡有。買水貨鏡頭平行貨30-40%。",
        "tags": ["相機", "鏡頭", "水貨"],
        "traffic": "港鐵旺角站E2出口，行5分鐘",
        "hours": "11:30-20:30",
        "image": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=1200&q=80",
        "highlights": [
            {"title": "📷 相機舖集中地", "desc": "超過20間相機舖集中喺星際城市！Canon、Nikon、Sony、Fujifilm、Leica各大品牌齊全。行貨水貨都有得揀，基本上行一圈就可以格勻全場價錢。"},
            {"title": "🔭 鏡頭選擇超多", "desc": "水貨鏡頭平行貨平30-40%，係攝影愛好者嘅天堂。原廠鏡、副廠鏡（Tamron、Sigma、Tokina）應有盡有。買水貨雖然冇行保，但平一截。"},
            {"title": "📂 二手相機&器材", "desc": "二樓有好多二手相機舖，機身、鏡頭、閃光燈、腳架等。成色好嘅二手器材性價比好高，適合新手入門。"},
        ],
        "shops": [
            ("一樓相機店", "多間相機舖集中地，行貨水貨都有，店員通常好專業。"),
            ("二樓二手相機", "專賣二手相機器材，成色參差，需要識睇先買。"),
            ("配件舖", "相機袋、三腳架、filter、記憶卡等配件，款式齊全。"),
        ],
        "tips": [
            "水貨鏡頭平好多，但冇行保要留意",
            "二樓有好多二手相機舖，識睇嘅好抵",
            "買貴重器材建議用信用卡有保障",
            "新機出嗰陣，水貨價會跌得快",
            "Check清楚有冇光點死點、配件齊唔齊",
        ],
        "foods": [
            ("富記粥品", "旺角馳名粥店，及第粥、燒鵝粥都好好食。行完星際行過來幾分鐘。"),
            ("義順牛奶公司", "馳名雙皮奶同薑汁撞奶，行完相機舖嚟碗甜品。"),
            ("佳佳甜品", "米芝蓮甜品，芝麻糊同合桃露一流，行完星際嚟食。"),
        ],
    },
    {
        "slug": "electronics-wing-shing-mong-shing",
        "emoji": "🏪",
        "name": "永成 / 萬成",
        "name_full": "永成攝影器材 / 萬成攝影器材（旺角）",
        "page_title": "永成萬成攝影器材（旺角）| SunnyHK 電子產品攻略",
        "og_title": "永成萬成｜SunnyHK 電子產品攻略",
        "meta_desc": "旺角永成萬成攻略 — 相機行貨水貨、老字號攝影器材店，香港相機購物指南。",
        "desc": "旺角兩大老牌相機舖，行貨水貨都有。永成主打行貨，萬成水貨多啲。兩間舖頭隔籬，行完一間行第二間。服務專業，售後有保障。推薦俾第一次買相機嘅新手，雖然比星際貴少少但可靠。",
        "tags": ["行貨", "老字號", "可靠"],
        "traffic": "港鐵旺角站D3出口",
        "hours": "10:00-21:00",
        "image": "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?auto=format&fit=crop&w=1200&q=80",
        "highlights": [
            {"title": "🏪 永成：行貨首選", "desc": "永成以行貨為主，各大品牌相機、鏡頭齊全。價錢比細舖貴少少，但勝在可靠，有香港代理保養。適合第一次買貴價相機嘅新手。"},
            {"title": "🏪 萬成：水貨選擇多", "desc": "萬成喺永成隔籬，水貨選擇多，價錢平一截。鏡頭、配件如filter、記憶卡等水貨價好抵。行完永成過萬成格價，基本上一條街搞掂。"},
            {"title": "🤝 專業服務", "desc": "兩間舖店員都好專業，對相機產品熟悉，可以提供客觀建議。售後服務好，有問題可以返嚟問。"},
        ],
        "shops": [
            ("永成攝影器材", "旺角老牌行貨相機舖，服務專業，售後有保障，新手首選。"),
            ("萬成攝影器材", "永成隔籬，水貨為主，價錢平一截，鏡頭同配件好抵。"),
        ],
        "tips": [
            "行貨有保養，貴啲但安心",
            "行完永成就過萬成格價",
            "買鏡頭Check清楚有冇塵點",
            "會員有時有額外折扣",
            "新機上市前排隊預訂，第一批最快",
        ],
        "foods": [
            ("沙嗲王", "旺角經典平民餐廳，沙嗲牛肉粉絲煲必食，行過嚟幾分鐘。"),
            ("佳佳甜品", "米芝蓮甜品，芝麻糊好好食，行完相機舖食碗甜品。"),
            ("十八座狗仔粉", "米芝蓮街頭小食，狗仔粉同火鴨翅都出色。"),
        ],
    },
    {
        "slug": "electronics-sin-tat",
        "emoji": "📱",
        "name": "先達廣場",
        "name_full": "先達廣場（旺角）",
        "page_title": "先達廣場（旺角）| SunnyHK 電子產品攻略",
        "og_title": "先達廣場｜SunnyHK 電子產品攻略",
        "meta_desc": "旺角先達廣場攻略 — 手機集中地、水貨手機、二手手機、手機配件，香港手機購物指南。",
        "desc": "香港手機集中地！全新手機、水貨手機、二手手機、手機配件（殼、貼、充電器）應有盡有。想買最新水貨旗艦機？呢度第一時間有。先達以水貨手機出名，價錢比官方平一截。提提你：幫襯信譽好嘅舖頭。",
        "tags": ["手機", "水貨", "旺角"],
        "traffic": "港鐵旺角站D3出口",
        "hours": "12:00-20:30",
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=1200&q=80",
        "highlights": [
            {"title": "📱 水貨手機大王", "desc": "先達係香港水貨手機第一站！最新日本、韓國水貨機最先到先達。iPhone水貨、Android旗艦水貨，比官方早幾日就有。價錢平過行貨一截。"},
            {"title": "🔄 二手手機市場", "desc": "好多舖專賣二手手機，成色由A至C級，價格相應。iPhone二手價特別透明，適合budget有限或者想平玩旗艦機嘅人。"},
            {"title": "📲 手機配件大全", "desc": "手機殼、保護貼、充電線、行動電源、耳機，款式多到揀唔晒。仲可以搵到好多冷門配件，舊款機型都有。"},
        ],
        "shops": [
            ("水貨手機店", "先達地舖，最新水貨手機最先返貨，日韓水貨最齊全。"),
            ("二手手機店", "一樓多間二手手機舖，買二手記得Check清楚所有功能。"),
            ("配件專門店", "手機配件款式齊全，殼貼充電器耳機，價錢平過連鎖店。"),
        ],
        "tips": [
            "先達質素參差，揀信譽舖幫襯",
            "日韓水貨機呢度最齊",
            "買手機Check清楚配件同IMEI",
            "水貨機冇香港保養，留意維修問題",
            "建議格多幾間先決定，價錢可以差好遠",
        ],
        "foods": [
            ("佳佳甜品", "米芝蓮甜品，行完先達行過來食碗芝麻糊，滿足。"),
            ("沙嗲王", "旺角經典平民美食，沙嗲粉絲煲好正，行過嚟5分鐘。"),
            ("十八座狗仔粉", "狗仔粉同火鴨翅一流，米芝蓮街頭小食，好多人排隊。"),
        ],
    },
    {
        "slug": "electronics-ap-liu-street",
        "emoji": "🔌",
        "name": "鴨寮街",
        "name_full": "鴨寮街（深水埗）",
        "page_title": "鴨寮街（深水埗）| SunnyHK 電子產品攻略",
        "og_title": "鴨寮街｜SunnyHK 電子產品攻略",
        "meta_desc": "深水埗鴨寮街攻略 — 電子零件、二手電子產品、充電線、轉插、電池、二手音響，香港電子產品購物指南。",
        "desc": "深水埗鴨寮街係香港著名嘅電子零件同二手電子產品街。充電線、轉插、電池、電子零件、舊音響、二手喇叭，平到笑！好多外國遊客專程嚟尋寶。週末仲有地攤，更加熱鬧。行完鴨寮街，可以順便行黃金高登。",
        "tags": ["電子零件", "平價", "尋寶"],
        "traffic": "港鐵深水埗站A2出口，出站就係",
        "hours": "朝早10點就開，週末最旺",
        "image": "https://images.unsplash.com/photo-1550009158-9ebf2f0c0f2f?auto=format&fit=crop&w=1200&q=80",
        "highlights": [
            {"title": "🔌 電子零件街", "desc": "鴨寮街兩旁全部係電子零件舖！電阻、電容、LED、電線、connector，整電子嘢需要嘅零件乜都有。價錢平到笑，一條充電線$10-20就有。"},
            {"title": "📻 二手音響寶藏", "desc": "鴨寮街嘅二手音響器材好抵玩！舊喇叭、擴音機、黑膠唱盤、收音機，好多發燒友嚟尋寶。識貨嘅可以用好平嘅價錢買到好嘢。"},
            {"title": "🎪 周末地攤", "desc": "週末鴨寮街特別熱鬧，街邊會擺滿地攤賣二手電子產品、舊玩具、古董。氣氛好似跳蚤市場，慢慢行可以搵到好多意外驚喜。"},
        ],
        "shops": [
            ("電子零件店", "街邊同舖頭都係電子零件，需要整嘢嘅話材料齊全。"),
            ("二手音響店", "專賣二手音響器材，喇叭、擴音機、黑膠盤，識貨之人必到。"),
            ("地攤檔", "週末限定，賣二手電子產品同雜貨，尋寶必行。"),
        ],
        "tips": [
            "充電線$10-20就有交易，平過連鎖店好多",
            "二手音響器材好抵玩，但要有知識先買",
            "週末地攤最多，星期六日下午去最好",
            "格價都係必要，同一條街可以差幾倍",
            "帶現金，地攤通常只收現金",
        ],
        "foods": [
            ("合益泰小食", "深水埗腸粉王，行完鴨寮街行過嚟食腸粉，快捷方便。"),
            ("公和荳品廠", "百年荳品老店，豆腐花同煎釀三寶都好好食。"),
            ("文記車仔麵", "深水埗車仔麵之王，湯底濃郁餸菜多，行完鴨寮街食碗麵。"),
        ],
    },
]

for item in ITEMS:
    generate_page(item)

print(f"\nDone! Generated {len(ITEMS)} pages.")
