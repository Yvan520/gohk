#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const https = require('https');

const SITE_URL = 'https://gohk.gamewayz.com';
const DAILY_DIR = path.join(__dirname, '..', 'daily-content');
const LISTING_FILE = path.join(__dirname, '..', 'daily-content.html');

const contentData = {
  trails: [
    { name: '龍脊', url: 'hiking-dragons-back.html', difficulty: '新手', duration: '2-3 小時', dist: '4.5 km', desc: 'CNN旅遊榜上有名。山脊兩邊都係海景，新手都行到。', transport: '筲箕灣巴士總站搭9號巴士到大浪灣入口', start: '石澳道土地灣', end: '大浪灣', features: ['海景山脊', '無敵海景', '大浪灣沙灘'], tips: '朝早出發避開人潮，大浪灣可以落水消暑' },
    { name: '獅子山', url: 'hiking-lion-rock.html', difficulty: '中等', duration: '3-4 小時', dist: '5 km', desc: '香港精神象徵，山頂望到九龍半島全景。', transport: '樂富站行去天馬苑入口', start: '天馬苑', end: '獅子山頂來回', features: ['九龍全景', '獅頭岩壁', '日落'], tips: '近尾段有手腳並用位，記得着防滑鞋' },
    { name: '大帽山', url: 'hiking-tai-mo-shan.html', difficulty: '中等', duration: '4-5 小時', dist: '8 km', desc: '香港最高峰957米，秋冬雲海季節必去。', transport: '荃灣西站搭51號巴士到大帽山郊野公園', start: '大帽山郊野公園', end: '山頂天氣雷達站', features: ['香港最高點', '雲海', '芒草'], tips: '秋冬溫差大，山頂比市區低5-8°C，帶定外套' },
    { name: '麥理浩徑第二段', url: 'hiking-maclehose-s2.html', difficulty: '中等', duration: '5-6 小時', dist: '13.5 km', desc: '香港最美行山路線之一，浪茄灣至北潭凹。', transport: '西貢市中心搭的士或29R小巴到西灣亭', start: '西灣亭', end: '北潭凹', features: ['浪茄灣', '西灣沙灘', '鹹田灣'], tips: '全程無補給點，帶夠2L水，西灣村假日有士多開' },
    { name: '大東山', url: 'hiking-sunset-peak.html', difficulty: '挑戰', duration: '4-5 小時', dist: '7 km', desc: '芒草季節（11-12月）打卡熱點，日落超靚。', transport: '東涌站搭3M/11/23號巴士到伯公坳', start: '伯公坳', end: '南山', features: ['芒草海', '日落', '爛頭營石屋'], tips: '芒草季人山人海，平日去體驗差好遠' },
    { name: '鶴咀', url: 'hiking-cape-daguilar.html', difficulty: '新手', duration: '2-3 小時', dist: '4 km', desc: '海岸保護區，蟹洞、雷音洞、燈塔打卡。', transport: '筲箕灣巴士總站搭9號巴士到鶴咀道', start: '鶴咀道入口', end: '鶴咀燈塔', features: ['蟹洞', '雷音洞', '白色燈塔', '鯨魚骨'], tips: '保護區唔可以亂拋垃圾，做個負責任嘅遊客' },
    { name: '南丫島', url: 'hiking-lamma-island.html', difficulty: '新手', duration: '3-4 小時', dist: '7 km', desc: '離島行山，由榕樹灣行到索罟灣，沿途海景餐廳。', transport: '中環4號碼頭搭船到榕樹灣', start: '榕樹灣', end: '索罟灣', features: ['海景步道', '海鮮酒家', '風力發電站'], tips: '索罟灣海鮮比榕樹灣平，記得留肚食海鮮' },
    { name: '千島湖', url: 'hiking-thousand-islands.html', difficulty: '新手', duration: '3-4 小時', dist: '5 km', desc: '大欖涌水塘，俯瞰千島湖美景，適合影相。', transport: '元朗站搭K66號巴士到大棠', start: '大棠', end: '千島湖清景台', features: ['千島湖景', '紅葉（秋冬）', '水塘景'], tips: '秋冬紅葉季節大棠段超多人，早啲出發' },
  ],
  food: [
    { name: '十八座狗仔粉', url: 'food-18-seats.html', dish: '招牌狗仔粉', price: '$22', area: '深水埗', style: '街頭小食', desc: '米芝蓮必比登推薦，狗仔粉煙韌彈牙，湯底金華火腿豬骨熬足六個鐘。', hours: '12:00-22:00', tips: '加辣菜脯係靈魂，記得叫多份火鴨翅', nearby: '合益泰腸粉、公和荳品廠' },
    { name: '澳洲牛奶公司', url: 'food-australia-dairy.html', dish: '燉奶', price: '$32', area: '佐敦', style: '港式茶餐', desc: '馳名炒蛋多士同燉奶，佐敦街坊飯堂。', hours: '07:30-23:00', tips: '炒蛋多士配凍奶茶係招牌，燉奶可揀熱食', nearby: '佳佳甜品、麥文記麵家' },
    { name: 'Bakehouse', url: 'food-bakehouse.html', dish: '酸種蛋撻', price: '$12', area: '中環', style: '烘焙', desc: '前四季酒店糕餅總監主理，酸種蛋撻每日大排長龍。', hours: '08:00-17:00', tips: '蛋撻出爐約9am/12pm/2pm，跟時間去唔使排咁耐', nearby: '蘭芳園、鏞記酒家' },
    { name: '炳記茶檔', url: 'food-bing-kee.html', dish: '豬扒麵', price: '$30', area: '大坑', style: '大牌檔', desc: '大坑隱世茶檔，豬扒麵同奶茶係招牌。', hours: '06:00-15:00', tips: '收三點，星期日休息，唔好白行', nearby: '大坑鐵皮檔、民聲冰室' },
    { name: '合益泰小食', url: 'food-hop-yick-tai.html', dish: '腸粉', price: '$7', area: '深水埗', style: '街頭小食', desc: '深水埗掃街必食，腸粉滑溜，醬汁係靈魂。', hours: '11:00-20:00', tips: '腸粉逐條計，甜醬麻醬辣醬要晒', nearby: '狗仔粉、公和荳品廠' },
    { name: '甘牌燒鵝', url: 'food-kam-shao-wan.html', dish: '燒鵝髀', price: '$150', area: '灣仔', style: '燒味', desc: '米芝蓮一星燒鵝，皮脆肉嫩，日日排隊。', hours: '11:00-21:00', tips: '外賣唔使排隊，可以行去附近公園食', nearby: '再興燒臘、華嫂冰室' },
    { name: '蘭芳園', url: 'food-lan-fong-yuen.html', dish: '絲襪奶茶', price: '$20', area: '中環', style: '港式茶餐', desc: '香港絲襪奶茶始祖，1952年創立，中環老字號。', hours: '07:30-18:00', tips: '中環總店最正宗，蔥油雞扒撈丁都係招牌', nearby: '泰昌蛋撻、鏞記酒家' },
    { name: '新興食家', url: 'food-sun-hing.html', dish: '流沙包', price: '$20', area: '堅尼地城', style: '點心', desc: '凌晨三點開門嘅傳統點心店，流沙包流心程度爆燈。', hours: '03:00-16:00', tips: '凌晨三點到六點最靜，流沙包同蝦餃必叫', nearby: '西環碼頭、泳棚' },
    { name: '添好運', url: 'food-tim-ho-wan-ssp.html', dish: '酥皮叉燒包', price: '$30', area: '深水埗', style: '點心', desc: '最平米芝蓮一星，酥皮叉燒包一絕。', hours: '09:00-21:30', tips: '酥皮叉燒包每籠三個，即叫即焗等約15分鐘', nearby: '合益泰腸粉、公和荳品廠' },
    { name: '通達食店', url: 'food-tung-tat.html', dish: '碗仔翅', price: '$20', area: '油麻地', style: '街頭小食', desc: '油麻地名物，碗仔翅足料，咖喱魚蛋都出色。', hours: '11:00-23:00', tips: '碗仔翅加胡椒粉同醋先係正宗食法', nearby: '廟街夜市、美都餐室' },
  ],
  swimming: [
    { name: '淺水灣', url: 'swimming-repulse-bay.html', type: '沙灘', desc: '港島最出名沙灘，水清環境靚，設施完善。附近餐廳多，游完水可以 chill。', transport: '中環交易廣場搭6/6X/260號巴士', tips: '假日超多人，朝早10點前去會好好多', nearby: '影灣園商場、The Pulse' },
    { name: '黃金泳灘', url: 'swimming-golden-beach.html', type: '沙灘', desc: '屯門最長沙灘，水清沙幼，日落靚到爆。', transport: '屯門站轉K53輕鐵到黃金泳灘站', tips: '泳灘旁有燒烤場，可以搞沙灘燒烤', nearby: '黃金海岸商場、三聖邨海鮮' },
    { name: '維園游泳池', url: 'swimming-victoria-park.html', type: '泳池', desc: '港島最大公眾泳池，室外室內都有，位置方便。', transport: '天后站A2出口行3分鐘', tips: '室外池夏天最搶手，室內池全年開放', nearby: '維園、銅鑼灣食街' },
    { name: '九龍公園游泳池', url: 'swimming-kowloon-park.html', type: '泳池', desc: '尖沙咀市中心，游完水行去海港城食嘢。', transport: '尖沙咀站A1出口行5分鐘', tips: '主池水深1.4-1.9米，大人細路都啱', nearby: '海港城、K11 MUSEA' },
  ],
  snorkeling: [
    { name: '廈門灣', url: 'snorkeling-half-moon-bay.html', level: '新手', desc: '半月形沙灘水清沙幼，被譽為香港馬爾代夫。有救生員，啱第一次浮潛。', transport: '西貢碼頭搭街渡約20分鐘', tips: '假日街渡班次密，平日可能要等耐啲', nearby: '橋咀洲、西貢海鮮街' },
    { name: '海下灣', url: 'snorkeling-hoi-ha-wan.html', level: '新手', desc: '海岸保護區，生態豐富，珊瑚同魚仔都多。', transport: '西貢市中心搭7號小巴到海下', tips: '保護區嚴禁破壞海洋生物，用礁石防曬', nearby: '荔枝窩、鴨洲' },
    { name: '橋咀洲', url: 'snorkeling-sharp-island.html', level: '新手', desc: '地質公園，連島沙洲奇景，水清見底。', transport: '西貢碼頭搭街渡約15分鐘', tips: '連島沙洲退潮先行得過，check天文台潮汐時間', nearby: '廈門灣、西貢市' },
    { name: '綠蛋島', url: 'snorkeling-green-egg.html', level: '中級', desc: '隱世小島，水質清澈，珊瑚多樣性高。需包船或划艇。', transport: '西貢包船或由相思灣划獨木舟', tips: '無救生員同設施，自備所有裝備補給', nearby: '相思灣、大坑墩' },
  ],
  hiddenGems: [
    { name: '南蓮園池', area: '鑽石山', desc: '市區入面嘅唐風庭院，地鐵站出行幾步就到。靜坐聽錦鯉游水，時間都慢咗。', transport: '鑽石山站C2出口行5分鐘', tips: '免費入場，下午四點後光影最靚', nearby: '志蓮淨苑、荷里活廣場' },
    { name: '大埔海濱公園', area: '大埔', desc: '香港最大公園，海濱長廊踩單車，回歸塔睇日落。', transport: '大埔墟站轉71K巴士或步行15分鐘', tips: '公園有單車租，踩足全場', nearby: '大埔墟街市、林村許願樹' },
    { name: '西環泳棚', area: '堅尼地城', desc: '60年代泳棚遺跡，日落時分影相位。木橋延伸出海，浪花拍打。', transport: '堅尼地城站步行約15分鐘', tips: '日落前半小時到，影金黃色海面', nearby: '新興食家、西環碼頭' },
    { name: '坪洲', area: '離島', desc: '細小寧靜小島，手指山、牛皮廠，一日遊啱啱好。', transport: '中環6號碼頭搭船約40分鐘', tips: '島上有單車租，踩車環島約1小時', nearby: '手指山、東灣沙灘' },
    { name: '大澳漁村', area: '大嶼山', desc: '香港威尼斯，棚屋、漁村風情、海味乾貨。', transport: '東涌站搭11號巴士直達', tips: '棚屋參觀$20/位，蝦醬係必買手信', nearby: '昂坪360、分流炮台' },
    { name: '荔枝窩', area: '新界東北', desc: '三百年客家古村，風水林、銀葉樹林、紅樹林。', transport: '馬料水碼頭搭街渡（週末限定）', tips: '街渡班次稀疏，計劃好時間', nearby: '鴨洲、吉澳' },
  ],
};

