import sys, pathlib

OUT = pathlib.Path(sys.argv[1])

PHONE = "+971 XX XXX XXXX"
PHONE_HREF = "tel:+971XXXXXXXXX"
WHATSAPP_HREF = "https://wa.me/971XXXXXXXXX"
EMAIL = "maharadipati.ae@gmail.com"
HOURS = "Mon – Sat, 9:00 AM – 9:00 PM"
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

POSTS = [
    ("air-tickets", "International Air Tickets", "plane", "Air Tickets"),
    ("visas", "Visas & Travel Services", "visa", "Visas & Travel"),
    ("passport-renewal", "Passport & Document Services", "passport", "Passport & Documents"),
    ("car-rental", "Car Rental & Transfers", "car", "Car Rental & Transfers"),
    ("tour-packages", "Tour Packages", "tour", "Tour Packages"),
]


def cover(slug, name, icon, root, cls):
    """The service image if it has been added to assets/services/, otherwise a purple cover with a gold icon."""
    if (OUT / "assets" / "services" / f"{slug}.jpg").exists():
        lazy = ' loading="lazy"' if cls == "post-img" else ""
        return f'<img class="{cls}" src="{root}assets/services/{slug}.jpg" alt="{name} by Mahar Adipati Travel Company"{lazy} width="800" height="800">'
    return f'<div class="{cls} cover-fallback" role="img" aria-label="{name}">{ICON[icon]}</div>'


def head(title, desc, root):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="icon" type="image/png" href="{root}assets/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{root}styles.css">
</head>
<body>
"""


def header(root, active=""):
    home = f"{root}index.html" if root else ""
    def cls(name):
        return ' class="active"' if name == active else ""
    return f"""  <header class="site-header{' solid' if root else ''}">
    <div class="container nav">
      <a class="brand" href="{root}index.html" aria-label="Mahar Adipati home">
        <img src="{root}assets/logo-mark.png" alt="">
        <span class="brand-name gold-text">MAHAR ADIPATI<small>Travel Company</small></span>
      </a>
      <ul class="nav-links">
        <li><a href="{home}#services"{cls('services')}>Services</a></li>
        <li><a href="{home}#about">About Us</a></li>
      </ul>
      <div class="nav-actions">
        <a class="btn btn-gold nav-cta" href="{home}#contact">Contact Us</a>
        <button class="menu-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>
"""


def footer(root):
    home = f"{root}index.html" if root else ""
    return f"""  <footer class="site-footer" id="contact">
    <div class="container footer-grid">
      <div>
        <a class="brand" href="{root}index.html">
          <img src="{root}assets/logo-mark.png" alt="">
          <span class="brand-name gold-text">MAHAR ADIPATI<small>Travel Company</small></span>
        </a>
        <p style="margin-top:20px">Visas and passport renewal from one friendly desk in Abu Dhabi. Walk in, call or message us — we'll take it from there.</p>
        <h4 style="margin-top:28px">Quick Links</h4>
        <ul class="footer-list">
          <li><a href="{home}#services">Our Services</a></li>
          <li><a href="{home}#about">About Us</a></li>
        </ul>
      </div>
      <div>
        <h4>Visit Our Office</h4>
        <ul class="footer-list">
          <li class="contact-line">{ICON['pin']}<span>{ADDRESS_HTML}</span></li>
          <li class="contact-line">{ICON['phone']}<a href="{PHONE_HREF}">{PHONE}</a></li>
          <li class="contact-line">{ICON['mail']}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li class="contact-line">{ICON['clock']}<span>{HOURS}</span></li>
        </ul>
      </div>
      <div>
        <h4>Find Us on the Map</h4>
        <div class="map-wrap">
          <iframe src="{MAP_EMBED}" title="Mahar Adipati office location on Google Maps" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
        </div>
        <a class="map-link" href="{MAP_LINK}" target="_blank" rel="noopener">Get directions on Google Maps →</a>
      </div>
    </div>
    <div class="container footer-bottom">
      <span>© <span data-year>2026</span> Mahar Adipati Travel Company. All rights reserved.</span>
      <span>Abu Dhabi, United Arab Emirates</span>
    </div>
  </footer>
  <script src="{root}script.js"></script>
