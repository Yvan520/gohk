import os, json

TRAILS = [
  {
    "id": "dragons-back",
    "name": "龍脊 Dragon's Back",
    "difficulty": "🌱 新手",
    "time": "2-3小時",
    "distance": "4-5公里",
    "elevation": "打爛埕頂山 284m",
    "meta_desc": "香港最出名行山路線，CNN旅遊榜上有名。龍脊係港島徑第八段，全程4-5公里，山脊兩邊都係海景。",
    "meta_keywords": "龍脊,香港行山,港島徑,石澳,大浪灣,打爛埕頂山,香港行山路線",
    "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&q=80",
    "header_image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1200&q=80",
    "intro": "龍脊（Dragon's Back）係香港最出名嘅行山路線之一，CNN 旅遊網站評為「全球最佳城市遠足徑」之一。行喺山脊之上，兩邊都係無敵海景——一邊係石澳、大浪灣，另一邊係大潭灣同赤柱，景色開揚到令人嘩一聲。",
    "route": [
      {"title": "🚌 起點：土地灣", "content": "筲箕灣巴士總站搭 9 號巴士，喺「土地灣」站落車。車程約 20 分鐘，落車就見到登山入口。巴士約 15-20 分鐘一班，記住預時間。"},
      {"title": "🥾 第一段：上打爛埕頂山", "content": "由土地灣出發，沿石級上山約 45 分鐘到打爛埕頂山（284米）。呢段路主要係石級同泥路交錯，初段有樹蔭，越上越開揚。唔好急，慢慢行，沿途已經可以睇到石澳半島嘅景色。"},
      {"title": "🐉 第二段：龍脊山脊", "content": "龍脊嘅精華路段！由打爛埕頂山沿山脊前行，左邊係石澳高爾夫球場同大浪灣，右邊係赤柱半島同大潭灣。呢段路平坦易行，大約 1 公里，但風景係全段最靚。觀景台位置必停，可以影到經典嘅龍脊相。"},
      {"title": "🌊 第三段：落大浪灣", "content": "經過龍脊之後開始落山，約 30 分鐘落到大浪灣村。落山路以石級為主，有啲位較斜，膝頭唔好嘅朋友可以帶行山杖。大浪灣係港島最東面嘅沙灘，水清沙幼，好多人會帶衝浪板嚟玩。"},
      {"title": "🍜 終點：大浪灣茶座", "content": "落到沙灘右邊有茶座，西多士、餐蛋麵、凍檸茶樣樣齊。呢度係行完山最 perfect 嘅 ending。食飽之後可以搭小巴或者行 15 分鐘出石澳道搭 9 號巴士返筲箕灣。"}
    ],
    "transport": "🚌 筲箕灣巴士總站搭 9 號巴士，土地灣站落車（約 $8.2）。回程由大浪灣搭小巴或行出石澳道搭 9 號巴士。",
    "season": "🍂 秋冬天（10月-3月）最適合，唔曬又涼爽。夏天行要 7am 前出發避開烈日。",
    "tips": [
      "夏天暴曬，最少帶 2L 水",
      "大浪灣茶座只收現金",
      "建議 8am 前到土地灣，避開人潮",
      "著防滑行山鞋，部分路段有浮沙",
      "落山後可以去石澳村打卡食嘢"
    ],
    "nearby": "行完龍脊可以落石澳村影彩色屋仔，或者喺大浪灣游水消暑。仲有時間嘅話可以搭車去赤柱食海鮮。"
  },
  {
    "id": "peak-circle",
    "name": "太平山頂環山步道 Victoria Peak Circle",
    "difficulty": "🌱 新手",
    "time": "1小時",
    "distance": "3.5公里",
    "elevation": "約 400m",
    "meta_desc": "最輕鬆又最經典！盧吉道環山步道平坦到BB車都推到，圍繞太平山一圈，180度俯瞰維港同九龍半島。",
    "meta_keywords": "太平山頂,盧吉道,香港夜景,維港景色,香港行山,親子行山",
    "image": "https://images.unsplash.com/photo-1582568072276-3a4c366c6b3b?auto=format&fit=crop&w=800&q=80",
    "header_image": "https://images.unsplash.com/photo-1582568072276-3a4c366c6b3b?auto=format&fit=crop&w=1200&q=80",
    "intro": "太平山頂環山步道（盧吉道）係香港最輕鬆又最有代表性嘅行山路線。全程石屎平路，冇上落斜，連 BB 車都推到。圍繞太平山山腰一圈，維港景色、九龍半島、離島風光盡收眼底。外國遊客必到，香港人自己都成日上嚟散步。",
    "route": [
      {"title": "🚠 上山方式", "content": "有三種方式上山：1）山頂纜車——最經典，中環站上約 7 分鐘（來回 $88）；2）15 號巴士——中環碼頭/交易廣場上，約 35 分鐘（$12.5）；3）的士——中環上的約 $60-80。"},
      {"title": "🥾 盧吉道起步", "content": "山頂廣場出嚟向左行就係盧吉道入口。步道約 3.5 公里，全程平坦石屎路。一開始就見到維港景色，右手邊係山頂別墅群。"},
      {"title": "📸 最佳影相位", "content": "行約 15 分鐘後到達第一個觀景台，呢度係影維港全景最佳位置。再前行 10 分鐘有另一個觀景台，可以影到西環同青馬大橋。"},
      {"title": "🌅 時間推薦", "content": "建議下晝 4-5 點上山，行到 6 點左右睇日落。之後落返山頂廣場食晚飯，等到 7:30 再睇百萬夜景。"},
      {"title": "🍽️ 山頂美食", "content": "山頂廣場有丼丼屋、翡翠拉麵等連鎖餐廳，凌霄閣有阿甘蝦餐廳。想平啲可以喺麥當勞或者便利店搞掂。"}
    ],
    "transport": "🚠 山頂纜車中環站（來回 $88）/ 15號巴士中環碼頭（$12.5）/ 的士",
    "season": "四季皆宜。秋冬睇日落最靚，夏天要帶風扇。",
    "tips": [
      "全程石屎平路，穿普通波鞋都得",
      "黃昏人最多，想清靜可以朝早上",
      "山頂風大，帶件薄風褸",
      "盧吉道部份路段冇欄杆，睇路",
      "週末纜車排長龍，建議搭巴士"
    ],
    "nearby": "落山可以去中環蘭桂坊飲嘢，或者去上環荷里活道行古董街。"
  },
  {
    "id": "por-lo-shan",
    "name": "菠蘿山 Por Lo Shan 良田坳峽谷",
    "difficulty": "🌱 新手",
    "time": "2-3小時",
    "distance": "5公里來回",
    "elevation": "約 200m",
    "meta_desc": "香港都有大峽谷！菠蘿山良田坳嘅丹霞地貌，橙紅色岩石加峽谷景觀，仲可以行落下白泥睇日落。",
    "meta_keywords": "菠蘿山,良田坳峽谷,屯門行山,下白泥日落,香港大峽谷,丹霞地貌",
    "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=800&q=80",
    "header_image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80",
    "intro": "菠蘿山嘅良田坳峽谷被稱為「香港大峽谷」。橙紅色嘅沉積岩經過千萬年風化，形成咗獨特嘅丹霞地貌，喺香港非常少見。由良景邨出發唔使一個鐘就到峽谷，之後可以沿山脊行落下白泥睇日落——被譽為香港最美日落之一。",
    "route": [
      {"title": "🚌 起步：良景邨", "content": "屯門良景邨巴士總站落車，向良景商場後面行，沿「良田坳」嘅指示牌上山。初段係石屎斜路，約行 20 分鐘。"},
      {"title": "🏜️ 到達峽谷", "content": "繼續沿山路上約 25 分鐘，突然眼前開揚——橙紅色嘅峽谷出現在你面前！呢度就係良田坳峽谷，可以落去行入峽谷入面影相，地面係沙石，小心跣腳。"},
      {"title": "📸 峽谷打卡", "content": "峽谷最佳影相位係由高處向下影，人企喺峽谷入面，影出嚟好似喺美國西部一樣。下晝 3-4 點光影最靚，陽光穿過峽谷形成強烈對比。"},
      {"title": "🌅 繼續行落下白泥", "content": "由峽谷沿山脊行約 45 分鐘落到下白泥。呢段路係山徑，望住后海灣同深圳景色。下白泥嘅泥灘係香港最佳日落景點之一，退潮時可以行出泥灘影相。"},
      {"title": "🚐 回程", "content": "下白泥有 33 號小巴返屯門市中心，約 20 分鐘一班。留意尾班車時間，約 9pm。或者可以沿路行出去流浮山搭 K65 巴士返元朗。"}
    ],
    "transport": "🚌 良景邨巴士總站（多條巴士/輕鐵到達），回程下白泥搭 33 號小巴",
    "season": "🍂 秋冬最佳，夏天曝曬無遮蔭。日落前 2 小時出發最理想。",
    "tips": [
      "沙石路面極易跣，必著行山鞋",
      "全程冇樹蔭，做足防曬",
      "帶 1.5L 水以上",
      "解放軍靶場區域，見到紅旗唔好進入",
      "下白泥蚊多，帶蚊怕水",
      "影日落最好帶腳架"
    ],
    "nearby": "流浮山食海鮮係經典行程，或者去屯門三聖邨海鮮街都得。"
  },
  {
    "id": "lamma-island",
    "name": "南丫島家樂徑 Lamma Island Family Walk",
    "difficulty": "🌱 新手",
    "time": "1.5-2小時",
    "distance": "5公里",
    "elevation": "約 100m",
    "meta_desc": "由榕樹灣行到索罟灣，全程石屎路輕鬆易行。洪聖爺灣游水、觀景亭打卡、豆腐花店唞唞，行完食海鮮。",
    "meta_keywords": "南丫島,南丫島行山,榕樹灣,索罟灣,洪聖爺灣,香港離島,親子行山",
    "image": "https://images.unsplash.com/photo-1505118380757-91f5f5632de0?auto=format&fit=crop&w=800&q=80",
    "header_image": "https://images.unsplash.com/photo-1505118380757-91f5f5632de0?auto=format&fit=crop&w=1200&q=80",
    "intro": "南丫島家樂徑係香港最 iconic 嘅離島行山路線。由榕樹灣到索罟灣，全程石屎路、平緩易行，就算著拖鞋都行到（不過唔建議）。兩邊都係海景，沿途有沙灘、小賣店、豆腐花，仲可以喺索罟灣食海鮮收尾。半日輕鬆遊最 perfect。",
    "route": [
      {"title": "🚢 出發：中環去榕樹灣", "content": "中環 4 號碼頭搭船去榕樹灣，船程約 25 分鐘。普通船 $25、高速船 $35。星期六日班次加密，約 20 分鐘一班。"},
      {"title": "🏖️ 洪聖爺灣", "content": "落船後沿指示行約 10 分鐘就到洪聖爺灣沙灘。呢度水清沙幼，有更衣室同淋浴設施。可以游水消暑再繼續行。沙灘後面有小食亭，賣魚蛋同冰凍椰青。"},
      {"title": "🌿 家樂徑主路段", "content": "由洪聖爺灣繼續前行，經過觀景亭——呢度可以望到南丫島發電廠嘅三支大煙囪同大片海景。再前行會經過幾間豆腐花店，必試凍豆腐花加花奶。"},
      {"title": "🏘️ 索罟灣", "content": "約行多 30 分鐘就到索罟灣。呢度係漁村風情，海邊停滿漁船，空氣中係淡淡嘅海味香氣。天后廟可以順便參觀。"},
      {"title": "🦐 海鮮大餐", "content": "索罟灣海邊有幾間海鮮酒家，天虹海鮮最出名。二人套餐約 $400-600，有椒鹽瀨尿蝦、清蒸海上鮮、蒜蓉蒸扇貝等。食完搭船返中環，船程約 35 分鐘。"}
    ],
    "transport": "🚢 中環 4 號碼頭搭船，可選擇榕樹灣上/索罟灣返，或相反",
    "season": "四季皆宜。夏天建議行朝早或者下晝 4 點後。",
    "tips": [
      "豆腐花約 $15-20 碗",
      "索罟灣海鮮酒家多可以揀",
      "帶拖鞋方便落沙灘",
      "回程船期留意時間表",
      "週末人多，平日更有慢活感"
    ],
    "nearby": "南丫島有風力發電站可以參觀，或者喺榕樹灣行手工藝小店。"
  },
  {
    "id": "lion-rock",
    "name": "獅子山 Lion Rock",
    "difficulty": "⛰️ 中級",
    "time": "4小時來回",
    "distance": "4公里來回",
    "elevation": "獅子山頂 495m",
    "meta_desc": "香港精神嘅象徵！獅子山頂俯瞰九龍全景同維港。最後一段要手腳並用爬石級，斜度唔細但唔危險。",
    "meta_keywords": "獅子山,香港精神,九龍全景,獅子山行山,香港行山路線,九龍行山",
    "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=800&q=80",
    "header_image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1200&q=80",
    "intro": "獅子山係香港精神嘅象徵。呢座 495 米高嘅山峰，山形似一頭伏臥嘅獅子，守護住九龍半島。上到山頂可以俯瞰九龍全景、維港兩岸，甚至遠眺大嶼山。路線斜度唔細，最後一段需要手腳並用，但上到山頂嘅一刻，你會覺得一切都值。",
    "route": [
      {"title": "🚌 起步：樂富橫頭磡", "content": "樂富站 A 出口，沿天馬苑方向行約 20 分鐘到獅子山郊野公園入口。或者搭巴士到橫頭磡邨，沿指示上山。"},
      {"title": "🌳 獅子山郊野公園", "content": "由入口沿麥理浩徑第五段行約 30 分鐘，經過樹林同小溪，呢段路比較平坦，可以當熱身。"},
      {"title": "🪨 一線天", "content": "繼續上行約 20 分鐘到達「一線天」——兩塊大石之間嘅狹窄通道，只容一人通過。呢度開始感受到獅子山嘅氣勢。"},
      {"title": "🧗 最後衝刺", "content": "由一線天到山頂最後一段係最斜嘅，需要手腳並用爬石級。路徑清晰，有繩索輔助，唔算危險但要好小心。約 15 分鐘到頂。"},
      {"title": "🦁 山頂打卡", "content": "獅子山頂有塊大石叫做「獅頭」，企喺獅頭位置可以影到經典嘅九龍全景相。不過要小心，獅頭位冇欄杆，唔好為咗影相而出太出。"}
    ],
    "transport": "🚌 樂富站 A 出口步行約 20 分鐘 / 橫頭磡邨巴士站",
    "season": "🍂 秋冬最佳。夏天朝早 7 點前出發，避免西曬。",
    "tips": [
      "最後一段較斜，手腳並用最穩陣",
      "著抓地力好嘅行山鞋",
      "帶手套方便爬石",
      "山頂風大，唔好企太出",
      "朝早去最好，下晝西曬好熱",
      "帶 2L 水以上"
    ],
    "nearby": "落山可以去樂富廣場食嘢，或者行過嚟九龍城食泰國菜。"
  },
  {
    "id": "tai-mo-shan",
    "name": "大帽山 Tai Mo Shan",
    "difficulty": "⛰️ 中級",
    "time": "2-3小時來回",
    "distance": "8公里來回",
    "elevation": "大帽山頂 957m",
    "meta_desc": "香港最高峰——957米！大帽山道馬路直上閘口，再行石屎路上山頂，360度俯瞰新界、九龍、港島。冬天有機會結霜！",
    "meta_keywords": "大帽山,香港最高峰,香港行山,荃灣行山,結霜,芒草,日出",
    "image": "https://images.unsplash.com/photo-1516893676001-52fdf7605797?auto=format&fit=crop&w=800&q=80",
    "header_image": "https://images.unsplash.com/photo-1516893676001-52fdf7605797?auto=format&fit=crop&w=1200&q=80",
    "intro": "大帽山係香港最高峰——957米！山頂有天文台雷達站，天氣好時可以 360 度俯瞰新界、九龍、港島、大嶼山，甚至遠眺深圳。秋冬芒草季、冬天結霜、春夏蝴蝶——每個季節都有唔同景致。可以開車上到閘口，再行石屎路到頂，難度大大降低。",
    "route": [
      {"title": "🚌 起步：大帽山郊野公園", "content": "荃灣西站搭 51 號巴士到大帽山郊野公園站落車。或者自駕到荃錦公路嘅大帽山停車場（車位有限，週末好爆）。"},
      {"title": "🛣️ 大帽山道", "content": "由閘口沿大帽山道向上行，全程係石屎馬路，約 4 公里到頂。坡度唔算太斜，但一直上唔停都幾考體能。沿途有多個觀景位，可以唞唞氣影相。"},
      {"title": "🌄 山頂雷達站", "content": "山頂嘅白色波波（天文台雷達站）係大帽山地標。企喺雷達站下面，360 度全景盡收眼底——天氣清朗時可以望到深圳天際線。"},
      {"title": "🌾 芒草季（11-12月）", "content": "秋天嘅大帽山山頭鋪滿金黃色芒草，隨風搖曳。雖然唔及大東山咁出名，但勝在易行，唔使勁辛苦就睇到芒草。"},
      {"title": "❄️ 結霜（冬季限定）", "content": "每年 12-2 月寒流襲港時，大帽山有機會結霜。植物同草地鋪滿白色霜雪，好似落咗雪咁。不過呢段時間山上得 0-2 度，要著足保暖衣物。"}
    ],
    "transport": "🚌 荃灣西站搭 51 號巴士到大帽山郊野公園 / 自駕到荃錦公路停車場",
    "season": "四季皆宜。秋冬睇芒草結霜，春夏蝴蝶翩翩。",
    "tips": [
      "山頂風大溫度低，帶風褸",
      "睇日出要凌晨 4 點出發，帶頭燈",
      "冬天結霜時路面濕滑，要小心",
      "51 號巴士班次疏，check 定時間",
      "閘口到山頂約 1 小時不停行",
      "大帽山茶水亭有簡單補給"
    ],
    "nearby": "落山可以去川龍飲茶（端記/彩龍），西洋菜都好出名。或者去荃灣食嘢。"
  },
  {
    "id": "high-junk-peak",
    "name": "釣魚翁 High Junk Peak",
    "difficulty": "⛰️ 中級",
    "time": "2-6小時",
    "distance": "2-8公里",
    "elevation": "釣魚翁頂 344m",
    "meta_desc": "香港三尖之一，山形尖削似釣魚翁。清水灣半島全景、布袋澳靚景。碎石浮沙較多，著好鞋先好去。",
    "meta_keywords": "釣魚翁,香港三尖,清水灣,布袋澳,香港行山,西貢行山",
    "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
    "header_image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80",
    "intro": "釣魚翁係香港三尖之一（另外兩個係蚺蛇尖同青山），海拔 344 米。因為山形尖削，似一個企喺岸邊釣魚嘅老翁而得名。上到山頂可以俯瞰清水灣半島、布袋澳同牛尾海，景色一絕。路線有多種行法，可以揀短途只上頂，或者挑戰橫走。",
    "route": [
      {"title": "🚌 起步：五塊田", "content": "鑽石山站搭 91 號巴士到五塊田站落車，或者喺寶琳搭 16 號小巴。落車後沿指示上山。"},
      {"title": "🥾 上釣魚翁", "content": "由五塊田上釣魚翁頂約 1 小時，路程短但斜度大，碎石多。呢段路主要係泥路同碎石交錯，要小心落腳。沿途望到清水灣高爾夫球場同海景。"},
      {"title": "📸 山頂打卡", "content": "釣魚翁頂位唔大，可以企嘅空間有限。但 360 度景觀超開揚——清水灣半島、布袋澳、牛尾海、喱啲景色盡收眼底。東望仲可以見到果洲群島。"},
      {"title": "🏁 短途/長途選擇", "content": "短途：上頂原路落返五塊田（約 2 小時）。長途：五塊田 → 釣魚翁 → 田下山 → 大廟（約 6 小時）。後者挑戰性高，要行約 8 公里，上落多。"},
      {"title": "🦐 布袋澳食海鮮", "content": "行完可以落布袋澳食海鮮。布袋澳係一個小漁村，有發記海鮮同幾間海邊餐廳。椒鹽瀨尿蝦同豉椒炒蜆係必試。"}
    ],
    "transport": "🚌 鑽石山站 91 號巴士 / 寶琳 16 號小巴，五塊田落車",
    "season": "🍂 秋冬最佳。夏天極曬，全程冇遮蔭。",
    "tips": [
      "碎石浮沙多，必著防滑行山鞋",
      "長途路線要帶充足糧水",
      "短途上頂原路落最穩陣",
      "釣魚翁頂風大，小心企穩",
      "布袋澳海鮮可以打電話預訂"
    ],
    "nearby": "清水灣沙灘游水、布袋澳食海鮮、或者去坑口食泰國菜。"
  },
  {
    "id": "thousand-islands",
    "name": "千島湖清景台 Thousand Islands Lake",
    "difficulty": "⛰️ 中級",
    "time": "3-4小時",
    "distance": "7公里來回",
    "elevation": "清景台約 250m",
    "meta_desc": "大欖涌水塘被稱為「香港千島湖」，清景台係最佳觀景點。紅葉季節大棠山路兩邊楓香樹轉紅，景色雙重享受。",
    "meta_keywords": "千島湖,清景台,大欖涌水塘,大棠紅葉,元朗行山,香港行山",
    "image": "https://images.unsplash.com/photo-1504664911901-2518a8bfc164?auto=format&fit=crop&w=800&q=80",
    "header_image": "https://images.unsplash.com/photo-1504664911901-2518a8bfc164?auto=format&fit=crop&w=1200&q=80",
    "intro": "大欖涌水塘有「香港千島湖」之稱，因為水塘中有多個小島，高空俯瞰就好似千島湖一樣。清景台係政府搭建嘅觀景台，可以 180 度欣賞千島湖景色。每年 12-1 月仲有大棠紅葉，一次過滿足兩個願望。",
    "route": [
      {"title": "🚌 起步：大棠山路", "content": "朗屏站搭 K66 巴士到大棠山路站落車。沿大棠山路行約 30 分鐘到大棠郊野公園燒烤場。11-1 月紅葉季節嘅大棠山路兩邊楓香樹會轉紅。"},
      {"title": "🌳 大棠郊野公園", "content": "由燒烤場繼續前行約 20 分鐘，經過大棠自然教育徑。沿途仲有機會見到牛牛。"},
      {"title": "🏞️ 千島湖清景台", "content": "到達清景台——一個木製觀景平台。企喺平台向前望，大欖涌水塘同多個小島盡收眼底。水面平靜時倒影超靚，係香港少有嘅湖景。"},
      {"title": "📸 最佳影相時間", "content": "下晝 2-4 點光線最好，太陽喺正前方，千島湖顏色最分明。紅葉季節 12 月中去最準，楓香樹會變到橙紅色。"},
      {"title": "🍁 大棠紅葉", "content": "11 月底到 1 月初係紅葉季節。大棠山路嘅楓香樹轉紅，係香港市區最近嘅紅葉景點。不過人多到好似年宵市場，平日去會好啲。"}
    ],
    "transport": "🚌 朗屏站 K66 巴士到大棠山路站 / 元朗千色廣場搭紅色小巴",
    "season": "🍁 秋冬（11-1月）千島湖＋紅葉雙重享受",
    "tips": [
      "紅葉季節週末極度多人",
      "建議平日去，或者朝早 8 點",
      "清景台有長櫈可以坐低睇景",
      "帶長鏡頭影千島湖全景",
      "大棠山路有士多補給"
    ],
    "nearby": "去元朗食 B 仔涼粉、亞玉豆腐花，或者去流浮山食海鮮。"
  },
  {
    "id": "maclehose-s2",
    "name": "麥理浩徑第二段 MacLehose Trail S2",
    "difficulty": "🏔️ 高手",
    "time": "5-6小時",
    "distance": "14公里",
    "elevation": "上落約 600m",
    "meta_desc": "麥理浩徑精華路段！東壩出發經浪茄、西灣山、鹹田灣、赤徑到北潭凹。沿途沙灘、山景、士多餐蛋麵，體能考驗但景色頂級。",
    "meta_keywords": "麥理浩徑,麥理浩徑第二段,浪茄,西灣,鹹田灣,赤徑,香港行山,長途行山",
    "image": "https://images.unsplash.com/photo-1524704654690-b56c05c78a00?auto=format&fit=crop&w=800&q=80",
    "header_image": "https://images.unsplash.com/photo-1524704654690-b56c05c78a00?auto=format&fit=crop&w=1200&q=80",
    "intro": "麥理浩徑全長 100 公里分 10 段，第二段係公認最精華路段。由萬宜水庫東壩出發，經浪茄、西灣山、西灣、鹹田灣、赤徑，最後到北潭凹。沿途多個水清沙幼嘅沙灘，上山落海不斷重複，體能要求高但景色係全港頂級。",
    "route": [
      {"title": "🚕 起步：萬宜水庫東壩", "content": "鑽石山站搭 96R 巴士（假日限定）到北潭涌，再轉的士到東壩（約 $60）。平日可以喺西貢搭 7 號小巴到北潭涌，再轉的士。東壩嘅六角形岩柱係世界級地質景觀，出發前可以影陣相。"},
      {"title": "🏖️ 浪茄灣", "content": "由東壩行約 30 分鐘落山就到浪茄——被譽為香港最美沙灘之一。水清沙幼，背後係樹林，幾乎冇開發。沙灘左邊有露營位。呢度可以做最後補給——之後就冇士多喇！"},
      {"title": "⛰️ 西灣山", "content": "由浪茄上西灣山係全段最甘嘅部分——要上約 300 米嘅斜路，全程曝曬冇遮蔭。約 45 分鐘到頂，但山頂望到成個西灣、大浪灣同遠眺果洲群島，係全段最佳影相位。"},
      {"title": "🌊 西灣", "content": "落山到西灣——大浪灣四大灘之一。呢度有士多補給，餐蛋麵 $40、冰凍可樂 $15。喺沙灘唞夠先繼續前行。"},
      {"title": "🌉 鹹田灣木橋", "content": "由西灣行約 30 分鐘到鹹田灣。鹹田灣嘅特色係一條木橋橫跨河口，係經典打卡位。呢度同樣有士多，可以食碗豆腐花。"},
      {"title": "🏁 終點：北潭凹", "content": "由鹹田灣經赤徑到北潭凹約 1.5 小時。赤徑係一個古老村落，而家已經荒廢，但嗰片紅樹林同草地好有味道。北潭凹有巴士站搭 94 號或者 96R 返西貢。"}
    ],
    "transport": "🚌 鑽石山 96R 巴士（假日）/ 西貢 7 號小巴到北潭涌，轉的士到東壩。回程北潭凹搭 94/96R",
    "season": "🍂 秋冬最佳。夏天行嘅話要 6am 出發避開烈日。",
    "tips": [
      "全程約 14 公里，5-6 小時",
      "帶 3L 水以上（夏天要 4L）",
      "西灣同鹹田有士多，帶現金",
      "東壩週末的士較多",
      "著好啲行山鞋，路段多碎石",
      "防曬做足，全段冇樹蔭",
      "可以分兩日行，喺西灣露營"
    ],
    "nearby": "返西貢食海鮮、行西貢海傍街、或者去白沙灣游水。"
  },
  {
    "id": "sunset-peak",
    "name": "大東山 Sunset Peak",
    "difficulty": "🏔️ 高手",
    "time": "4小時",
    "distance": "7公里",
    "elevation": "大東山頂 869m",
    "meta_desc": "香港第三高峰，秋冬芒草季嘅王者！爛頭營石屋群配上金黃色芒草，影出嚟好似去咗蘇格蘭高地。",
    "meta_keywords": "大東山,日落大東山,芒草,爛頭營,香港行山,伯公坳,大嶼山行山",
    "image": "https://images.unsplash.com/photo-1580137189272-c9379f8864fd?auto=format&fit=crop&w=800&q=80",
    "header_image": "https://images.unsplash.com/photo-1580137189272-c9379f8864fd?auto=format&fit=crop&w=1200&q=80",
    "intro": "大東山（869米）係香港第三高峰，秋冬芒草季嘅王者。每年 11 月到 12 月，成個山頭鋪滿金黃色嘅芒草，隨風搖曳。爛頭營嘅古老石屋群係標誌性地標，配合芒草景，影出嚟嘅相好似去咗蘇格蘭高地或者新西蘭。",
    "route": [
      {"title": "🚌 起步：伯公坳", "content": "東涌站搭 11 或 23 號巴士到伯公坳落車。伯公坳係大嶼山嘅馬路最高點（約 400 米），由呢度上大東山最短但最斜。留意巴士班次，約 30 分鐘一班。"},
      {"title": "⛰️ 上大東山", "content": "由伯公坳沿石級上大東山，約 1.5 小時到頂。全程約 2.5 公里但上 470 米斜度，好多遊人會行到抖氣。中途有幾個位可以停低回望東涌同機場景色。"},
      {"title": "🏚️ 爛頭營石屋", "content": "大東山山頂附近散落咗多間石屋，係 1920 年代興建嘅度假屋，而家已經荒廢。呢啲石屋配芒草係大東山嘅 signature 影相位。注意石屋係私人財產，唔好入內。"},
      {"title": "🌾 芒草草原", "content": "每年 11 月中到 12 月底，大東山山頭嘅芒草會轉為金黃色。黃昏時分陽光穿過芒草形成夢幻光影。最佳觀賞期係 11 月下旬，太早芒草未黃，太遲已經凋謝。"},
      {"title": "🏁 落山選擇", "content": "原路落返伯公坳（約 1 小時），或者經南山西面落山（約 2 小時，較長但風景開揚）。南山落山後有 3M 巴士返東涌。"}
    ],
    "transport": "🚌 東涌站 11/23 號巴士到伯公坳",
    "season": "🍂 11月中至12月底——芒草季限定！",
    "tips": [
      "山頂風極大，必帶防風褸",
      "芒草季週末人山人海",
      "平日朝早去最正",
      "帶手套，部分路段要手腳並用",
      "落山注意碎石，減慢速度",
      "東涌巴士站可以補給糧水",
      "唔好採摘芒草，留畀其他人欣賞"
    ],
    "nearby": "落山可以去東涌東薈城 outlet 購物，或者去大澳食沙翁睇棚屋。"
  },
  {
    "id": "tung-o-trail",
    "name": "東澳古道 Tung O Ancient Trail",
    "difficulty": "🏔️ 高手",
    "time": "4-5小時",
    "distance": "15公里",
    "elevation": "約 200m 上落",
    "meta_desc": "由東涌行到大澳嘅古時通道，沿途多條古老村落，海景、飛機、港珠澳大橋景色不斷。大澳棚屋同蝦醬一定唔可以錯過。",
    "meta_keywords": "東澳古道,東涌行山,大澳行山,沙螺灣,港珠澳大橋,飛機景,香港行山",
    "image": "https://images.unsplash.com/photo-1559128010-7c1ad6e1b6a5?auto=format&fit=crop&w=800&q=80",
    "header_image": "https://images.unsplash.com/photo-1559128010-7c1ad6e1b6a5?auto=format&fit=crop&w=1200&q=80",
    "intro": "東澳古道係昔日東涌往來大澳嘅主要通道，而家變成超受歡迎嘅行山路線。全程約 15 公里，沿途經過沙螺灣、䃟石灣、深石村等多條古老村落。最正係一路都係海景，可以望到港珠澳大橋同機場跑道，飛機喺頭頂低飛而過超震撼！",
    "route": [
      {"title": "🚌 起步：東涌逸東邨", "content": "東涌站經東薈城行到逸東邨，約 15 分鐘。由逸東邨後面嘅小路行入東澳古道，初段係石屎路。"},
      {"title": "✈️ 機場跑道景", "content": "行約 20 分鐘後到達第一個觀景位，可以望到機場中跑道。飛機降落時離你頭頂只有幾百米，轟鳴聲同震撼感係香港獨有體驗。"},
      {"title": "🏘️ 沙螺灣村", "content": "繼續前行約 40 分鐘到達沙螺灣——一條有 300 年歷史嘅古老村落。村內有天后廟、士多補給，仲可以見到一啲古老嘅村屋同祠堂。"},
      {"title": "🌉 港珠澳大橋景", "content": "經過沙螺灣後，港珠澳大橋會一直喺你右邊。大橋嘅宏偉同海天一色嘅景色，係東澳古道嘅 signature view。"},
      {"title": "🏘️ 深石村", "content": "約行到一半到達深石村，呢度有士多可以唞唞。要注意東澳古道沿途士多數量有限，見到就補給。"},
      {"title": "🏁 終點：大澳", "content": "最後約 1 小時到達大澳。大澳係香港最後嘅棚屋漁村，最出名係沙翁、蝦醬、魷魚乾同棚屋景色。行足一日，喺大澳食完嘢先走。"}
    ],
    "transport": "🚌 東涌站起步，回程大澳搭 11 號巴士返東涌",
    "season": "秋冬最佳。夏天全程曝曬，要有心理準備。",
    "tips": [
      "全程 15 公里，4-5 小時",
      "帶 2L 水，沿途有士多補給",
      "夏天極熱，建議秋冬行",
      "飛機景位要小心，唔好走出馬路",
      "大澳巴士返東涌尾班車約 12mn",
      "大澳沙翁 $15/個，必試"
    ],
    "nearby": "大澳棚屋遊、食沙翁蝦醬、坐船睇中華白海豚。"
  },
  {
    "id": "cape-daguilar",
    "name": "鶴咀 Cape D'Aguilar",
    "difficulty": "🏔️ 高手",
    "time": "3-4小時",
    "distance": "8公里來回",
    "elevation": "約 100m",
    "meta_desc": "香港最東南端海岸保護區，雷音洞海蝕洞、蟹洞海蝕拱、1867年古老燈塔、鯨魚骨標本——世界級地質景觀。",
    "meta_keywords": "鶴咀,鶴咀行山,雷音洞,蟹洞,鶴咀燈塔,香港古蹟,海岸保護區,石澳行山",
    "image": "https://images.unsplash.com/photo-1505228395891-9a51e7e86bf6?auto=format&fit=crop&w=800&q=80",
    "header_image": "https://images.unsplash.com/photo-1505228395891-9a51e7e86bf6?auto=format&fit=crop&w=1200&q=80",
    "intro": "鶴咀（Cape D'Aguilar）係香港最東南端嘅海岸保護區，擁有世界級嘅地質景觀。雷音洞（海蝕洞）、蟹洞（海蝕拱）、1867 年嘅燈塔（香港最古老燈塔）同巨型鯨魚骨標本——一個地方集合咗自然奇觀同歷史古蹟。由筲箕灣出發行石屎路就到，唔使攀山涉水。",
    "route": [
      {"title": "🚌 起步：筲箕灣", "content": "筲箕灣巴士總站搭 9 號巴士到鶴咀站落車（同龍脊同一條線）。落車後沿鶴咀道行入去，全程係石屎路，約 1 小時到鶴咀。"},
      {"title": "🅿️ 鶴咀電台", "content": "步行途中會經過鶴咀電台（而家係香港大學海洋研究所），白色建築物配大海做背景都係一個打卡點。繼續前行。"},
      {"title": "🕳️ 雷音洞", "content": "第一個到達嘅地質奇觀係雷音洞——一個巨大嘅海蝕洞穴。洞口闊約 5 米，行入去可以聽到海浪拍打洞穴嘅迴音。光線由洞頂嘅裂縫射入，形成夢幻光影。入洞要小心地面濕滑。"},
      {"title": "🦀 蟹洞", "content": "繼續前行到蟹洞——一個海蝕拱門，形狀似蟹鉗。企喺拱門中間向外影，可以影到「天圓地方」嘅效果——拱門框住大海同天空，係鶴咀最經典嘅影相位。"},
      {"title": "🗼 鶴咀燈塔", "content": "1867 年建成，係香港最古老燈塔之一。白色圓形塔身配上黑色燈頂，企喺懸崖邊，充滿歷史感。燈塔而家仍然運作。"},
      {"title": "🐋 鯨魚骨", "content": "燈塔附近有一副巨型鯨魚骨標本，係 1955 年喺維港擱淺嘅一條長鬚鯨。骨架長約 10 米，好震撼。呢度亦係影相打卡熱點。"}
    ],
    "transport": "🚌 筲箕灣 9 號巴士到鶴咀站",
    "season": "四季皆宜。大風時唔好靠近岸邊。",
    "tips": [
      "石屎路為主，穿普通波鞋都得",
      "保護區範圍，唔好騷擾海洋生物",
      "大風時唔好靠近岸邊",
      "雷音洞地面濕滑，小心",
      "鶴咀冇士多，自備糧水",
      "建議朝早出發，下晝人多"
    ],
    "nearby": "行完可以去石澳食嘢游水，或者返筲箕灣食東大街小食。"
  },
  {
    "id": "shing-mun",
    "name": "城門水塘 Shing Mun Reservoir",
    "difficulty": "👨‍👩‍👧 親子",
    "time": "2-4小時",
    "distance": "4-8公里",
    "elevation": "約 50m 平路",
    "meta_desc": "新界最受歡迎親子行山路線！環塘徑平坦易行，白千層林道影相超靚，仲有猴子、牛牛同鸚鵡。",
    "meta_keywords": "城門水塘,白千層,親子行山,新界行山,荃灣行山,猴子,燒烤",
    "image": "https://images.unsplash.com/photo-1540979388789-6cee28a1cdc9?auto=format&fit=crop&w=800&q=80",
    "header_image": "https://images.unsplash.com/photo-1540979388789-6cee28a1cdc9?auto=format&fit=crop&w=1200&q=80",
    "intro": "城門水塘係新界最受歡迎嘅親子行山路線。環塘徑全程平坦，樹蔭多，沿途可以見到猴子、牛牛同鸚鵡，細路仔會超級開心。最出名係白千層林道——兩排白色嘅樹幹企喺水邊，影出嚟好似仙境。",
    "route": [
      {"title": "🚌 起步：城門水塘", "content": "荃灣兆和街搭 82 號小巴到城門水塘總站。落車後就係菠蘿壩，呢度有小食亭同燒烤場。"},
      {"title": "🌳 環塘徑", "content": "由菠蘿壩沿環塘徑行，全程平坦石屎路。初段經過燒烤場，之後進入林蔭大道。途中有多個觀景台可以睇水塘景色。"},
      {"title": "🌿 白千層林道", "content": "行約 30 分鐘到達白千層林道——兩排白色嘅白千層樹生長喺水邊，形成一條天然走廊。影相效果超夢幻，尤其係有霧嘅日子。"},
      {"title": "🐒 野生動物", "content": "城門水塘係觀賞野生動物嘅好地方。最常見係猴子（唔好餵食！）、黃牛，仲有色彩繽紛嘅鸚鵡。細路仔會超級興奮。"},
      {"title": "🏁 主壩", "content": "繼續前行到主壩，呢度可以俯瞰成個水塘同山谷。主壩附近有另一條路返回菠蘿壩完成環塘。"}
    ],
    "transport": "🚌 荃灣兆和街 82 號小巴到城門水塘總站",
    "season": "四季皆宜。夏天樹蔭多都算涼爽。",
    "tips": [
      "見到猴子唔好餵食",
      "唔好拎膠袋出嚟，猴子會搶",
      "細路仔著長褲防蚊",
      "主壩風大，小心小朋友",
      "小食亭有簡單補給",
      "可以帶單車，部份路段平坦"
    ],
    "nearby": "落山去荃灣食嘢，或者去川龍飲茶。"
  },
  {
    "id": "yuen-tsuen",
    "name": "元荃古道 Yuen Tsuen Ancient Trail",
    "difficulty": "👨‍👩‍👧 親子",
    "time": "2小時（部分路段）",
    "distance": "4公里（部分）",
    "elevation": "約 150m",
    "meta_desc": "昔日元朗到荃灣嘅主要通道。石龍拱大草地俯瞰荃灣青衣，秋天有芒草睇，唔洗去大東山人擠人。",
    "meta_keywords": "元荃古道,石龍拱,荃灣行山,元朗行山,香港行山,親子行山,芒草",
    "image": "https://images.unsplash.com/photo-1566020110-968e308ec215?auto=format&fit=crop&w=800&q=80",
    "header_image": "https://images.unsplash.com/photo-1566020110-968e308ec215?auto=format&fit=crop&w=1200&q=80",
    "intro": "元荃古道係昔日新界西居民來往元朗同荃灣嘅主要通道。而家變成超受歡迎嘅行山路線。由荃灣港安醫院起步到石龍拱一段最適合新手同親子——石龍拱嘅大草地可以俾小朋友跑嚟跑去，俯瞰荃灣同青衣景色一流。秋天仲有芒草，唔洗去大東山人擠人。",
    "route": [
      {"title": "🚌 起步：荃灣港安醫院", "content": "荃灣站行到港安醫院約 15 分鐘。由醫院旁邊嘅石級上山，初段係幾條村落同農田。"},
      {"title": "🌿 上山路段", "content": "由港安醫院上石龍拱約 45 分鐘，以石級為主，途中有樹蔭。呢段路唔算太斜，小朋友慢慢行都應付到。"},
      {"title": "🏞️ 石龍拱大草地", "content": "石龍拱頂係一大片草地，係成條路線最正嘅部分！小朋友可以喺草地跑嚟跑去，大人可以坐低欣賞荃灣、青衣、藍巴勒海峽嘅全景。"},
      {"title": "📸 芒草+城市景", "content": "秋天（10-12月）石龍拱附近嘅山頭有芒草，配埋城市景同海景，形成獨特嘅對比。呢度影相好有層次感。"},
      {"title": "🏁 回程", "content": "可以原路落返港安醫院（約 45 分鐘），或者繼續前行經元荃古道到元朗（約 4-5 小時）。後者適合有經驗嘅行山人士。"}
    ],
    "transport": "🚌 荃灣站步行 15 分鐘到港安醫院",
    "season": "四季皆宜。秋天芒草季最靚。",
    "tips": [
      "路段多樹蔭，夏天都算涼爽",
      "石龍拱草地可以野餐",
      "帶蚊怕水",
      "回程可以去荃灣廣場食嘢",
      "秋天芒草大約 10 月中開始"
    ],
    "nearby": "荃灣南豐紗廠文創區、三棟屋博物館、川龍飲茶。"
  }
]