function fetchWeather() {
  return new Promise((resolve) => {
    https.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=tc', (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const w = JSON.parse(data);
          const desc = w.weather?.data?.[0]?.value || '天色一般';
          const forecast = w.forecastDesc || '';
          resolve({
            temp: parseInt(w.temperature?.data?.[0]?.value?.replace('°C', '') || '25'),
            humidity: parseInt(w.humidity?.data?.[0]?.value?.replace('%', '') || '75'),
            desc: desc,
            forecast: forecast,
            uv: w.uvindex?.data?.[0]?.value || '',
          });
        } catch (e) {
          resolve({ temp: 25, humidity: 75, desc: '天色一般', forecast: '', uv: '' });
        }
      });
    }).on('error', () => {
      resolve({ temp: 25, humidity: 75, desc: '天色一般', forecast: '', uv: '' });
    });
  });
}

function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }

function getDateInfo() {
  const now = new Date();
  const hktMs = now.getTime() + (now.getTimezoneOffset() + 480) * 60 * 1000;
  const hkt = new Date(hktMs);
  return {
    dateStr: `${hkt.getUTCFullYear()}-${String(hkt.getUTCMonth()+1).padStart(2,'0')}-${String(hkt.getUTCDate()).padStart(2,'0')}`,
    month: hkt.getUTCMonth() + 1,
    day: hkt.getUTCDate(),
    dayOfWeek: hkt.getUTCDay(),
    year: hkt.getUTCFullYear(),
    label: { 0: '星期日', 1: '星期一', 2: '星期二', 3: '星期三', 4: '星期四', 5: '星期五', 6: '星期六' }[hkt.getUTCDay()],
  };
}