</body>
</html>
"""


def cta(root, title="Ready to get started?", text="Visit us at Al Khazna Tower or send us a message — we usually reply within the hour."):
    return f"""  <section class="cta">
    <div class="container">
      <div class="cta-box reveal">
        <div>
          <h2 class="gold-text">{title}</h2>
          <p>{text}</p>
        </div>
        <div class="hero-actions">
          <a class="btn btn-gold" href="{WHATSAPP_HREF}" target="_blank" rel="noopener">Chat on WhatsApp</a>
          <a class="btn btn-ghost" href="{PHONE_HREF}">Call Us</a>
        </div>
      </div>
    </div>
  </section>
"""


# ---------------------------------------------------------------- index
EXCERPTS = {
    "air-tickets": ("One-way, return and multi-city flights worldwide, for individuals, families and groups, at the best fares we can find for your dates.", "4 min read"),
    "visas": ("Visit visas for nine destinations, UAE visa change (inside, A2A and B2B), plus hotels, insurance and entry tickets.", "6 min read"),
    "passport-renewal": ("Passport renewal and extension, degree attestation, Vacation Leave Return Certificates and Certificates of Identification.", "6 min read"),
    "car-rental": ("Airport pick-up and drop-off, plus car rental by the day, week or month, self-drive or with a driver.", "5 min read"),
    "tour-packages": ("Desert safaris, dinner cruises, private yacht rental and UAE sightseeing tours, planned and booked for you.", "4 min read"),
}

WHY = [
    ("shield", "Checked before it's submitted", "Every application is reviewed by our team first. Most delays and rejections start with a small mistake, and we catch them early."),
    ("tag", "Upfront, honest pricing", "Government fees and our service charge are itemised before you pay. No hidden extras and no surprises later."),
    ("chat", "Updates without chasing", "We keep you informed by phone or WhatsApp at every stage, so you always know where your file stands."),
    ("user", "One person, start to finish", "You deal with the same friendly person who knows your case, not a different call-centre agent every time."),
    ("layers", "Everything under one roof", "Air tickets, visas, passport renewal, car rental and tours from a single desk. One visit, one contact, less running around."),
    ("pin", "Easy to find in Abu Dhabi", "Walk in at Al Khazna Tower on Najda Road, beside the Nissan showroom, right in the heart of the city."),
]
why_cards = ""
for i, (icon, title, text) in enumerate(WHY, 1):
    why_cards += f"""        <div class="why-card reveal" style="transition-delay:{(i-1)%3*0.1:.1f}s">
          <span class="why-num">0{i}</span>
          <span class="why-ico">{ICON[icon]}</span>
          <h3>{title}</h3>
          <p>{text}</p>
        </div>
"""

cards = ""
for i, (slug, name, icon, meta) in enumerate(POSTS, 1):
    excerpt, read = EXCERPTS[slug]
    cards += f"""        <a class="post-card reveal" href="services/{slug}.html" style="transition-delay:{(i-1)*0.1:.1f}s">
          <div class="post-cover"><span class="post-num">0{i}</span>{cover(slug, name, icon, "", "post-img")}</div>
          <div class="post-body">
            <div class="post-meta">{meta}</div>
            <h3>{name}</h3>
            <p>{excerpt}</p>
            <span class="read-more">Read the full guide</span>
          </div>
        </a>
