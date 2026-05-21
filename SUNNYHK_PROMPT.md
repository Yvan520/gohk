# SunnyHK 網站完整 Prompt

將以下內容直接貼俾任何 AI coding agent（Claude、ChatGPT 等），即可生成同風格網站。

---

## 專案概述

建立一個名為 **SunnyHK** 的香港旅遊靈感平台，定位為「小紅書風格」的靜態網站，部署在 GitHub Pages。

- **風格調性**：溫暖、陽光、真摯、帶有粵語口吻，像朋友推薦而非教科書
- **目標用戶**：華語年輕旅客，附加英文支援給外國人
- **技術限制**：純靜態 HTML/CSS/JS，無後端，無框架，無 build step
- **圖片來源**：Unsplash（所有 photo ID 必須手動驗證 HTTP 200，不可用 AI 偽造 ID）
- **部署方式**：GitHub Pages + 自定義網域

## 設計系統

### 色彩
```css
--brand: #f59e0b          /* 主色：溫暖金黃 */
--brand-light: #fbbf24
--brand-dark: #d97706
--primary: #1e3a5f        /* 深藍輔助 */
--accent-coral: #f472b6   /* 粉紅點綴 */
--accent-teal: #14b8a6    /* 青綠點綴 */
--bg-warm: #fefcf5        /* 暖白背景 */
--text: #1e293b            /* 主文字 */
--text-light: #64748b     /* 次要文字 */
--text-muted: #94a3b8     /* 弱文字 */
--card-bg: #ffffff
--card-shadow: 0 4px 24px rgba(0,0,0,0.06)
--card-shadow-hover: 0 12px 40px rgba(0,0,0,0.1)
```

### 字體
```css
--font-serif: 'Noto Serif SC', serif   /* 標題用 */
--font-sans: 'Plus Jakarta Sans', ...   /* 內文用 */
```

### 圓角
```css
--radius-sm: 12px; --radius-md: 20px; --radius-lg: 32px; --radius-xl: 40px
```
所有元素使用大圓角，營造柔和親切感。

### 陰影
卡片陰影輕柔（`0 4px 24px rgba(0,0,0,0.06)`），hover 時加深並微微上移（`translateY(-4px)`）。

### 過渡
所有互動元素使用 `0.3s cubic-bezier(0.4,0,0.2,1)`。

## 頁面結構（6+1 頁）

### 1. index.html（首頁）
- **Navigation Bar**：固定頂部，透明背景（hero 上白色文字），滾動 80px 後變半透明白底。Logo 用金色漸層圓形太陽 + "SunnyHK"。導航連結：首頁／探索指南／美食地圖／實用資訊／香港故事／關於
- **語言切換**：三個圓角按鈕並排 [繁 | 简 | EN]，active 的 highlight
- **暗色模式切換**：月亮/太陽 icon 按鈕
- **Mobile 漢堡選單**：螢幕 <768px 顯示，側滑抽屜 + 半透明遮罩
- **Hero 區**：100vh 全屏，深色漸層 overlay + 背景圖片 Ken Burns 緩慢縮放動畫。內容：標籤徽章（"香港 · 發掘屬於你嘅角落"）、主標題（含漸層 highlight）、副標題、搜尋下拉選單（5 種人格選項）+「出發」按鈕
- **統計橫幅**：4 項數據（50+ 目的地／6 種指南／100% 真實／24/7 發呆）
- **年齡分組卡片**：6 張卡片（親子／青年／上班族／銀髮／I人發呆／3日路線），每張有背景圖、彩色標籤、標題、描述，點擊可跳轉到 explore.html 對應錨點
- **發呆地圖**：6 張特徵卡片（西九海濱／中環碼頭／石澳海灘／南蓮園池／誠品書店／大帽山）
- **最新故事預覽**：從 localStorage 載入最新 3 則故事
- **Footer**：4 欄（品牌介紹／探索連結／關於連結／社群媒體），深色底 `#0f172a`