function getSeason(month) {
  if (month >= 3 && month <= 5) return { name: '春天', swim: false };
  if (month >= 6 && month <= 8) return { name: '夏天', swim: true };
  if (month >= 9 && month <= 11) return { name: '秋天', swim: false };
  return { name: '冬天', swim: false };
}

function weatherFeeling(temp) {
  if (temp >= 33) return { feel: '熱到融', emoji: '🥵' };
  if (temp >= 28) return { feel: '熱辣辣', emoji: '🌞' };
  if (temp >= 23) return { feel: '和暖舒服', emoji: '😊' };
  if (temp >= 18) return { feel: '清涼', emoji: '🌤️' };
  return { feel: '涼浸浸', emoji: '🧥' };
}

const weatherPhrases = {
  sunny: ['天朗氣清', '陽光普照', '風和日麗', '藍天白雲'],
  cloudy: ['多雲', '陰天', '天色灰灰哋'],
  rainy: ['落雨', '潮濕', '落緊雨'],
  hot: ['炎熱', '熱辣辣', '高溫'],
  cool: ['清涼', '涼爽', '秋高氣爽'],
};

function getWeatherPhrase(temp, desc) {
  if (temp >= 30) return pick(weatherPhrases.hot);
  if (temp >= 23) return pick(weatherPhrases.sunny);
  if (temp >= 18) return pick(weatherPhrases.cool);
  return pick(weatherPhrases.cool);
}