PAGE_TPL = '''<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{meta_desc}">
<meta name="keywords" content="{meta_keywords}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://gohk.gamewayz.com/hiking-{id}.html">
<link rel="manifest" href="/manifest.json">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-L9RMXXLKYK"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', 'G-L9RMXXLKYK');
</script>
<meta property="og:title" content="{name} | SunnyHK 行山攻略">
<meta property="og:description" content="{meta_desc}">
<meta property="og:url" content="https://gohk.gamewayz.com/hiking-{id}.html">
<meta property="og:type" content="article">
<meta property="og:image" content="{header_image}">
<meta property="og:locale" content="zh_HK">
<title>{name} | SunnyHK 行山攻略</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;700;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="css/style.css">
<style>
.trail-hero {{
  position: relative; min-height: 50vh; display: flex; align-items: flex-end;
  background: linear-gradient(135deg, var(--primary) 0%, #0f172a 100%);
  overflow: hidden;
}}
.trail-hero img {{
  position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.6;
}}
.trail-hero .overlay {{
  position: absolute; inset: 0;
  background: linear-gradient(transparent 30%, rgba(0,0,0,0.8));
}}
.trail-hero .inner {{
  position: relative; z-index: 1; padding: 40px 24px 48px; width: 100%;
  max-width: 1200px; margin: 0 auto;
}}
.trail-hero h1 {{ font-size: 2.4rem; font-weight: 900; color: white;
  font-family: var(--font-serif); margin-bottom: 8px; }}
.trail-hero .meta {{ display: flex; gap: 16px; flex-wrap: wrap; color: rgba(255,255,255,0.8); font-size: 0.9rem; }}
.trail-hero .meta span {{ background: rgba(255,255,255,0.12); padding: 4px 14px; border-radius: 100px; }}
.trail-content {{ max-width: 800px; margin: 0 auto; padding: 48px 24px; }}
.trail-intro {{ font-size: 1.05rem; line-height: 1.9; color: var(--text-light); margin-bottom: 40px; }}
.step-card {{
  background: var(--card-bg); border-radius: var(--radius-md);
  padding: 24px 28px; margin-bottom: 16px; box-shadow: var(--card-shadow);
  border-left: 4px solid var(--brand);
}}
.step-card h3 {{ margin-bottom: 8px; font-size: 1.1rem; }}
.step-card p {{ color: var(--text-light); font-size: 0.93rem; line-height: 1.8; }}
.trail-tips {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(250px,1fr)); gap: 12px; }}
.trail-tips li {{ background: var(--card-bg); border-radius: var(--radius-sm); padding: 14px 18px;
  list-style: none; box-shadow: var(--card-shadow); font-size: 0.9rem; color: var(--text-light); }}
.trail-tips li::before {{ content: "💡 "; }}
.back-link {{ display: inline-flex; align-items: center; gap: 8px; color: var(--brand);
  font-weight: 600; font-size: 0.9rem; margin-bottom: 32px; }}
.back-link:hover {{ text-decoration: underline; }}
@media (max-width: 768px) {{
  .trail-hero h1 {{ font-size: 1.6rem; }}
  .step-card {{ padding: 18px 20px; }}
}}
</style>
</head>
<body>

<nav class="navbar">
  <div class="inner">
    <a href="index.html" class="logo">
      <div class="sun"><i class="fas fa-sun"></i></div> Sunny<span>HK</span>
    </a>
    <div class="nav-links">
      <a href="index.html" data-i18n="nav-home">首頁</a>
      <div class="nav-dropdown active">
        <a href="explore.html" data-i18n="nav-explore">探索指南</a>
        <div class="nav-dropdown-menu">
          <a href="explore.html" data-i18n="nav-explore-all">🌟 人群指南</a>
          <a href="hiking.html" class="active" data-i18n="nav-hiking">🥾 行山路線</a>
          <a href="snorkeling.html" data-i18n="nav-snorkeling">🤿 浮潛攻略</a>
          <a href="swimming.html" data-i18n="nav-swimming">🏊 游水指南</a>
        </div>
      </div>
      <a href="food.html" data-i18n="nav-food">美食地圖</a>
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
</div>

<div class="trail-hero">
  <img src="{header_image}" alt="{name}" loading="lazy">
  <div class="overlay"></div>
  <div class="inner">
    <a href="hiking.html" class="back-link" style="color:rgba(255,255,255,0.7);margin-bottom:16px;">← 返回行山攻略</a>
    <h1>{name}</h1>
    <div class="meta">
      <span>{difficulty}</span>
      <span>⏱ {time}</span>
      <span>📏 {distance}</span>
      <span>📊 {elevation}</span>
    </div>
  </div>
</div>

<div class="trail-content">
  <p class="trail-intro">{intro}</p>

  <h2 style="margin-bottom:20px;">📋 詳細路線</h2>
  {steps}

  <h2 style="margin:40px 0 20px;">🚌 交通</h2>
  <div class="step-card" style="border-left-color:#3b82f6;">
    <p style="color:var(--text-light);font-size:0.95rem;">{transport}</p>
  </div>

  <h2 style="margin:40px 0 20px;">📅 最佳季節</h2>
  <div class="step-card" style="border-left-color:#8b5cf6;">
    <p style="color:var(--text-light);font-size:0.95rem;">{season}</p>
  </div>

  <h2 style="margin:40px 0 20px;">💡 小貼士</h2>
  <ul class="trail-tips">
    {tips}
  </ul>

  <h2 style="margin:40px 0 20px;">📍 附近好去處</h2>
  <div class="step-card" style="border-left-color:#06b6d4;">
    <p style="color:var(--text-light);font-size:0.95rem;">{nearby}</p>
  </div>

  <div style="text-align:center;margin:48px 0;">
    <a href="hiking.html" class="submit-btn" style="display:inline-block;width:auto;padding:14px 36px;border-radius:100px;text-decoration:none;">
      ← 返回行山攻略
    </a>
  </div>
</div>

<footer class="footer">
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
</footer>

<script src="js/lang.js"></script>
<script src="js/main.js"></script>
<script>navigator.serviceWorker?.register("/sw.js");</script>
</body>
</html>'''

def gen_steps(trail):
    html = ''
    for i, s in enumerate(trail['route']):
        html += f'<div class="step-card">\n'
        html += f'  <h3>{s["title"]}</h3>\n'
        html += f'  <p>{s["content"]}</p>\n'
        html += f'</div>\n'
    return html

def gen_tips(trail):
    html = ''
    for t in trail['tips']:
        html += f'<li>{t}</li>\n'
    return html

for t in TRAILS:
    filename = f'hiking-{t["id"]}.html'
    steps_html = gen_steps(t)
    tips_html = gen_tips(t)
    content = PAGE_TPL.format(
        id=t['id'],
        name=t['name'],
        meta_desc=t['meta_desc'],
        meta_keywords=t['meta_keywords'],
        header_image=t['header_image'],
        difficulty=t['difficulty'],
        time=t['time'],
        distance=t['distance'],
        elevation=t['elevation'],
        intro=t['intro'],
        steps=steps_html,
        transport=t['transport'],
        season=t['season'],
        tips=tips_html,
        nearby=t['nearby']
    )
    with open(filename, 'w') as f:
        f.write(content)
    print(f'Generated: {filename}')

print(f'\nDone! {len(TRAILS)} trail pages generated.')