"""

index = head("Mahar Adipati | Air Tickets, Visas, Passports, Car Rental & Tours in Abu Dhabi",
             "Mahar Adipati Travel Company in Abu Dhabi — international air tickets, visa services, passport renewal, car rental and tour packages from one trusted team at Al Khazna Tower, Najda Road.", "")
index += header("")
index += f"""
  <section class="hero">
    <img class="hero-pattern" src="assets/logo-mark.png" alt="">
    <div class="container hero-grid">
      <div>
        <span class="eyebrow" style="color:var(--gold-300)">Travel Company · Abu Dhabi</span>
        <h1>Your journey,<br><span class="gold-text">handled with care.</span></h1>
        <p class="lead">Air tickets, visas, passport renewal, car rental and tours from one trusted team. Tell us where you're going and we'll take care of the paperwork and the plans, so you can enjoy the trip.</p>
        <div class="hero-actions">
          <a class="btn btn-gold" href="#services">Explore Our Services</a>
          <a class="btn btn-ghost" href="#contact">Visit Our Office</a>
        </div>
      </div>
      <div class="hero-mark"><img src="assets/logo-mark.png" alt="Mahar Adipati mandala emblem"></div>
    </div>
  </section>

  <section class="services" id="services">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Our Services</span>
        <h2>Guides from our travel desk</h2>
        <p>Practical guides to everything we do, from flights and visas to cars and tours. Read up, then let us handle the rest.</p>
      </div>
      <div class="post-grid">
{cards}      </div>
    </div>
  </section>

  <section class="about" id="about">
    <div class="container about-grid">
      <div class="about-visual reveal">
        <img src="assets/logo-mark.png" alt="">
        <div class="about-badge">
          <strong>Al Khazna Tower</strong>
          <span>Office 309, Najda Road, Abu Dhabi</span>
        </div>
      </div>
      <div class="about-copy reveal">
        <span class="eyebrow">About Us</span>
        <h2>Travel made easier, one client at a time</h2>
        <p><strong>Mahar Adipati Travel Company</strong> is an Abu Dhabi travel and documentation office. We help residents, visitors and families with everything a trip involves: international air tickets, visas, passport renewals, a reliable car once you arrive, and tours and experiences to enjoy while you're here.</p>
        <p>Every application is reviewed by a real person before it's submitted. We explain what's needed, quote our fees up front and keep you updated until the job is finished. Our clients come back, and send their friends, because we treat their plans as if they were our own.</p>
        <ul class="values">
          <li><span class="ico">{ICON['tag']}</span><div><strong>Clear pricing</strong><span>Know the full cost before you commit.</span></div></li>
          <li><span class="ico">{ICON['bolt']}</span><div><strong>Fast follow-up</strong><span>We track every file until it's done.</span></div></li>
          <li><span class="ico">{ICON['heart']}</span><div><strong>Personal care</strong><span>Guidance from people, not call centres.</span></div></li>
          <li><span class="ico">{ICON['home']}</span><div><strong>One roof</strong><span>Flights, visas, passports, cars and tours in one place.</span></div></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="why" id="why-us">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Why Choose Us</span>
        <h2>Why travellers choose <span class="gold-text">Mahar Adipati</span></h2>
        <p>Paperwork goes better when someone careful is handling it. Here's what you get when you work with us.</p>
      </div>
      <div class="why-grid">
{why_cards}      </div>
    </div>
  </section>

"""
index += cta("")
index += footer("")
(OUT / "index.html").write_text(index)


# ---------------------------------------------------------------- articles
ARTICLES = {
"air-tickets": dict(
    title="International Air Tickets",
    lead="Flights from the UAE to anywhere in the world. Tell us where and when, and we'll find the fare and book it for you.",
    read="4 min read",
    body="""
      <p>Searching dozens of websites for the right flight takes time, and it's easy to miss a better fare or a baggage rule. Tell us where you're going and when, and we'll compare the options and book the one that suits you.</p>

      <h2>What we book</h2>
      <div class="option-grid">
        <div class="option"><strong>One-way &amp; Return</strong><span>Flights from the UAE to destinations worldwide, or back home.</span></div>
        <div class="option"><strong>Multi-city Trips</strong><span>Visiting more than one country? We plan the route and book every leg.</span></div>
        <div class="option"><strong>Families &amp; Groups</strong><span>Seats for the whole family or group on the same booking.</span></div>
        <div class="option"><strong>Changes &amp; Rebooking</strong><span>Help changing your travel dates when plans change, subject to the airline's fare rules.</span></div>
      </div>
      <div class="callout"><p><strong>Fares change daily.</strong> Send us your destination, travel dates and number of passengers, and we'll give you the current fare and baggage allowance before you book.</p></div>

      <h2>What we need from you</h2>
      <ul>
        <li>Each passenger's name exactly as it appears in their passport</li>
        <li>A copy of each passport, valid for at least <strong>6 months</strong> from your travel date</li>
        <li>Your travel dates, and whether your dates are flexible</li>
        <li>The visa for your destination, if one is needed (we can arrange that too)</li>
      </ul>

      <h2>Make it a complete trip</h2>
      <p>Book your flight together with your <a href="visas.html">visit visa, hotel and travel insurance</a>, and we'll make sure all your dates line up. Flying into the UAE? We can also arrange an <a href="car-rental.html">airport pick-up</a>.</p>

      <h2>Book in four steps</h2>
      <ol class="steps">
        <li><strong>Tell us your trip.</strong> Destination, dates and number of passengers.</li>
        <li><strong>Choose your fare.</strong> We send you the best options we find, with prices and baggage allowance.</li>
        <li><strong>Confirm and pay.</strong> Send us the passport copies and we'll issue your tickets.</li>
        <li><strong>Fly.</strong> Your e-tickets arrive by WhatsApp or email, ready for check-in.</li>
      </ol>