function slugify(text) { return text.replace(/[^\w\u4e00-\u9fff]/g, '-').replace(/-+/g, '-').toLowerCase(); }

function generateHtml(title, content, weather, dateInfo, tags) {
  const feel = weatherFeeling(weather.temp);
  return `<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="${title} — SunnyHK 每日推介，香港在地深度旅遊建議">
<meta property="og:title" content="${title} | SunnyHK 每日推介">
<meta property="og:type" content="article">
<meta property="og:locale" content="zh_HK">
<meta property="og:image" content="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80">
<title>${title} | SunnyHK 每日推介</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;700;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="../css/style.css">
<style>
.trail-hero { position: relative; min-height: 40vh; display: flex; align-items: flex-end; background: linear-gradient(135deg, #1e3a5f 0%, #0f172a 100%); overflow: hidden; }
.trail-hero img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.5; }
.trail-hero .overlay { position: absolute; inset: 0; background: linear-gradient(transparent 30%, rgba(0,0,0,0.8)); }
.trail-hero .inner { position: relative; z-index: 1; padding: 40px 24px 48px; width: 100%; max-width: 800px; margin: 0 auto; }
.trail-hero h1 { font-size: 2rem; font-weight: 900; color: white; font-family: var(--font-serif); margin-bottom: 8px; }
.trail-hero .meta { display: flex; gap: 12px; flex-wrap: wrap; color: rgba(255,255,255,0.8); font-size: 0.85rem; margin-top: 8px; }
.trail-hero .meta span { background: rgba(255,255,255,0.12); padding: 3px 12px; border-radius: 100px; }
.trail-content { max-width: 700px; margin: 0 auto; padding: 40px 24px; }
.trail-content p { font-size: 1rem; line-height: 2.1; color: #334155; margin-bottom: 20px; }
.weather-box { background: #f8fafc; border-radius: 16px; padding: 16px 20px; margin-bottom: 28px; display: flex; gap: 16px; flex-wrap: wrap; align-items: center; justify-content: center; text-align: center; border: 1px solid #e2e8f0; }
.weather-box .temp { font-size: 2rem; font-weight: 900; color: #1e3a5f; }
.weather-box .detail { font-size: 0.85rem; color: #64748b; }
.cta-link { display:inline-block;margin-top:8px;color:#1e3a5f;font-weight:500;text-decoration:underline; }
@media (max-width: 600px) { .trail-hero h1 { font-size: 1.4rem; } }
</style>
</head>
<body>
<nav class="navbar">
  <div class="inner">
    <a href="../index.html" class="logo"><div class="sun"><i class="fas fa-sun"></i></div> Sunny<span>HK</span></a>
    <div class="nav-links">
      <a href="../index.html">首頁</a>
      <a href="../explore.html">探索指南</a>
      <a href="../hiking.html">🥾 行山</a>
      <a href="../food.html">🍜 美食</a>
      <a href="../snorkeling.html">🤿 浮潛</a>
      <a href="../swimming.html">🏊 游水</a>
      <a href="../daily-content.html" class="active">📝 每日推介</a>
      <a href="../map.html">🗺️ 地圖</a>
    </div>
    <div class="nav-actions">
      <button class="theme-toggle" id="themeToggle"><i class="fas fa-moon"></i></button>
      <button class="mobile-menu-btn" id="mobileMenuBtn"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>
<div class="mobile-drawer" id="mobileDrawer">
  <a href="../index.html">首頁</a>
  <a href="../hiking.html">🥾 行山路線</a>
  <a href="../food.html">美食地圖</a>
  <a href="../snorkeling.html">🤿 浮潛攻略</a>
  <a href="../swimming.html">🏊 游水指南</a>
  <a href="../daily-content.html">📝 每日推介</a>
  <a href="../tips.html">💡 實用貼士</a>
  <a href="../map.html">🗺️ 地圖</a>
  <a href="../stories.html">香港故事</a>
</div>

<div class="trail-hero">
  <img src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80" alt="${title}" loading="lazy">
  <div class="overlay"></div>
  <div class="inner">
    <a href="../daily-content.html" class="back-link" style="color:rgba(255,255,255,0.7);margin-bottom:12px;">← 每日推介</a>
    <h1>${title}</h1>
    <div class="meta">
      <span>📅 ${dateInfo.dateStr} ${dateInfo.label}</span>
      ${tags.map(t => `<span>${t}</span>`).join('')}
    </div>
  </div>
</div>

<div class="trail-content">
  <div class="weather-box">
    <div>
      <div class="temp">${weather.temp}°C</div>
      <div class="detail">🌡️ 溫度</div>
    </div>
    <div>
      <div class="temp">${weather.humidity}%</div>
      <div class="detail">💧 濕度</div>
    </div>
    <div>
      <div class="temp">${feel.emoji}</div>
      <div class="detail">${weather.desc.replace(/，.*$/, '')} · ${feel.feel}</div>
    </div>
  </div>

  ${content}

  <p style="border-top:1px solid #e2e8f0;padding-top:24px;font-size:0.9rem;color:#94a3b8;">— SunnyHK 每日為你發掘香港最好玩、最好食、最隱世嘅角落。</p>

  <div style="text-align:center;margin:32px 0;">
    <a href="../daily-content.html" style="display:inline-block;padding:10px 28px;border-radius:100px;background:#1e3a5f;color:white;text-decoration:none;font-weight:500;">← 睇更多每日推介</a>
  </div>
</div>

<footer class="footer">
  <div class="inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="logo-text"><div class="sun"><i class="fas fa-sun"></i></div> SunnyHK</div>
        <p>一個年輕、陽光、真實嘅香港旅行靈感平台。</p>
      </div>
      <div class="footer-col">
        <h4>探索</h4>
        <a href="../hiking.html">🥾 行山路線</a>
        <a href="../snorkeling.html">🤿 浮潛攻略</a>
        <a href="../swimming.html">🏊 游水指南</a>
        <a href="../food.html">🍜 美食地圖</a>
      </div>
      <div class="footer-col">
        <h4>資訊</h4>
        <a href="../daily-content.html">📝 每日推介</a>
        <a href="../tips.html">💡 實用貼士</a>
        <a href="../map.html">🗺️ 網站地圖</a>
        <a href="../about.html">關於 SunnyHK</a>
      </div>
    </div>
    <div class="footer-bottom"><p>© ${dateInfo.year} SunnyHK</p></div>
  </div>
</footer>
</body>
</html>`;
}