### 2. explore.html（探索指南）
- **頁首橫幅**：深色漸層
- **側邊欄**：黏性定位，7 個分類錨點連結（親子／青年／上班族／銀髮／發呆／攝影機位／行程路線）
- **搜尋輸入框**：即時過濾目的地卡片
- **7 個分類區域**，每個包含多張 `.place-card`
- **Place Card 結構**：
```html
<div class="place-card">
  <div class="thumb"><img src="..." alt="..." loading="lazy"></div>
  <div class="info">
    <h3>📛 名稱</h3>
    <p>一句描述</p>
    <div class="tags"><span>標籤1</span><span>標籤2</span><span>標籤3</span></div>
    <div class="tip"><i class="fas fa-train"></i> 交通貼士</div>
    <div class="tip"><i class="fas fa-clock"></i> 時間貼士</div>
    <div class="tip"><i class="fas fa-camera"></i> 攝影貼士</div>
    <div class="tip"><i class="fas fa-yen-sign"></i> 價格貼士</div>
    <div class="tip"><i class="fas fa-utensils"></i> 美食貼士</div>
  </div>
</div>
```
- **Modal**：點擊卡片開啟全螢幕 modal，有上下張導航（prev/next 按鈕 + 鍵盤左右鍵）、Escape 關閉、body scroll lock

### 3. stories.html（香港故事）
- 訊息留言板風格，資料存於 localStorage
- **發佈表單**：暱稱、來自、分類（5 種）、內容、送出
- **篩選按鈕**：全部／夜景🌇／美食🍜／治癒💛／親子👨‍👩‍👧／獨旅🎒
- **故事卡片**：大頭貼（暱稱首字母）、暱稱、來源、時間、分類色標、內容、喜歡按鈕
- **預設種子資料**：40 則故事硬編碼在 `<script>` 中，首次載入時寫入 localStorage
- **CSS Masonry**：使用 `columns: 4` 搭配 `break-inside: avoid`

### 4. food.html（美食地圖）
- 側邊欄 10 個分類（茶餐廳／街頭小食／燒味／點心／糖水／打冷／車仔麵／煲仔飯／海鮮／隱藏驚喜）
- 每個分類下多張餐廳卡片（格式與 place-card 相同）

### 5. tips.html（實用資訊）
- 頂部快速參考條（999／HK$150／24min 等）
- 側邊欄目錄
- 8 個分類：交通／通訊／語言／省錢／購物／禮儀／實用 App／緊急情況
- 貼士卡片使用左側 brand 色邊框

### 6. about.html（關於）
- 平台使命、3 張特色卡片
- FAQ 手風琴（點擊展開）
- 私隱政策

### 7. 404.html
- 簡潔風格，404 標題漸層色，提示用戶檢查 URL 大小寫

## JavaScript 功能清單

### main.js
- 主題切換（localStorage 持久化）
- 語言按鈕點擊（呼叫 lang.js 的 setLang）
- Navbar 滾動效果（80px 閾值）
- Mobile menu 抽屜開關
- IntersectionObserver 滾動淡入動畫
- FAQ 手風琴
- Age card 點擊跳轉
- Hero 搜尋下拉跳轉
- Sidebar active 狀態
- Stories CRUD（localStorage 讀寫、渲染、喜歡 toggle）
- 目的地搜尋即時過濾
- Place card modal（prev/next/keyboard）

### lang.js
- 繁→簡字元對照表（~680 對），使用 TreeWalker 遍歷 DOM 文字節點
- 簡→繁反向對照表（自動生成）
- 英文翻譯物件（~100 組 UI 字串），使用 `data-i18n` / `data-i18n-placeholder` / `data-i18n-option` 屬性對應
- 三種模式：trad / simp / en
- localStorage 持久化，切換時重整頁面
- 自動初始化（DOMContentLoaded）

## 內容策略
- 所有文字使用傳統繁體中文（zh-HK），混入粵語口吻（嘅、咗、嗰、啲）
- 分類邏輯：依人格/節奏分類，而非傳統景點分類
- 每個目的地包含 5 個實用貼士（交通／時機／攝影／價格／美食）
- 種子故事來自小紅書、HK01、OpenRice 等真實來源改編

## 第三方資源
- Google Fonts：Noto Serif SC + Plus Jakarta Sans
- Font Awesome 6（free CDN）
- Unsplash 圖片（所有 photo ID 需經 API 驗證 HTTP 200）

## Responsive Breakpoints
- 1024px：sidebar 變水平、footer 變 2 欄
- 768px：導航隱藏、漢堡顯示、hero 搜尋變直向、footer 單欄、grid 變單欄
- 480px：stories 單欄、hero 字體縮小

## 建議生成方式
將以上 prompt 一次過俾 AI，然後補充以下指示：
1. 「先用 HTML 建立 index.html，包含完整設計系統和所有頁面結構」
2. 「用 CSS 實現完整設計系統，包括 dark mode」
3. 「用 JS 實現語言切換、主題切換、modal、stories CRUD」
4. 每完成一個步驟要停下來讓你檢查

---

以上內容已包含所有設計決策、元件結構、互動行為和技術限制，AI 應該可以直接生成一個風格一致的網站。
