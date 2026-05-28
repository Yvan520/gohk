#!/usr/bin/env python3
import re
import os

BASE = '/Users/admin/Documents/test/sunnyhk'

items = [
  # ====== HK ======
  {
    'slug': 'swimming-victoria-park',
    'emoji': '🏊', 'name': '維多利亞公園游泳池', 'query_name': '維多利亞公園游泳池',
    'tags': '50米池, 暖水, 地鐵可達',
    'card_tips': ['港鐵銅鑼灣站E出口，行5分鐘', '清潔日：逢星期二', '室內暖水池，冬天都游得'],
    'intro': '維多利亞公園游泳池（Victoria Park Swimming Pool）係港島最大型公眾泳池之一，位於銅鑼灣核心地帶。無論你係認真練水嘅泳手，定係想帶仔女玩水嘅家長，呢度都滿足到你。室內池冬天有暖水，全年游得！',
    'features': [
      ('🏊 50米標準主池', '戶外50米主池係練水首選，8條泳線夠闊落。水質清徹，長期保持標準溫度。'),
      ('🏠 室內暖水池', '冬天最正就係室內暖水池，keep住約28°C，落雨或者冬天都照游可也。'),
      ('🤸 跳水池', '設有1米同3米跳板，鍾意玩跳水嘅朋友可以盡情發揮。'),
      ('👶 幼童池', '親子友好！另有幼童池，水淺又安全，細路仔玩水好開心。'),
    ],
    'transport': '🚇 港鐵銅鑼灣站E出口，沿記利佐治街行5分鐘就到。\n🚌 多條巴士路線途經銅鑼灣，喺維多利亞公園或皇室堡落車。\n🚐 附近有小巴站，交通非常方便。',
    'facilities': '• 50米戶外主池（8線）\n• 室內暖水池\n• 跳水池（1米/3米跳板）\n• 幼童池\n• 更衣室及淋浴間\n• 儲物櫃（$5按金）\n• 小食亭',
    'tips': [
      '朝早6:30開門就去，水最乾淨、人最少',
      '室內暖水池冬天開放，全年游得',
      '清潔日逢星期二，記住避開',
      '銅鑼灣食肆選擇多，游完水可以去利舞臺廣場搵食',
      '泳池附近有維園，可以跑步熱身',
    ],
    'nearby': '游完水過馬路就係維多利亞公園，可以喺草地抖下。行5分鐘到皇室堡商場，食買玩齊全。銅鑼灣SOGO、時代廣場都喺附近，行街食飯超方便。',
    'img': 'https://images.unsplash.com/photo-1572341304527-1f08b3d13c47?auto=format&fit=crop&w=1200&q=80',
    'lat': 22.282, 'lng': 114.190,
  },
  {
    'slug': 'swimming-kennedy-town',
    'emoji': '🌊', 'name': '堅尼地城游泳池', 'query_name': '堅尼地城游泳池',
    'tags': '西環, 新裝修, 暖水',
    'card_tips': ['港鐵堅尼地城站C出口，行3分鐘', '清潔日：逢星期四', '游完水去西環碼頭影日落'],
    'intro': '堅尼地城游泳池（Kennedy Town Swimming Pool）係西環友嘅游水天堂！新裝修之後設施好新淨，室內暖水池加戶外池嘅組合深受街坊喜愛。最正係游完水行去海旁吹海風，或者去西環碼頭睇日落。',
    'features': [
      ('🏊 50米戶外主池', '標準50米戶外池，夏天開放，陽光下暢泳夠爽快。'),
      ('🏠 室內暖水池', '25米室內暖水池，冬天keep住暖水，西環友冬天練水首選。'),
      ('✨ 新裝修設施', '近年完成翻新，更衣室、淋浴間、地板全部煥然一新，乾淨企理。'),
      ('🌊 近海位置', '泳池距離海旁只有幾分鐘路程，游完水去海邊散步吹風，係西環獨有體驗。'),
    ],
    'transport': '🚇 港鐵堅尼地城站C出口，沿士美菲路行3分鐘就到。\n🚌 乘搭5B、10、101等巴士喺堅尼地城站落車。\n🚐 小巴23線途經泳池附近。',
    'facilities': '• 50米戶外主池\n• 25米室內暖水池\n• 習泳池\n• 更衣室及淋浴間\n• 儲物櫃\n• 無障礙設施',
    'tips': [
      '室內暖水池全年開放，冬天最啱去',
      '游完水必去西環碼頭睇日落，約5分鐘路程',
      '清潔日逢星期四，留意開放時間',
      '朝早8點前人較少，可以游得暢快',
      '附近有咖啡店，游完水可以嘆杯咖啡',
    ],
    'nearby': '游完水行去西環碼頭（Instagram打卡熱點）睇日落係必做行程。海旁一帶有好多特色咖啡店同餐廳。仲可以沿海旁散步去堅尼地城海濱長廊，吹海風超寫意。',
    'img': 'https://images.unsplash.com/photo-1560090995-01632a28895b?auto=format&fit=crop&w=1200&q=80',
    'lat': 22.281, 'lng': 114.127,
  },
  {
    'slug': 'swimming-morrison-hill',
    'emoji': '🏅', 'name': '摩理臣山游泳池', 'query_name': '摩理臣山游泳池',
    'tags': '灣仔, 室內暖水, 打工仔',
    'card_tips': ['港鐵銅鑼灣站A出口，行8分鐘', '清潔日：逢星期三', '附近利舞台廣場好多好嘢食'],
    'intro': '摩理臣山游泳池（Morrison Hill Swimming Pool）係灣仔區嘅熱門泳池，好多年輕打工仔放工之後嚟游水減壓放鬆。室內暖水池全年開放，戶外池夏天先開，無論你係咩時候想游都有得游。',
    'features': [
      ('🏠 室內暖水池', '25米室內暖水池，冬天都有暖水，全年開放唔受天氣影響。'),
      ('🌞 戶外習泳池', '夏天開放嘅戶外習泳池，陽光下游水特別暢快。'),
      ('👶 幼童池', '設有幼童池，水深較淺，家長可以帶埋小朋友一齊嚟。'),
      ('📍 位置便利', '位於灣仔同銅鑼灣交界，附近有好多餐廳，游完水搵食好方便。'),
    ],
    'transport': '🚇 港鐵銅鑼灣站A出口，沿摩理臣山道行8分鐘。\n🚌 乘搭1、5B、8X、10等巴士喺摩理臣山道落車。\n🚐 附近有電車站，搭電車都好方便。',
    'facilities': '• 室內暖水池\n• 戶外習泳池\n• 幼童池\n• 更衣室及淋浴間\n• 儲物櫃\n• 洗手間及無障礙設施',
    'tips': [
      '放工時段（6-8pm）比較多人，想避開人流可以朝早或夜晚去',
      '室內池全年開放，冬天都游得',
      '清潔日逢星期三，記住留意',
      '附近利舞台廣場有好多餐廳，游完水可以去食好西',
      '泳池無提供風筒，建議自備',
    ],
    'nearby': '摩理臣山泳池地點超方便，行5分鐘到利舞台廣場同時代廣場，有齊各式餐廳。銅鑼灣購物區近在咫尺，行街睇戲唱K全部行路就到。',
    'img': 'https://images.unsplash.com/photo-1576610616656-d3aa5d1f4534?auto=format&fit=crop&w=1200&q=80',
    'lat': 22.278, 'lng': 114.178,
  },
  # ====== Kowloon ======
  {
    'slug': 'swimming-kowloon-park',
    'emoji': '🌴', 'name': '九龍公園游泳池', 'query_name': '九龍公園游泳池',
    'tags': '尖沙咀, 50米池, 遊客必到',
    'card_tips': ['港鐵尖沙咀站A1出口，行5分鐘', '清潔日：逢星期三', '摩天輪景觀主池'],
    'intro': '九龍公園游泳池（Kowloon Park Swimming Pool）係尖沙咀市中心嘅一片綠洲！喺鬧市之中有個咁大嘅泳池，真係難得。50米主池、跳水池、室內暖水池樣樣齊，仲有日光浴場可以曬太陽。行完海港城過嚟游水消暑，一流！',
    'features': [
      ('🏊 50米戶外主池', '標準50米主池，旁邊可以望到摩天輪，游水都有靚景。'),
      ('🏠 室內暖水池', '25米室內暖水池，冬天游都得，尖沙咀區冬天必去。'),
      ('🤸 跳水池', '設有跳水池，適合跳水愛好者。'),
      ('🌞 日光浴場', '香港少見嘅日光浴場，可以喺池畔曬太陽放鬆，好似去咗度假咁。'),
      ('👶 幼童池', '另有幼童池，親子友善。'),
    ],
    'transport': '🚇 港鐵尖沙咀站A1出口，沿彌敦道行5分鐘，經九龍公園入口進入。\n🚌 多條巴士路線途經尖沙咀，喺尖沙咀警署或海防道落車。\n🚐 搭天星小輪到尖沙咀碼頭，行10分鐘就到。',
    'facilities': '• 50米戶外主池\n• 25米室內暖水池\n• 跳水池\n• 日光浴場\n• 幼童池\n• 更衣室及淋浴間\n• 儲物櫃\n• 小食亭',
    'tips': [
      '游水時可以望到摩天輪景觀，打卡一流',
      '週末比較多人，建議平日朝早去',
      '清潔日逢星期三，留意開放時間',
      '游完水可以行九龍公園，有鳥湖同雕塑徑',
      '附近海港城、K11 Musea有大量餐廳選擇',
    ],
    'nearby': '九龍公園本身已經好好行，有鳥湖、迷宮花園同雕塑徑。行出嚟就係海港城同K11 Musea，購物餐飲應有盡有。行多幾步到尖沙咀海濱長廊，可以睇維港夜景。',
    'img': 'https://images.unsplash.com/photo-1519315901367-f34ff9154487?auto=format&fit=crop&w=1200&q=80',
    'lat': 22.301, 'lng': 114.170,
  },
  {
    'slug': 'swimming-kwun-tong',
    'emoji': '🏗️', 'name': '觀塘游泳池', 'query_name': '觀塘游泳池',
    'tags': '東九龍, 50米, 翻新',
    'card_tips': ['港鐵觀塘站D出口，行10分鐘', '清潔日：逢星期四', '多條巴士線直達'],
    'intro': '觀塘游泳池（Kwun Tong Swimming Pool）係東九龍最大型泳池，服務觀塘、藍田、秀茂坪一帶嘅街坊。50米主池加室內暖水池嘅組合，無論你練水定休閒都得。近年翻新過，設施乾淨齊全。',
    'features': [
      ('🏊 50米主池', '標準50米戶外主池，8條泳線，練水首選。'),
      ('🏠 室內暖水池', '25米室內暖水池，冬天都游得，東九龍冬天游水好去處。'),
      ('✨ 翻新設施', '近年完成翻新，更衣室同淋浴間都好乾淨，整體感覺煥然一新。'),
      ('👶 習泳池', '設有習泳池，適合初學者同小朋友。'),
    ],
    'transport': '🚇 港鐵觀塘站D出口，沿觀塘道行10分鐘。\n🚌 多條巴士線直達泳池門口，包括1A、11C、14、15、16等。\n🚐 小巴路線密集，交通極方便。',
    'facilities': '• 50米戶外主池\n• 25米室內暖水池\n• 習泳池\n• 更衣室及淋浴間\n• 儲物櫃\n• 無障礙設施',
    'tips': [
      '翻新後設施好新淨，整體體驗大提升',
      '清潔日逢星期四，留意安排',
      '平日朝早人少，水質最佳',
      '附近觀塘廣場同APM有大把餐廳',
      '泳池門口有多條巴士線，交通方便',
    ],
    'nearby': '游完水行10分鐘去APM，觀塘最大型商場，食買玩一條龍。或者去觀塘海濱長廊散步，海景日落好靚。觀塘駱駝漆大廈有好多隱世美食同文青小店。',
    'img': 'https://images.unsplash.com/photo-1530541937845-3b3b40fb082b?auto=format&fit=crop&w=1200&q=80',
    'lat': 22.312, 'lng': 114.226,
  },
  {
    'slug': 'swimming-lai-chi-kok',
    'emoji': '🌳', 'name': '荔枝角公園游泳池', 'query_name': '荔枝角公園游泳池',
    'tags': '美孚, 戶外池, 街坊',
    'card_tips': ['港鐵美孚站C出口，行8分鐘', '清潔日：逢星期二', '隔離荔枝角公園'],
    'intro': '荔枝角公園游泳池（Lai Chi Kok Park Swimming Pool）係美孚街坊最愛嘅夏日好去處！戶外50米主池夠大，夏天人流好旺。旁邊就係荔枝角公園，游完水可以去散步野餐，一家大細都啱玩。',
    'features': [
      ('🏊 50米戶外主池', '大型50米戶外主池，夏天開放，空間感十足。'),
      ('🤸 跳水池', '設有跳水池，鍾意挑戰跳水嘅朋友可以玩過癮。'),
      ('👶 兒童池', '設有兒童專用池，水深較淺，小朋友玩水好安全。'),
      ('🌳 公園相鄰', '隔離係荔枝角公園，游完水可以直接去公園散步野餐。'),
    ],
    'transport': '🚇 港鐵美孚站C出口，沿荔枝角公園行8分鐘。\n🚌 6C、6D、40、86等巴士途經美孚。\n🚐 小巴線直達美孚各區。',
    'facilities': '• 50米戶外主池\n• 跳水池\n• 兒童池\n• 更衣室及淋浴間\n• 儲物櫃\n• 洗手間',
    'tips': [
      '夏天人流好旺，下晝去可能要排隊，建議朝早去',
      '清潔日逢星期二，記住留意',
      '游完水去荔枝角公園行下，有中式亭園同體育館',
      '附近美孚廣場有餐廳同超市',
      '戶外池夏天先開，秋冬季留意開放安排',
    ],
    'nearby': '荔枝角公園係香港其中一個最大嘅公園，有中式亭園、嶺南之風同體育館。游完水喺公園散步野餐好寫意。美孚廣場有超市同餐廳，日常所需一應俱全。',
    'img': 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=1200&q=80',
    'lat': 22.338, 'lng': 114.136,
  },
  # ====== NT ======
  {
    'slug': 'swimming-tuen-mun-northwest',
    'emoji': '🏊', 'name': '屯門西北游泳池', 'query_name': '屯門西北游泳池',
    'tags': '旗艦級, 暖水, 按摩池',
    'card_tips': ['港鐵屯門站轉輕鐵', '清潔日：逢星期三', '新界最好泳池之一'],
    'intro': '屯門西北游泳池（Tuen Mun North West Swimming Pool）係新界西嘅旗艦級泳池！室內暖水池、戶外50米主池、跳水池、兒童池、按摩池——應有盡有。設施超新淨，冬天室內暖水池keep住28度，舒服到唔想走。',
    'features': [
      ('🏊 50米戶外主池', '標準50米戶外主池，空間闊落，陽光暢泳好爽。'),
      ('🏠 室內暖水池', '冬天最正！室內池約28°C暖水，冬天都可以舒服游水。'),
      ('💆 按摩池', '少見嘅按摩池設施，游完水可以沖下按摩 relax 下。'),
      ('🤸 跳水池', '設有跳水池，適合跳水訓練同娛樂。'),
      ('👶 兒童池', '另設兒童池，親子友善。'),
    ],
    'transport': '🚇 港鐵屯門站轉乘輕鐵（507/610/614/615等）到屯門泳池站。\n🚌 K53巴士直達泳池附近。\n🚐 多條屯門區巴士線途經。',
    'facilities': '• 50米戶外主池\n• 室內暖水池\n• 跳水池\n• 按摩池\n• 兒童池\n• 更衣室及淋浴間\n• 儲物櫃\n• 小食亭',
    'tips': [
      '新界最好嘅公眾泳池之一，設施頂級',
      '冬天去室內暖水池最正，28°C暖水好舒服',
      '清潔日逢星期三，留意安排',
      '按摩池係必試項目，游完水 relax 一流',
      '平日朝早去人最少，可以慢慢游',
    ],
    'nearby': '游完水可以行去屯門公園，或者去屯門市廣場食飯行街。附近仲有黃金海岸商場同沙灘，週末可以玩足一日。屯門河畔有人行徑，散步睇風景好舒服。',
    'img': 'https://images.unsplash.com/photo-1574643156929-51fa098b0394?auto=format&fit=crop&w=1200&q=80',
    'lat': 22.404, 'lng': 113.971,
  },
  {
    'slug': 'swimming-sha-tin',
    'emoji': '🏇', 'name': '沙田賽馬會游泳池', 'query_name': '沙田賽馬會游泳池',
    'tags': '沙田, 50米, 集體回憶',
    'card_tips': ['港鐵沙田站步行15分鐘', '清潔日：逢星期三', '游完水可以踩單車去大埔'],
    'intro': '沙田賽馬會游泳池（Sha Tin Jockey Club Swimming Pool）係沙田地標級泳池！50米主池、跳水池、室內暖水池，仲有日光浴場同超大兒童池。沙田友由細游到大，滿載集體回憶。城門河隔離，環境清幽。',
    'features': [
      ('🏊 50米戶外主池', '標準50米主池，8條泳線，係沙田最大嘅公眾泳池。'),
      ('🏠 室內暖水池', '25米室內暖水池，冬天都游得，全年無休。'),
      ('🤸 跳水池', '設有跳水池，跳水愛好者必到。'),
      ('🌞 日光浴場', '泳池旁邊有日光浴場，曬太陽放鬆好地方。'),
      ('👶 超大兒童池', '兒童池面積大，小朋友可以盡情玩水。'),
    ],
    'transport': '🚇 港鐵沙田站步行15分鐘，或搭小巴60K直達。\n🚌 多條巴士路線途經沙田市中心。\n🚐 小巴60K、62K等直達泳池。',
    'facilities': '• 50米戶外主池\n• 25米室內暖水池\n• 跳水池\n• 日光浴場\n• 兒童池\n• 更衣室及淋浴間\n• 儲物櫃\n• 小食亭',
    'tips': [
      '游完水可以踩單車沿城門河去大埔（約30分鐘）',
      '清潔日逢星期三，記住避開',
      '沙田地標泳池，集體回憶滿滿',
      '朝早6:30開門就係最佳時機，人少水清',
      '沙田市中心有好多餐廳，游完水可以去新城市廣場',
    ],
    'nearby': '泳池鄰近城門河，可以踩單車或者散步。行10分鐘到沙田新城市廣場，食買玩齊全。史諾比開心世界喺附近，小朋友最愛。城門河兩岸嘅單車徑可以一路踩到大埔。',
    'img': 'https://images.unsplash.com/photo-1530541937845-3b3b40fb082b?auto=format&fit=crop&w=1200&q=80',
    'lat': 22.385, 'lng': 114.188,
  },
  {
    'slug': 'swimming-tseung-kwan-o',
    'emoji': '🌅', 'name': '將軍澳游泳池', 'query_name': '將軍澳游泳池',
    'tags': '將軍澳, 落地玻璃, 山景',
    'card_tips': ['港鐵將軍澳站B出口，行10分鐘', '清潔日：逢星期四', '落地玻璃窗打卡一流'],
    'intro': '將軍澳游泳池（Tseung Kwan O Swimming Pool）係將軍澳唯一公眾泳池，設計新穎，最特色係落地玻璃採光一流，游水時可以望到窗外翠綠山景，景觀開揚。假日比較多人，建議平日朝早去享受寧靜。',
    'features': [
      ('🏠 室內暖水池', '室內暖水池配落地玻璃，自然光灑落，游水心情都特別好。'),
      ('🌞 戶外池', '夏天開放嘅戶外池，陽光下游水好爽。'),
      ('🪟 落地玻璃設計', '全場落地玻璃係最大賣點，採光一流，打卡位處處。'),
      ('⛰️ 翠綠山景', '泳池望向山邊，游水時可以欣賞窗外翠綠景色。'),
    ],
    'transport': '🚇 港鐵將軍澳站B出口，沿寶康路行10分鐘。\n🚌 多條巴士線直達泳池附近，包括796系、98系等。\n🚐 小巴線密集，將軍澳各區都可直達。',
    'facilities': '• 室內暖水池\n• 戶外池\n• 習泳池\n• 更衣室及淋浴間\n• 儲物櫃\n• 洗手間',
    'tips': [
      '落地玻璃窗打卡一流，記得影相',
      '平日朝早人少，可以享受落地玻璃嘅自然光',
      '清潔日逢星期四，留意開放時間',
      '泳池設計新穎，設施好新淨',
      '游完水可以去將軍澳海濱長廊散步',
    ],
    'nearby': '泳池附近有將軍澳運動場同香港單車館公園。行15分鐘到將軍澳海濱長廊，海景優美，適合散步跑步。將軍澳中心同PopCorn商場有齊餐廳同商店。',
    'img': 'https://images.unsplash.com/photo-1519315901367-f34ff9154487?auto=format&fit=crop&w=1200&q=80',
    'lat': 22.307, 'lng': 114.258,
  },
  # ====== Non-gov ======
  {
    'slug': 'swimming-golden-beach',
    'emoji': '🏖️', 'name': '黃金泳灘 / 加多利灣', 'query_name': '黃金泳灘 加多利灣',
    'tags': '免費, 沙灘, 救生員',
    'card_tips': ['屯門搭K53巴士直達', '夏天4-6月水質最佳', '黃金海岸商場好多餐廳'],
    'intro': '黃金泳灘（Golden Beach）同加多利灣（Cafeteria Beach）係屯門青山灣一帶嘅免費沙灘，水清沙幼，有更衣室同淋浴設施。夏天好多屯門友去游水曬太陽。唔使錢，仲有救生員當值。黃金海岸商場喺附近，食買玩一條龍。',
    'features': [
      ('🏖️ 免費沙灘', '完全免費開放，唔使入場費，啱晒 budget travel 嘅朋友。'),
      ('🏊 水清沙幼', '青山灣一帶水質唔錯，夏天4-6月水質最佳，清澈見底。'),
      ('🛟 救生員當值', '泳灘有救生員當值，游水更安心。'),
      ('🚿 完善設施', '設有更衣室、淋浴設施同小食亭，方便沙灘遊客。'),
    ],
    'transport': '🚌 屯門站轉乘K53巴士直達黃金泳灘。\n🚐 小巴43系同巴士52X、61M等途經。\n🚗 駕駛人士可以使用黃金泳灘停車場（收費）。',
    'facilities': '• 沙灘區域\n• 更衣室\n• 淋浴設施\n• 小食亭\n• 救生員服務\n• 停車場',
    'tips': [
      '夏天4-6月水質最佳，最適合游水',
      '週末好多人，建議平日去',
      '黃金海岸商場有好多餐廳同商店',
      '游完水後可以喺沙灘睇日落',
      '帶備防曬用品，沙灘較少遮蔭',
    ],
    'nearby': '行幾分鐘就到黃金海岸商場，有齊餐廳、超市同商店。黃金海岸遊艇會風景優美，係打卡熱點。喺沙灘睇完日落可以行去附近海鮮餐廳食晚飯。',
    'img': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80',
    'lat': 22.371, 'lng': 113.995,
  },
  {
    'slug': 'swimming-repulse-bay',
    'emoji': '🌊', 'name': '淺水灣', 'query_name': '淺水灣',
    'tags': '港島, 外國人, 海景餐廳',
    'card_tips': ['中環搭6/6X/260巴士直達', '週末好多人，平日最正', '影相打卡熱點'],
    'intro': '淺水灣（Repulse Bay）係港島最出名嘅沙灘，水清環境靚，設施完善（更衣室、淋浴、小食亭）。好多外國人同本地人去曬太陽游水。附近有The Pulse商場同好多海景餐廳，游完水可以去chill。',
    'features': [
      ('🏖️ 港島最靚沙灘', '淺水灣係香港最具代表性嘅沙灘之一，水清沙幼，環境優美。'),
      ('🌊 水質清澈', '港島南區水質長期保持良好，適合游水消暑。'),
      ('🛟 完善設施', '更衣室、淋浴設施、小食亭、救生員一應俱全。'),
      ('🍽️ 海景餐廳', '沙灘旁邊有The Pulse商場同多間海景餐廳酒吧。'),
    ],
    'transport': '🚌 中環交易廣場搭6/6X/260巴士直達淺水灣海灘（約30分鐘）。\n🚌 銅鑼灣搭63/65巴士直達。\n🚗 駕駛人士可以使用淺水灣停車場（假日較緊張）。',
    'facilities': '• 沙灘區域\n• 更衣室\n• 淋浴設施\n• 小食亭\n• 救生員服務\n• 停車場\n• The Pulse商場',
    'tips': [
      '週末好多人，平日去最舒服',
      '淺水灣係影相打卡熱點，記得帶相機',
      '鎮海樓公園有觀音像同天后像，值得一睇',
      'The Pulse商場有好多海景餐廳同咖啡店',
      '游完水可以沿海濱長廊散步去深水灣（約30分鐘）',
    ],
    'nearby': '淺水灣鎮海樓公園有大型觀音像同天后像，係著名地標。The Pulse商場有齊餐廳服飾店。行30分鐘可以去深水灣，或者搭車去赤柱食海鮮行市集。',
    'img': 'https://images.unsplash.com/photo-1537956965359-7573183d1f57?auto=format&fit=crop&w=1200&q=80',
    'lat': 22.236, 'lng': 114.196,
  },
  {
    'slug': 'swimming-hotel-day-pass',
    'emoji': '🏨', 'name': '酒店泳池 Day Pass', 'query_name': '酒店泳池 Day Pass',
    'tags': '酒店, Day Pass, 人少',
    'card_tips': ['Klook/KKDay有酒店泳池通行證賣', '約$200-500/日', '無邊際泳池打卡一流'],
    'intro': '想游水但又想享受酒店級設施？香港好多酒店有泳池Day Pass！例如愉景灣酒店、黃金海岸酒店、帝京酒店等，$200-500全日任游，仲可以用健身室同更衣室。環境靚、人少、有毛巾供應，適合週末chill relax。',
    'features': [
      ('🏨 酒店級享受', '酒店泳池環境優美，人少唔使同人逼，有毛巾供應同更衣室。'),
      ('💰 Day Pass收費', '約$200-500/日，視乎酒店等級同設施。全日任游，仲可以用健身室。'),
      ('📱 平台預訂', 'Klook、KKDay等平台有酒店泳池通行證，可以事先預訂。'),
      ('🏊 無邊際泳池', '部分酒店有無邊際泳池，海景打卡一流。'),
    ],
    'transport': '唔同酒店位置不同，詳情請參閱Klook/KKDay。\n🚇 愉景灣酒店：中環搭船到愉景灣。\n🚌 黃金海岸酒店：屯門轉K53巴士。\n🚇 帝京酒店：旺角東站步行5分鐘。',
    'facilities': '• 酒店泳池\n• 健身室\n• 更衣室及淋浴間\n• 毛巾供應\n• 儲物櫃\n• 部分包餐飲',
    'tips': [
      'Klook/KKDay不時有優惠，可以留意折扣',
      '平日去更少人，體驗更好',
      '無邊際泳池建議帶水機或電話防水袋，方便打卡',
      '酒店泳池通常較細，適合休閒多過練水',
      '部分酒店Day Pass包餐飲，抵玩好多',
    ],
    'nearby': '視乎選擇嘅酒店而定。愉景灣酒店可以順便玩愉景灣，黃金海岸酒店可以行黃金海岸商場同泳灘，帝京酒店就去旺角市中心行街食飯。',
    'img': 'https://images.unsplash.com/photo-1473496169904-658ba7c44d8a?auto=format&fit=crop&w=1200&q=80',
    'lat': 22.298, 'lng': 114.169,
  },
  {
    'slug': 'swimming-hksi',
    'emoji': '🏅', 'name': '香港體育學院泳池', 'query_name': '香港體育學院泳池',
    'tags': '專業級, 50米, 訓練',
    'card_tips': ['港鐵火炭站步行10分鐘', '公眾開放時段有限', '泳會訓練班可以報名'],
    'intro': '如果你係認真游水嘅人，香港體育學院（HKSI）嘅泳池係頂級選擇。50米標準池、專業計時系統，奧運級水質。不過只限註冊運動員或特定時段開放俾公眾。一般泳友可以考慮參加泳會訓練班，體驗專業級訓練。',
    'features': [
      ('🏊 奧運級50米池', '標準50米比賽級泳池，配備專業計時系統，水質達奧運標準。'),
      ('📊 專業設施', '專業跳台、電子計時板、分道線等設施一應俱全。'),
      ('🎯 訓練環境', '香港頂尖運動員訓練場地，水溫水質嚴格控制。'),
      ('👨‍🏫 泳會訓練', '可以報名參加體育學院舉辦嘅泳會訓練班，接受專業指導。'),
    ],
    'transport': '🚇 港鐵東鐵線火炭站步行10分鐘。\n🚌 乘搭88K、88X等巴士喺火炭村落車。\n🚐 小巴線60P、60K等途經。',
    'facilities': '• 50米標準比賽池\n• 專業計時系統\n• 跳台\n• 熱身池\n• 更衣室及淋浴間\n• 健身室（學員專用）',
    'tips': [
      '公眾開放時段有限，出發前先查官網確認',
      '泳會訓練班可以報名參加，專業教練指導',
      '適合認真練水嘅泳手，休閒游泳可能更適合去公眾泳池',
      '火炭站附近有好多工廈餐廳，游完水可以去覓食',
      '體育學院設施頂級，水質同環境都係香港最佳之一',
    ],
    'nearby': '火炭站附近有好多工廈餐廳同咖啡店，近年成為文青好去處。亦可以去沙田踩單車或行新城市廣場。距離香港中文大學唔遠，可以順便參觀大學校園。',
    'img': 'https://images.unsplash.com/photo-1559128010-7c1ad6e1b6a5?auto=format&fit=crop&w=1200&q=80',
    'lat': 22.395, 'lng': 114.202,
  },
]