/* ── Natural content generators ── */

function generateTrailArticle(weather, dateInfo) {
  const trail = pick(contentData.trails);
  const feel = weatherFeeling(weather.temp);
  const phrase = getWeatherPhrase(weather.temp, weather.desc);
  const tips = pick(['💧 帶夠水，最少一升', '🌅 朝早出發避開烈日', '📱 出發前下載离线地圖', '👟 著防滑鞋，唔好著波鞋']);

  const title = `${trail.name} 行山路線 · 全程${trail.duration} · ${trail.difficulty}難度`;

  const content = `
    <p>${phrase}，氣溫大約 ${weather.temp}°C，濕度 ${weather.humidity}%，係一個適合出行嘅${dateInfo.label}。想出去走走但又唔知去邊好？不如試下行山。</p>

    <p>今次介紹嘅係 <strong>${trail.name}</strong>，一條位於香港嘅${trail.difficulty}難度路線，全長約 ${trail.dist}，行晒大約 ${trail.duration}。唔使好專業嘅裝備，普通運動鞋加一兩枝水就已經足夠。</p>

    <p>呢條路線最大嘅賣點係沿途風景多變——${trail.features.slice(0, 2).join('、')}，行到一半停低望吓個景，你就會明點解咁多人會愛上喺香港行山。起步點喺 ${trail.start}，終點係 ${trail.end}。交通方面，可以喺 ${trail.transport}，好易去到。</p>

    <p>行山貼士一樣：${trail.tips}。仲有就係 ${tips}。成條路都有唔少影相位，帶定電話充電器，唔好錯過沿途風光。</p>

    <p>如果行完想搵嘢食，路線附近有唔少好去處。詳細路線圖、中途補給點同交通班次，可以睇我哋嘅完整攻略：<br>
    <a href="../${trail.url}" class="cta-link">🥾 ${trail.name} 完整路線攻略 →</a></p>

    <p>嫌呢條太易或者太難？我哋網站仲有十幾條行山路線，由新手到挑戰級都有，可以去 <a href="../hiking.html" class="cta-link">完整行山路線清單</a> 揀一條啱你程度嘅。</p>

    <p>就算你平時唔係成日行山，呢條路線嘅風景都絕對值得你花半日時間。喺香港生活咁耐，有時最靚嘅風景就喺身邊。</p>
  `;

  return { title, content, tags: ['行山', trail.difficulty, trail.dist] };
}

function generateFoodArticle(weather, dateInfo) {
  const food = pick(contentData.food);
  const feel = weatherFeeling(weather.temp);
  const phrase = getWeatherPhrase(weather.temp, weather.desc);
  const openers = ['冇乜嘢比', '唔知食咩好？不如試吓', '今日想同大家推介'];

  const title = `${food.area} · ${food.name} | ${food.dish} $${food.price ? food.price.replace('$','') : '價錢相宜'}`;

  const content = `
    <p>${phrase}嘅${dateInfo.label}，${weather.temp}°C，身體已經自動 switch 咗去「想食好嘢」mode。如果你都係咁，今日介紹嘅地方可能會啱你心水。</p>

    <p>位於${food.area}嘅 <strong>${food.name}</strong>，係一間專做${food.style}嘅小店。佢哋嘅招牌菜係 <strong>${food.dish}</strong>，價錢大約 ${food.price} 起，喺香港嚟講算係好合理。${food.desc.replace('。','。')}</p>

    <p>講到點樣食先係內行，有一個重點你要記住：${food.tips}。成日有人第一次去唔知，跟住就 miss 咗最好食嘅部分，好可惜。</p>

    <p>營業時間係 ${food.hours}，如果打算周末去可能要預少少排隊時間，平日會好啲。食完之後行幾步仲有 ${food.nearby}，全部都行到，可以順便掃街。</p>

    <p>想睇詳細菜單、更多圖片同交通指引？我哋有完整嘅餐廳介紹：<br>
    <a href="../${food.url}" class="cta-link">🍜 ${food.name} 完整食評 →</a></p>

    <p>計我話，喺香港搵食唔使成日諗住去高級餐廳，好多街頭小店同老字號先係真係好食嘅。我哋網站有超過三十間餐廳攻略，由茶記到大牌檔都有，去 <a href="../food.html" class="cta-link">美食地圖</a> 慢慢睇。</p>
  `;

  return { title, content, tags: ['美食', food.area, food.style] };
}

