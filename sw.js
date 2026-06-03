const CACHE = 'sunnyhk-v3';
const STATIC_CACHE = 'sunnyhk-static-v3';
const IMAGE_CACHE = 'sunnyhk-img-v3';

const PRECACHE_URLS = [
  '/',
  '/css/style.css',
  '/js/lang.js',
  '/js/main.js',
  '/js/map-data.js',
  '/manifest.json',
  '/icon.svg',
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(STATIC_CACHE).then(cache => cache.addAll(PRECACHE_URLS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== STATIC_CACHE && k !== IMAGE_CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  const isImage = /\.(jpg|jpeg|png|gif|webp|avif|svg)$/.test(url.pathname);
  const isPage = event.request.mode === 'navigate';
  const isStatic = /\.(css|js|json)$/.test(url.pathname);

  if (isImage) {
    event.respondWith(cacheFirst(event.request, IMAGE_CACHE));
  } else if (isStatic) {
    event.respondWith(cacheFirst(event.request, STATIC_CACHE));
  } else if (isPage) {
    event.respondWith(networkFirst(event.request));
  }
});

async function cacheFirst(request, cacheName) {
  const cached = await caches.match(request);
  if (cached) return cached;
  const response = await fetch(request);
  if (response.ok) {
    const cache = await caches.open(cacheName);
    cache.put(request, response.clone());
  }
  return response;
}

async function networkFirst(request) {
  try {
    const response = await fetch(request);
    if (response.ok) {
      const cache = await caches.open(CACHE);
      cache.put(request, response.clone());
    }
    return response;
  } catch {
    const cached = await caches.match(request);
    return cached || new Response('Offline', { status: 503 });
  }
}