def make_page(item):
    features_html = ''.join(
        '<div class="step-card">\n  <h3>' + f[0] + '</h3>\n  <p>' + f[1] + '</p>\n</div>\n'
        for f in item['features']
    )
    tips_html = ''.join(
        '    <li>' + t + '</li>\n' for t in item['tips']
    )
    emoji = item['emoji']
    name = item['name']
    slug = item['slug']
    imgsrc = item['img']
    intro = item['intro']
    tags = item['tags']
    tag1 = tags.split(',')[0].strip()
    tag2 = tags.split(',')[1].strip()
    tag3 = tags.split(',')[2].strip()
    transport = item['transport']
    facilities = item['facilities']
    nearby = item['nearby']
    intro120 = intro[:120]
    return f'''<!DOCTYPE html>
<html lang="zh-HK">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{intro120}">
<meta name="keywords" content="{name},香港游水,香港泳池,游水指南,{tags}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://gohk.gamewayz.com/{slug}.html">
<link rel="manifest" href="/manifest.json">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-L9RMXXLKYK"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', 'G-L9RMXXLKYK');
</script>
<meta property="og:title" content="{emoji} {name} | SunnyHK 游水攻略">
<meta property="og:description" content="{intro120}">
<meta property="og:url" content="https://gohk.gamewayz.com/{slug}.html">
<meta property="og:type" content="article">
<meta property="og:image" content="{imgsrc}">
<meta property="og:locale" content="zh_HK">
<title>{emoji} {name} | SunnyHK 游水攻略</title>
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
.trail-tips li::before {{ content: "\U0001f4a1 "; }}
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
  <img src="{imgsrc}" alt="{name}" loading="lazy">
  <div class="overlay"></div>
  <div class="inner">
    <a href="swimming.html" class="back-link" style="color:rgba(255,255,255,0.7);margin-bottom:16px;">← 返回游水指南</a>
    <h1>{emoji} {name}</h1>
    <div class="meta">
      <span>{tag1}</span>
      <span>{tag2}</span>
      <span>{tag3}</span>
    </div>
  </div>
</div>

<div class="trail-content">
  <p class="trail-intro">{intro}</p>

  <h2 style="margin-bottom:20px;">🏊 泳池特色</h2>
{features_html}

  <h2 style="margin:40px 0 20px;">🚌 交通詳情</h2>
  <div class="step-card" style="border-left-color:#3b82f6;">
    <p style="color:var(--text-light);font-size:0.95rem;white-space:pre-line;">{transport}</p>
  </div>

  <h2 style="margin:40px 0 20px;">📋 設施一覽</h2>
  <div class="step-card" style="border-left-color:#8b5cf6;">
    <p style="color:var(--text-light);font-size:0.95rem;white-space:pre-line;">{facilities}</p>
  </div>

  <h2 style="margin:40px 0 20px;">💡 小貼士</h2>
  <ul class="trail-tips">
{tips_html}
  </ul>

  <h2 style="margin:40px 0 20px;">📍 附近好去處</h2>
  <div class="step-card" style="border-left-color:#06b6d4;">
    <p style="color:var(--text-light);font-size:0.95rem;">{nearby}</p>
  </div>

  <div style="text-align:center;margin:48px 0;">
    <a href="swimming.html" class="submit-btn" style="display:inline-block;width:auto;padding:14px 36px;border-radius:100px;text-decoration:none;">
      ← 返回游水指南
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


def update_swimming_html():
    path = os.path.join(BASE, 'swimming.html')
    with open(path, 'r') as f:
        html = f.read()

    # For each item, find its place-card by h3 content and add button wrapper
    for item in items:
        search_text = item['emoji'] + ' ' + item['name']
        button_html = f'''                <div style="display:flex;gap:10px;margin-top:12px;flex-wrap:wrap;">
                  <a href="{item['slug']}.html" class="hiking-card-btn" style="background:var(--brand);color:white;"><i class="fas fa-book-open"></i> 完整攻略</a>
                  <a href="map.html?q={item['query_name']}" target="_blank" class="hiking-card-btn" style="border:1.5px solid var(--brand);color:var(--brand);background:transparent;"><i class="fas fa-map-marked-alt"></i> 睇地圖位置</a>
                </div>'''

        # Find the last tip div before closing </div> of .info
        # Pattern: find the h3 containing search_text, then from there find the closing </div> of .info
        pattern = re.escape(search_text) + r'.*?(</div>)\s*</div>'
        match = re.search(pattern, html, re.DOTALL)

        if match:
            original = match.group()
            # Insert button_html before the final </div> (which closes .info)
            # The regex captures everything up to the last </div> of .info
            # We need to insert BEFORE that final </div>
            # Find the position of the last </div> in the match
            last_close = original.rstrip().rfind('</div>')
            if last_close != -1:
                before = original[:last_close]
                modified = before + '\n' + button_html + '\n              </div>'
            else:
                modified = original.rstrip() + '\n' + button_html + '\n              </div>'
            html = html.replace(original, modified, 1)
        else:
            print(f"WARNING: Could not find card for {search_text}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated swimming.html")


def update_map_data():
    path = os.path.join(BASE, 'js', 'map-data.js')
    with open(path, 'r') as f:
        content = f.read()

    new_entries = []
    for item in items:
        name_escaped = item['name'].replace("'", "\\'")
        emoji = item['emoji']
        lat = item['lat']
        lng = item['lng']
        slug = item['slug']
        new_entries.append(f"  {{ id: '{slug}', name: '{name_escaped}', emoji: '{emoji}', category: 'swimming', lat: {lat}, lng: {lng}, section: 'swimming', link: '{slug}.html' }},")

    entries_str = '\n'.join(new_entries)

    # Insert before the final ];
    content = content.replace('];', entries_str + '\n];')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated map-data.js")


if __name__ == '__main__':
    for item in items:
        slug = item['slug']
        filepath = os.path.join(BASE, f'{slug}.html')
        page = make_page(item)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(page)
        print(f"Created {slug}.html")

    update_swimming_html()
    update_map_data()
    print("\nDone! All 13 swimming detail pages generated.")
