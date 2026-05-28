#!/usr/bin/env python3
"""Generate restaurant detail pages for all 29 food items."""
import os

OUT_DIR = "/Users/admin/Documents/test/sunnyhk"

HEAD = '<!DOCTYPE html>\n<html lang="zh-HK">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
CANONICAL = '<link rel="canonical" href="https://gohk.gamewayz.com/{slug}.html">\n'
MANIFEST = '<link rel="manifest" href="/manifest.json">\n'
GA_HEAD = '<script async src="https://www.googletagmanager.com/gtag/js?id=G-L9RMXXLKYK"></script>\n'
GA_BODY = '<script>\nwindow.dataLayer = window.dataLayer || [];\nfunction gtag(){dataLayer.push(arguments);}\ngtag("js", new Date());\ngtag("config", "G-L9RMXXLKYK");\n</script>\n'

NAV = '''<nav class="navbar">
  <div class="inner">
    <a href="index.html" class="logo">
      <div class="sun"><i class="fas fa-sun"></i></div> Sunny<span>HK</span>
    </a>
    <div class="nav-links">
      <a href="index.html" data-i18n="nav-home">首页</a>
      <div class="nav-dropdown">
        <a href="explore.html" data-i18n="nav-explore">探索指南</a>
        <div class="nav-dropdown-menu">
          <a href="explore.html" data-i18n="nav-explore-all">🌟 人群指南</a>
          <a href="hiking.html" data-i18n="nav-hiking">🥾 行山路線</a>
          <a href="snorkeling.html" data-i18n="nav-snorkeling">🤿 浮潛攻略</a>
          <a href="swimming.html" data-i18n="nav-swimming">🏊 游水指南</a>
        </div>
      </div>
      <a href="food.html" class="active" data-i18n="nav-food">美食地圖</a>
      <div class="nav-dropdown">
        <a href="tips.html" data-i18n="nav-tips">實用資訊</a>
        <div class="nav-dropdown-menu">
          <a href="tips.html" data-i18n="nav-tips-all">💡 實用貼士</a>
          <a href="electronics.html" data-i18n="nav-electronics">💻 電子產品</a>
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
</nav>

<div class="mobile-overlay" id="mobileOverlay"></div>
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

STYLES = """.trail-hero {
  position: relative; min-height: 50vh; display: flex; align-items: flex-end;
  background: linear-gradient(135deg, var(--primary) 0%, #0f172a 100%);
  overflow: hidden;
}
.trail-hero img {
  position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.6;
}
.trail-hero .overlay {
  position: absolute; inset: 0;
  background: linear-gradient(transparent 30%, rgba(0,0,0,0.8));
}
.trail-hero .inner {
  position: relative; z-index: 1; padding: 40px 24px 48px; width: 100%;
  max-width: 1200px; margin: 0 auto;
}
.trail-hero h1 { font-size: 2.4rem; font-weight: 900; color: white;
  font-family: var(--font-serif); margin-bottom: 8px; }
.trail-hero .meta { display: flex; gap: 16px; flex-wrap: wrap; color: rgba(255,255,255,0.8); font-size: 0.9rem; }
.trail-hero .meta span { background: rgba(255,255,255,0.12); padding: 4px 14px; border-radius: 100px; }
.trail-content { max-width: 800px; margin: 0 auto; padding: 48px 24px; }
.trail-intro { font-size: 1.05rem; line-height: 1.9; color: var(--text-light); margin-bottom: 40px; }
.step-card {
  background: var(--card-bg); border-radius: var(--radius-md);
  padding: 24px 28px; margin-bottom: 16px; box-shadow: var(--card-shadow);
  border-left: 4px solid var(--brand);
}
.step-card h3 { margin-bottom: 8px; font-size: 1.1rem; }
.step-card p { color: var(--text-light); font-size: 0.93rem; line-height: 1.8; }
.trail-tips { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px,1fr)); gap: 12px; }
.trail-tips li { background: var(--card-bg); border-radius: var(--radius-sm); padding: 14px 18px;
  list-style: none; box-shadow: var(--card-shadow); font-size: 0.9rem; color: var(--text-light); }
.trail-tips li::before { content: "💡 "; }
.back-link { display: inline-flex; align-items: center; gap: 8px; color: var(--brand);
  font-weight: 600; font-size: 0.9rem; margin-bottom: 32px; }
.back-link:hover { text-decoration: underline; }
@media (max-width: 768px) {
  .trail-hero h1 { font-size: 1.6rem; }
  .step-card { padding: 18px 20px; }
}
.dish-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px,1fr)); gap: 12px; }
.dish-card { background: var(--card-bg); border-radius: var(--radius-md); padding: 18px 22px;
  box-shadow: var(--card-shadow); border-left: 4px solid #f59e0b; }
.dish-card h4 { font-size: 1rem; margin-bottom: 6px; }
.dish-card p { font-size: 0.85rem; color: var(--text-light); line-height: 1.7; }
.price-box { background: var(--card-bg); border-radius: var(--radius-md); padding: 20px 24px;
  box-shadow: var(--card-shadow); text-align: center; border-left: 4px solid #10b981; }
.price-box .amount { font-size: 2rem; font-weight: 900; color: var(--brand); }
.price-box p { color: var(--text-light); font-size: 0.9rem; margin-top: 4px; }"""


def make_page(slug, emoji, name, hero_img,
              desc_para1, desc_para2, desc_para3,
              transport, dishes, price_range, price_detail,
              tips, nearby, og_title, og_desc):
    # Build dishes HTML outside the main template to avoid nested f-string issues
    dishes_html = ""
    for d in dishes:
        dishes_html += (
            '    <div class="dish-card">\n'
            '      <h4>\U0001f37d\ufe0f ' + d["name"] + '</h4>\n'
            '      <p>' + d["desc"] + '</p>\n'
            '    </div>\n'
        )
    # Build tips HTML
    tips_html = ""
    for t in tips:
        tips_html += '    <li>' + t + '</li>\n'

    meta_tags = ('<meta name="description" content="' + og_desc + '">\n'
        '<meta name="keywords" content="香港美食 ' + og_desc[:30] + '">\n')
    meta_og = ('<meta property="og:title" content="' + og_title + '">\n'
        '<meta property="og:description" content="' + og_desc + '">\n'
        '<meta property="og:url" content="https://gohk.gamewayz.com/' + slug + '.html">\n'
        '<meta property="og:type" content="article">\n'
        '<meta property="og:image" content="' + hero_img + '">\n'
        '<meta property="og:locale" content="zh_HK">\n')

    title = emoji + ' ' + name + ' | SunnyHK 美食地圖'

    html = (
        '<!DOCTYPE html>\n'
        '<html lang="zh-HK">\n'
        '<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        + meta_tags +
        '<meta name="robots" content="index, follow">\n'
        '<link rel="canonical" href="https://gohk.gamewayz.com/' + slug + '.html">\n'
        '<link rel="manifest" href="/manifest.json">\n'
        '<script async src="https://www.googletagmanager.com/gtag/js?id=G-L9RMXXLKYK"></script>\n'
        '<script>\n'
        'window.dataLayer = window.dataLayer || [];\n'
        'function gtag(){dataLayer.push(arguments);}\n'
        'gtag("js", new Date());\n'
        'gtag("config", "G-L9RMXXLKYK");\n'
        '</script>\n'
        + meta_og +
        '<title>' + title + '</title>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;700;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">\n'
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n'
        '<link rel="stylesheet" href="css/style.css">\n'
        '<style>' + STYLES + '</style>\n'
        '</head>\n'
        '<body>\n'
        '\n'
        + NAV + '\n'
        '\n'
        '<div class="trail-hero">\n'
        '  <img src="' + hero_img + '" alt="' + name + '" loading="lazy">\n'
        '  <div class="overlay"></div>\n'
        '  <div class="inner">\n'
        '    <a href="food.html" class="back-link" style="color:rgba(255,255,255,0.7);margin-bottom:16px;">← 回到美食地圖</a>\n'
        '    <h1>' + emoji + ' ' + name + '</h1>\n'
        '    <div class="meta">\n'
        '      <span>' + emoji + ' ' + name + '</span>\n'
        '    </div>\n'
        '  </div>\n'
        '</div>\n'
        '\n'
        '<div class="trail-content">\n'
        '\n'
        '  <h2 style="margin-bottom:20px;">\U0001f37d\ufe0f 食店介紹</h2>\n'
        '  <p class="trail-intro">' + desc_para1 + '</p>\n'
        '  <p style="margin-bottom:16px;color:var(--text-light);font-size:0.98rem;line-height:1.9;">' + desc_para2 + '</p>\n'
        '  <p style="margin-bottom:16px;color:var(--text-light);font-size:0.98rem;line-height:1.9;">' + desc_para3 + '</p>\n'
        '\n'
        '  <h2 style="margin:40px 0 20px;">📍 交通</h2>\n'
        '  <div class="step-card" style="border-left-color:#3b82f6;">\n'
        '    <p style="color:var(--text-light);font-size:0.95rem;">' + transport + '</p>\n'
        '  </div>\n'
        '\n'
        '  <h2 style="margin:40px 0 20px;">📋 必食推介</h2>\n'
        '  <div class="dish-grid">\n'
        + dishes_html +
        '  </div>\n'
        '\n'
        '  <h2 style="margin:40px 0 20px;">💰 價格參考</h2>\n'
        '  <div class="price-box">\n'
        '    <div class="amount">' + price_range + '</div>\n'
        '    <p>' + price_detail + '</p>\n'
        '  </div>\n'
        '\n'
        '  <h2 style="margin:40px 0 20px;">💡 小編貼士</h2>\n'
        '  <ul class="trail-tips">\n'
        + tips_html +
        '  </ul>\n'
        '\n'
        '  <h2 style="margin:40px 0 20px;">🗺️ 附近好去處</h2>\n'
        '  <div class="step-card" style="border-left-color:#06b6d4;">\n'
        '    <p style="color:var(--text-light);font-size:0.95rem;">' + nearby + '</p>\n'
        '  </div>\n'
        '\n'
        '  <div style="text-align:center;margin:48px 0;">\n'
        '    <a href="food.html" class="submit-btn" style="display:inline-block;width:auto;padding:14px 36px;border-radius:100px;text-decoration:none;">\n'
        '      ← 回到美食地圖\n'
        '    </a>\n'
        '  </div>\n'
        '</div>\n'
        '\n'
        + FOOTER + '\n'
        '\n'
        + SCRIPTS + '\n'
        '</body>\n'
        '</html>\n'
    )
    return html


# ====== DATA ======

restaurants = [
  {"slug":"food-red-tea-house","emoji":"\U0001f947","name":"紅茶冰室","lat":22.296,"lng":114.171,"hero_img":"https://images.unsplash.com/photo-1651658313775-90bf2751913e?auto=format&fit=crop&w=1200&q=80","og_title":"紅茶冰室 · 尖沙咀人氣冰室 | SunnyHK 美食攻略","og_desc":"尖沙咀金馬倫道人氣冰室，小紅書爆紅。冰火菠蘿油熱辣辣，沙嗲牛肉麵濃郁，芝士流心西多士邪惡到極點。","desc_para1":"紅茶冰室係近年尖沙咀最火爆嘅茶餐廳之一，喺小紅書上瘋傳為「最好食嘅茶餐廳」，日日排長龍。位於金馬倫道嘅呢間冰室，憑藉超高質素嘅港式美食同懷舊裝修，成功俘虜咗一大班年輕食客嘅心。","desc_para2":"店內裝潢走懷舊香港風，綠色瓷磚、霓虹燈牌、鐵閘、舊式吊扇，每個角落都係打卡位。水吧師傅手腳快，沖奶茶、整菠蘿油、煮公仔麵，每一個動作都充滿節奏感。廚房出餐速度驚人，快狠準係佢哋嘅宗旨。","desc_para3":"除咗招牌冰火菠蘿油同日賣過千個嘅沙嗲牛肉公仔麵，紅茶冰室嘅芝士流心西多士亦係一絕——炸到金黃嘅多士中間夾住流心芝士，上面仲有牛油同糖漿，邪惡到極點但一啖接一啖停唔到口。","transport":"🚇 港鐵尖沙咀站B2出口，沿金馬倫道行約3分鐘就到。或者由尖東站P3出口行過去都係5分鐘左右。","dishes":[{"name":"冰火菠蘿油","desc":"熱辣辣出爐菠蘿包夾住冰凍牛油，一冷一熱嘅口感係冰室靈魂之作。外皮酥脆到一咬即碎，牛油慢慢融化滲入麵包。必點！"},{"name":"沙嗲牛肉公仔麵","desc":"濃郁沙嗲醬汁配上嫩滑牛肉，公仔麵煮得恰到好處。湯底濃稠掛汁，每一啖都食到沙嗲嘅香辣同花生味。"},{"name":"芝士流心西多士","desc":"炸得金黃香脆嘅厚切西多士，中間夾住流心芝士，上面淋上牛油同糖漿。切開一刻芝士流心嘅畫面令人無法抗拒。"},{"name":"紅豆冰","desc":"經典港式紅豆冰，紅豆煮得軟腍起沙，花奶同碎冰完美融合。食完濃味嘢飲返杯，清爽解膩。"}],"price_range":"$40-60","price_detail":"早餐 $40起 · 常餐 $50-60 · 下午茶 $38起 · 只收現金","tips":["朝早8點至10點早餐時段人最少，唔使排隊","菠蘿油出爐時間大約朝早8點同下晝3點，新鮮出爐最好食","尖沙咀店長期排隊，建議平日去","手機落單，用QR code掃Menu就得","芝士流心西多士邪惡指數爆燈，建議同人share","凍飲+$3，熱飲免費"],"nearby":"食完紅茶冰室可以行去尖沙咀海旁睇維港夜景，或者去K11 Musea行街打卡。附近仲有海港城、1881 Heritage。","query_name":"紅茶冰室"},
  {"slug":"food-wah-sou","emoji":"\U0001f35e","name":"華嫂冰室","lat":22.314,"lng":114.225,"hero_img":"https://images.unsplash.com/photo-1576444356170-66073046b1bc?auto=format&fit=crop&w=1200&q=80","og_title":"華嫂冰室 · 余文樂也愛嘅招牌鹹牛肉豬仔包 | SunnyHK 美食攻略","og_desc":"元朗起家嘅人氣冰室，招牌鹹牛肉芝士豬仔包、番茄雞翼通粉、凍奶茶。周潤發都食過！","desc_para1":"華嫂冰室由元朗起家，憑藉招牌鹹牛肉芝士豬仔包同番茄雞翼通粉打響名堂，連余文樂、周潤發都係熟客。而家喺觀塘、灣仔、尖沙咀都有分店，但元朗總店依然係最有feel。","desc_para2":"老闆娘華嫂堅持用新鮮食材，鹹牛肉係自家調味，豬仔包烘得外脆內軟。番茄湯底用新鮮番茄熬製，酸甜濃郁，配雞翼或者通粉都一流。每個細節都做到足，難怪由元朗做到出晒名。","desc_para3":"舖頭細細但人情味濃，伙記同客人有講有笑，係典型嘅港式街坊冰室氛圍。無論係早餐、午餐定下午茶，華嫂冰室都係元朗街坊同遊客嘅必到之地。","transport":"🚇 元朗總店：元朗站B出口行15分鐘／觀塘店：觀塘站B1出口行5分鐘／灣仔店：灣仔站A4出口行8分鐘／尖沙咀店：尖沙咀站N2出口行3分鐘","dishes":[{"name":"鹹牛肉芝士豬仔包","desc":"鎮店之寶！烘得香脆嘅豬仔包夾住鹹香牛肉同半溶芝士，一啖咬落去多重口感，係華嫂嘅代表作。"},{"name":"番茄雞翼通粉","desc":"新鮮番茄熬成濃郁湯底，配上滷得入味嘅雞翼同滑溜通粉。酸甜開胃，大人細路都鍾意。"},{"name":"凍奶茶","desc":"港式絲襪奶茶，茶底濃厚順滑，凍飲都唔會淡味。用正宗黑白淡奶沖製，係冰室嘅靈魂飲品。"},{"name":"招牌菠蘿油","desc":"同傳統菠蘿油唔同，華嫂嘅菠蘿油夾住厚切蕃茄同煎蛋，酸甜鹹香一次過滿足晒。"}],"price_range":"$50-70","price_detail":"招牌豬仔包 $25 · 番茄通粉 $45-55 · 凍奶茶 $18 · 人均 $50-70","tips":["午市12點至2點最爆，建議避開高峰時段","元朗總店最有風味，但較偏僻；灣仔/尖沙咀分店較方便","鹹牛肉芝士豬仔包每日新鮮限量，晏咗可能賣晒","凍奶茶比熱奶茶更出名，必試","番茄雞翼通粉可以揀轉螺絲粉或者米粉","只收現金嘅分店要留意，建議帶定錢"],"nearby":"元朗總店附近可以行南生圍睇草原同濕地，或者去元朗公園。灣仔分店就近會展同金紫荊廣場。","query_name":"華嫂冰室"},
  {"slug":"food-australia-dairy","emoji":"\U0001f96a","name":"澳洲牛奶公司","lat":22.305,"lng":114.169,"hero_img":"https://images.unsplash.com/photo-1550396790-1502488d7fde?auto=format&fit=crop&w=1200&q=80","og_title":"澳洲牛奶公司 · 佐敦傳奇茶餐廳 | SunnyHK 美食攻略","og_desc":"佐敦白加士街傳奇茶餐廳，炒蛋多士滑到震，燉奶清爽香甜。店員速度同態度一樣出名，快狠準！","desc_para1":"澳洲牛奶公司（簡稱「澳牛」）係香港茶餐廳界嘅傳奇。位於佐敦白加士街，以光速上菜同「澳牛式服務」聞名——伙記落單快、出餐快、收碗快，新手未坐暖櫈就已經有嘢食擺喺面前。","desc_para2":"澳牛嘅炒蛋多士係全港數一數二，用咩方法炒到咁滑？秘密係落足牛油，快火翻炒至半凝固狀態，蛋香濃郁、口感滑溜。配合烘得金黃嘅厚多士，簡單但完美。燉奶亦係招牌，清爽香甜，凍食尤其正。","desc_para3":"雖然伙記講話大聲、動作粗魯，但呢種高效率嘅服務風格反而成為澳牛嘅特色。佢哋其實好細心，會記住熟客嘅口味。嚟得澳牛就要遵守「澳牛規則」——落單要快、食完就走、唔好阻住地球轉。","transport":"🚇 港鐵佐敦站C2出口，沿白加士街行約2分鐘就到。或者柯士甸站F出口行5分鐘都得。","dishes":[{"name":"炒蛋多士","desc":"澳牛靈魂之作！半凝固炒蛋滑到不得了，蛋味濃郁，配上烘底厚多士，簡單但係人間美味。"},{"name":"燉奶","desc":"清爽香甜嘅燉奶，凍食係夏天一流嘅甜品。奶味濃郁但唔膩，口感似絲絨咁滑。"},{"name":"叉燒湯意粉","desc":"港式茶餐廳經典，叉燒切得厚身，湯底係雞湯底，意粉軟硬適中。簡單但暖胃嘅comfort food。"},{"name":"凍檸茶","desc":"經典港式凍檸茶，茶底夠濃，檸檬新鮮。食完炒蛋多士飲返杯，完美配搭。"}],"price_range":"$40-60","price_detail":"炒蛋多士 $35 · 燉奶 $28 · 常餐 $48-58 · 只收現金","tips":["落單要快！伙記會等你3秒就催，諗好先舉手","朝早8點前去到最少人，下晝同週末排到出街","燉奶可以揀熱食或者凍食，夏天推薦凍食","炒蛋可以加$5轉雙蛋","食完快啲走，後面有人等緊位","記住：唔好叫「澳洲牛奶公司」全名，叫「澳牛」就得"],"nearby":"佐敦附近有廟街夜市、九龍公園、玉器市場。行遠少少可以去尖沙咀海旁同香港藝術館。","query_name":"澳洲牛奶公司"},
  {"slug":"food-wong-gee","emoji":"\U0001f9c8","name":"旺記冰室","lat":22.278,"lng":114.173,"hero_img":"https://images.unsplash.com/photo-1465403157034-1d5e05cc2ac0?auto=format&fit=crop&w=1200&q=80","og_title":"旺記冰室 · 灣仔滑蛋飯專家 | SunnyHK 美食攻略","og_desc":"灣仔人氣冰室，滑蛋飯系列係招牌。蝦仁滑蛋飯、叉燒滑蛋飯，蛋香濃郁。價錢公道，打工仔午餐首選。","desc_para1":"旺記冰室係灣仔打工仔嘅午餐聖地，以滑蛋飯系列聞名。佢哋用日本雞蛋，炒出嚟嘅滑蛋半熟流心、蛋香濃郁，配上新鮮蝦仁或者厚切叉燒，簡單但係完美嘅comfort food。","desc_para2":"雖然灣仔食肆林立，但旺記冰室總係大排長龍。$50-60就有一碟滑蛋飯，仲要係日本雞蛋，性價比極高。用豉油撈飯食係指定動作，滑蛋同飯完美結合，每一啖都係享受。","desc_para3":"除咗滑蛋飯，旺記嘅下午茶餐都好抵食。櫻花蝦滑蛋飯、沙爹牛肉麵、鮮牛油多士，樣樣都用心做。環境乾淨企理，伙記服務快又有禮貌，係一間令人會翻啅嘅冰室。","transport":"🚇 灣仔站A4出口，沿軒尼詩道行約5分鐘就到。或者銅鑼灣站行過嚟都係10分鐘左右。","dishes":[{"name":"滑蛋叉燒蝦仁雙拼飯","desc":"招牌菜！日本雞蛋炒到半熟流心，叉燒厚身唔乾，蝦仁大粒爽脆。用豉油撈飯食係最正宗食法。"},{"name":"櫻花蝦滑蛋飯","desc":"櫻花蝦嘅鹹香同滑蛋嘅嫩滑完美配合，加上秘製醬油，簡單但令人回味。"},{"name":"沙爹牛肉公仔麵","desc":"濃郁沙爹醬汁、嫩滑牛肉、彈牙公仔麵，係港式茶餐廳嘅經典配搭。湯底濃稠，每一啖都掛汁。"},{"name":"鮮牛油多士","desc":"厚多士烘得金黃香脆，夾住冰凍鮮牛油。雖然簡單，但係最考功夫嘅港式小食。"}],"price_range":"$50-70","price_detail":"滑蛋飯 $50-60 · 下午茶餐 $38起 · 沙爹牛麵 $42 · 凍飲+$3","tips":["下晝2點至5點下午茶時段最抵，滑蛋飯都有下午茶價","午市12點至2點一定排隊，建議早啲或者遲啲去","日本雞蛋用晒就轉普通蛋，建議中午前去","可以叫「多豉油」，撈飯更惹味","灣仔店星期日休息，留意","凍飲+$3，但熱飲免費，冬天可以慳返"],"nearby":"灣仔附近有利東街（喜帖街）、合和中心觀景台、太原街玩具街。行遠少少可以去金紫荊廣場同會展。","query_name":"旺記冰室"},
  {"slug":"food-lee-keung-kei","emoji":"\U0001f95a","name":"利強記北角雞蛋仔","lat":22.291,"lng":114.200,"hero_img":"https://images.unsplash.com/photo-1629007006355-d75f7b828bfd?auto=format&fit=crop&w=1200&q=80","og_title":"利強記北角雞蛋仔 · 米芝蓮街頭小食 | SunnyHK 美食攻略","og_desc":"北角雞蛋仔代表，外脆內軟、蛋香濃郁，粒粒飽滿。即叫即製，出爐香噴噴。仲有格仔餅同紅豆沙。","desc_para1":"利強記北角雞蛋仔係香港街頭小食嘅傳奇，連續多年獲得米芝蓮街頭小食推薦。位於北角英皇道嘅呢間小店，每日新鮮即製雞蛋仔，外脆內軟、蛋香濃郁，粒粒都飽滿圓潤。","desc_para2":"同坊間嘅雞蛋仔唔同，利強記嘅雞蛋仔外層特別脆，咬落去有「咔嚓」聲，但入面係軟心嘅。唔會太甜，蛋味十足，係香港人由細食到大嘅味道。出爐時香氣飄到成條街都聞到，排隊都值得。","desc_para3":"除了雞蛋仔，利強記仲有格仔餅（窩夫）同紅豆沙。格仔餅搽滿花生醬、煉奶同砂糖，口感豐富。紅豆沙煲得起沙，甜度適中。冬天食一碗暖笠笠，係街頭小食嘅完美ending。","transport":"🚇 港鐵北角站A1出口，行出英皇道就見到。或者搭電車喺北角站落車都得。","dishes":[{"name":"原味雞蛋仔","desc":"招牌原味雞蛋仔，外層金黃酥脆，內裏軟心。蛋香濃郁，粒粒飽滿，出爐時趁熱食最正。"},{"name":"格仔餅","desc":"即叫即製格仔餅，熱辣辣搽滿花生醬、煉奶同砂糖。外脆內軟，甜到入心。"},{"name":"紅豆沙","desc":"傳統中式甜品，紅豆煲得起沙，加入陳皮同冰糖調味。甜度適中，冬天食暖笠笠。"}],"price_range":"$20-30","price_detail":"雞蛋仔 $20/底 · 格仔餅 $18 · 紅豆沙 $15","tips":["出爐即食最正，放耐咗就唔脆","下晝3點至6點出爐最新鮮","雞蛋仔要趁熱食，凍咗會變韌","格仔餅可以要求「多醬」，花生醬煉奶多啲更好味","米芝蓮推薦所以長期有遊客排隊，但等10-15分鐘就搞掂","只收現金，記住帶散銀"],"nearby":"北角有春秧街街市（叮叮車穿過街市嘅經典場景）、北角碼頭、紅香爐峰行山。仲可以搭電車遊港島。","query_name":"利強記北角雞蛋仔"},
  {"slug":"food-lee-tung-fishballs","emoji":"\U0001f41f","name":"利東街炸魚蛋","lat":22.276,"lng":114.171,"hero_img":"https://images.unsplash.com/photo-1528973549867-6fa7842e20c0?auto=format&fit=crop&w=1200&q=80","og_title":"利東街炸魚蛋 · 灣仔隱世魚蛋檔 | SunnyHK 美食攻略","og_desc":"灣仔利東街附近嘅隱世魚蛋檔，炸魚蛋金黃酥脆，配上辣醬甜醬，係香港人由細食到大嘅味道。","desc_para1":"喺灣仔利東街（喜帖街）附近，有間低調得嚟又人氣極高嘅魚蛋檔，專賣炸魚蛋同煎釀三寶。唔講你可能行過都唔覺，但佢嘅炸魚蛋係灣仔區數一數二咁好食。","desc_para2":"魚蛋每日新鮮炸起，金黃酥脆，咬開入面彈牙有魚味。最正係配上甜醬同辣醬，一甜一辣嘅味道係香港人由細到大嘅集體回憶。仲有煎釀三寶——茄子、青椒、豆腐釀魚肉，即叫即炸。","desc_para3":"呢間檔仔雖然冇華麗裝修，但正正係呢種地道風味先最吸引。$15-25就有一串炸魚蛋或者幾件煎釀三寶，邊行邊食，就係最地道嘅香港街頭美食體驗。","transport":"🚇 港鐵灣仔站A3出口，沿莊士敦道行向利東街方向約5分鐘。或者搭電車喺灣仔站落車。","dishes":[{"name":"炸魚蛋","desc":"金黃酥脆嘅炸魚蛋，外皮脆卜卜，入面彈牙有魚味。配甜醬辣醬一齊食，係最經典嘅港式小食。"},{"name":"煎釀三寶","desc":"茄子、青椒、豆腐釀入魚肉即叫即炸。茄子軟腍、青椒清爽、豆腐嫩滑，三種口感一次過滿足。"},{"name":"混醬腸粉","desc":"滑溜腸粉配上甜醬、麻醬、辣醬同芝麻，係香港街頭經典小食。$10就有一份。"}],"price_range":"$15-25","price_detail":"炸魚蛋 $12/串 · 煎釀三寶 $15/3件 · 腸粉 $10/份","tips":["炸魚蛋配辣醬最夾，可以叫「多辣」","煎釀三寶即叫即炸，等3-5分鐘","利東街係步行街，可以邊行邊食","附近仲有好多小食檔，可以一次掃街","只收現金，帶定散銀","下晝2點至6點最新鮮出爐"],"nearby":"利東街（喜帖街）本身係打卡景點，婚紗攝影熱點。附近有太原街玩具街、灣仔街市、藍屋建築群。","query_name":"利東街炸魚蛋"},
  {"slug":"food-kung-so","emoji":"\U0001f95f","name":"公和荳品廠","lat":22.330,"lng":114.162,"hero_img":"https://images.unsplash.com/photo-1504664911901-2518a8bfc164?auto=format&fit=crop&w=1200&q=80","og_title":"公和荳品廠 · 深水埗百年豆腐花 | SunnyHK 美食攻略","og_desc":"深水埗百年老字號！豆腐花滑到好似絲綢咁，仲有煎釀豆腐、豆卜、豆漿。傳統風味，$10幾蚊就食到開心。","desc_para1":"公和荳品廠係深水埗嘅百年老字號，1893年創立，由一個小豆品檔做到家傳戶曉。佢哋嘅豆腐花滑到好似絲綢咁，入口即溶，豆味濃郁。$10幾蚊就有一碗，平靚正到冇朋友。","desc_para2":"店內仍然保留住舊式豆品廠嘅格局，你可以睇到師傅點樣石磨豆、煮豆漿、壓豆腐。每日新鮮即製，用傳統石磨方法保留黃豆嘅原味。煎釀豆腐、炸豆卜、豆漿，樣樣都係水準之上。","desc_para3":"公和荳品廠唔單止係食店，更係深水埗嘅社區中心。老街坊每日嚟食早餐傾計，遊客專程嚟朝聖。$10幾蚊就買到一份百年傳統同埋香港情懷，仲要係米芝蓮都有推薦過。","transport":"🚇 港鐵深水埗站B2出口，沿北河街行約3分鐘就到。或者深水埗站A2出口行5分鐘都得。","dishes":[{"name":"豆腐花","desc":"招牌豆腐花，滑溜如絲，豆味濃郁。可以揀熱食或者凍食，加黃糖或者薑汁，簡單但係完美。"},{"name":"煎釀豆腐","desc":"即叫即煎，豆腐外皮煎得金黃，入面嫩滑。配上甜豉油同辣椒醬，一試難忘。"},{"name":"豆漿","desc":"每日新鮮石磨豆漿，濃郁順滑。可以揀甜或者淡，凍飲或者熱飲，真材實料。"},{"name":"炸豆卜","desc":"金黃酥脆嘅炸豆卜，豆香十足。沾辣椒醬食仲正。"}],"price_range":"$10-30","price_detail":"豆腐花 $12-15 · 煎釀豆腐 $18 · 豆漿 $10 · 炸豆卜 $15","tips":["豆腐花可以揀「加花奶」，更香滑","煎釀豆腐要等5分鐘即叫即煎","朝早8點去食最新鮮，豆品係凌晨開始整","外賣可以買一大盒豆腐花返屋企","星期日好多人，建議平日去","只收現金，記住帶錢"],"nearby":"深水埗仲有合益泰腸粉、文記車仔麵、十八座狗仔粉等美食。附近仲有黃金電腦商場、鴨寮街、荔枝角公園。","query_name":"公和荳品廠"},
  {"slug":"food-mommy-eggette","emoji":"\U0001f361","name":"媽咪雞蛋仔","lat":22.303,"lng":114.188,"hero_img":"https://images.unsplash.com/photo-1562757258-05a61b40eeee?auto=format&fit=crop&w=1200&q=80","og_title":"媽咪雞蛋仔 · 紅磡人氣波波雞蛋仔 | SunnyHK 美食攻略","og_desc":"紅磡人氣雞蛋仔，粒粒都係波波型，外脆內軟口感超特別。多款口味：原味、朱古力、抹茶紅豆、芝士。","desc_para1":"媽咪雞蛋仔係紅磡嘅人氣雞蛋仔專門店，佢哋嘅雞蛋仔同傳統嘅好唔同——每一粒都係波波型，粒粒分離，外脆內軟，口感超特別。呢種獨特嘅製作方法令媽咪雞蛋仔喺雞蛋仔界突圍而出。","desc_para2":"除咗經典原味，媽咪雞蛋仔仲有好多創新口味：比利時朱古力味濃郁香甜、抹茶紅豆味帶日式風情、芝士味鹹香有趣。每底都係即叫即製，熱辣辣出爐最好食。","desc_para3":"舖頭細細但人氣旺盛，長期有街坊同學生幫襯。$20-35就有一底特色雞蛋仔，性價比高。拎住一底熱辣辣嘅雞蛋仔邊行邊食，就係最地道嘅香港街頭美食體驗。","transport":"🚇 港鐵紅磡站B1出口，沿機利士南路行約8分鐘。或者由黃埔站行過去都係10分鐘。","dishes":[{"name":"原味雞蛋仔","desc":"經典原味，蛋香濃郁。粒粒波波型，外脆內軟，食得出師傅嘅手藝。"},{"name":"抹茶紅豆味","desc":"日式抹茶配紅豆，抹茶味甘香，紅豆甜而不膩。係最受歡迎嘅創新口味。"},{"name":"朱古力味","desc":"用比利時朱古力製作，濃郁香甜。朱古力半融化喺雞蛋仔入面，邪惡但好食。"},{"name":"芝士味","desc":"鹹香芝士味雞蛋仔，芝士控必試。芝士拉絲效果，鹹甜交錯好特別。"}],"price_range":"$20-35","price_detail":"原味 $20 · 特色口味 $25-35 · 格仔餅 $22","tips":["出爐即刻食最正，放耐咗會變腍","抹茶紅豆味係人氣No.1，好快賣晒","可以WhatsApp落單預訂，唔使等","夜晚8點後可能賣晒，建議早啲去","$5可以加煉奶或者朱古力醬topping","格仔餅都好出色，可以試埋"],"nearby":"紅磡有黃埔天地商場、紅磡碼頭海濱長廊、觀音廟。搭船去北角或者灣仔都好方便。","query_name":"媽咪雞蛋仔"},
  {"slug":"food-choi-hing","emoji":"\U0001f357","name":"再興燒臘","lat":22.277,"lng":114.173,"hero_img":"https://images.unsplash.com/photo-1651658313775-90bf2751913e?auto=format&fit=crop&w=1200&q=80","og_title":"再興燒臘 · 百年叉燒之王 | SunnyHK 美食攻略","og_desc":"灣仔百年老字號，叉燒嘅天花板級別！蜜汁叉燒半肥瘦，邊位焦香，入口即溶。燒肉皮脆肉嫩。","desc_para1":"再興燒臘係灣仔嘅百年老字號，由清末創立至今已經過百年歷史。CNN曾封佢為「叉燒嘅同義詞」，話食過再興嘅叉燒就明白叉燒應該係咩味道。呢度嘅蜜汁叉燒半肥瘦，邊位焦香，入口即溶，係叉燒界嘅天花板。","desc_para2":"再興嘅燒味全部係店內工場新鮮燒製，每日出爐三至四次。叉燒用梅頭肉，脂肪分佈均勻，蜜汁香甜不膩。燒肉皮脆到好似薯片，層次分明。燒鴨同油雞都係水準之上，每樣都係招牌。","desc_para3":"舖頭裝修樸實無華，伙記快手快腳，係典型香港燒臘店嘅格局。好多灣仔打工仔由細食到大，係真正嘅街坊食堂。外賣嘅話記住叫「多汁」，加$2就可以多一碗靚湯。","transport":"🚇 港鐵灣仔站A4出口，沿軒尼詩道行約5分鐘，喺史釗域道交界就見到。","dishes":[{"name":"蜜汁叉燒","desc":"用梅頭肉燒製，半肥瘦，邊位焦香。蜜汁香甜，肉質軟腍，入口即溶。係全港數一數二嘅叉燒。"},{"name":"燒肉","desc":"皮脆到好似薯片咁，層次分明。肥瘦相間，肉嫩多汁。點芥末醬食最夾。"},{"name":"三寶飯","desc":"叉燒、燒肉、油雞三合一，一次過滿足三個願望。飯底加薑蓉豉油，簡單但係完美。"},{"name":"油雞","desc":"雞肉嫩滑，雞皮爽脆，滷水汁香甜入味。配薑蔥蓉一齊食，令人回味。"}],"price_range":"$50-80","price_detail":"叉燒飯 $45 · 三寶飯 $58 · 燒肉飯 $48 · 外賣湯+$2","tips":["午市12點至2點大排長龍，建議下晝2點後去","叫「多汁」會加多啲叉燒汁，撈飯一流","燒味可以買外賣斬料，半斤叉燒約$60","加$2有老火靚湯，日日唔同","只收現金，記住帶錢","星期日休息，唔好摸門釘"],"nearby":"灣仔有利東街、太原街玩具街、藍屋、和昌大押。行遠少少可以去金紫荊廣場同會展。","query_name":"再興燒臘"},
  {"slug":"food-yung-kee","emoji":"\U0001f969","name":"鏞記酒家","lat":22.281,"lng":114.155,"hero_img":"https://images.unsplash.com/photo-1549212408-d6b0defe25cf?auto=format&fit=crop&w=1200&q=80","og_title":"鏞記酒家 · 中環傳奇金牌燒鵝 | SunnyHK 美食攻略","og_desc":"中環威靈頓街傳奇燒味店，金牌燒鵝馳名中外。皮脆肉嫩，肉汁豐富，炭燒風味獨一無二。","desc_para1":"鏞記酒家係中環威靈頓街嘅傳奇燒味店，以金牌燒鵝馳名中外。創立於1942年，由一個小燒臘檔發展到今日嘅國際知名酒家。鏞記嘅燒鵝被譽為「香港第一燒鵝」，連外國元首同明星都專程嚟食。","desc_para2":"鏞記嘅燒鵝用獨門醬料醃製，再用傳統炭火爐燒烤。鵝皮薄脆如玻璃，皮下脂肪甘香，肉質嫩滑多汁。每一隻燒鵝都係師傅幾十年手藝嘅結晶。除咗燒鵝，佢哋嘅叉燒、燒肉、蜜汁燒鳳肝都係招牌。","desc_para3":"鏞記酒家係一間正式酒樓，環境典雅，服務專業。多年來獲得無數獎項，包括米芝蓮一星。雖然價錢偏高，但質素絕對對得住個價。好多香港人過時過節或者宴請親朋都會揀鏞記。","transport":"🚇 港鐵中環站D2出口，沿德己立街行上威靈頓街約8分鐘。或者由香港站C出口行10分鐘。","dishes":[{"name":"金牌燒鵝","desc":"鏞記鎮店之寶，鵝皮薄脆如玻璃，皮下脂香四溢，肉嫩多汁。炭火燒烤風味獨一無二。"},{"name":"蜜汁叉燒","desc":"用優質梅頭肉，蜜汁香甜，肉質軟腍。邊位微微焦香，係叉燒嘅頂級示範。"},{"name":"酸薑皮蛋","desc":"鏞記另一招牌前菜，皮蛋晶瑩剔透，配酸甜子薑，開胃好食。"},{"name":"禮雲子琵琶蝦","desc":"季節限定菜式，用珍貴禮雲子配大蝦，鮮味濃郁。係鏞記名菜之一。"}],"price_range":"$150-300","price_detail":"燒鵝髀 $180 · 叉燒 $120/例 · 外賣燒鵝髀飯 $80 · 晚市$300起","tips":["外賣燒鵝髀飯平過堂食成半，$80就食到","朝早11點前外賣最少人排隊","燒鵝可以買半隻或者全隻外賣，返屋企慢慢食","中秋節鏞記月餅好出名，要預訂","二樓環境比地下一樓好啲","加$20可以轉鵝髀，值得"],"nearby":"中環附近有大館、PMQ元創方、半山扶手電梯、蘭桂坊。行遠啲可以去太平山頂睇夜景。","query_name":"鏞記酒家"},
  {"slug":"food-yat-lok","emoji":"\U0001f986","name":"一樂燒鵝","lat":22.283,"lng":114.155,"hero_img":"https://images.unsplash.com/photo-1549212408-d6b0defe25cf?auto=format&fit=crop&w=1200&q=80","og_title":"一樂燒鵝 · 中環米芝蓮抵食燒鵝 | SunnyHK 美食攻略","og_desc":"中環最抵食嘅米芝蓮燒鵝！燒鵝髀飯$70左右，平過鏞記一半但水準極高。皮脆肉嫩，外國遊客都慕名而來。","desc_para1":"一樂燒鵝係中環最抵食嘅米芝蓮燒鵝店，連續多年獲得米芝蓮一星。位於中環士丹利街，燒鵝髀飯$70左右就食到，平過鏞記一半但水準極高。皮脆肉嫩，燒味香濃，係中環打工仔嘅 luxury lunch。","desc_para2":"一樂嘅燒鵝用廣東傳統方法製作，鵝皮薄脆、肉質嫩滑、肉汁豐富。秘製醬汁係靈魂，鹹甜適中，襯托出鵝肉嘅鮮味。除咗燒鵝，佢哋嘅化皮燒肉同蜜汁叉燒都好出色。","desc_para3":"舖頭細細，坐位唔多，午市一定排長龍。但排隊係值得嘅——一碟燒鵝髀飯、一碟薑蓉、一杯凍檸茶，就係完美嘅香港午餐。連外國遊客都慕名而來，餐牌有中英日對照。","transport":"🚇 港鐵中環站D2出口，沿德己立街行上士丹利街約5分鐘。或者由香港站C出口行8分鐘。","dishes":[{"name":"燒鵝髀飯","desc":"招牌菜！鵝皮薄脆如玻璃，鵝肉嫩滑多汁。髀位係全鵝最靚嘅部位，肉質最嫩。"},{"name":"化皮燒肉","desc":"燒肉皮脆到一咬就碎，層次分明。肥瘦肉相間，肉味濃郁。點芥末醬食一流。"},{"name":"蜜汁叉燒","desc":"半肥瘦叉燒，蜜汁香甜唔膩。邊位微微焦香，肉質軟腍入味。"},{"name":"油雞","desc":"雞肉嫩滑，雞皮爽脆。滷水汁香甜，配薑蔥蓉食最夾。"}],"price_range":"$60-120","price_detail":"燒鵝髀飯 $75 · 燒鵝瀨粉 $68 · 化皮燒肉飯 $55 · 三寶飯 $65","tips":["平日下晝2點後少人啲，唔使排咁耐","燒鵝髀飯係招牌，但鵝髀好快賣晒","可以叫「髀瀨」= 燒鵝髀瀨粉","加$5轉鵝髀，值得畀","店內坐位有限，可以考慮外賣","只收現金，隔離有銀行可以撳錢"],"nearby":"中環附近有蘭桂坊、大館、PMQ、半山扶手電梯。行遠啲可以去太平山頂睇夜景。","query_name":"一樂燒鵝"},
  {"slug":"food-sun-kwai-heung","emoji":"\U0001f437","name":"新桂香燒臘","lat":22.264,"lng":114.237,"hero_img":"https://images.unsplash.com/photo-1529692236675-6b5097e14b01?auto=format&fit=crop&w=1200&q=80","og_title":"新桂香燒臘 · 柴灣薯片燒肉 | SunnyHK 美食攻略","og_desc":"柴灣人氣燒臘店，燒肉皮脆到好似薯片咁！日日新鮮出爐，下晝兩點通常賣得七七八八。柴灣街坊嘅集體回憶。","desc_para1":"新桂香燒臘係柴灣嘅人氣燒臘店，佢哋嘅燒肉皮脆到好似薯片咁，咬落去「咔嚓」聲，係柴灣街坊嘅集體回憶。日日新鮮出爐，下晝兩點通常已經賣得七七八八，想食就要趁早。","desc_para2":"新桂香雖然唔係米芝蓮，但喺街坊心中嘅地位絕對係米芝蓮級。佢哋嘅燒味全部係店內工場新鮮燒製，唔用隔夜貨。燒肉嘅皮脆係全港數一數二，好多區外人專程入柴灣都係為咗呢碟燒肉。","desc_para3":"舖頭細細，坐位唔多，主要做外賣同街坊生意。老細同伙記都係柴灣街坊，親切有禮。價錢公道、份量十足，係真正嘅街坊食堂。$40-60就食到一碟靚燒味飯，性價比極高。","transport":"🚇 港鐵柴灣站A出口，沿柴灣道行約10分鐘。或者由柴灣站轉乘綠色小巴，喺新桂香燒臘門口落車。","dishes":[{"name":"燒肉","desc":"招牌菜！皮脆到好似薯片咁，層次分明。肥瘦相間，肉嫩多汁。點芥末醬或淮鹽食最夾。"},{"name":"蜜汁叉燒","desc":"半肥瘦叉燒，蜜汁香甜。邊位焦香，肉質軟腍入味。係街坊最愛嘅外賣斬料。"},{"name":"燒鴨","desc":"鴨皮薄脆，鴨肉嫩滑。滷水汁香甜，肉味濃郁。配酸梅醬一食，開胃好食。"},{"name":"燒腩仔飯","desc":"燒肉中最靚嘅腩位，皮脆肉嫩，層次分明。配上薑蓉豉油飯，簡單但完美。"}],"price_range":"$40-60","price_detail":"燒肉飯 $45 · 叉燒飯 $42 · 燒腩仔飯 $50 · 三寶飯 $55","tips":["下晝早啲去，兩點後好多嘢就賣晒","燒肉出爐時間大約朝早11點同下晝1點","可以打電話外賣自取，唔使排隊","叫「腩仔」係燒肉中最靚嘅部位","星期日通常休息，留意","只收現金，帶定錢"],"nearby":"柴灣有羅屋民俗館、柴灣公園、鯉魚門渡假村。搭地鐵去筲箕灣可以轉車去石澳或者龍脊行山。","query_name":"新桂香燒臘"},
  {"slug":"food-tim-ho-wan-ssp","emoji":"\U0001f95f","name":"添好運 (深水埗)","lat":22.329,"lng":114.161,"hero_img":"https://images.unsplash.com/photo-1563241529-3005b030e8a8?auto=format&fit=crop&w=1200&q=80","og_title":"添好運 · 深水埗最平米芝蓮一星 | SunnyHK 美食攻略","og_desc":"全世界最平嘅米芝蓮星級餐廳！酥皮叉燒包係招牌，外酥內軟，叉燒餡香甜。馬拉糕、蝦餃、糯米雞全部水準之上。","desc_para1":"添好運係「全世界最平嘅米芝蓮星級餐廳」，創辦人梁輝強師傅係前四季酒店龍景軒嘅點心主管。2009年開業，短短幾個月就獲得米芝蓮一星，創下紀錄。深水埗總店最有風味，日日排長龍。","desc_para2":"招牌酥皮焗叉燒包係添好運嘅代表作——將叉燒包嘅餡料放入菠蘿包皮入面焗製，外層酥脆、內餡香甜。日賣過千個，即叫即焗。除咗叉燒包，馬拉糕、蝦餃、賽螃蟹春卷、糯米雞都係水準之作。","desc_para3":"雖然係米芝蓮星級餐廳，但添好運嘅裝修樸實，價錢大眾化，人均$60-100就食到米芝蓮級點心。即叫即蒸，新鮮熱辣。係香港人同遊客都喜愛嘅飲茶選擇。","transport":"🚇 港鐵深水埗站B2出口，沿北河街行約5分鐘，喺福榮街交界就見到。","dishes":[{"name":"酥皮焗叉燒包","desc":"添好運嘅神級招牌！酥皮菠蘿包皮包住香甜叉燒餡，外酥內軟，一咬就爆餡。日賣過千個。"},{"name":"賽螃蟹春卷","desc":"春卷皮炸得金黃酥脆，入面係滑溜嘅賽螃蟹餡。外脆內軟，口感層次豐富。"},{"name":"馬拉糕","desc":"傳統做法，蒸得鬆軟彈牙，甜度適中。蜂巢結構完美，係香港最好食嘅馬拉糕之一。"},{"name":"晶瑩蝦餃","desc":"蝦餃皮薄得嚟有韌性，蝦肉大粒爽脆。即叫即蒸，新鮮熱辣。"}],"price_range":"$60-100","price_detail":"酥皮叉燒包 $28/3個 · 蝦餃 $32 · 馬拉糕 $22 · 茶錢 $3/位","tips":["朝早10點前到最少人，11點後開始排長龍","酥皮叉燒包出爐時間：11am、1pm、3pm","可以外賣酥皮叉燒包，唔使排隊等位","深水埗總店質素最穩定，分店有啲唔同","馬拉糕經常早早就賣晒，建議叫定","茶錢$3/位，可以自己揀鐵觀音、普洱、香片"],"nearby":"深水埗有合益泰腸粉、公和荳品廠、文記車仔麵、鴨寮街。仲有黃金電腦商場同荔枝角公園。","query_name":"添好運"},
  {"slug":"food-lin-heung","emoji":"\U0001fad6","name":"蓮香樓","lat":22.286,"lng":114.151,"hero_img":"https://images.unsplash.com/photo-1574227492706-f65b24c3688a?auto=format&fit=crop&w=1200&q=80","og_title":"蓮香樓 · 中環百年推車點心 | SunnyHK 美食攻略","og_desc":"中環百年茶樓，保留推車仔點心傳統！蝦餃、燒賣、牛肉球、馬拉糕，樣樣都係老師傅手勢。香港飲茶文化嘅活化石。","desc_para1":"蓮香樓係中環嘅百年老字號茶樓，創立於1927年。到今日仍然保留著最傳統嘅推車仔點心——姐姐推住點心車喺大堂穿梭，你想食咩就自己拎。呢種舊式飲茶體驗喺香港已經買少見少，蓮香樓係碩果僅存嘅代表。","desc_para2":"蓮香樓嘅點心全部係老師傅每日新鮮手製，蝦餃皮薄餡靚、燒賣肉汁豐富、鵪鶉蛋燒賣經典懷舊、蓮蓉包香甜軟滑。茶盅泡茶係另一個傳統——用蓋碗自己沖茶，飲完可以打開蓋叫伙記加熱水。","desc_para3":"環境方面，蓮香樓保留住八九十年代嘅老式茶樓裝修：圓枱、吊扇、舊式地磚、字畫掛牆。食客有老街坊、有遊客、有一個人嚟飲茶睇報纸嘅伯伯。呢種氛圍係香港飲茶文化嘅活化石，值得每個人體驗一次。","transport":"🚇 港鐵上環站E2出口，沿德輔道中行約5分鐘，喺威靈頓街交界就見到。或者中環站D2出口行8分鐘。","dishes":[{"name":"鵪鶉蛋燒賣","desc":"經典懷舊點心，燒賣上面放咗一隻鵪鶉蛋。蛋香同豬肉餡完美結合，係蓮香樓嘅招牌之一。"},{"name":"蓮蓉包","desc":"蓮香樓自家製作嘅蓮蓉包，蓮蓉香甜幼滑，包身軟熟。係必食嘅傳統點心。"},{"name":"馬拉糕","desc":"蒸得鬆軟彈牙，甜度適中。蜂巢結構完美，係老師傅嘅手藝。"},{"name":"蝦餃","desc":"皮薄餡靚，蝦肉大粒爽脆。新鮮即蒸，係飲茶必點嘅經典點心。"}],"price_range":"$80-120","price_detail":"點心 $25-45/籠 · 茶錢 $8/位 · 人均 $80-120","tips":["朝早7點到9點最安靜，可以慢慢嘆茶","點心車出嘅點心要搶，見到中意嘅就舉手","茶盅泡茶：第一次倒茶係洗杯，唔好飲","老伙記有啲脾氣，但其實好 nice","下午2點後有啲點心會賣晒","枱布下有膠枱布，食到成枱都係都唔怕"],"nearby":"中環附近有大館、PMQ元創方、半山扶手電梯、蘭桂坊。行遠啲可以去太平山頂睇夜景。","query_name":"蓮香樓"},
  {"slug":"food-luk-yu","emoji":"\U0001f962","name":"陸羽茶室","lat":22.281,"lng":114.156,"hero_img":"https://images.unsplash.com/photo-1516893676001-52fdf7605797?auto=format&fit=crop&w=1200&q=80","og_title":"陸羽茶室 · 中環古色古香老茶樓 | SunnyHK 美食攻略","og_desc":"中環另一間老字號，裝修古色古香。豬肝燒賣、杏汁白肺湯係招牌。價錢比蓮香樓貴，但環境同服務都高一班。","desc_para1":"陸羽茶室係中環另一間傳奇老字號茶樓，創立於1933年。相比蓮香樓嘅熱鬧喧囂，陸羽茶室更加古雅安靜，裝修用咗大量酸枝傢俬、字畫同古董，充滿民國時期嘅文人氣息。","desc_para2":"陸羽茶室嘅點心同菜式比一般茶樓精緻，招牌豬肝燒賣係全港獨有——用新鮮豬肝製成，口感獨特。杏汁白肺湯清甜滋潤，係佢哋嘅另一代表作。灌湯餃、炸蟹鉗、糯米雞，樣樣都係老師傅嘅手藝。","desc_para3":"服務方面，陸羽嘅伙記著白色制服，服務專業有禮，同老式茶樓嘅粗獷風格好唔同。價錢自然比蓮香樓貴一截，但環境同食物質素都高一班。係宴請長輩或者想體驗老香港高雅一面嘅好選擇。","transport":"🚇 港鐵中環站D2出口，沿德己立街行約5分鐘，喺士丹利街交界就見到。","dishes":[{"name":"豬肝燒賣","desc":"陸羽招牌點心，用新鮮豬肝製成，口感粉嫩獨特。係全港獨有嘅經典懷舊點心，每日限量。"},{"name":"杏汁白肺湯","desc":"清甜滋潤嘅燉湯，用杏仁、豬肺、瘦肉燉製。湯頭清甜，杏仁味香濃，滋潤養顏。"},{"name":"灌湯餃","desc":"傳統灌湯餃，餃皮薄而韌，入面包住鮮味湯汁。一咬落去湯汁四溢，鮮味十足。"},{"name":"炸蟹鉗","desc":"蝦膠釀蟹鉗炸至金黃，外脆內彈牙。係陸羽嘅經典宴客菜式。"}],"price_range":"$150-250","price_detail":"點心 $40-80/籠 · 燉湯 $80-120 · 茶錢 $15/位","tips":["豬肝燒賣每日限量，建議朝早去","陸羽嘅杏汁白肺湯冬天最受歡迎","可以叫一盅兩件，一個人飲茶都可以","裝修行古色古香，適合影相打卡","星期日同公眾假期要加一","有一人茶餐，$150左右有齊點心燉湯"],"nearby":"中環附近有大館、PMQ元創方、半山扶手電梯、蘭桂坊。行遠啲可以去太平山頂睇夜景。","query_name":"陸羽茶室"},
  {"slug":"food-kai-kai-dessert","emoji":"\U0001f36e","name":"佳佳甜品","lat":22.307,"lng":114.170,"hero_img":"https://images.unsplash.com/photo-1504664911901-2518a8bfc164?auto=format&fit=crop&w=1200&q=80","og_title":"佳佳甜品 · 佐敦米芝蓮甜品 | SunnyHK 美食攻略","og_desc":"佐敦米芝蓮甜品店！芝麻糊香濃幼滑，合桃露、杏仁露都係即磨。最正係湯圓，皮薄餡靚。","desc_para1":"佳佳甜品係佐敦嘅米芝蓮必比登甜品店，連續九年獲得推薦。1979年創立，由街坊糖水舖做到今日國際知名嘅甜品名店。佢哋嘅芝麻糊香濃幼滑，合桃露、杏仁露都係即磨，真材實料。","desc_para2":"最正嘅係寧波湯圓，皮薄餡靚，芝麻餡香甜流心。薑汁湯圓就更加暖胃驅寒，冬天食一碗成個人都暖晒。佳佳嘅所有糖水都係每日新鮮製作，唔用罐頭或者現成貨，呢份堅持係佢哋成功嘅關鍵。","desc_para3":"舖頭裝修樸實，長期深夜都有人排隊。由中午12點開到凌晨1點，無論係飯後甜品定宵夜都啱。$25-40就食到米芝蓮級糖水，性價比極高。係香港人同遊客都喜愛嘅甜品店。","transport":"🚇 港鐵佐敦站C2出口，沿寧波街行約5分鐘。或者柯士甸站F出口行8分鐘。","dishes":[{"name":"芝麻糊","desc":"招牌芝麻糊，每日即磨，香濃幼滑。芝麻味濃郁，口感細膩如絲，係全港最好食嘅芝麻糊之一。"},{"name":"寧波湯圓","desc":"皮薄餡靚嘅寧波湯圓，芝麻餡香甜流心。可以配薑汁或者芝麻糊一齊食，暖胃驅寒。"},{"name":"合桃露","desc":"即磨合桃露，合桃味香濃，口感濃稠順滑。加湯圓一齊食更滿足。"},{"name":"楊枝甘露","desc":"經典港式甜品，芒果香甜、柚子清新、椰汁濃郁。夏天食清爽開胃。"}],"price_range":"$25-40","price_detail":"芝麻糊 $25 · 湯圓 $28 · 合桃露 $30 · 楊枝甘露 $35","tips":["中午12點開門就去最少人，夜晚排到出街","芝麻糊加湯圓係最經典嘅食法","冬天有番薯糖水同湯圓，暖胃驅寒","夏天必試楊枝甘露，清爽好食","只收現金，記住帶錢","可以外賣，但堂食嘅碗靚啲"],"nearby":"佐敦有廟街夜市、澳洲牛奶公司、九龍公園、玉器市場。行遠啲可以去尖沙咀海旁。","query_name":"佳佳甜品"},
  {"slug":"food-chung-so","emoji":"\U0001f368","name":"聰嫂甜品","lat":22.280,"lng":114.185,"hero_img":"https://images.unsplash.com/photo-1653923302062-9fb10f6f3d8f?auto=format&fit=crop&w=1200&q=80","og_title":"聰嫂甜品 · 銅鑼灣人氣水果甜品 | SunnyHK 美食攻略","og_desc":"將軍澳同銅鑼灣人氣甜品店。龍眼椰果冰、榴槤水晶珠係招牌。水果新鮮，冰品口感細膩。","desc_para1":"聰嫂甜品係香港人氣甜品店，喺銅鑼灣同將軍澳都有分店。以新鮮水果甜品聞名，龍眼椰果冰同榴槤水晶珠係招牌。佢哋嘅甜品唔單止好食，仲好靚，每一碗都係藝術品。","desc_para2":"聰嫂嘅龍眼椰果冰係夏天必食——龍眼肉新鮮清甜，配搭爽口椰果同冰沙，口感層次豐富。榴槤水晶珠更加係榴槤控嘅天堂，用新鮮榴槤肉打成冰沙，加上晶瑩剔透嘅水晶珠，榴槤味濃郁到爆。","desc_para3":"除咗招牌甜品，聰嫂仲有好多創新款式：芒果黑糯米、雜果涼粉、木糠布甸，樣樣都用心製作。甜品賣相精緻，打卡一流。係年輕人同遊客嘅熱門甜品店。","transport":"🚇 銅鑼灣站B出口，沿羅素街行約5分鐘，喺時代廣場附近。將軍澳分店：將軍澳站A出口，PopCorn商場。","dishes":[{"name":"龍眼椰果冰","desc":"招牌甜品！龍眼肉新鮮清甜，配爽口椰果同冰沙。口感清爽，夏天食最佳。"},{"name":"榴槤水晶珠","desc":"榴槤控必試！新鮮榴槤肉打成冰沙，加上晶瑩水晶珠。榴槤味濃郁到爆。"},{"name":"芒果黑糯米","desc":"芒果香甜，黑糯米煙韌有嚼勁，配椰汁一齊食。係經典港式甜品嘅代表。"},{"name":"雜果涼粉","desc":"多種新鮮生果配滑溜涼粉，清爽消暑。夏天必食。"}],"price_range":"$30-50","price_detail":"龍眼椰果冰 $38 · 榴槤水晶珠 $48 · 芒果黑糯米 $35 · 雜果涼粉 $32","tips":["銅鑼灣店夜晚好多人，建議下午去","龍眼椰果冰係夏天限定，冬天未必有","榴槤味濃郁，唔食榴槤嘅人可以揀其他","可以叫少甜，香港甜品普遍偏甜","有最低消費每人一款甜品","只收現金同八達通"],"nearby":"銅鑼灣有時光廣場、希慎廣場、維多利亞公園。食完可以行去維園散步或者去銅鑼灣海旁。","query_name":"聰嫂甜品"},
  {"slug":"food-tai-leung","emoji":"\U0001f963","name":"大良八記","lat":22.318,"lng":114.170,"hero_img":"https://images.unsplash.com/photo-1543342570-d7c19e5af14b?auto=format&fit=crop&w=1200&q=80","og_title":"大良八記 · 旺角老牌即磨糖水 | SunnyHK 美食攻略","og_desc":"旺角老牌糖水舖，芝麻糊、合桃露、杏仁露全部即磨。口感濃稠，真材實料。冬天番薯糖水同湯丸都好正。","desc_para1":"大良八記係旺角嘅老牌糖水舖，以即磨芝麻糊、合桃露、杏仁露聞名。所有糊類糖水都係每日新鮮即磨，口感濃稠順滑，真材實料。冬天仲有番薯糖水同湯丸，暖胃驅寒。","desc_para2":"大良八記嘅芝麻糊係全港數一數二——用優質黑芝麻慢火炒香再石磨，香氣四溢。合桃露同杏仁露都係同樣用心製作，每一碗都係師傅嘅心血。佢哋嘅湯丸同樣出色，皮薄餡靚，芝麻餡流心。","desc_para3":"舖頭裝修簡單樸實，冇花巧嘅裝飾，靠嘅係真材實料同幾十年嘅口碑。$20-35就食到一碗即磨糖水，價錢大眾化，係旺角街坊嘅飯後甜品首選。","transport":"🚇 港鐵旺角站E2出口，沿西洋菜南街行約5分鐘。或者旺角東站行過去都係10分鐘。","dishes":[{"name":"芝麻糊","desc":"招牌即磨芝麻糊，香濃幼滑。用優質黑芝麻炒香再石磨，芝麻味濃郁，口感細膩。"},{"name":"合桃露","desc":"即磨合桃露，合桃味香濃，口感濃稠順滑。養顏滋潤，係女仔最愛。"},{"name":"杏仁露","desc":"杏仁味香濃、口感順滑。用南北杏混合研磨，味道層次豐富。"},{"name":"番薯糖水","desc":"冬天限定，番薯煲得軟腍，糖水清甜暖胃。加湯丸一齊食更滿足。"}],"price_range":"$20-35","price_detail":"芝麻糊 $22 · 合桃露 $25 · 杏仁露 $22 · 番薯糖水 $20","tips":["芝麻糊最出名，第一次去必試","可以叫「雙拼」—芝麻糊溝合桃露","冬天番薯糖水加湯丸係 perfect match","糖水可以外賣，但堂食質感更好","旺角店夜晚好多人，建議下午去","只收現金，帶定散銀"],"nearby":"旺角有女人街、波鞋街、金魚街、朗豪坊。附近仲有油麻地廟街夜市同果欄。","query_name":"大良八記"},
  {"slug":"food-chan-kan-kee","emoji":"\U0001f962","name":"陳勤記","lat":22.287,"lng":114.150,"hero_img":"https://images.unsplash.com/photo-1582234372722-50d7ccc30ebd?auto=format&fit=crop&w=1200&q=80","og_title":"陳勤記 · 上環米芝蓮必比登潮州菜 | SunnyHK 美食攻略","og_desc":"上環米芝蓮必比登潮州菜！蠔仔粥鮮甜足料，滷水拼盤入味，蠔餅外脆內軟。正宗潮州家鄉風味。","desc_para1":"陳勤記係上環嘅米芝蓮必比登潮州菜館，1948年創立，三代傳承、70年滷水膽。佢哋嘅滷水鵝用獅頭鵝，肉嫩入味，滷水汁香濃複雜。蠔仔粥用大地魚湯底，鮮甜足料。蠔餅外脆內軟，係正宗潮州家鄉風味。","desc_para2":"老闆同伙記都係潮州人，對食材同味道嘅要求好嚴格。滷水膽係陳勤記嘅靈魂——經過70年不斷添加同熬煮，味道層次豐富到難以複製。滷水鵝片、滷水豆腐、滷水蛋，樣樣都入味到極致。","desc_para3":"環境係典型嘅中式酒樓格局，樸實企理。價格喺潮州菜館中屬中等水平，人均$100-200就食到正宗潮州菜。連續多年獲得米芝蓮必比登推薦，係香港食潮州菜嘅首選之一。","transport":"🚇 港鐵上環站A2出口，沿永樂街行約8分鐘，喺文咸東街交界就見到。","dishes":[{"name":"滷水鵝片","desc":"陳勤記招牌菜！用獅頭鵝，肉嫩入味。70年滷水膽嘅味道層次豐富，鵝肉嫩滑。必點！"},{"name":"蠔仔肉碎粥","desc":"大地魚湯底鮮甜，蠔仔新鮮飽滿，肉碎增添口感。食完一碗仲想食多碗。"},{"name":"蠔餅","desc":"即叫即炸，外脆內軟。蠔仔新鮮，鴨蛋同薯粉嘅比例完美。點魚露食最正宗。"},{"name":"滷水拼盤","desc":"一次過試晒鵝片、豆腐、蛋、豬大腸。滷水汁香濃，每樣都入味。適合兩個人share。"}],"price_range":"$100-200","price_detail":"滷水鵝片 $98 · 蠔仔粥 $68 · 蠔餅 $58 · 滷水拼盤 $88","tips":["晚市6點後最旺，建議平日中午去","蠔仔粥可以叫一人份量，唔使叫一大鍋","滷水鵝片+蠔仔粥+蠔餅係經典組合","可以買外賣滷水鵝返屋企慢慢食","加$20可以轉鵝髀，肉質更嫩","星期日休息，留意"],"nearby":"上環有海味街、文武廟、摩羅上街古董街、PMQ元創方。行遠啲可以去中環蘭桂坊同大館。","query_name":"陳勤記"},
  {"slug":"food-sheung-hing","emoji":"\U0001f9aa","name":"尚興潮州飯店","lat":22.287,"lng":114.151,"hero_img":"https://images.unsplash.com/photo-1582234372722-50d7ccc30ebd?auto=format&fit=crop&w=1200&q=80","og_title":"尚興潮州飯店 · 上環精緻潮州菜 | SunnyHK 美食攻略","og_desc":"上環另一潮州名店，凍蟹、蠔仔烙、胡椒豬肚湯做得精緻。環境比陳勤記好啲，適合宴客。","desc_para1":"尚興潮州飯店係上環另一間潮州菜名店，環境比陳勤記精緻，適合宴客同家庭聚會。佢哋嘅潮州菜做得細膩精緻，凍蟹、蠔仔烙、胡椒豬肚湯都係招牌，每道菜都展現出潮州菜嘅精粹。","desc_para2":"尚興嘅凍蟹係必試菜式——用新鮮花蟹凍食，蟹肉鮮甜彈牙，配薑醋汁一食，鮮味突出。蠔仔烙用鴨蛋煎得金黃香脆，蠔仔新鮮飽滿。胡椒豬肚湯暖胃驅寒，胡椒味香濃但不嗆喉。","desc_para3":"服務方面，尚興嘅伙記專業有禮，會細心介紹菜式同建議份量。環境雅致，有古式傢俬同字畫裝飾。價錢比陳勤記高一截，但物有所值。如果想帶屋企人或者朋友食一餐正宗潮州菜，尚興係好選擇。","transport":"🚇 港鐵上環站A2出口，沿永樂街行約8分鐘，喺文咸東街附近。","dishes":[{"name":"凍蟹","desc":"尚興招牌！用新鮮花蟹凍食，蟹肉鮮甜彈牙。配薑醋汁一食，鮮味更加突出。要預訂。"},{"name":"蠔仔烙","desc":"用鴨蛋煎得金黃香脆，蠔仔新鮮飽滿。外脆內軟，點魚露食最正宗。"},{"name":"胡椒豬肚湯","desc":"豬肚洗得乾淨，湯頭乳白色。胡椒味香濃但不嗆喉，暖胃驅寒，冬天必飲。"},{"name":"滷水鵝","desc":"獅頭鵝滷得入味，肉質嫩滑。滷水汁香濃複雜，係潮州菜嘅經典代表。"}],"price_range":"$200-400","price_detail":"凍蟹 $300-500（時價）· 蠔仔烙 $78 · 滷水鵝 $128 · 胡椒豬肚湯 $88","tips":["凍蟹要預訂，唔係成日有貨","叫菜嘅時候可以問伙計份量建議","蠔仔烙建議叫細份，太大份會膩","胡椒豬肚湯可以加$20轉胡椒豬肚雞","適合宴客，有廂房可以訂","價錢偏高，建議睇Menu先決定"],"nearby":"上環有海味街、文武廟、摩羅上街古董街、PMQ元創方。行遠啲可以去中環。","query_name":"尚興潮州飯店"},
  {"slug":"food-man-kei","emoji":"\U0001f35c","name":"文記車仔麵","lat":22.331,"lng":114.162,"hero_img":"https://images.unsplash.com/photo-1651658313775-90bf2751913e?auto=format&fit=crop&w=1200&q=80","og_title":"文記車仔麵 · 深水埗車仔麵之王 | SunnyHK 美食攻略","og_desc":"深水埗車仔麵之王！三餸麵$30起，選擇超過50款餸：蘿蔔、豬腸、魚肉春卷、瑞士雞翼。湯底有三種。","desc_para1":"文記車仔麵係深水埗嘅車仔麵之王，永遠排長龍。三餸麵$30起，選擇超過50款餸菜：蘿蔔清甜無渣、豬腸洗得乾淨滷得入味、魚肉春卷彈牙、瑞士雞翼香甜入味。湯底有三種：清湯、辣汁、咖喱，各有特色。","desc_para2":"文記嘅蘿蔔係全港數一數二——清甜無渣，滷得入味，入口即溶。豬腸處理得非常乾淨，滷水汁香濃。瑞士雞翼用瑞士汁慢煮，香甜入味，骨肉分離。魚肉春卷彈牙有魚味，係即叫即炸。","desc_para3":"雖然長期排隊，但因為車仔麵上得快，等10-15分鐘就搞掂。湯底濃郁，餸菜新鮮，價錢大眾化，係深水埗街坊同學生嘅最愛。十幾年嚟水準穩定，OpenRice長期高分。","transport":"🚇 港鐵深水埗站A2出口，沿福榮街行約3分鐘。或者深水埗站B2出口行5分鐘。","dishes":[{"name":"蘿蔔","desc":"文記招牌餸！清甜無渣，滷得入味，入口即溶。係全港數一數二嘅車仔麵蘿蔔，必點！"},{"name":"豬腸","desc":"豬腸處理得非常乾淨，滷水汁香濃入味。口感軟腍彈牙，係車仔麵嘅經典配料。"},{"name":"瑞士雞翼","desc":"用瑞士汁慢煮，香甜入味，骨肉分離。雞肉嫩滑，醬汁濃郁。"},{"name":"魚肉春卷","desc":"即叫即炸，彈牙有魚味。外皮金黃酥脆，係文記嘅人氣餸菜。"}],"price_range":"$30-60","price_detail":"三餸麵 $30 · 五餸麵 $38 · 加餸 $6-10/款 · 汽水+$6","tips":["平日下晝3點少人啲，唔使排咁耐","蘿蔔+豬腸+瑞士雞翼係經典組合","湯底推薦咖喱湯，香濃好味","可以叫「汁撈」—湯麵走湯加腩汁","辣汁好辣，唔食得辣嘅可以叫小辣","只收現金，帶定錢"],"nearby":"深水埗有合益泰腸粉、公和荳品廠、添好運、十八座狗仔粉。仲有黃金電腦商場同鴨寮街。","query_name":"文記車仔麵"},
  {"slug":"food-wing-kei","emoji":"\U0001f372","name":"榮記車仔麵","lat":22.280,"lng":114.185,"hero_img":"https://images.unsplash.com/photo-1550396790-1502488d7fde?auto=format&fit=crop&w=1200&q=80","og_title":"榮記車仔麵 · 銅鑼灣濃湯車仔麵 | SunnyHK 美食攻略","og_desc":"銅鑼灣糖街人氣車仔麵，湯底濃郁，配料豐富。蘿蔔入味、豬紅彈牙、牛肚軟腍。宵夜時段都排長龍。","desc_para1":"榮記車仔麵係銅鑼灣糖街嘅人氣車仔麵店，以濃郁湯底聞名。佢哋嘅湯底用牛腩、豬骨同多種香料熬製，味道濃厚。配料豐富：蘿蔔入味、豬紅彈牙、牛肚軟腍，每樣都係心機之作。","desc_para2":"榮記嘅湯底係佢哋嘅靈魂——用牛腩同豬骨熬足幾個鐘，加埋秘製香料，湯色深濃、味道豐富。蘿蔔滷得入味清甜，豬紅彈牙有口感，牛肚軟腍入味。每樣配料都處理得好仔細。","desc_para3":"舖頭細細，但人氣旺盛，即使宵夜時段都排長龍。銅鑼灣區嘅街坊同遊客都鍾意嚟幫襯。價錢公道，人均$40-70就食到一碗豐富嘅車仔麵。係銅鑼灣掃街嘅必經站。","transport":"🚇 港鐵銅鑼灣站E出口，沿記利佐治街行去糖街約5分鐘。","dishes":[{"name":"蘿蔔","desc":"榮記招牌餸！滷得入味清甜，入口即溶。係榮記最好食嘅配料之一，必點。"},{"name":"豬紅","desc":"豬紅彈牙有口感，滷水汁入味。係車仔麵嘅經典配料。"},{"name":"牛肚","desc":"牛肚軟腍入味，滷得夠淋。口感豐富，係榮記嘅人氣餸菜。"},{"name":"瑞士雞翼","desc":"瑞士汁慢煮，香甜入味。雞肉嫩滑，醬汁濃郁。"}],"price_range":"$40-70","price_detail":"三餸麵 $35 · 五餸麵 $45 · 加餸 $7-12/款 · 凍飲+$5","tips":["宵夜時段（10pm後）少人啲","湯底係靈魂，推薦腩汁湯底","豬紅係限量，好快賣晒","加$10可以轉大碗，份量更多","銅鑼灣店得十幾個位，建議外賣","可以WhatsApp落單外賣自取"],"nearby":"銅鑼灣有時光廣場、希慎廣場、維多利亞公園。食完可以行去維園散步或者去銅鑼灣海旁。","query_name":"榮記車仔麵"},
  {"slug":"food-kwan-kee","emoji":"\U0001f35a","name":"坤記煲仔小菜","lat":22.287,"lng":114.143,"hero_img":"https://images.unsplash.com/photo-1549212408-d6b0defe25cf?auto=format&fit=crop&w=1200&q=80","og_title":"坤記煲仔小菜 · 西環煲仔飯天花板 | SunnyHK 美食攻略","og_desc":"西環煲仔飯嘅天花板！白鱔煲仔飯同臘味煲仔飯係招牌，飯焦香脆，豉油係靈魂。煲仔小菜都好出色。","desc_para1":"坤記煲仔小菜係西環煲仔飯嘅天花板，米芝蓮必比登推介。佢哋嘅煲仔飯用炭火明爐即叫即製，飯焦金黃香脆可以原塊刮起，米飯乾爽甘香。白鱔煲仔飯同臘味煲仔飯係招牌，一開蓋滋滋聲，淋上甜豉油蓋住焗一分鐘——人間美味。","desc_para2":"坤記嘅白鱔煲仔飯係必食——白鱔新鮮肥美，魚油滲入飯中，加埋飯焦一齊食，口感豐富。臘味煲仔飯用優質臘腸、潤腸同臘肉，臘味嘅油香滲透每一粒飯。煲仔小菜同樣出色，豉椒炒蜆、椒鹽鮮魷都好受歡迎。","desc_para3":"秋冬夜晚，坤記門外永遠排長龍。寒風中聞住炭火煲仔飯嘅香氣，係香港冬天最溫暖嘅畫面。舖頭細細，坐位逼啲，但正正係呢種街坊大牌檔嘅氛圍先最吸引。","transport":"🚇 港鐵西營盤站A1出口，沿皇后大道西行約8分鐘。或者搭電車喺西環屈地街落車。","dishes":[{"name":"白鱔煲仔飯","desc":"坤記招牌！白鱔新鮮肥美，魚油滲入飯中。飯焦金黃香脆，加甜豉油焗一分鐘，人間美味。"},{"name":"臘味煲仔飯","desc":"優質臘腸、潤腸同臘肉，臘味油香滲透每一粒飯。飯焦香脆，係冬天必食。"},{"name":"滑雞煲仔飯","desc":"雞肉嫩滑多汁，飯焦香脆。簡單但係經典嘅煲仔飯口味。"},{"name":"豉椒炒蜆","desc":"新鮮蜆肉配上豆豉同辣椒炒香，惹味好食。係煲仔飯嘅最佳拍檔。"}],"price_range":"$80-150","price_detail":"白鱔煲仔飯 $98 · 臘味煲仔飯 $78 · 滑雞煲仔飯 $68 · 小菜 $60-120","tips":["秋冬最正，但夜晚排到癲，建議6點前去到","煲仔飯要等20-30分鐘，即叫即製","加甜豉油之後蓋住焗一分鐘先食","飯焦係精華，可以用匙羹刮出嚟食","煲仔小菜都好出色，可以叫一兩碟share","建議提早打電話訂位"],"nearby":"西環有西環碼頭、西環泳棚、石塘嘴街市。行遠啲可以去堅尼地城海旁睇日落。","query_name":"坤記煲仔小菜"},
  {"slug":"food-hing-kee","emoji":"\U0001f35a","name":"興記煲仔飯","lat":22.305,"lng":114.169,"hero_img":"https://images.unsplash.com/photo-1529692236675-6b5097e14b01?auto=format&fit=crop&w=1200&q=80","og_title":"興記煲仔飯 · 廟街炭火煲仔飯 | SunnyHK 美食攻略","og_desc":"廟街煲仔飯嘅代表！夜晚廟街成條街都係興記嘅煲仔飯，炭火明爐即叫即製。臘味、滑雞、田雞，每款$50起。","desc_para1":"興記煲仔飯係廟街煲仔飯嘅代表，夜晚廟街成條街都係興記嘅煲仔飯檔口，炭火明爐即叫即製，場面壯觀。臘味煲仔飯、滑雞煲仔飯、田雞煲仔飯，每款$50起，價錢大眾化。","desc_para2":"興記用傳統炭火爐燒煲仔飯，炭火嘅香氣係煤氣爐做唔到嘅。飯焦香脆，米飯乾爽。豉油係靈魂——佢哋嘅甜豉油係自家調配，淋上熱辣辣嘅煲仔飯，滋滋聲令人食慾大增。","desc_para3":"廟街夜晚嘅氣氛係興記嘅最佳調味料——霓虹燈、大牌檔、人聲鼎沸，係最地道嘅香港夜市體驗。坐喺街邊食一煲熱辣辣嘅煲仔飯，再加一碟椒鹽鮮魷，就係香港人嘅宵夜天堂。","transport":"🚇 港鐵佐敦站A出口，沿廟街行約5分鐘。或者油麻地站C出口行8分鐘。","dishes":[{"name":"臘味煲仔飯","desc":"經典煲仔飯，臘腸、潤腸、臘肉嘅油香滲入飯中。飯焦香脆，係興記嘅招牌。"},{"name":"滑雞煲仔飯","desc":"雞肉嫩滑多汁，飯焦金黃香脆。簡單但係經典嘅口味。"},{"name":"田雞煲仔飯","desc":"田雞肉嫩滑，味道鮮甜。係老饕先識叫嘅隱藏美味。"},{"name":"椒鹽鮮魷","desc":"即炸鮮魷，外脆內彈牙。椒鹽味香濃，係煲仔飯嘅最佳小菜。"}],"price_range":"$50-80","price_detail":"煲仔飯 $50-70 · 椒鹽鮮魷 $45 · 油菜 $20","tips":["夜晚廟街氣氛一流，但建議7點前去到搵位","煲仔飯要等15-20分鐘，即叫即製","加豉油之後蓋住焗一陣先食","可以加$10轉臘腸，更好味","廟街夜晚熱鬧，但注意財物","只收現金，廟街好多檔都係"],"nearby":"廟街附近有油麻地果欄、百老匯電影中心、玉器市場。行遠啲可以去佐敦海旁。","query_name":"興記煲仔飯"},
  {"slug":"food-bridge-bottom","emoji":"\U0001f990","name":"橋底辣蟹","lat":22.276,"lng":114.174,"hero_img":"https://images.unsplash.com/photo-1574227492706-f65b24c3688a?auto=format&fit=crop&w=1200&q=80","og_title":"橋底辣蟹 · 灣仔避風塘炒蟹 | SunnyHK 美食攻略","og_desc":"灣仔橋底辣蟹聞名中外，避風塘炒蟹辣得過癮！大量炸蒜配辣椒炒到香噴噴，蟹肉鮮甜。仲有瀨尿蝦、炒蜆。","desc_para1":"橋底辣蟹係灣仔嘅傳奇海鮮餐廳，以避風塘炒蟹聞名中外。大量炸蒜配辣椒炒到金黃香噴噴，蟹肉鮮甜彈牙，辣得過癮。來自世界各地嘅遊客都專程嚟食，係香港必食嘅海鮮體驗之一。","desc_para2":"雖然叫橋底辣蟹，但其實佢哋嘅避風塘瀨尿蝦同炒蜆都好出色。瀨尿蝦超大隻，椒鹽做法外脆內嫩。炒蜆用豉椒炒，新鮮好食。避風塘嘅炸蒜係靈魂——金黃酥脆，蒜香濃郁，撈飯食一流。","desc_para3":"餐廳環境普通，係典型嘅港式海鮮酒家格局。伙記服務專業，會幫你揀蟹同建議煮法。價錢唔平，但物有所值。一大班人嚟食最開心，叫幾隻蟹、一碟瀨尿蝦、幾碟小菜，啤一啤，就係完美嘅香港夜晚。","transport":"🚇 港鐵灣仔站A4出口，沿莊士敦道行約8分鐘，喺橋底附近。","dishes":[{"name":"避風塘炒蟹","desc":"橋底鎮店之寶！大量炸蒜配辣椒炒到金黃香噴噴，蟹肉鮮甜彈牙。辣度可以揀，推薦中辣。"},{"name":"椒鹽瀨尿蝦","desc":"超大隻瀨尿蝦，椒鹽做法外脆內嫩。蝦肉鮮甜彈牙，係橋底另一招牌。"},{"name":"豉椒炒蜆","desc":"新鮮蜆肉配上豆豉辣椒炒香，惹味好食。係海鮮餐嘅經典小菜。"},{"name":"蒜蓉蒸開邊蝦","desc":"開邊蝦鋪滿蒜蓉蒸熟，蝦肉鮮甜，蒜香濃郁。簡單但係完美。"}],"price_range":"$200-500","price_detail":"避風塘炒蟹 $200-400（時價）· 瀨尿蝦 $150-300 · 炒蜆 $80 · 白飯 $15","tips":["避風塘炒蟹嘅炸蒜係精華，可以打包返屋企","叫蟹之前先問清楚價錢，時價","可以揀辣度：小辣/中辣/大辣","一大班人嚟食最抵，可以share","夜晚6點後先有得食","泊車唔方便，建議搭地鐵"],"nearby":"灣仔有利東街、太原街玩具街、藍屋建築群。行遠啲可以去金紫荊廣場同會展。","query_name":"橋底辣蟹"},
  {"slug":"food-chuen-kee","emoji":"\U0001f99e","name":"全記海鮮","lat":22.381,"lng":114.274,"hero_img":"https://images.unsplash.com/photo-1574227492706-f65b24c3688a?auto=format&fit=crop&w=1200&q=80","og_title":"全記海鮮 · 西貢即撈即煮海鮮 | SunnyHK 美食攻略","og_desc":"西貢海鮮街嘅代表，自選海鮮即撈即煮。椒鹽瀨尿蝦、豉椒炒蜆、清蒸海上鮮，新鮮到彈牙。西貢碼頭海景伴食。","desc_para1":"全記海鮮係西貢海鮮街嘅代表餐廳，以「自選海鮮即撈即煮」聞名。客人可以喺魚缸揀選新鮮海鮮，指定煮法，師傅即場炮製。椒鹽瀨尿蝦、豉椒炒蜆、清蒸海上鮮，樣樣都新鮮到彈牙。","desc_para2":"全記嘅海鮮選擇好多：龍蝦、瀨尿蝦、蟹、魚、蜆、鮑魚，全部係新鮮運到。最正係可以自己揀——見到邊隻生猛就揀邊隻，然後話俾師傅知你想點煮。清蒸食到原味，椒鹽夠香口，避風塘就夠惹味。","desc_para3":"餐廳位於西貢碼頭旁邊，可以望住海景食海鮮，氣氛一流。假日好多香港人會揸車入西貢，食海鮮、行沙灘、睇日落，係週末最佳行程之一。價錢豐儉由人，由幾百到幾千都得。","transport":"🚇 港鐵鑽石山站轉乘92號巴士，到西貢碼頭落車，行2分鐘。或者喺彩虹站搭1A小巴。","dishes":[{"name":"椒鹽瀨尿蝦","desc":"全記招牌！超大隻瀨尿蝦椒鹽炸香，外脆內嫩。蝦肉鮮甜彈牙，係必點菜式。"},{"name":"清蒸海上鮮","desc":"新鮮靚魚清蒸，食到原汁原味。魚肉嫩滑鮮甜，蒸魚豉油撈飯一流。"},{"name":"豉椒炒蜆","desc":"新鮮蜆肉配上豆豉辣椒炒香，惹味好食。係海鮮餐嘅經典小菜。"},{"name":"芝士龍蝦伊麵","desc":"龍蝦肉鮮甜彈牙，芝士汁濃郁香滑。伊麵索滿芝士汁，邪惡但極好食。"}],"price_range":"$200-400","price_detail":"椒鹽瀨尿蝦 $188 · 清蒸魚 $150-300（時價）· 芝士龍蝦伊麵 $300-500","tips":["揀海鮮前先問清楚價錢，時價海鮮要預算","可以叫套餐，比散叫抵食","假日下午最旺，建議平日去","西貢碼頭可以泊車，但假日好迫","食完可以行西貢海濱長廊睇日落","全記有幾間分店喺同一條街，揀總店最好"],"nearby":"西貢有西貢碼頭、橋咀洲、三星灣沙灘。行遠啲可以去萬宜水庫東壩睇地質奇觀。","query_name":"全記海鮮"},
  {"slug":"food-kau-kee","emoji":"\U0001f35d","name":"九記牛腩","lat":22.284,"lng":114.153,"hero_img":"https://images.unsplash.com/photo-1589977326928-0c4681f1f1d3?auto=format&fit=crop&w=1200&q=80","og_title":"九記牛腩 · 中環傳奇牛腩店 | SunnyHK 美食攻略","og_desc":"中環歌賦街傳奇牛腩店，全香港最好食嘅牛腩！清湯牛爽腩同咖喱牛筋腩係招牌。湯頭濃郁，牛腩軟腍入味。","desc_para1":"九記牛腩係中環歌賦街嘅傳奇牛腩店，被譽為「全香港最好食嘅牛腩」。清湯牛爽腩同咖喱牛筋腩係招牌菜。湯頭用牛骨同多種藥材熬足幾十個鐘，清澈見底但味道濃郁。牛腩軟腍入味，每日賣完就收，絕不添加。","desc_para2":"九記嘅清湯牛爽腩係鎮店之寶——牛爽腩係牛腩中最矜貴嘅部位，筋膜肉三層分明，入口即化。清湯清澈但味道極濃，飲完唔會口渴。咖喱牛筋腩係另一招牌——咖喱汁香濃微辣，牛筋腩軟腍入味，配伊麵或者米粉食一流。","desc_para3":"舖頭細細，坐位逼到不得了，永遠排長龍。伙記快手快腳，食完就要讓位。只收現金，唔設加一，呢種老派作風反而成為九記嘅特色。排隊一個鐘、食麵十分鐘，但人人都話值得。","transport":"🚇 港鐵上環站A2出口，沿禧利街上歌賦街約10分鐘。或者中環站D2出口行12分鐘。","dishes":[{"name":"清湯牛爽腩","desc":"九記鎮店之寶！牛爽腩筋膜肉三層分明，入口即化。清湯清澈但味道極濃，係全港最好食嘅牛腩。"},{"name":"咖喱牛筋腩","desc":"咖喱汁香濃微辣，牛筋腩軟腍入味。配伊麵或者米粉食一流。"},{"name":"淨爽腩","desc":"唔要麵，只要腩同湯。適合想專心食牛腩嘅人。"},{"name":"蠔油撈麵","desc":"麵條彈牙，蠔油汁香濃。簡單但係經典嘅港式撈麵。"}],"price_range":"$60-100","price_detail":"清湯牛爽腩 $85 · 咖喱牛筋腩 $65 · 淨爽腩 $120 · 凍飲+$3","tips":["下晝2點少人啲，避開午市高峰","牛爽腩係限量，好快賣晒","只收現金！隔離冇銀行，記住帶錢","星期日同公眾假期休息","排隊等位時可以諗定食咩，加快落單","湯可以免費加，記得叫伙記加湯"],"nearby":"中環歌賦街附近有PMQ元創方、大館、半山扶手電梯。行遠啲可以去太平山頂。","query_name":"九記牛腩"},
  {"slug":"food-18-seats","emoji":"\U0001f35c","name":"十八座狗仔粉","lat":22.329,"lng":114.161,"hero_img":"https://images.unsplash.com/photo-1629007006355-d75f7b828bfd?auto=format&fit=crop&w=1200&q=80","og_title":"十八座狗仔粉 · 深水埗米芝蓮街頭小食 | SunnyHK 美食攻略","og_desc":"深水埗米芝蓮街頭小食！招牌狗仔粉（傳統銀針粉）、火鴨翅、招牌大雜燴，$20-40就食到米芝蓮水準。","desc_para1":"十八座狗仔粉係深水埗嘅米芝蓮街頭小食店，以傳統狗仔粉（銀針粉）聞名。湯底用金華火腿同豬骨熬足六個鐘，麵條煙韌彈牙。加埋辣菜脯同豬油渣，冬天食一碗暖到入心。","desc_para2":"除咗狗仔粉，十八座嘅火鴨翅同樣出色——用燒鴨殼熬湯，加埋冬菇絲、木耳絲同素翅，濃稠適中、味道鮮美。招牌大雜燴有豬皮、蘿蔔、豬腸、魚蛋等，滷得入味，係掃街必食。","desc_para3":"舖頭細細，坐位有限，但正正係呢種街頭小食店先最有風味。$20-40就食到米芝蓮水準，性價比極高。連續多年米芝蓮必比登推薦，深水埗掃街嘅必經站。","transport":"🚇 港鐵深水埗站D2出口，沿福榮街行約5分鐘。或者深水埗站A2出口行8分鐘。","dishes":[{"name":"招牌狗仔粉","desc":"十八座鎮店之寶！銀針粉煙韌彈牙，湯底用金華火腿同豬骨熬足六個鐘。加辣菜脯同豬油渣更惹味。"},{"name":"火鴨翅","desc":"用燒鴨殼熬湯，加冬菇絲、木耳絲同素翅。濃稠適中，味道鮮美，係狗仔粉嘅最佳拍檔。"},{"name":"招牌大雜燴","desc":"豬皮、蘿蔔、豬腸、魚蛋等滷得入味。份量十足，係掃街必食。"},{"name":"碗仔翅","desc":"傳統港式碗仔翅，落足冬菇絲、仿翅同雞絲。濃稠適中，加胡椒粉同醋食更香。"}],"price_range":"$20-40","price_detail":"狗仔粉 $22 · 火鴨翅 $25 · 大雜燴 $28 · 碗仔翅 $20","tips":["狗仔粉加辣菜脯同豬油渣係最正宗食法","火鴨翅可以叫「撈丁」—撈出前一丁","深水埗總店最有風味，佐敦分店都唔錯","24小時營業，宵夜一流","最少$20就食到米芝蓮，性價比極高","只收現金，帶定錢"],"nearby":"深水埗有公和荳品廠、合益泰腸粉、文記車仔麵、添好運。仲有黃金電腦商場同鴨寮街。","query_name":"十八座狗仔粉"},
  {"slug":"food-islamic-beef","emoji":"\U0001f95f","name":"清真牛肉館","lat":22.327,"lng":114.188,"hero_img":"https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=1200&q=80","og_title":"清真牛肉館 · 九龍城爆汁牛肉餅 | SunnyHK 美食攻略","og_desc":"九龍城嘅傳奇牛肉館！牛肉餅係王牌——皮薄餡靚爆汁，咬開要小心燙嘴。仲有咖喱羊腩同牛肉餃子。","desc_para1":"清真牛肉館係九龍城嘅傳奇餐廳，以牛肉餅聞名全港。佢哋嘅牛肉餅皮薄餡靚，一咬開就爆汁，熱辣辣嘅肉汁噴出嚟，要小心燙嘴。呢個牛肉餅被譽為「全港最好食嘅牛肉餅」，好多區外人都專程入九龍城就係為咗佢。","desc_para2":"除咗牛肉餅，清真牛肉館嘅咖喱羊腩同牛肉餃子都好出色。咖喱汁香濃微辣，羊腩燉得軟腍入味，配飯或者薄餅食一流。牛肉餃子即叫即蒸，皮薄餡靚，牛肉餡鮮味多汁。","desc_para3":"餐廳係清真認證，唔用豬肉，所有菜式都係清真食品。環境樸實企理，伙記服務街坊味濃。九龍城本身係美食集中地，附近仲有好多泰國菜館同地道小食，可以一次過掃街。","transport":"🚇 港鐵宋皇臺站B2出口，沿聯合道行約5分鐘。或者九龍城廣場行5分鐘。","dishes":[{"name":"牛肉餅","desc":"清真牛肉館嘅王牌！皮薄餡靚，一咬爆汁。肉汁鮮甜，牛肉餡調味恰到好處。必點，但要小心燙嘴！"},{"name":"咖喱羊腩","desc":"咖喱汁香濃微辣，羊腩燉得軟腍入味。配白飯或者薄餅食一流，係冬天暖身之選。"},{"name":"牛肉餃子","desc":"即叫即蒸，皮薄餡靚。牛肉餡鮮味多汁，點醋同薑絲食最正。"},{"name":"羊肉串","desc":"孜然羊肉串烤得香噴噴，羊肉嫩滑冇騷味。係睇波或者宵夜嘅最佳小食。"}],"price_range":"$60-100","price_detail":"牛肉餅 $25/個 · 咖喱羊腩 $68 · 牛肉餃子 $42 · 羊肉串 $38","tips":["牛肉餅要小心燙嘴！先咬一小口等散熱","牛肉餅最好趁熱食，放耐咗就唔爆汁","可以叫「牛肉餅+咖喱羊腩飯」經典組合","九龍城好多泰國嘢食，可以一次過食埋","清真認證，唔好帶外來食物入去","假日好多人，建議平日去"],"nearby":"九龍城有九龍寨城公園、九龍城廣場、啟德郵輪碼頭。附近仲有好多泰國菜館同地道小食店。","query_name":"清真牛肉館"},
]

# ====== GENERATE ======
os.makedirs(OUT_DIR, exist_ok=True)
created = []
for r in restaurants:
    html = make_page(
        slug=r["slug"],
        emoji=r["emoji"],
        name=r["name"],
        hero_img=r["hero_img"],
        desc_para1=r["desc_para1"],
        desc_para2=r["desc_para2"],
        desc_para3=r["desc_para3"],
        transport=r["transport"],
        dishes=r["dishes"],
        price_range=r["price_range"],
        price_detail=r["price_detail"],
        tips=r["tips"],
        nearby=r["nearby"],
        og_title=r["og_title"],
        og_desc=r["og_desc"],
    )
    fpath = os.path.join(OUT_DIR, f"{r['slug']}.html")
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    created.append(r["slug"])
    print(f"Done: {r['slug']}.html")

print(f"\nGenerated {len(created)} pages.")

# ====== MAP DATA ======
print("\n\n===== MAP DATA ENTRIES (add to map-data.js before final ]); =====\n")
for r in restaurants:
    s = "  {{ id: '{0}', name: '{1}', emoji: '{2}', category: 'food', lat: {3}, lng: {4}, section: 'food', link: '{0}.html' }},".format(
        r["slug"], r["name"], r["emoji"], r["lat"], r["lng"])
    print(s)