"""),
"visas": dict(
    title="Visas &amp; Travel Services",
    lead="Visit visas for nine destinations, UAE visa change, plus hotels, travel insurance and entry tickets. Plan your whole trip from one desk in Abu Dhabi.",
    read="6 min read",
    body="""
      <p>A good trip starts with the right paperwork. Whether you're inviting family to the UAE or heading off on holiday, Mahar Adipati takes care of your visit visa and can book the rest of your trip in the same visit.</p>

      <h2>Visit visas we process</h2>
      <div class="option-grid option-grid-3">
        <div class="option"><strong>UAE Visit Visa</strong><span>For family, friends and tourists coming to the Emirates.</span></div>
        <div class="option"><strong>Qatar Visit Visa</strong><span>Short trips to Doha for holidays, business or family.</span></div>
        <div class="option"><strong>Oman Visit Visa</strong><span>Mountains, wadis and coastline, right next door.</span></div>
        <div class="option"><strong>Thailand Visit Visa</strong><span>Bangkok, Phuket, Pattaya and beyond.</span></div>
        <div class="option"><strong>Malaysia Visit Visa</strong><span>Kuala Lumpur, Penang and Langkawi.</span></div>
        <div class="option"><strong>Vietnam Visit Visa</strong><span>Hanoi, Ho Chi Minh City and Ha Long Bay.</span></div>
        <div class="option"><strong>India Visit Visa</strong><span>Family visits, business trips and holidays.</span></div>
        <div class="option"><strong>Taiwan Visit Visa</strong><span>Taipei and the rest of the island.</span></div>
        <div class="option"><strong>China Visit Visa</strong><span>Tourist and family visits across mainland China.</span></div>
      </div>

      <h2>UAE visa change</h2>
      <p>Visa running out but want to stay longer? We arrange a new UAE visa for you, either from inside the country or with a quick exit and re-entry.</p>
      <div class="option-grid option-grid-3">
        <div class="option"><strong>UAE Visa Change</strong><span>Change to a new visa from inside the UAE without leaving the country, where eligible.</span></div>
        <div class="option"><strong>A2A Visa Change</strong><span>Airport to Airport: fly out to a nearby country and fly back in on your new UAE visa.</span></div>
        <div class="option"><strong>B2B Visa Change</strong><span>Bus to Bus: travel by bus to the border and return on your new UAE visa.</span></div>
      </div>

      <div class="callout"><p><strong>Prices and processing times change often.</strong> Contact us with your nationality and travel dates and we'll give you the current fee, processing time and document list for your visa.</p></div>

      <h2>Travel services</h2>
      <p>Once your visa is sorted, we can book the rest of your trip too. Need a flight? See our <a href="air-tickets.html">International Air Tickets</a> service.</p>
      <div class="option-grid option-grid-3">
        <div class="option"><strong>Worldwide Hotel Booking</strong><span>Hotels for every budget, from city stays to beach resorts, wherever you're going.</span></div>
        <div class="option"><strong>Worldwide Travel Insurance</strong><span>Cover for your trip abroad, with the policy explained before you buy.</span></div>
        <div class="option"><strong>Entry Tickets</strong><span>Tickets to attractions, theme parks and landmarks at your destination.</span></div>
      </div>

      <h2>Documents you'll usually need</h2>
      <p>Requirements depend on the country and your nationality. For most visit visas, start with:</p>
      <ul>
        <li>A clear colour copy of your passport, valid for at least <strong>6 months</strong></li>
        <li>A recent passport-size photo on a white background</li>
        <li>A return flight ticket and hotel booking (we can arrange both for you)</li>
        <li>A copy of your UAE residence visa or Emirates ID, if you're a UAE resident travelling abroad</li>
        <li>Some countries also ask for a recent bank statement</li>
      </ul>
      <div class="callout"><p><strong>Not sure what applies to you?</strong> Send us a photo of your passport bio page on WhatsApp and we'll tell you exactly what's needed. There's no charge for the check.</p></div>

      <h2>How it works</h2>
      <ol class="steps">
        <li><strong>Talk to us.</strong> Visit the office, call or message us with your destination, travel dates and nationality.</li>
        <li><strong>Document check.</strong> We review everything before submission, which is when most problems get caught.</li>
        <li><strong>We apply and book.</strong> We submit your visa application and, if you like, book your flights, hotel, insurance and entry tickets.</li>
        <li><strong>Ready to travel.</strong> We send your approved visa and bookings as soon as they're issued.</li>
      </ol>

      <h2>Why book with Mahar Adipati?</h2>
      <ul>
        <li><strong>Fewer rejections:</strong> careful document checks before anything is submitted.</li>
        <li><strong>Transparent fees:</strong> visa fees and our service charge, itemised up front.</li>
        <li><strong>One desk for the whole trip:</strong> visa, flights, hotel, insurance and tickets in one place.</li>
      </ul>
      <p>Processing times are set by each country's immigration authorities and can vary, so apply early, especially around holidays and peak travel seasons.</p>
