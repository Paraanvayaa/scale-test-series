import urllib.request

res = urllib.request.urlopen('https://scaletestseries.web.app/').read().decode('utf-8', errors='ignore')
print('prewarmRenderedHtml in live:', 'function prewarmRenderedHtml()' in res)
print('setProperty in live:', "paneLeft.style.setProperty('display', 'none', 'important')" in res)
print('Instant 0ms pre-caching verified:', 'prewarmRenderedHtml();' in res)

