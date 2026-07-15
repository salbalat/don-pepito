const C='mojito-boat-v1';
self.addEventListener('install',e=>{self.skipWaiting();e.waitUntil(caches.open(C).then(c=>c.addAll(['./','index.html','manifest.json'])))});
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('fetch',e=>{
  const u=new URL(e.request.url);
  if(u.pathname.startsWith('/api/'))return; // API siempre en vivo
  e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request)));
});
