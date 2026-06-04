#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const https = require('https');

const SITE_URL = 'https://gohk.gamewayz.com';
const DAILY_DIR = path.join(__dirname, '..', 'daily-content');
const LISTING_FILE = path.join(__dirname, '..', 'daily-content.html');

const weatherKeywords = {
  sunny: ['天朗氣清', '陽光普照', '晴朗', '藍天白雲'],
  cloudy: ['多雲', '陰天', '天色灰灰哋'],
  rainy: ['落雨', '潮濕', '陰雨綿綿'],
  hot: ['炎熱', '熱辣辣', '高溫酷熱'],
  cool: ['清涼', '涼爽', '秋高氣爽'],
  windy: ['大風', '風勢頗大'],
};

const contentData = {
  trails: [
    { name: '龍脊', url: 'hiking-dragons-back.html', difficulty: '⭐ 新手', duration: '2-3 小時', dist: '4.5 km', desc: 'CNN旅遊榜上有名。山脊兩邊都係海景，新手都行到。', transport: '筲箕灣巴士總站搭9號巴士到大浪灣入口', start: '石澳道土地灣', end: '大浪灣', features: ['海景山脊', '無敵海景', '大浪灣沙灘'], tips: '朝早出發避開人潮，大浪灣可以落水消暑' },
    { name: '獅子山', url: 'hiking-lion-rock.html', difficulty: '⭐⭐ 中等', duration: '3-4 小時', dist: '5 km', desc: '香港精神象徵，山頂望到九龍半島全景。', transport: '樂富站行去天馬苑入口', start: '天馬苑', end: '獅子山頂來回', features: ['九龍全景', '獅頭岩壁', '日落'], tips: '近尾段有手腳並用位，記得着防滑鞋' },
    { name: '大帽山', url: 'hiking-tai-mo-shan.html', difficulty: '⭐⭐ 中等', duration: '4-5 小時', dist: '8 km', desc: '香港最高峰957米，秋冬雲海季節必去。', transport: '荃灣西站搭51號巴士到大帽山郊野公園', start: '大帽山郊野公園', end: '山頂天氣雷達站', features: ['香港最高點', '雲海', '芒草'], tips: '秋冬溫差大，山頂比市區低5-8°C，帶定外套' },
    { name: '麥理浩徑第二段', url: 'hiking-maclehose-s2.html', difficulty: '⭐⭐ 中等', duration: '5-6 小時', dist: '13.5 km', desc: '香港最美行山路線之一，浪茄灣至北潭凹。', transport: '西貢市中心搭的士或29R小巴到西灣亭', start: '西灣亭', end: '北潭凹', features: ['浪茄灣', '西灣沙灘', '鹹田灣'], tips: '全程無補給點，帶夠2L水，西灣村假日有士多開' },
    { name: '大東山', url: 'hiking-sunset-peak.html', difficulty: '⭐⭐⭐ 挑戰', duration: '4-5 小時', dist: '7 km', desc: '芒草季節（11-12月）打卡熱點，日落超靚。', transport: '東涌站搭3M/11/23號巴士到伯公坳', start: '伯公坳', end: '南山', features: ['芒草海', '日落', '爛頭營石屋'], tips: '芒草季人山人海，平日去體驗差好遠' },
    { name: '鶴咀', url: 'hiking-cape-daguilar.html', difficulty: '⭐ 新手', duration: '2-3 小時', dist: '4 km', desc: '海岸保護區，蟹洞、雷音洞、燈塔打卡。', transport: '筲箕灣巴士總站搭9號巴士到鶴咀道', start: '鶴咀道入口', end: '鶴咀燈塔', features: ['蟹洞', '雷音洞', '白色燈塔', '鯨魚骨'], tips: '保護區唔可以亂拋垃圾，做個負責任嘅遊客' },
    { name: '南丫島', url: 'hiking-lamma-island.html', difficulty: '⭐ 新手', duration: '3-4 小時', dist: '7 km', desc: '離島行山，由榕樹灣行到索罟灣，沿途海景餐廳。', transport: '中環4號碼頭搭船到榕樹灣', start: '榕樹灣', end: '索罟灣', features: ['海景步道', '海鮮酒家', '風力發電站'], tips: '索罟灣海鮮比榕樹灣平，記得留肚食海鮮' },
    { name: '千島湖', url: 'hiking-thousand-islands.html', difficulty: '⭐ 新手', duration: '3-4 小時', dist: '5 km', desc: '大欖涌水塘，俯瞰千島湖美景，適合影相。', transport: '元朗站搭K66號巴士到大棠', start: '大棠', end: '千島湖清景台', features: ['千島湖景', '紅葉（秋冬）', '水塘景'], tips: '秋冬紅葉季節大棠段超多人，早啲出發' },
  ],
  food: [
    { name: '十八座狗仔粉', url: 'food-18-seats.html', dish: '招牌狗仔粉', price: '$22', area: '深水埗', style: '街頭小食', desc: '米芝蓮必比登推薦，狗仔粉煙韌彈牙，湯底金華火腿豬骨熬足六個鐘。', hours: '12:00-22:00', tips: '加辣菜脯係靈魂，記得叫多份火鴨翅', nearby: '合益泰腸粉、公和荳品廠' },
    { name: '澳洲牛奶公司', url: 'food-australia-dairy.html', dish: '燉奶', price: '$32', area: '佐敦', style: '港式茶餐', desc: '馳名炒蛋多士同燉奶，佐敦街坊飯堂。', hours: '07:30-23:00', tips: '炒蛋多士配凍奶茶係招牌，燉奶可揀熱食', nearby: '佳佳甜品、麥文記麵家' },
    { name: 'Bakehouse', url: 'food-bakehouse.html', dish: '酸種蛋撻', price: '$12', area: '中環', style: '烘焙', desc: '前四季酒店糕餅總監主理，酸種蛋撻每日大排長龍。', hours: '08:00-17:00', tips: '蛋撻出爐時間約9am/12pm/2pm，跟住時間去唔使排咁耐', nearby: '蘭芳園、鏞記酒家' },
    { name: '炳記茶檔', url: 'food-bing-kee.html', dish: '豬扒麵', price: '$30', area: '大坑', style: '大牌檔', desc: '大坑隱世茶檔，豬扒麵同奶茶係招牌。', hours: '06:00-15:00', tips: '注意收三點，星期日休息，唔好白行', nearby: '大坑鐵皮檔、民聲冰室' },
    { name: '合益泰小食', url: 'food-hop-yick-tai.html', dish: '腸粉', price: '$7', area: '深水埗', style: '街頭小食', desc: '深水埗掃街必食，腸粉滑溜，醬汁係靈魂。', hours: '11:00-20:00', tips: '腸粉逐條計，$7/4條，甜醬麻醬辣醬要晒', nearby: '十八座狗仔粉、公和荳品廠' },
    { name: '甘牌燒鵝', url: 'food-kam-shao-wan.html', dish: '燒鵝髀', price: '$150', area: '灣仔', style: '燒味', desc: '米芝蓮一星燒鵝，皮脆肉嫩，日日排隊。', hours: '11:00-21:00', tips: '外賣唔使排隊，可以行去附近公園食', nearby: '再興燒臘、華嫂冰室' },
    { name: '蘭芳園', url: 'food-lan-fong-yuen.html', dish: '絲襪奶茶', price: '$20', area: '中環', style: '港式茶餐', desc: '香港絲襪奶茶始祖，1952年創立，中環老字號。', hours: '07:30-18:00', tips: '中環總店最正宗，蔥油雞扒撈丁都係招牌', nearby: '泰昌蛋撻、鏞記酒家' },
    { name: '新興食家', url: 'food-sun-hing.html', dish: '流沙包', price: '$20', area: '堅尼地城', style: '點心', desc: '凌晨三點開門嘅傳統點心店，流沙包流心程度爆燈。', hours: '03:00-16:00', tips: '凌晨三點到六點最靜，流沙包同蝦餃必叫', nearby: '西環碼頭、泳棚睇日落' },
    { name: '添好運', url: 'food-tim-ho-wan-ssp.html', dish: '酥皮叉燒包', price: '$30', area: '深水埗', style: '點心', desc: '最平米芝蓮一星，酥皮叉燒包一絕。', hours: '09:00-21:30', tips: '酥皮叉燒包每籠三個，即叫即焗等約15分鐘', nearby: '合益泰腸粉、公和荳品廠' },
    { name: '通達食店', url: 'food-tung-tat.html', dish: '碗仔翅', price: '$20', area: '油麻地', style: '街頭小食', desc: '油麻地名物，碗仔翅足料，咖喱魚蛋都出色。', hours: '11:00-23:00', tips: '碗仔翅加胡椒粉同醋先係正宗食法', nearby: '廟街夜市、美都餐室' },
  ],
  swimming: [
    { name: '淺水灣', url: 'swimming-repulse-bay.html', type: '沙灘', desc: '港島最出名沙灘，水清環境靚，設施完善。附近餐廳多，游完水可以 chill。', transport: '中環交易廣場搭6/6X/260號巴士', tips: '假日超多人，朝早10點前去會好好多', nearby: '影灣園商場、The Pulse餐廳' },
    { name: '黃金泳灘', url: 'swimming-golden-beach.html', type: '沙灘', desc: '屯門最長沙灘，水清沙幼，日落靚到爆。', transport: '屯門站轉K53輕鐵到黃金泳灘站', tips: '泳灘旁有燒烤場，可以搞沙灘燒烤', nearby: '黃金海岸商場、三聖邨海鮮' },
    { name: '維園游泳池', url: 'swimming-victoria-park.html', type: '泳池', desc: '港島最大公眾泳池，室外室內都有，位置方便。', transport: '天后站A2出口行3分鐘', tips: '室外池夏天最搶手，室內池全年開放', nearby: '維園、銅鑼灣食街' },
    { name: '九龍公園游泳池', url: 'swimming-kowloon-park.html', type: '泳池', desc: '尖沙咀市中心，游完水行去海港城食嘢。', transport: '尖沙咀站A1出口行5分鐘', tips: '主池水深1.4-1.9米，適合大人細路', nearby: '海港城、K11 MUSEA' },
  ],
  snorkeling: [
    { name: '廈門灣', url: 'snorkeling-half-moon-bay.html', level: '新手', desc: '半月形沙灘水清沙幼，被譽為香港馬爾代夫。有救生員，適合第一次浮潛。', transport: '西貢碼頭搭街渡約20分鐘', tips: '假日街渡班次密，平日可能要等耐啲', nearby: '橋咀洲、西貢海鮮街' },
    { name: '海下灣', url: 'snorkeling-hoi-ha-wan.html', level: '新手', desc: '海岸保護區，生態豐富，珊瑚同魚仔都多。', transport: '西貢市中心搭7號小巴到海下', tips: '保護區嚴禁破壞海洋生物，用礁石防曬', nearby: '荔枝窩、鴨洲' },
    { name: '橋咀洲', url: 'snorkeling-sharp-island.html', level: '新手', desc: '地質公園，連島沙洲奇景，水清見底。', transport: '西貢碼頭搭街渡約15分鐘', tips: '連島沙洲退潮先行得過，check天文台潮汐時間', nearby: '廈門灣、西貢市' },
    { name: '綠蛋島', url: 'snorkeling-green-egg.html', level: '中級', desc: '隱世小島，水質清澈，珊瑚多樣性高。需包船或划艇。', transport: '西貢包船或由相思灣划獨木舟', tips: '無救生員同設施，自備所有裝備補給', nearby: '相思灣、大坑墩' },
  ],
  hiddenGems: [
    { name: '南蓮園池', area: '鑽石山', desc: '市區入面嘅唐風庭院，地鐵站出行幾步就到。靜坐聽錦鯉游水，時間都慢咗。', transport: '鑽石山站C2出口行5分鐘', tips: '免費入場，下午四點後光影最靚', nearby: '志蓮淨苑、荷里活廣場' },
    { name: '大埔海濱公園', area: '大埔', desc: '香港最大公園，海濱長廊踩單車，回歸塔睇日落。', transport: '大埔墟站轉71K巴士或步行15分鐘', tips: '公園有單車租，$20/hr 踩足全場', nearby: '大埔墟街市、林村許願樹' },
    { name: '西環泳棚', area: '堅尼地城', desc: '60年代泳棚遺跡，日落時分影相位。木橋延伸出海，浪花拍打。', transport: '堅尼地城站步行約15分鐘', tips: '日落前半小時到，可以影到金黃色海面', nearby: '新興食家、西環碼頭' },
    { name: '坪洲', area: '離島', desc: '細小寧靜小島，手指山、牛皮廠，一日遊啱啱好。', transport: '中環6號碼頭搭船約40分鐘', tips: '島上有單車租，踩車環島約1小時', nearby: '手指山、東灣沙灘、坪洲市集' },
    { name: '大澳漁村', area: '大嶼山', desc: '香港威尼斯，棚屋、漁村風情、海味乾貨。', transport: '東涌站搭11號巴士直達', tips: '棚屋參觀$20/位，蝦醬係必買手信', nearby: '昂坪360、分流炮台' },
    { name: '荔枝窩', area: '新界東北', desc: '三百年客家古村，風水林、銀葉樹林、紅樹林。', transport: '馬料水碼頭搭街渡（週末限定）', tips: '街渡班次稀疏，計劃好時間，錯過咗要行返出去', nearby: '鴨洲、吉澳' },
  ],
  tips: [
    { tip: '行山記得帶夠水，最少 1L 每人', icon: '💧' },
    { tip: '公共交通用八達通，搭車食飯都用到', icon: '💳' },
    { tip: '夏天行山最好朝早出發，避開正午太陽', icon: '🌅' },
    { tip: '街頭小食多數只收現金，帶定錢', icon: '💰' },
    { tip: '浮潛記得著防曬衣，環保之餘唔怕曬傷', icon: '🤿' },
    { tip: '游水前半個鐘唔好食太飽', icon: '🏊' },
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
          const desc = w.weather?.data?.[0]?.value || '';
          const forecast = w.forecastDesc || '';
          resolve({
            temp: parseInt(w.temperature?.data?.[0]?.value?.replace('°C', '') || '25'),
            humidity: parseInt(w.humidity?.data?.[0]?.value?.replace('%', '') || '75'),
            desc: desc,
            forecast: forecast,
            uv: w.uvindex?.data?.[0]?.value || '',
            source: 'hko',
          });
        } catch (e) {
          resolve({ temp: 25, humidity: 75, desc: '天朗氣清', forecast: '', uv: '', source: 'fallback' });
        }
      });
    }).on('error', () => {
      resolve({ temp: 25, humidity: 75, desc: '天朗氣清', forecast: '', uv: '', source: 'fallback' });
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
  if (month >= 3 && month <= 5) return { name: '春天', swim: false, hike: true, suggestions: ['行山', '賞花', '野餐'] };
  if (month >= 6 && month <= 8) return { name: '夏天', swim: true, hike: false, suggestions: ['游水', '浮潛', '消暑'] };
  if (month >= 9 && month <= 11) return { name: '秋天', swim: false, hike: true, suggestions: ['行山', '露營', '影相'] };
  return { name: '冬天', swim: false, hike: false, suggestions: ['食暖嘢', '行山', '睇雲海'] };
}

function weatherFeeling(temp, desc) {
  if (temp >= 33) return { feel: '熱到融', emoji: '🥵', tag: '炎熱' };
  if (temp >= 28) return { feel: '熱辣辣', emoji: '🌞', tag: '炎熱' };
  if (temp >= 23) return { feel: '和暖舒服', emoji: '😊', tag: '和暖' };
  if (temp >= 18) return { feel: '清涼', emoji: '🌤️', tag: '清涼' };
  return { feel: '涼浸浸', emoji: '🧥', tag: '寒冷' };
}

function slugify(text) { return text.replace(/[^\w\u4e00-\u9fff]/g, '-').replace(/-+/g, '-').toLowerCase(); }

function generateHtml(title, content, weather, dateInfo, tags) {
  const feel = weatherFeeling(weather.temp, weather.desc);
  const season = getSeason(dateInfo.month);
  return `<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="${title} — SunnyHK 每日推介">
<meta name="robots" content="index, follow">
<link rel="canonical" href="${SITE_URL}/daily-content/${dateInfo.dateStr}-${tags[0] || 'daily'}.html">
<meta property="og:title" content="${title} | SunnyHK 每日推介">
<meta property="og:type" content="article">
<meta property="og:locale" content="zh_HK">
<meta property="og:image" content="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80">
<title>${title} | SunnyHK 每日推介</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;700;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="../css/style.css">
<style>
.trail-hero { position: relative; min-height: 40vh; display: flex; align-items: flex-end; background: linear-gradient(135deg, var(--primary) 0%, #0f172a 100%); overflow: hidden; }
.trail-hero img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.5; }
.trail-hero .overlay { position: absolute; inset: 0; background: linear-gradient(transparent 30%, rgba(0,0,0,0.8)); }
.trail-hero .inner { position: relative; z-index: 1; padding: 40px 24px 48px; width: 100%; max-width: 800px; margin: 0 auto; }
.trail-hero h1 { font-size: 2rem; font-weight: 900; color: white; font-family: var(--font-serif); margin-bottom: 8px; }
.trail-hero .meta { display: flex; gap: 12px; flex-wrap: wrap; color: rgba(255,255,255,0.8); font-size: 0.85rem; margin-top: 8px; }
.trail-hero .meta span { background: rgba(255,255,255,0.12); padding: 3px 12px; border-radius: 100px; }
.trail-content { max-width: 700px; margin: 0 auto; padding: 40px 24px; }
.trail-content p { font-size: 1rem; line-height: 2; color: var(--text-light); margin-bottom: 16px; }
.daily-card { background: var(--card-bg); border-radius: var(--radius-md); padding: 20px 24px; margin-bottom: 12px; box-shadow: var(--card-shadow); border-left: 4px solid var(--brand); }
.daily-card h3 { font-size: 1rem; margin-bottom: 4px; }
.daily-card p { font-size: 0.9rem; color: var(--text-light); margin: 0; line-height: 1.7; }
.daily-card ul { margin: 6px 0 0; padding-left: 20px; }
.daily-card li { font-size: 0.9rem; color: var(--text-light); line-height: 1.7; }
.weather-box { background: var(--card-bg); border-radius: var(--radius-md); padding: 16px 20px; margin-bottom: 24px; box-shadow: var(--card-shadow); display: flex; gap: 16px; flex-wrap: wrap; align-items: center; justify-content: center; text-align: center; }
.weather-box .temp { font-size: 2rem; font-weight: 900; color: var(--brand); }
.weather-box .detail { font-size: 0.85rem; color: var(--text-light); }
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 16px 0; }
.two-col .daily-card { margin: 0; }
@media (max-width: 600px) { .two-col { grid-template-columns: 1fr; } .trail-hero h1 { font-size: 1.4rem; } }
</style>
</head>
<body>
<nav class="navbar">
  <div class="inner">
    <a href="../index.html" class="logo"><div class="sun"><i class="fas fa-sun"></i></div> Sunny<span>HK</span></a>
    <div class="nav-links">
      <a href="../index.html">首頁</a>
      <div class="nav-dropdown">
        <a href="../explore.html">探索指南</a>
        <div class="nav-dropdown-menu">
          <a href="../hiking-top10.html">🏆 十大行山路線</a>
          <a href="../hiking.html">🥾 行山路線</a>
          <a href="../snorkeling-map.html">🗺️ 浮潛地圖</a>
          <a href="../snorkeling.html">🤿 浮潛攻略</a>
          <a href="../summer-swimming.html">🏖️ 夏天游水好去處</a>
          <a href="../swimming.html">🏊 游水指南</a>
          <a href="../sham-shui-po-food.html">🍜 深水埗掃街攻略</a>
        </div>
      </div>
      <a href="../food.html">美食地圖</a>
      <div class="nav-dropdown">
        <a href="../tips.html">實用資訊</a>
        <div class="nav-dropdown-menu">
          <a href="../tips.html">💡 實用貼士</a>
          <a href="../electronics.html">💻 電子產品</a>
        </div>
      </div>
      <a href="../daily-content.html" class="active">📝 每日推介</a>
      <a href="../map.html">🗺️ 地圖</a>
      <a href="../stories.html">香港故事</a>
      <a href="../about.html">關於</a>
    </div>
    <div class="nav-actions">
      <button class="theme-toggle" id="themeToggle" aria-label="主題"><i class="fas fa-moon"></i></button>
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
      <div class="detail">${weather.desc} · ${feel.feel}</div>
    </div>
  </div>

  ${content}

  <div style="text-align:center;margin:40px 0;">
    <a href="../daily-content.html" class="submit-btn" style="display:inline-block;width:auto;padding:12px 32px;border-radius:100px;text-decoration:none;">
      ← 睇更多每日推介
    </a>
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
    <div class="footer-bottom"><p>© ${dateInfo.year} SunnyHK. All rights reserved.</p></div>
  </div>
</footer>
<script src="../js/main.js"></script>
</body>
</html>`;
}

function generateTrailArticle(weather, dateInfo) {
  const trail = pick(contentData.trails);
  const feel = weatherFeeling(weather.temp, weather.desc);
  const season = getSeason(dateInfo.month);
  const keyword = pick(weatherKeywords[weather.temp >= 30 ? 'hot' : weather.temp >= 23 ? 'sunny' : 'cool'] || weatherKeywords.sunny);
  const related = contentData.trails.filter(t => t.name !== trail.name && t.difficulty === trail.difficulty).slice(0, 2);

  const title = `${trail.name}行山攻略 | ${dateInfo.label}天氣${feel.feel}`;

  const content = `
    <p>${dateInfo.label}！${keyword}，氣溫約 ${weather.temp}°C，濕度 ${weather.humidity}%。${feel.emoji} 呢個天氣行山一流。</p>

    <p>今日同你詳細介紹 <strong>${trail.name}</strong> — ${trail.desc}</p>

    <div class="daily-card" style="border-left-color:#22c55e;">
      <h3>🥾 ${trail.name}</h3>
      <table style="width:100%;border-collapse:collapse;margin-top:8px;">
        <tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">難度</td><td style="padding:4px 8px;font-size:0.9rem;">${trail.difficulty}</td></tr>
        <tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">距離</td><td style="padding:4px 8px;font-size:0.9rem;">${trail.dist}</td></tr>
        <tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">需時</td><td style="padding:4px 8px;font-size:0.9rem;">${trail.duration}</td></tr>
        <tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">起點</td><td style="padding:4px 8px;font-size:0.9rem;">${trail.start}</td></tr>
        <tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">終點</td><td style="padding:4px 8px;font-size:0.9rem;">${trail.end}</td></tr>
        <tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">交通</td><td style="padding:4px 8px;font-size:0.9rem;">${trail.transport}</td></tr>
      </table>
      <p style="margin-top:10px;"><a href="../${trail.url}" style="color:var(--brand);font-weight:500;">睇完整路線攻略 →</a></p>
    </div>

    <h3 style="font-family:var(--font-serif);margin:24px 0 8px;font-size:1.1rem;">路線亮點</h3>
    <ul style="color:var(--text-light);line-height:2;padding-left:20px;">
      ${trail.features.map(f => `<li>${f}</li>`).join('')}
    </ul>

    <h3 style="font-family:var(--font-serif);margin:24px 0 8px;font-size:1.1rem;">行山貼士</h3>
    <div class="daily-card" style="border-left-color:#f59e0b;">
      <p>${pick(contentData.tips).tip}</p>
      <p style="margin-top:6px;">🔸 ${trail.tips}</p>
    </div>

    ${related.length > 0 ? `
    <h3 style="font-family:var(--font-serif);margin:24px 0 8px;font-size:1.1rem;">同難度路線推介</h3>
    <div class="two-col">
      ${related.map(t => `
        <div class="daily-card" style="border-left-color:#22c55e;">
          <h3>🥾 ${t.name}</h3>
          <p>${t.duration} · ${t.dist}</p>
          <p><a href="../${t.url}" style="color:var(--brand);">睇路線 →</a></p>
        </div>
      `).join('')}
    </div>` : ''}
  `;

  return { title, content, tags: ['🥾 行山', trail.difficulty, season.name] };
}

function generateFoodArticle(weather, dateInfo) {
  const food = pick(contentData.food);
  const feel = weatherFeeling(weather.temp, weather.desc);
  const season = getSeason(dateInfo.month);
  const keyword = pick(weatherKeywords[weather.temp >= 30 ? 'hot' : 'cool'] || weatherKeywords.sunny);
  const styleRelated = contentData.food.filter(f => f.style === food.style && f.name !== food.name).slice(0, 2);

  const title = `${food.area}美食：${food.name} | ${food.dish}／${
    food.price ? `${food.price}` : ''}起`;

  const content = `
    <p>${weather.desc}嘅${dateInfo.label}，氣溫 ${weather.temp}°C。${feel.emoji} ${keyword}，最適合去${food.area}搵食。</p>

    <p>今日同你深入介紹 <strong>${food.name}</strong>，一間位於${food.area}嘅${food.style}名店。</p>

    <div class="daily-card" style="border-left-color:#f43f5e;">
      <h3>🍜 ${food.name}</h3>
      <table style="width:100%;border-collapse:collapse;margin-top:8px;">
        <tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">類別</td><td style="padding:4px 8px;font-size:0.9rem;">${food.style}</td></tr>
        <tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">招牌菜</td><td style="padding:4px 8px;font-size:0.9rem;">${food.dish}</td></tr>
        ${food.price ? `<tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">參考價</td><td style="padding:4px 8px;font-size:0.9rem;">${food.price} 起</td></tr>` : ''}
        ${food.hours ? `<tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">營業時間</td><td style="padding:4px 8px;font-size:0.9rem;">${food.hours}</td></tr>` : ''}
        <tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">地區</td><td style="padding:4px 8px;font-size:0.9rem;">${food.area}</td></tr>
      </table>
      <p style="margin-top:10px;"><a href="../${food.url}" style="color:var(--brand);font-weight:500;">睇完整餐廳攻略 →</a></p>
    </div>

    <h3 style="font-family:var(--font-serif);margin:24px 0 8px;font-size:1.1rem;">點樣食先係內行</h3>
    <div class="daily-card" style="border-left-color:#f59e0b;">
      <p>🔸 ${food.tips}</p>
    </div>

    ${food.nearby ? `
    <h3 style="font-family:var(--font-serif);margin:24px 0 8px;font-size:1.1rem;">附近仲有咩食</h3>
    <p>食完可以順便去：${food.nearby}。全部都係步行距離，一街之隔。</p>` : ''}

    ${styleRelated.length > 0 ? `
    <h3 style="font-family:var(--font-serif);margin:24px 0 8px;font-size:1.1rem;">同類餐廳推介</h3>
    <div class="two-col">
      ${styleRelated.map(r => `
        <div class="daily-card" style="border-left-color:#f43f5e;">
          <h3>🍜 ${r.name}</h3>
          <p>${r.area} · ${r.dish}</p>
          <p><a href="../${r.url}" style="color:var(--brand);">睇詳情 →</a></p>
        </div>
      `).join('')}
    </div>` : ''}

    <p style="margin-top:20px;">睇更多美食推介？去我哋嘅 <a href="../food.html" style="color:var(--brand);">完整美食地圖</a>，全港超過三十間餐廳攻略。</p>
  `;

  return { title, content, tags: ['🍜 美食', food.area, food.style] };
}

function generateSwimArticle(weather, dateInfo) {
  const season = getSeason(dateInfo.month);
  if (!season.swim) {
    return generateFoodArticle(weather, dateInfo);
  }

  const isPool = weather.temp <= 28 || pick([true, false]);
  const spots = isPool ? contentData.swimming : contentData.swimming.concat(contentData.snorkeling);
  const spot = pick(spots);
  const waterTemp = weather.temp >= 30 ? '28-30' : weather.temp >= 25 ? '25-28' : '22-25';

  const title = `夏日消暑好去處：${spot.name}`;

  const content = `
    <p>${weather.temp}°C！${weather.desc}，熱辣辣嘅${dateInfo.label}，唔玩水對唔住自己。${feel.emoji}</p>

    <p>今日水溫約 <strong>${waterTemp}°C</strong>，非常適合游水。同你介紹 <strong>${spot.name}</strong>。</p>

    <div class="daily-card" style="border-left-color:#3b82f6;">
      <h3>🏖️ ${spot.name}</h3>
      <p>${spot.desc}</p>
      <table style="width:100%;border-collapse:collapse;margin-top:8px;">
        <tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">交通</td><td style="padding:4px 8px;font-size:0.9rem;">${spot.transport}</td></tr>
        <tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">貼士</td><td style="padding:4px 8px;font-size:0.9rem;">${spot.tips}</td></tr>
        ${spot.nearby ? `<tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">附近</td><td style="padding:4px 8px;font-size:0.9rem;">${spot.nearby}</td></tr>` : ''}
      </table>
      <p style="margin-top:10px;"><a href="../${spot.url}" style="color:var(--brand);font-weight:500;">睇完整攻略 →</a></p>
    </div>

    <h3 style="font-family:var(--font-serif);margin:24px 0 8px;font-size:1.1rem;">游水安全貼士</h3>
    <ul style="color:var(--text-light);line-height:2;padding-left:20px;">
      <li>☀️ 紫外線指數唔低，記得搽防曬</li>
      <li>💧 游水前半個鐘唔好食太飽</li>
      <li>🚩 喺沙灘記得喺防鯊網範圍內游水</li>
    </ul>

    <p>睇更多玩水好去處？去我哋嘅 <a href="../swimming.html" style="color:var(--brand);">游水指南</a> 或者 <a href="../snorkeling.html" style="color:var(--brand);">浮潛攻略</a>。</p>
  `;

  return { title, content, tags: ['🏖️ 消暑', isPool ? '游水' : '浮潛', '夏天'] };
}

function generateHiddenGemArticle(weather, dateInfo) {
  const gem = pick(contentData.hiddenGems);
  const feel = weatherFeeling(weather.temp, weather.desc);
  const keyword = pick(weatherKeywords[weather.temp >= 30 ? 'hot' : weather.temp >= 23 ? 'sunny' : 'cool'] || weatherKeywords.sunny);

  const title = `隱世好去處：${gem.name}（${gem.area}）`;

  const content = `
    <p>${keyword}嘅${dateInfo.label}，氣溫 ${weather.temp}°C。唔想同人逼？帶你去一個香港人先識嘅地方。</p>

    <p><strong>${gem.name}</strong> — ${gem.desc}</p>

    <div class="daily-card" style="border-left-color:#8b5cf6;">
      <h3>📍 ${gem.name}</h3>
      <table style="width:100%;border-collapse:collapse;margin-top:8px;">
        <tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">地區</td><td style="padding:4px 8px;font-size:0.9rem;">${gem.area}</td></tr>
        <tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">交通</td><td style="padding:4px 8px;font-size:0.9rem;">${gem.transport}</td></tr>
        ${gem.tips ? `<tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">貼士</td><td style="padding:4px 8px;font-size:0.9rem;">${gem.tips}</td></tr>` : ''}
        ${gem.nearby ? `<tr><td style="padding:4px 8px;color:var(--text-light);font-size:0.9rem;">附近景點</td><td style="padding:4px 8px;font-size:0.9rem;">${gem.nearby}</td></tr>` : ''}
      </table>
    </div>

    <p>呢啲地方仲未俾遊客攻陷，趁而家快啲去探索。嗰種「得我知」嘅感覺，正過任何景點。</p>

    <p>仲有更多隱世地方？睇我哋嘅 <a href="../tips.html" style="color:var(--brand);">實用貼士</a>。</p>
  `;

  return { title, content, tags: ['📍 隱世', gem.area, '好去處'] };
}

function generateWeekendArticle(weather, dateInfo) {
  const trail = pick(contentData.trails);
  const food = pick(contentData.food);
  const gem = pick(contentData.hiddenGems);
  const feel = weatherFeeling(weather.temp, weather.desc);
  const season = getSeason(dateInfo.month);

  const title = `周末好去處（${dateInfo.dateStr}）行山＋美食＋隱世一日遊`;

  const content = `
    <p>又到周末！氣溫 ${weather.temp}°C，${weather.desc}。${feel.emoji} 天時地利人和，最適合出去玩足一日。</p>

    <p>以下係一個 <strong>一日遊行程建議</strong>，由朝玩到晚：</p>

    <h3 style="font-family:var(--font-serif);margin:24px 0 8px;font-size:1.1rem;">🌅 上午：行山 — ${trail.name}</h3>
    <div class="daily-card" style="border-left-color:#22c55e;">
      <p><strong>${trail.name}</strong> · ${trail.difficulty} · ${trail.duration} · ${trail.dist}</p>
      <p>${trail.desc}</p>
      <p style="margin-top:6px;">交通：${trail.transport}</p>
      <p><a href="../${trail.url}" style="color:var(--brand);">睇路線詳情 →</a></p>
    </div>

    <h3 style="font-family:var(--font-serif);margin:24px 0 8px;font-size:1.1rem;">🍜 中午：食好西 — ${food.name}</h3>
    <div class="daily-card" style="border-left-color:#f43f5e;">
      <p><strong>${food.name}</strong> · ${food.area} · ${food.style}</p>
      <p>招牌：${food.dish}${food.price ? `（$${food.price}起）` : ''}</p>
      <p>${food.tips}</p>
      <p><a href="../${food.url}" style="color:var(--brand);">睇餐廳詳情 →</a></p>
    </div>

    <h3 style="font-family:var(--font-serif);margin:24px 0 8px;font-size:1.1rem;">🌇 下午：隱世 — ${gem.name}</h3>
    <div class="daily-card" style="border-left-color:#8b5cf6;">
      <p><strong>${gem.name}</strong>（${gem.area}）</p>
      <p>${gem.desc}</p>
      <p>交通：${gem.transport}</p>
    </div>

    <p style="margin-top:24px;">💡 行程可以按你喜好調動，行山同隱世景點距離可能較遠，建議揀同一區嘅組合。</p>

    <p>更多周末靈感？睇 <a href="../hiking-top10.html" style="color:var(--brand);">十大行山路線</a>、<a href="../sham-shui-po-food.html" style="color:var(--brand);">深水埗掃街攻略</a> 同 <a href="../explore.html" style="color:var(--brand);">探索指南</a>。</p>
  `;

  return { title, content, tags: ['🎉 周末', '一日遊', season.name] };
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
  updateNavbar();
  updateSitemap(filename, dateInfo);
}

function updateListing(filename, article, dateInfo) {
  const existing = fs.existsSync(LISTING_FILE) ? fs.readFileSync(LISTING_FILE, 'utf-8') : null;

  if (existing && existing.includes(filename)) {
    console.log('listing 已包含今日內容');
    return;
  }

    const excerpt = article.content.replace(/<[^>]+>/g, '').slice(0, 80).trim();
    const entry = `
      <a href="daily-content/${filename}" class="feature-card" style="text-decoration:none;display:block;border:2px solid #e2e8f0;box-shadow:0 4px 20px rgba(0,0,0,0.12);background:#ffffff;border-radius:20px;padding:28px;">
        <h3 style="font-family:var(--font-serif);font-size:1.15rem;margin-bottom:8px;color:#1e293b;">${article.title}</h3>
        <p style="color:#64748b;font-size:0.82rem;margin-bottom:8px;">📅 ${dateInfo.dateStr} · ${dateInfo.label}</p>
        <p style="margin:0;color:#475569;">${excerpt}</p>
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
.trail-hero { position: relative; min-height: 30vh; display: flex; align-items: flex-end; background: linear-gradient(135deg, var(--primary) 0%, #0f172a 100%); overflow: hidden; }
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
      <div class="nav-dropdown">
        <a href="explore.html">探索指南</a>
        <div class="nav-dropdown-menu">
          <a href="hiking-top10.html">🏆 十大行山路線</a>
          <a href="hiking.html">🥾 行山路線</a>
          <a href="snorkeling-map.html">🗺️ 浮潛地圖</a>
          <a href="snorkeling.html">🤿 浮潛攻略</a>
          <a href="summer-swimming.html">🏖️ 夏天游水好去處</a>
          <a href="swimming.html">🏊 游水指南</a>
          <a href="sham-shui-po-food.html">🍜 深水埗掃街攻略</a>
        </div>
      </div>
      <a href="food.html">美食地圖</a>
      <div class="nav-dropdown">
        <a href="tips.html">實用資訊</a>
        <div class="nav-dropdown-menu">
          <a href="tips.html">💡 實用貼士</a>
          <a href="electronics.html">💻 電子產品</a>
        </div>
      </div>
      <a href="daily-content.html" class="active">📝 每日推介</a>
      <a href="map.html">🗺️ 地圖</a>
      <a href="stories.html">香港故事</a>
      <a href="about.html">關於</a>
    </div>
    <div class="nav-actions">
      <div class="lang-group">
        <button class="lang-btn" data-lang="trad">繁</button>
        <button class="lang-btn" data-lang="simp">简</button>
        <button class="lang-btn" data-lang="en">EN</button>
      </div>
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
    <p style="color:var(--text-light);margin-bottom:32px;">每日為你精選香港好去處。</p>
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
      console.log('❌ listing 格式有問題，跳過更新');
      return;
    }
    const updated = existing.slice(0, insertPos) + entry + existing.slice(insertPos);
    fs.writeFileSync(LISTING_FILE, updated, 'utf-8');
    console.log('✅ 已更新: daily-content.html');
  }
}

function updateNavbar() {
  const indices = ['index.html', 'food.html', 'hiking.html', 'snorkeling.html', 'swimming.html', 'electronics.html', 'tips.html', 'map.html', 'stories.html', 'about.html'];

  for (const file of indices) {
    const filepath = path.join(__dirname, '..', file);
    if (!fs.existsSync(filepath)) continue;

    let content = fs.readFileSync(filepath, 'utf-8');

    const hasDaily = content.includes('daily-content.html');
    if (hasDaily) continue;

    const navLinks = [
      '<a href="index.html" data-i18n="nav-home">',
      '<a href="explore.html" data-i18n="nav-explore">',
      '<a href="food.html" data-i18n="nav-food">',
      '<a href="map.html" data-i18n="nav-map">',
      '<a href="stories.html" data-i18n="nav-stories">',
      '<a href="about.html" data-i18n="nav-about">',
    ];

    for (const link of navLinks) {
      if (content.includes(link)) {
        content = content.replace(link, `<a href="daily-content.html">📝 每日推介</a>\n      ${link}`);
        break;
      }
    }

    const mobileLinks = [
      '<a href="index.html" data-i18n="nav-mobile-home">',
      '<a href="stories.html" data-i18n="nav-mobile-stories">',
    ];

    for (const link of mobileLinks) {
      if (content.includes(link) && !content.includes('daily-content.html')) {
        content = content.replace(link, `${link}\n  <a href="daily-content.html">📝 每日推介</a>`);
        break;
      }
    }

    fs.writeFileSync(filepath, content, 'utf-8');
    console.log(`✅ navbar 已更新: ${file}`);
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

main().catch(console.error);
