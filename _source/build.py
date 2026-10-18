import sys, pathlib, importlib.util, urllib.parse

OUT = pathlib.Path(sys.argv[1])

PHONE = "+971 XX XXX XXXX"
PHONE_HREF = "tel:+971XXXXXXXXX"
WHATSAPP_HREF = "https://wa.me/971XXXXXXXXX"
EMAIL = "maharadipati.ae@gmail.com"
ADDRESS_HTML = "No: 309, 3rd Floor, Al Khazna Tower<br>(Beside of Nissan Car Showroom)<br>Najda Road, Abu Dhabi, UAE"
MAP_Q = "Al%20Khazna%20Tower%2C%20Abu%20Dhabi"
MAP_EMBED = f"https://maps.google.com/maps?q={MAP_Q}&z=16&output=embed"
MAP_LINK = "https://www.google.com/maps/search/?api=1&query=Al+Khazna+Tower+Abu+Dhabi"

ICON = {
    "visa": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="8" y="14" width="48" height="36" rx="5"/><circle cx="24" cy="30" r="6"/><path d="M14 44c1.5-5 5.5-7 10-7s8.5 2 10 7"/><path d="M38 26h12M38 32h12M38 38h8"/><circle cx="48" cy="12" r="7" stroke-dasharray="3 2.5"/></svg>',
    "passport": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="14" y="6" width="36" height="52" rx="4"/><circle cx="32" cy="27" r="9"/><path d="M23 27h18M32 18c3 3 3 15 0 18M32 18c-3 3-3 15 0 18"/><path d="M24 45h16M27 50h10"/><path d="M50 14l6 3v28l-6 3" opacity=".6"/></svg>',
    "car": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 40v-7l5-12c1-2.5 3-4 5.5-4h27c2.5 0 4.5 1.5 5.5 4l5 12v7a3 3 0 0 1-3 3H11a3 3 0 0 1-3-3z"/><path d="M12 31h40"/><circle cx="19" cy="43" r="5"/><circle cx="45" cy="43" r="5"/><path d="M27 37h10"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.6"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
    "tag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L2 12V2h10l8.6 8.6a2 2 0 0 1 0 2.8z"/><circle cx="7" cy="7" r="1.5"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h9l-1 8 10-12h-9z"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 8.6 8.6 0 0 1-3.9-.9L3 21l1.9-5.1A8.4 8.4 0 1 1 21 11.5z"/><path d="M8 11h.01M12 11h.01M16 11h.01"/></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>',
    "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 2 10 5-10 5L2 7z"/><path d="m2 12 10 5 10-5M2 17l10 5 10-5"/></svg>',
    "tour": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="32" cy="32" r="24"/><path d="m40.5 23.5-5 12-12 5 5-12z"/><circle cx="32" cy="32" r="1.5"/><path d="M32 4v5M32 55v5M4 32h5M55 32h5"/></svg>',
    "plane": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M58 10c-2-2-6-1.5-8.5 1L40 20.5 14 12l-5 5 21 13-9 9.5-8-1.5-4 4 10 5 5 10 4-4-1.5-8L37 35l13 21 5-5-8.5-26 9.5-9.5c2.5-2.5 3-6.5 1-8.5z"/></svg>',
    "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/></svg>',
}

SITE = "https://maharadipati.ae/"
SRC = pathlib.Path(__file__).resolve().parent

# Service order on the homepage and in the Previous/Next links: (slug, icon)
ORDER = [
    ("air-tickets", "plane"),
    ("visas", "visa"),
    ("passport-renewal", "passport"),
    ("car-rental", "car"),
    ("tour-packages", "tour"),
]


