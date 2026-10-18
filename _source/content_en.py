# English text for the site. build.py renders every page from this file and content_my.py.

LANG = "en"
HOURS = "Mon – Sat, 9:00 AM – 9:00 PM"

POSTS = {
    "air-tickets": ("International Air Tickets", "Air Tickets"),
    "visas": ("Visas & Travel Services", "Visas & Travel"),
    "passport-renewal": ("Passport & Document Services", "Passport & Documents"),
    "car-rental": ("Car Rental & Transfers", "Car Rental & Transfers"),
    "tour-packages": ("Tour Packages", "Tour Packages"),
}

EXCERPTS = {
    "air-tickets": "One-way, return and multi-city flights worldwide, for individuals, families and groups, at the best fares we can find for your dates.",
    "visas": "Visit visas for nine destinations, UAE visa change (inside, A2A and B2B), plus hotels, insurance and entry tickets.",
    "passport-renewal": "Passport renewal and extension, degree attestation, Vacation Leave Return Certificates and Certificates of Identification.",
    "car-rental": "Airport pick-up and drop-off, plus car rental by the day, week or month, self-drive or with a driver.",
    "tour-packages": "Desert safaris, dinner cruises, private yacht rental and UAE sightseeing tours, planned and booked for you.",
}

WHY = [
    ("shield", "Checked before it's submitted", "Every application is reviewed by our team first. Most delays and rejections start with a small mistake, and we catch them early."),
    ("tag", "Upfront, honest pricing", "Government fees and our service charge are itemised before you pay. No hidden extras and no surprises later."),
    ("chat", "Updates without chasing", "We keep you informed by phone or WhatsApp at every stage, so you always know where your file stands."),
    ("user", "One person, start to finish", "You deal with the same friendly person who knows your case, not a different call-centre agent every time."),
    ("layers", "Everything under one roof", "Air tickets, visas, passport renewal, car rental and tours from a single desk. One visit, one contact, less running around."),
    ("pin", "Easy to find in Abu Dhabi", "Walk in at Al Khazna Tower on Najda Road, beside the Nissan showroom, right in the heart of the city."),
]

VALUES = [
    ("tag", "Clear pricing", "Know the full cost before you commit."),
    ("bolt", "Fast follow-up", "We track every file until it's done."),
    ("heart", "Personal care", "Guidance from people, not call centres."),
    ("home", "One roof", "Flights, visas, passports, cars and tours in one place."),
]

T = dict(
    # page titles
    index_title="Mahar Adipati | Air Tickets, Visas, Passports, Car Rental & Tours in Abu Dhabi",
    index_desc="Mahar Adipati Travel Company in Abu Dhabi — international air tickets, visa services, passport renewal, car rental and tour packages from one trusted team at Al Khazna Tower, Najda Road.",
    article_title="{title} | Mahar Adipati Travel Company",
    # header
    home_label="Mahar Adipati home",
    nav_services="Services",
    nav_about="About Us",
    contact="Contact Us",
    open_menu="Open menu",
    lang_group="Language",
    # hero
    hero_eyebrow="Travel Company · Abu Dhabi",
    hero_h1='Your journey,<br><span class="gold-text">handled with care.</span>',
    hero_lead="Air tickets, visas, passport renewal, car rental and tours from one trusted team. Tell us where you're going and we'll take care of the paperwork and the plans, so you can enjoy the trip.",
    hero_btn_services="Explore Our Services",
    hero_btn_office="Visit Our Office",
    emblem_alt="Mahar Adipati mandala emblem",
    # services
    services_eyebrow="Our Services",
    services_h2="Guides from our travel desk",
    services_p="Practical guides to everything we do, from flights and visas to cars and tours. Read up, then let us handle the rest.",
    read_more="Read the full guide",
    img_alt="{name} by Mahar Adipati Travel Company",
    # about
    badge_title="Al Khazna Tower",
    badge_text="Office 309, Najda Road, Abu Dhabi",
    about_eyebrow="About Us",
    about_h2="Travel made easier, one client at a time",
    about_p1="<strong>Mahar Adipati Travel Company</strong> is an Abu Dhabi travel and documentation office. We help residents, visitors and families with everything a trip involves: international air tickets, visas, passport renewals, a reliable car once you arrive, and tours and experiences to enjoy while you're here.",
    about_p2="Every application is reviewed by a real person before it's submitted. We explain what's needed, quote our fees up front and keep you updated until the job is finished. Our clients come back, and send their friends, because we treat their plans as if they were our own.",
    # why
    why_eyebrow="Why Choose Us",
    why_h2='Why travellers choose <span class="gold-text">Mahar Adipati</span>',
    why_p="Paperwork goes better when someone careful is handling it. Here's what you get when you work with us.",
    # cta
    cta_title="Ready to get started?",
    cta_text="Visit us at Al Khazna Tower or send us a message — we usually reply within the hour.",
    cta_article_title="Need help with {name_lower}?",
    whatsapp="Chat on WhatsApp",
    call="Call Us",
    # footer
    footer_blurb="Visas and passport renewal from one friendly desk in Abu Dhabi. Walk in, call or message us — we'll take it from there.",
    quick_links="Quick Links",
    our_services="Our Services",
    visit_office="Visit Our Office",
    find_map="Find Us on the Map",
    map_title="Mahar Adipati office location on Google Maps",
    directions="Get directions on Google Maps →",
    rights="Mahar Adipati Travel Company. All rights reserved.",
    country="Abu Dhabi, United Arab Emirates",
    # article pages
    crumb_home="Home",
    crumb_services="Services",
    desk="Mahar Adipati Travel Desk",
    prev="← Previous",
    back="← Back",
    all_services="All services",
    next="Next →",
    about_us="About Us",
)

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