"""),
"passport-renewal": dict(
    title="Passport &amp; Document Services",
    lead="Passport renewal and extension, degree attestation and Myanmar Embassy certificates, prepared, checked and followed up for you.",
    read="6 min read",
    body="""
      <p>Embassy paperwork takes time, and a missing document can mean a second trip. For Myanmar nationals in the UAE, we prepare your file, book your appointment with the Embassy of Myanmar in Abu Dhabi and follow it up until your document is ready.</p>

      <h2>Our services</h2>
      <div class="option-grid">
        <div class="option"><strong>Passport Renewal</strong><span>A new passport before your current one expires, with forms, photos and appointment prepared for you.</span></div>
        <div class="option"><strong>Passport Extension Service</strong><span>Extend the validity of your current passport through the Embassy, where eligible.</span></div>
        <div class="option"><strong>Degree Attestation Service</strong><span>Full attestation of your degree: home-country attestation, the Embassy and the UAE Ministry of Foreign Affairs (MOFA), so it's accepted for jobs and visas in the UAE.</span></div>
        <div class="option"><strong>Vacation Leave Return Certificate</strong><span>The Embassy certificate for travelling home on vacation leave and returning to your job in the UAE.</span></div>
        <div class="option"><strong>Certificate of Identification</strong><span>An Embassy identity document for nationals who don't hold a valid passport, for example to travel home.</span></div>
      </div>
      <div class="callout"><p><strong>Requirements and fees change.</strong> Tell us which service you need and we'll give you the current fee, processing time and document checklist.</p></div>

      <h2>Passport renewal: when should you renew?</h2>
      <p>Many countries, and most airlines, won't let you travel if your passport has less than <strong>six months</strong> of validity left. In the UAE, an expiring passport can also affect your residence visa and Emirates ID. Renewing early saves a lot of trouble.</p>

      <ul>
        <li>Your passport expires within the next 6–12 months</li>
        <li>You're running out of blank visa pages</li>
        <li>Your passport is damaged, worn or water-stained</li>
        <li>Your name or personal details have changed</li>
        <li>Your passport has been lost or stolen</li>
      </ul>

      <h2>What we take care of for you</h2>
      <div class="option-grid">
        <div class="option"><strong>Application Forms</strong><span>Filled in accurately to your embassy's or consulate's current requirements.</span></div>
        <div class="option"><strong>Appointments</strong><span>We book your embassy or consulate slot and tell you what to bring.</span></div>
        <div class="option"><strong>Photos &amp; Copies</strong><span>Passport photos to the exact specification, plus all supporting copies.</span></div>
        <div class="option"><strong>Follow-up</strong><span>We track the application and let you know when your passport or certificate is ready to collect.</span></div>
        <div class="option"><strong>Lost Passports</strong><span>Guidance on police reports and emergency travel documents.</span></div>
        <div class="option"><strong>Records Update</strong><span>Help updating your UAE residency details with your new passport number.</span></div>
      </div>

      <h2>Typical documents for passport renewal</h2>
      <ul>
        <li>Your current (or expired) passport and a copy of the bio page</li>
        <li>Recent passport photos to your country's specification</li>
        <li>Copy of your UAE residence visa and Emirates ID (for residents)</li>
        <li>National ID card or birth certificate, if your embassy requires it</li>
        <li>Police report, for lost or stolen passports</li>
      </ul>
      <p>Degree attestation needs your original degree certificate and transcripts. For the certificates, bring your passport or any ID you have, and your UAE visa or Emirates ID.</p>

      <h2>The process</h2>
      <ol class="steps">
        <li><strong>Bring your documents.</strong> Visit our office or send us the details to start.</li>
        <li><strong>We prepare the file.</strong> Forms, photos and copies, all checked before your appointment.</li>
        <li><strong>Submission.</strong> You attend the Embassy (if required) with a ready file, or we submit where allowed.</li>
        <li><strong>Collection &amp; update.</strong> Collect your passport or certificate, and we'll help update your UAE records if needed.</li>
      </ol>