def load(name):
    spec = importlib.util.spec_from_file_location(name, SRC / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Page:
    """Where one page lives, and the relative links it needs. English is at the site root, Burmese under my/."""

    def __init__(self, lang, path):
        self.lang, self.path = lang, path            # path: "index.html" or "services/<slug>.html"
        depth = path.count("/") + (lang == "my")
        self.root = "../" * depth                    # from this page back to the site root (assets, styles)
        self.home = "" if path == "index.html" else "../index.html"   # this language's homepage, for #anchors
        self.logo = "index.html" if path == "index.html" else "../index.html"
        self.out = OUT / ("my/" if lang == "my" else "") / path
        here = path.split("/")[-1]                   # this page, relative to itself
        self.en_href = here if lang == "en" else self.root + path
        self.my_href = here if lang == "my" else self.root + "my/" + path
        self.alt_href = self.my_href if lang == "en" else self.en_href

    def url(self, lang):
        p = "" if self.path == "index.html" else self.path
        return SITE + ("my/" if lang == "my" else "") + p


MY_FONT = "https://fonts.googleapis.com/css2?family=Noto+Sans+Myanmar:wght@400;500;600;700&family=Noto+Serif+Myanmar:wght@500;600;700&display=swap"
MY_LABEL_FONT = "https://fonts.googleapis.com/css2?family=Noto+Sans+Myanmar:wght@600&display=swap&text=" + urllib.parse.quote("မြန်မာ")


def cover(C, pg, slug, name, icon, cls):
    """The service image if it has been added to assets/services/, otherwise a purple cover with a gold icon."""
    if (OUT / "assets" / "services" / f"{slug}.jpg").exists():
        lazy = ' loading="lazy"' if cls == "post-img" else ""
        alt = C.T["img_alt"].format(name=name)
        return f'<img class="{cls}" src="{pg.root}assets/services/{slug}.jpg" alt="{alt}"{lazy} width="800" height="800">'
    return f'<div class="{cls} cover-fallback" role="img" aria-label="{name}">{ICON[icon]}</div>'


def head(C, pg, title, desc):
    other = "en" if C.LANG == "my" else "my"
    font = MY_FONT if C.LANG == "my" else MY_LABEL_FONT
    return f"""<!DOCTYPE html>
<html lang="{C.LANG}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script>try{{var l=localStorage.getItem("lang");if(l==="{other}")location.replace("{pg.alt_href}"+location.hash)}}catch(e){{}}</script>
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="alternate" hreflang="en" href="{pg.url('en')}">
  <link rel="alternate" hreflang="my" href="{pg.url('my')}">
  <link rel="alternate" hreflang="x-default" href="{pg.url('en')}">
  <link rel="icon" type="image/png" href="{pg.root}assets/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link href="{font}" rel="stylesheet">
  <link rel="stylesheet" href="{pg.root}styles.css">
</head>
<body>
"""


def lang_switch(C, pg):
    en = ' class="active" aria-current="true"' if C.LANG == "en" else ""
    my = ' class="active" aria-current="true"' if C.LANG == "my" else ""
    return (f'<div class="lang-switch" role="group" aria-label="{C.T["lang_group"]}">'
            f'<a href="{pg.en_href}" lang="en" hreflang="en" data-lang-link="en"{en}>EN</a>'
            f'<a href="{pg.my_href}" lang="my" hreflang="my" data-lang-link="my"{my}>မြန်မာ</a></div>')


def header(C, pg, active=""):
    T = C.T
    def cls(name):
        return ' class="active"' if name == active else ""
    switch = lang_switch(C, pg)
    return f"""  <header class="site-header{' solid' if pg.path != 'index.html' else ''}">
    <div class="container nav">
      <a class="brand" href="{pg.logo}" aria-label="{T['home_label']}">
        <img src="{pg.root}assets/logo-mark.png" alt="">
        <span class="brand-name gold-text">MAHAR ADIPATI<small>Travel Company</small></span>
      </a>
      <ul class="nav-links">
        <li><a href="{pg.home}#services"{cls('services')}>{T['nav_services']}</a></li>
        <li><a href="{pg.home}#about">{T['nav_about']}</a></li>
        <li class="menu-lang">{switch}</li>
      </ul>
      <div class="nav-actions">
        <a class="btn btn-gold nav-cta" href="{pg.home}#contact">{T['contact']}</a>
        {switch}
        <button class="menu-toggle" aria-label="{T['open_menu']}" aria-expanded="false"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>
"""


def footer(C, pg):
    T = C.T
    return f"""  <footer class="site-footer" id="contact">
    <div class="container footer-grid">
      <div>
        <a class="brand" href="{pg.logo}">
          <img src="{pg.root}assets/logo-mark.png" alt="">
          <span class="brand-name gold-text">MAHAR ADIPATI<small>Travel Company</small></span>
        </a>
        <p style="margin-top:20px">{T['footer_blurb']}</p>
        <h4 style="margin-top:28px">{T['quick_links']}</h4>
        <ul class="footer-list">
          <li><a href="{pg.home}#services">{T['our_services']}</a></li>
          <li><a href="{pg.home}#about">{T['nav_about']}</a></li>
        </ul>
      </div>
      <div>
        <h4>{T['visit_office']}</h4>
        <ul class="footer-list">
          <li class="contact-line">{ICON['pin']}<span>{ADDRESS_HTML}</span></li>
          <li class="contact-line">{ICON['phone']}<a href="{PHONE_HREF}">{PHONE}</a></li>
          <li class="contact-line">{ICON['mail']}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li class="contact-line">{ICON['clock']}<span>{C.HOURS}</span></li>
        </ul>
      </div>
      <div>
        <h4>{T['find_map']}</h4>
        <div class="map-wrap">
          <iframe src="{MAP_EMBED}" title="{T['map_title']}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
        </div>
        <a class="map-link" href="{MAP_LINK}" target="_blank" rel="noopener">{T['directions']}</a>
      </div>
    </div>
    <div class="container footer-bottom">
      <span>© <span data-year>2026</span> {T['rights']}</span>
      <span>{T['country']}</span>
    </div>
  </footer>
  <script src="{pg.root}script.js"></script>
</body>
</html>
"""


def cta(C, title=None, text=None):
    T = C.T
    return f"""  <section class="cta">
    <div class="container">
      <div class="cta-box reveal">
        <div>
          <h2 class="gold-text">{title or T['cta_title']}</h2>
          <p>{text or T['cta_text']}</p>
        </div>
        <div class="hero-actions">
          <a class="btn btn-gold" href="{WHATSAPP_HREF}" target="_blank" rel="noopener">{T['whatsapp']}</a>
          <a class="btn btn-ghost" href="{PHONE_HREF}">{T['call']}</a>
        </div>
      </div>
    </div>
  </section>
"""


def build_index(C):
    T = C.T
    pg = Page(C.LANG, "index.html")
    why_cards = ""
    for i, (icon, title, text) in enumerate(C.WHY, 1):
        why_cards += f"""        <div class="why-card reveal" style="transition-delay:{(i-1)%3*0.1:.1f}s">
          <span class="why-num">0{i}</span>
          <span class="why-ico">{ICON[icon]}</span>
          <h3>{title}</h3>
          <p>{text}</p>
        </div>
"""
    cards = ""
    for i, (slug, icon) in enumerate(ORDER, 1):
        name, meta = C.POSTS[slug]
        cards += f"""        <a class="post-card reveal" href="services/{slug}.html" style="transition-delay:{(i-1)*0.1:.1f}s">
          <div class="post-cover"><span class="post-num">0{i}</span>{cover(C, pg, slug, name, icon, "post-img")}</div>
          <div class="post-body">
            <div class="post-meta">{meta}</div>
            <h3>{name}</h3>
            <p>{C.EXCERPTS[slug]}</p>
            <span class="read-more">{T['read_more']}</span>
          </div>
        </a>
"""
    values = "".join(f'          <li><span class="ico">{ICON[icon]}</span><div><strong>{t}</strong><span>{d}</span></div></li>\n'
                     for icon, t, d in C.VALUES)
    html = head(C, pg, T["index_title"], T["index_desc"])
    html += header(C, pg)
    html += f"""
  <section class="hero">
    <img class="hero-pattern" src="{pg.root}assets/logo-mark.png" alt="">
    <div class="container hero-grid">
      <div>
        <span class="eyebrow" style="color:var(--gold-300)">{T['hero_eyebrow']}</span>
        <h1>{T['hero_h1']}</h1>
        <p class="lead">{T['hero_lead']}</p>
        <div class="hero-actions">
          <a class="btn btn-gold" href="#services">{T['hero_btn_services']}</a>
          <a class="btn btn-ghost" href="#contact">{T['hero_btn_office']}</a>
        </div>
      </div>
      <div class="hero-mark"><img src="{pg.root}assets/logo-mark.png" alt="{T['emblem_alt']}"></div>
    </div>
  </section>

  <section class="services" id="services">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">{T['services_eyebrow']}</span>
        <h2>{T['services_h2']}</h2>
        <p>{T['services_p']}</p>
      </div>
      <div class="post-grid">
{cards}      </div>
    </div>
  </section>

  <section class="about" id="about">
    <div class="container about-grid">
      <div class="about-visual reveal">
        <img src="{pg.root}assets/logo-mark.png" alt="">
        <div class="about-badge">
          <strong>{T['badge_title']}</strong>
          <span>{T['badge_text']}</span>
        </div>
      </div>
      <div class="about-copy reveal">
        <span class="eyebrow">{T['about_eyebrow']}</span>
        <h2>{T['about_h2']}</h2>
        <p>{T['about_p1']}</p>
        <p>{T['about_p2']}</p>
        <ul class="values">
{values}        </ul>
      </div>
    </div>
  </section>

  <section class="why" id="why-us">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">{T['why_eyebrow']}</span>
        <h2>{T['why_h2']}</h2>
        <p>{T['why_p']}</p>
      </div>
      <div class="why-grid">
{why_cards}      </div>
    </div>
  </section>

"""
    html += cta(C)
    html += footer(C, pg)
    pg.out.parent.mkdir(parents=True, exist_ok=True)
    pg.out.write_text(html)


def build_articles(C):
    T = C.T
    for i, (slug, icon) in enumerate(ORDER):
        pg = Page(C.LANG, f"services/{slug}.html")
        name, meta = C.POSTS[slug]
        a = C.ARTICLES[slug]
        prev_p = ORDER[i - 1][0] if i > 0 else None
        next_p = ORDER[i + 1][0] if i < len(ORDER) - 1 else None
        nav = '<div class="article-nav">'
        nav += (f'<a href="{prev_p}.html"><small>{T["prev"]}</small>{C.POSTS[prev_p][0]}</a>' if prev_p
                else f'<a href="../index.html#services"><small>{T["back"]}</small>{T["all_services"]}</a>')
        nav += (f'<a href="{next_p}.html" style="text-align:right"><small>{T["next"]}</small>{C.POSTS[next_p][0]}</a>' if next_p
                else f'<a href="../index.html#about" style="text-align:right"><small>{T["next"]}</small>{T["about_us"]}</a>')
        nav += "</div>"
        html = head(C, pg, T["article_title"].format(title=a["title"]), a["lead"])
        html += header(C, pg, "services")
        html += f"""
  <section class="article-hero">
    <img class="hero-pattern" src="{pg.root}assets/logo-mark.png" alt="">
    <div class="container article-hero-grid">
      <div>
        <div class="breadcrumb"><a href="../index.html">{T['crumb_home']}</a> / <a href="../index.html#services">{T['crumb_services']}</a> / {name}</div>
        <span class="eyebrow" style="color:var(--gold-300)">0{i+1} · {meta}</span>
        <h1 style="font-size:clamp(2rem,4.6vw,3.2rem)">{a['title']}</h1>
        <p class="lead">{a['lead']}</p>
        <div class="article-meta"><span>{T['desk']}</span></div>
      </div>
      {cover(C, pg, slug, name, icon, "article-hero-img")}
    </div>
  </section>

  <article class="article">
    <div class="container">
{a['body']}
      {nav}
    </div>
  </article>

"""
        html += cta(C, T["cta_article_title"].format(name=name, name_lower=name.lower()))
        html += footer(C, pg)
        pg.out.parent.mkdir(parents=True, exist_ok=True)
        pg.out.write_text(html)


for content in ("content_en", "content_my"):
    C = load(content)
    build_index(C)
    build_articles(C)

print("built", sorted(str(p.relative_to(OUT)) for p in OUT.rglob("*.html")))