function generateSwimArticle(weather, dateInfo) {
  const season = getSeason(dateInfo.month);
  if (!season.swim) return generateFoodArticle(weather, dateInfo);

  const spot = pick([...contentData.swimming, ...contentData.snorkeling]);
  const feel = weatherFeeling(weather.temp);
  const waterTemp = weather.temp >= 30 ? '大約28-30°C' : weather.temp >= 25 ? '大約25-28°C' : '22-25°C左右';

  const title = `${spot.name} · 夏日消暑好去處`;

  const content = `
    <p>${weather.temp}°C，仲要 humidity ${weather.humidity}%，老實講喺香港夏天真係冇乜嘢比跳入水更加舒服。今日推介一個玩水好地方——<strong>${spot.name}</strong>。</p>

    <p>呢度水溫今日大約 ${waterTemp}，水質唔錯，環境亦都企理。${spot.desc}</p>

    <p>點樣去？好簡單：${spot.transport}。到達之後會有指示牌，唔難搵。提提你：${spot.tips}。呢個係好多人唔為意嘅細節，但做好咗成個體驗會好好多。</p>

    <p>附近仲有 ${spot.nearby}，游完水可以過去 chill 下，食啲嘢補充體力。跟住黃昏時分再睇埋日落，完美嘅一日。</p>

    <p>有更多問題或者想睇詳細交通同設施介紹？可以睇我哋完整攻略：<br>
    <a href="../${spot.url}" class="cta-link">🏖️ ${spot.name} 完整攻略 →</a></p>

    <p>另外我哋網站仲有更多玩水好去處——<a href="../swimming.html" class="cta-link">游水指南</a> 同 <a href="../snorkeling.html" class="cta-link">浮潛攻略</a>，由沙灘到泳池都有。</p>
  `;

  return { title, content, tags: ['消暑', '游水', '夏天'] };
}

function generateHiddenGemArticle(weather, dateInfo) {
  const gem = pick(contentData.hiddenGems);
  const phrase = getWeatherPhrase(weather.temp, weather.desc);

  const title = `${gem.name}（${gem.area}）· 香港隱世角落`;

  const content = `
    <p>${phrase}嘅${dateInfo.label}，氣溫 ${weather.temp}°C。如果唔想同人逼商場、唔想排隊打卡，不如去一個香港人先識嘅地方。</p>

    <p>今日想介紹嘅係位於 <strong>${gem.area}</strong> 嘅 <strong>${gem.name}</strong>。呢度唔係旅遊書會推介嘅景點，正正因為咁，佢保留咗最真實嘅香港味道。${gem.desc}</p>

    <p>交通方面：${gem.transport}。去到之後你會發現，同外面嘅繁囂好似兩個世界。行入去嘅時候，腳步會不自覺放慢，連講嘢都細聲啲。</p>

    <p>有一個小貼士：${gem.tips}。附近仲有 ${gem.nearby}，可以順便去埋。</p>

    <p>如果你鍾意呢類隱世地方，我哋網站嘅 <a href="../tips.html" class="cta-link">實用貼士</a> 仲有更多類似推介。有時最好嘅旅行體驗，唔需要搭飛機，搭個巴士就已經去到。</p>
  `;

  return { title, content, tags: ['隱世', gem.area, '好去處'] };
}