"""),
"car-rental": dict(
    title="Car Rental &amp; Transfers",
    lead="Airport pick-up and drop-off, and car rental with or without a driver, all booked from one desk in Abu Dhabi.",
    read="5 min read",
    body="""
      <p>Whether you're landing in the UAE for the first time or need a car for the month, we'll arrange it for you. Tell us what you need and we'll take care of the rest.</p>

      <h2>Our services</h2>
      <div class="option-grid">
        <div class="option"><strong>Airport Pick-up &amp; Drop-off</strong><span>A driver meets you at arrivals and takes you to your hotel or home, and back again for your flight.</span></div>
        <div class="option"><strong>Car Rental</strong><span>Self-drive or with a driver, by the day, week or month.</span></div>
      </div>
      <div class="callout"><p><strong>Prices depend on the date, car and trip.</strong> Contact us with what you'd like to book and your dates, and we'll send you a quote.</p></div>

      <h2>Car rental, your way</h2>
      <div class="option-grid">
        <div class="option"><strong>Self-Drive</strong><span>Take the wheel yourself and explore on your own schedule.</span></div>
        <div class="option"><strong>With a Driver</strong><span>Sit back while a professional driver takes you to meetings, events or sightseeing.</span></div>
      </div>

      <h3>Choose your car</h3>
      <ul>
        <li><strong>Economy:</strong> compact and fuel-efficient, ideal for city driving</li>
        <li><strong>Sedan:</strong> more room and comfort for business trips and longer drives</li>
        <li><strong>SUV:</strong> space for the whole family and luggage</li>
        <li><strong>Premium:</strong> for special occasions, or when you want something a little nicer</li>
      </ul>

      <h3>Flexible rental plans</h3>
      <ul>
        <li><strong>Daily:</strong> for short trips and weekend getaways</li>
        <li><strong>Weekly:</strong> better rates for holidays and visiting family</li>
        <li><strong>Monthly:</strong> the best value for residents and long stays</li>
      </ul>

      <h3>What you'll need for self-drive</h3>
      <ul>
        <li><strong>UAE residents:</strong> valid UAE driving licence and Emirates ID</li>
        <li><strong>Visitors:</strong> passport with visit visa or entry stamp, your home driving licence, and an International Driving Permit where required</li>
        <li>A credit or debit card for the refundable security deposit</li>
      </ul>
      <div class="callout"><p><strong>Good to know:</strong> for self-drive rentals, Salik (road toll) charges and traffic fines incurred during the rental are billed back after the rental ends. We explain the fuel policy and insurance cover before you sign.</p></div>

      <h2>Book in four steps</h2>
      <ol class="steps">
        <li><strong>Tell us what you need.</strong> Airport transfer or car rental, your dates and the number of passengers.</li>
        <li><strong>Get a quote.</strong> One clear price, with any deposit shown separately.</li>
        <li><strong>Confirm your booking.</strong> Send the documents we need and we'll lock in your date.</li>
        <li><strong>On your way.</strong> Your driver or car is ready on the day.</li>
      </ol>
