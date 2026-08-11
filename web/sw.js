const C='donpepito-v4', TILES='donpepito-tiles-v1';
const CDN=['https://unpkg.com/leaflet@1.9.4/dist/leaflet.css','https://unpkg.com/leaflet@1.9.4/dist/leaflet.js'];
self.addEventListener('install',e=>{self.skipWaiting();e.waitUntil(caches.open(C).then(async c=>{
  await c.addAll(['./','index.html','manifest.json']);
  await Promise.allSettled([c.add('www/'),c.add('www/index.html'),c.add('www/qr-donpepito.png')]);  // web pública (mejor esfuerzo)
  await Promise.allSettled(CDN.map(u=>c.add(u)));                      // Leaflet en caché (mejor esfuerzo)
}))});
self.addEventListener('activate',e=>e.waitUntil((async()=>{
  const keys=await caches.keys();
  await Promise.all(keys.filter(k=>k!==C&&k!==TILES).map(k=>caches.delete(k)));  // borra cachés antiguas
  await self.clients.claim();
})()));
self.addEventListener('fetch',e=>{
  const u=new URL(e.request.url);
  if(u.pathname.startsWith('/api/'))return;                            // API siempre en vivo
  if(u.hostname==='tile.openstreetmap.org'||u.hostname==='tiles.openseamap.org'){
    e.respondWith((async()=>{                                          // teselas del mapa: caché primero
      const c=await caches.open(TILES);
      const hit=await c.match(e.request); if(hit)return hit;
      try{
        const r=await fetch(e.request);
        if(r.ok){ c.put(e.request,r.clone());
          c.keys().then(ks=>{ if(ks.length>400) ks.slice(0,60).forEach(k=>c.delete(k)); }); }
        return r;
      }catch(_){ return new Response('',{status:408}); }
    })());
    return;
  }
  if(e.request.mode==='navigate'){                                     // index/navegación: RED primero
    e.respondWith(fetch(e.request).then(r=>{const cp=r.clone();caches.open(C).then(c=>c.put(e.request,cp));return r})
      .catch(()=>caches.match(e.request).then(r=>r||caches.match('index.html'))));
    return;
  }
  e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request))); // resto: caché con respaldo de red
});