function generateWeekendArticle(weather, dateInfo) {
  const trail = pick(contentData.trails);
  const food = pick(contentData.food);
  const gem = pick(contentData.hiddenGems);
  const feel = weatherFeeling(weather.temp);
  const phrase = getWeatherPhrase(weather.temp, weather.desc);

  const title = `周末一日遊提案 · 行山＋美食＋隱世景點`;

  const content = `
    <p>又到周末。${weather.temp}°C，${phrase}，成個星期返工咁攰，唔出去唞下真係對唔住自己。以下係一個由朝玩到晚嘅 <strong>一日遊行程</strong>，你可以跟住行，亦可以隨意抽一個環節去。</p>

    <h3 style="font-family:var(--font-serif);font-size:1.1rem;margin:24px 0 8px;">🌅 上午：${trail.name}</h3>
    <p>朝早去行山係最好嘅選擇——未到正午，太陽唔係好猛，氣溫啱啱好。${trail.name} 係一條${trail.difficulty}路線，行晒約 ${trail.duration}，風景靚之餘又唔會太攰。起步喺 ${trail.start}，終點喺 ${trail.end}。行完出身汗，個人成個醒神晒。</p>
    <p><a href="../${trail.url}" class="cta-link">🥾 ${trail.name} 路線攻略 →</a></p>

    <h3 style="font-family:var(--font-serif);font-size:1.1rem;margin:24px 0 8px;">🍜 中午：${food.name}</h3>
    <p>行完山，肚餓係必然嘅。去${food.area}食 <strong>${food.name}</strong>，佢哋嘅招牌 ${food.dish}（${food.price}起）係每次去都必叫嘅。開 ${food.hours}，時間上好就腳。食完仲可以去附近嘅 ${food.nearby} 行個圈。</p>
    <p><a href="../${food.url}" class="cta-link">🍜 ${food.name} 餐廳詳情 →</a></p>

    <h3 style="font-family:var(--font-serif);font-size:1.1rem;margin:24px 0 8px;">🌇 下晝：${gem.name}</h3>
    <p>食飽飽，去一個比較靜嘅地方 hea 下。<strong>${gem.name}</strong> 喺${gem.area}，${gem.desc}。交通：${gem.transport}。嗰種遠離塵囂嘅感覺，同市區係兩個世界。</p>

    <p>當然，呢個行程你可以自由組合——如果同一區就更加順路。更多周末靈感，可以睇我哋網站嘅 <a href="../hiking-top10.html" class="cta-link">十大行山路線</a> 同 <a href="../sham-shui-po-food.html" class="cta-link">深水埗掃街攻略</a>。</p>

    <p>周末唔好淨係留喺屋企，香港仲有好多嘢等緊你。</p>
  `;

  return { title, content, tags: ['周末', '一日遊', '香港好去處'] };
}

async function main() {
  const weather = await fetchWeather();
  const dateInfo = getDateInfo();
  const dayOfWeek = dateInfo.dayOfWeek;

  let article;
  if (dayOfWeek === 5) {
    article = generateWeekendArticle(weather, dateInfo);
  } else if (dayOfWeek === 6) {
    article = generateTrailArticle(weather, dateInfo);
  } else if (dayOfWeek === 0) {
    article = generateSwimArticle(weather, dateInfo);
  } else if (dayOfWeek === 1) {
    article = generateTrailArticle(weather, dateInfo);
  } else if (dayOfWeek === 2 || dayOfWeek === 4) {
    article = generateFoodArticle(weather, dateInfo);
  } else if (dayOfWeek === 3) {
    article = generateHiddenGemArticle(weather, dateInfo);
  }

  const slug = `${dateInfo.dateStr}-${slugify(article.title).slice(0, 60)}`;
  const filename = `${slug}.html`;

  if (!fs.existsSync(DAILY_DIR)) fs.mkdirSync(DAILY_DIR, { recursive: true });

  const filepath = path.join(DAILY_DIR, filename);
  if (fs.existsSync(filepath)) {
    console.log('今日已有內容，跳過');
    return;
  }

  const html = generateHtml(article.title, article.content, weather, dateInfo, article.tags);
  fs.writeFileSync(filepath, html, 'utf-8');
  console.log(`✅ 已建立: daily-content/${filename}`);

  updateListing(filename, article, dateInfo);
  cleanSitemap();
  updateSitemap(filename, dateInfo);
}