"""),
"tour-packages": dict(
    title="Tour Packages",
    lead="Desert safaris, dinner cruises, private yachts and sightseeing tours. Tell us what you'd like to do and we'll plan and book it for you.",
    read="4 min read",
    body="""
      <p>The UAE has a lot to offer beyond the city, from golden dunes to evenings on the water. Whether it's a family day out, a celebration or showing visiting relatives around, we'll find the right package and book it for you.</p>

      <h2>Our tour packages</h2>
      <div class="option-grid">
        <div class="option"><strong>Desert Safari</strong><span>Dune bashing, camel rides and an evening at a desert camp with dinner.</span></div>
        <div class="option"><strong>Cruise Dinner</strong><span>An evening on the water with dinner on board and city skyline views.</span></div>
        <div class="option"><strong>Yacht Rental</strong><span>Private yacht trips for family outings, birthdays and celebrations.</span></div>
        <div class="option"><strong>UAE Tour Package</strong><span>Sightseeing tours of the top landmarks in Abu Dhabi, Dubai and the other Emirates.</span></div>
      </div>
      <div class="callout"><p><strong>Prices depend on the date and group size.</strong> Contact us with the package you'd like, your date and the number of people, and we'll send you a quote.</p></div>

      <h2>Good to know</h2>
      <ul>
        <li><strong>Book ahead:</strong> weekends, public holidays and the cooler winter months fill up fast.</li>
        <li><strong>Groups and families:</strong> tell us how many adults and children are coming so we can find the right option.</li>
        <li><strong>Celebrations:</strong> planning a birthday or special occasion on a yacht or cruise? Let us know when you book.</li>
        <li><strong>Visiting the UAE?</strong> We can arrange your visit visa, airport pick-up and tours together.</li>
      </ul>

      <h2>Book in four steps</h2>
      <ol class="steps">
        <li><strong>Choose your package.</strong> Tell us what you'd like to do, your date and the number of people.</li>
        <li><strong>Get a quote.</strong> One clear price, so you know exactly what you're paying for.</li>
        <li><strong>Confirm your booking.</strong> We reserve your date and send you the details.</li>
        <li><strong>Enjoy your day.</strong> Everything is arranged, so all you have to do is turn up and enjoy it.</li>
      </ol>
"""),
}

for i, (slug, name, icon, meta) in enumerate(POSTS):
    a = ARTICLES[slug]
    prev_p = POSTS[i - 1] if i > 0 else None
    next_p = POSTS[i + 1] if i < len(POSTS) - 1 else None
    nav = '<div class="article-nav">'
    nav += f'<a href="{prev_p[0]}.html"><small>← Previous</small>{prev_p[1]}</a>' if prev_p else '<a href="../index.html#services"><small>← Back</small>All services</a>'
    nav += f'<a href="{next_p[0]}.html" style="text-align:right"><small>Next →</small>{next_p[1]}</a>' if next_p else '<a href="../index.html#about" style="text-align:right"><small>Next →</small>About Us</a>'
    nav += "</div>"
    page = head(f"{a['title']} | Mahar Adipati Travel Company", a["lead"], "../")
    page += header("../", "services")
    page += f"""
  <section class="article-hero">
    <img class="hero-pattern" src="../assets/logo-mark.png" alt="">
    <div class="container article-hero-grid">
      <div>
        <div class="breadcrumb"><a href="../index.html">Home</a> / <a href="../index.html#services">Services</a> / {name}</div>
        <span class="eyebrow" style="color:var(--gold-300)">0{i+1} · {meta}</span>
        <h1 style="font-size:clamp(2rem,4.6vw,3.2rem)">{a['title']}</h1>
        <p class="lead">{a['lead']}</p>
        <div class="article-meta"><span>Mahar Adipati Travel Desk</span></div>
      </div>
      {cover(slug, name, icon, "../", "article-hero-img")}
    </div>
  </section>

  <article class="article">
    <div class="container">
{a['body']}
      {nav}
    </div>
  </article>

"""
    page += cta("../", f"Need help with {name.lower()}?")
    page += footer("../")
    (OUT / "services" / f"{slug}.html").write_text(page)

print("built", [p.name for p in OUT.rglob("*.html")])
