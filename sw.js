/* Service worker for luweilab.com
 * Strategy:
 *  - HTML pages:      network-first (content always fresh; cache = offline fallback)
 *  - Assets (css/js/img/fonts): stale-while-revalidate (instant repeat visits,
 *    refreshed silently in the background; at worst one visit stale)
 *  - Cross-origin requests: bypassed entirely
 * CACHE_VERSION is stamped with the build time, so every deploy forces a full
 * cache refresh on the next visit.
 */
const CACHE_VERSION = "1791740973";
const HTML_CACHE = `html-${CACHE_VERSION}`;
const ASSET_CACHE = `assets-${CACHE_VERSION}`;

self.addEventListener("install", (event) => {
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys
          .filter((k) => !k.endsWith(CACHE_VERSION))
          .map((k) => caches.delete(k))
      )
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  const isHTML =
    req.mode === "navigate" ||
    (req.headers.get("accept") || "").includes("text/html");

  if (isHTML) {
    event.respondWith(
      fetch(req)
        .then((res) => {
          if (res.ok) {
            const clone = res.clone();
            caches.open(HTML_CACHE).then((c) => c.put(req, clone));
          }
          return res;
        })
        .catch(() =>
          caches.match(req).then((cached) => cached || Response.error())
        )
    );
    return;
  }

  // stale-while-revalidate for everything else same-origin
  event.respondWith(
    caches.match(req).then((cached) => {
      const network = fetch(req)
        .then((res) => {
          if (res.ok) {
            const clone = res.clone();
            caches.open(ASSET_CACHE).then((c) => c.put(req, clone));
          }
          return res;
        })
        .catch(() => cached);
      return cached || network;
    })
  );
});