function updateListing(filename, article, dateInfo) {
  const existing = fs.existsSync(LISTING_FILE) ? fs.readFileSync(LISTING_FILE, 'utf-8') : null;

  if (existing && existing.includes(filename)) {
    console.log('listing 已包含今日內容');
    return;
  }

  const excerpt = article.content.replace(/<[^>]+>/g, '').slice(0, 100).trim();
  const entry = `
      <a href="daily-content/${filename}" class="feature-card" style="text-decoration:none;display:block;border:2px solid #e2e8f0;box-shadow:0 4px 20px rgba(0,0,0,0.12);background:#ffffff;border-radius:20px;padding:28px;">
        <h3 style="font-family:var(--font-serif);font-size:1.15rem;margin-bottom:8px;color:#1e293b;">${article.title}</h3>
        <p style="color:#64748b;font-size:0.82rem;margin-bottom:8px;">📅 ${dateInfo.dateStr} · ${dateInfo.label}</p>
        <p style="margin:0;color:#475569;">${excerpt}…</p>
      </a>`;

  if (!existing) {
    const listing = `<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="每日推介 — SunnyHK 每日更新嘅香港行山、美食、好去處推薦">
<meta property="og:title" content="📝 每日推介 | SunnyHK">
<meta property="og:type" content="website">
<meta property="og:locale" content="zh_HK">
<title>📝 每日推介 | SunnyHK</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;700;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="css/style.css">
<style>
.trail-hero { position: relative; min-height: 30vh; display: flex; align-items: flex-end; background: linear-gradient(135deg, #1e3a5f 0%, #0f172a 100%); overflow: hidden; }
.trail-hero .overlay { position: absolute; inset: 0; background: linear-gradient(transparent 30%, rgba(0,0,0,0.8)); }
.trail-hero .inner { position: relative; z-index: 1; padding: 40px 24px 48px; width: 100%; max-width: 800px; margin: 0 auto; }
.trail-hero h1 { font-size: 2.4rem; font-weight: 900; color: white; font-family: var(--font-serif); }
.trail-hero p { color: rgba(255,255,255,0.7); margin-top: 8px; }
@media (max-width: 600px) { .trail-hero h1 { font-size: 1.6rem; } }
</style>
</head>
<body>
<nav class="navbar">
  <div class="inner">
    <a href="index.html" class="logo"><div class="sun"><i class="fas fa-sun"></i></div> Sunny<span>HK</span></a>
    <div class="nav-links">
      <a href="index.html">首頁</a>
      <a href="explore.html">探索指南</a>
      <a href="hiking.html">🥾 行山</a>
      <a href="food.html">🍜 美食</a>
      <a href="snorkeling.html">🤿 浮潛</a>
      <a href="swimming.html">🏊 游水</a>
      <a href="daily-content.html" class="active">📝 每日推介</a>
      <a href="map.html">🗺️ 地圖</a>
    </div>
    <div class="nav-actions">
      <button class="theme-toggle" id="themeToggle"><i class="fas fa-moon"></i></button>
      <button class="mobile-menu-btn" id="mobileMenuBtn"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>
<div class="mobile-drawer" id="mobileDrawer">
  <a href="index.html">首頁</a>
  <a href="hiking.html">🥾 行山路線</a>
  <a href="food.html">美食地圖</a>
  <a href="snorkeling.html">🤿 浮潛攻略</a>
  <a href="swimming.html">🏊 游水指南</a>
  <a href="daily-content.html">📝 每日推介</a>
  <a href="tips.html">💡 實用貼士</a>
  <a href="map.html">🗺️ 地圖</a>
  <a href="stories.html">香港故事</a>
</div>

<div class="trail-hero">
  <div class="overlay"></div>
  <div class="inner">
    <h1>📝 每日推介</h1>
    <p>每日一篇，為你推薦香港最好玩、最好食、最隱世嘅好去處。</p>
  </div>
</div>

<section class="section">
  <div class="inner">
    <h2 style="font-size:1.5rem;margin-bottom:8px;font-family:var(--font-serif);">📝 最新推介</h2>
    <p style="color:#64748b;margin-bottom:32px;">每日為你精選香港好去處。</p>
    <div class="feature-grid">
      ${entry}
    </div>
  </div>
</section>

<footer class="footer">
  <div class="inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="logo-text"><div class="sun"><i class="fas fa-sun"></i></div> SunnyHK</div>
        <p>一個年輕、陽光、真實嘅香港旅行靈感平台。</p>
      </div>
      <div class="footer-col">
        <h4>探索</h4>
        <a href="hiking.html">🥾 行山路線</a>
        <a href="snorkeling.html">🤿 浮潛攻略</a>
        <a href="swimming.html">🏊 游水指南</a>
        <a href="food.html">🍜 美食地圖</a>
      </div>
      <div class="footer-col">
        <h4>資訊</h4>
        <a href="daily-content.html">📝 每日推介</a>
        <a href="tips.html">💡 實用貼士</a>
        <a href="map.html">🗺️ 網站地圖</a>
        <a href="about.html">關於 SunnyHK</a>
      </div>
    </div>
    <div class="footer-bottom"><p>© ${dateInfo.year} SunnyHK</p></div>
  </div>
</footer>

</body>
</html>`;
    fs.writeFileSync(LISTING_FILE, listing, 'utf-8');
    console.log('✅ 已建立: daily-content.html');
  } else {
    const insertPos = existing.lastIndexOf('</div>\n  </div>\n</section>');
    if (insertPos === -1) {
      console.log('listing 格式不匹配，跳過');
      return;
    }
    const updated = existing.slice(0, insertPos) + entry + existing.slice(insertPos);
    fs.writeFileSync(LISTING_FILE, updated, 'utf-8');
    console.log('✅ 已更新: daily-content.html');
  }
}

function updateSitemap(filename, dateInfo) {
  const sitemapPath = path.join(__dirname, '..', 'sitemap.xml');
  if (!fs.existsSync(sitemapPath)) return;
  let sitemap = fs.readFileSync(sitemapPath, 'utf-8');
  const url = `${SITE_URL}/daily-content/${filename}`;
  if (sitemap.includes(url)) return;
  const entry = `  <url><loc>${url}</loc><lastmod>${dateInfo.dateStr}</lastmod><changefreq>daily</changefreq><priority>0.8</priority></url>`;
  sitemap = sitemap.replace('</urlset>', `${entry}\n</urlset>`);
  fs.writeFileSync(sitemapPath, sitemap, 'utf-8');
  console.log('✅ sitemap 已更新');
}

function cleanSitemap() {
  const sitemapPath = path.join(__dirname, '..', 'sitemap.xml');
  if (!fs.existsSync(sitemapPath)) return;
  let sitemap = fs.readFileSync(sitemapPath, 'utf-8');
  const validDir = path.join(__dirname, '..', 'daily-content');
  const validFiles = fs.existsSync(validDir) ? fs.readdirSync(validDir).filter(f => f.endsWith('.html')) : [];
  const lines = sitemap.split('\n');
  const cleaned = lines.filter(line => {
    const match = line.match(/daily-content\/([^<]+)\.html/);
    if (!match) return true;
    return validFiles.includes(`${match[1]}.html`);
  });
  fs.writeFileSync(sitemapPath, cleaned.join('\n'), 'utf-8');
}

main().catch(console.error);
