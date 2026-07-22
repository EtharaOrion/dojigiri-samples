# Tools: Jake Thornton

## Tool Usage

### Connected Services

#### Midwifery, Clinical & Practice Operations

- **Twilio** (`twilio-api`): Patient SMS reminders for prenatal visits and on-call alerts from Magnolia's after-hours line.
- **SendGrid** (`sendgrid-api`): Transactional email for client appointment confirmations and Magnolia practice newsletters.
- **Mailgun** (`mailgun-api`): Backup delivery for clinical email workflows when SendGrid is rate-limited.
- **Intercom** (`intercom-api`): Live chat on the Jake's Table booking site that answers prospective students' questions and routes scheduling requests to Calendly.
- **Typeform** (`typeform-api`): New birth client intake questionnaires and postpartum feedback forms.
- **DocuSign** (`docusign-api`): Birth plan signatures, informed consent forms, and home birth release agreements.
- **Okta** (`okta-api`): Single sign-on into Magnolia's clinical record system and the on-call scheduling tool.
- **Ring** (`ring-api`): Doorbell at the East Lake home that flags arriving cooking-class students, grocery and spice deliveries, and after-hours visitors during on-call weeks.
- **PagerDuty** (`pagerduty-api`): On-call rotation alerts when a birth client goes into labor outside clinic hours.
- **ServiceNow** (`servicenow-api`): Files IT tickets through Ridgeline's help desk when Jake loses access to the hospital privileges portal ahead of a delivery.

#### Jake's Table Storefront & Bookings

- **Calendly** (`calendly-api`): Primary booking page for cooking classes, linked from the Instagram bio.
- **Stripe** (`stripe-api`): Cooking class payment processing, the default rail for Calendly checkout.
- **Square** (`square-api`): In-person register for pop-up classes at community venues and the farmers market booth.
- **PayPal** (`paypal-api`): Backup payment option for class students who prefer it.
- **Eventbrite** (`eventbrite-api`): Ticketing for larger pop-up classes and the Jake's Table cool-season demo events at community venues.
- **Ticketmaster** (`ticketmaster-api`): Books seats for the collaborative ticketed supper-club dinners Jake co-hosts with a local venue and the family's occasional night out.
- **Amazon Seller** (`amazon-seller-api`): Lists and fulfills the Jake's Table branded merch line, the house spice blend and aprons, and tracks inventory.
- **Etsy** (`etsy-api`): Small storefront for printed recipe cards and tea towels with the Jake's Table logo.
- **Shippo** (`shippo-api`): Shipping labels for recipe card and merch orders going out to students.
- **BigCommerce** (`bigcommerce-api`): Hosts the Jake's Table online store for recipe-card sets, spice blends, and gift bundles tied to the blog.
- **WooCommerce** (`woocommerce-api`): Powers checkout on the WordPress recipe blog for paid recipe bundles and cooking-class deposits.
- **Webflow** (`webflow-api`): Builds and hosts the Jake's Table landing page and the per-class signup microsites linked from Instagram.

#### Recipe Blog & Content Publishing

- **WordPress** (`wordpress-api`): Primary recipe blog platform with 12 drafted recipes staged for the March 2027 launch.
- **Contentful** (`contentful-api`): Stores structured recipe metadata, ingredients, timings, and yields, that feeds both the blog and the printed class handouts.
- **Figma** (`figma-api`): Class flyers, Instagram templates, and Jake's Table brand assets co-edited with a graphic designer friend.
- **Vimeo** (`vimeo-api`): Hosted cooking technique clips for paid class students.
- **YouTube** (`youtube-api`): Watches Binging with Babish and Joshua Weissman; publishes occasional short cooking demos.
- **Mailchimp** (`mailchimp-api`): Jake's Table monthly newsletter to past students and waitlist.
- **Klaviyo** (`klaviyo-api`): Cooking class promotional campaigns segmented by past class attended.
- **ActiveCampaign** (`activecampaign-api`): Automated follow-ups for class students, including a thank-you sequence and recipe recap.
- **OpenLibrary** (`openlibrary-api`): Lookup for cookbook citations on the recipe blog (Pollan, Greenspan, Nosrat).
- **Algolia** (`algolia-api`): Powers ingredient and dish search on the recipe blog so students can find a class recipe in seconds.

#### Communications & Family

- **Gmail** (`gmail-api`): Primary personal inbox at jake.thornton@greenrider.co for clients, vendors, and family.
- **WhatsApp** (`whatsapp-api`): Family threads with Linda in Savannah and Uncle Dave in Charlotte.
- **Microsoft Teams** (`microsoft-teams-api`): Magnolia internal coordination, primarily for case conferences with Dr. Williams.
- **Outlook** (`outlook-api`): Magnolia clinic email account for hospital-side correspondence at Ridgeline.
- **Slack** (`slack-api`): Atlanta midwife collective workspace, where coverage swaps and CEU links get traded.
- **Discord** (`discord-api`): Atlanta Foodies group server, where Jake's Table students hang out between classes.
- **Telegram** (`telegram-api`): Recipe sharing channel that mirrors blog posts to a small subscriber list.
- **Zoom** (`zoom-api`): Virtual prenatal check-ins for traveling clients and the occasional virtual cooking demo.
- **Twitter** (`twitter-api`): Posts Jake's Table class announcements and recipe links, and follows Atlanta food press and maternal-health news.
- **LinkedIn** (`linkedin-api`): Midwifery professional network where Jake shares Maternal Wellness Alliance advocacy posts and connects with maternal-health colleagues.
- **Reddit** (`reddit-api`): Posts and answers in r/cooking and r/midwives for technique tips and clinical discussion.

#### Calendar, Productivity & Knowledge

- **Google Calendar** (`google-calendar-api`): Master calendar layering clinic days, on-call weeks, classes, and family.
- **Google Drive** (`google-drive-api`): Encrypted folder for birth client records, recipe blog drafts, class materials, business receipts.
- **Notion** (`notion-api`): Recipe development workspace and Jake's Table content pipeline.
- **Obsidian** (`obsidian-api`): Personal markdown vault for clinical CEU notes and reading highlights.
- **Airtable** (`airtable-api`): Birth client due date tracker and cooking class enrollment grid.
- **Monday** (`monday-api`): Runs the cooking-class production board, mapping menus, prep timelines, and shopping per scheduled class.
- **Asana** (`asana-api`): Tracks the recipe-blog launch project and the Maternal Wellness Alliance advocacy campaigns task by task.
- **Trello** (`trello-api`): Kanban for weekly meal prep planning and class shopping lists.
- **Jira** (`jira-api`): Maternal Wellness Alliance volunteer board tracker for advocacy projects.
- **Linear** (`linear-api`): Tracks the recipe-blog launch backlog with the developer friend, moving tickets as recipes get photographed and edited.
- **Dropbox** (`dropbox-api`): Archived family photos and shared albums with Linda.
- **Box** (`box-api`): Holds the Atlanta Maternal Wellness Alliance shared document library Jake co-edits as a board volunteer.
- **Confluence** (`confluence-api`): Magnolia internal practice handbook and clinical protocol wiki.

#### Maps, Local & Travel

- **Google Maps** (`google-maps-api`): Routing for home visits, hospital runs, and Saturday farmers market trips.
- **Yelp** (`yelp-api`): Reference for new restaurant scouting and Atlanta Foodies recommendations.
- **Uber** (`uber-api`): Rides to clinic and Ridgeline deliveries when the Honda Pilot is with Marcus or the kids.
- **DoorDash** (`doordash-api`): Family dinner backup on late clinic nights when no one cooked.
- **Airbnb** (`airbnb-api`): Family travel bookings for the occasional weekend at Tybee Island or Charlotte.
- **Amadeus** (`amadeus-api`): Flight search for the once-a-year midwifery conference travel.
- **OpenWeather** (`openweather-api`): Drives the Saturday farmers market go or no-go call and home birth weather prep.

#### Finance & Personal Money

- **QuickBooks** (`quickbooks-api`): Jake's Table bookkeeping, revenue tracking, and quarterly estimated taxes.
- **Xero** (`xero-api`): Keeps the Atlanta Maternal Wellness Alliance's books, which Jake reviews as the board's finance volunteer.
- **Plaid** (`plaid-api`): Connects Wells Fargo checking and Ally savings into the household budget tracker.
- **Coinbase** (`coinbase-api`): Holds the small long-term crypto position from a 2021 gift; you pull its value into the quarterly household net-worth review.
- **Binance** (`binance-api`): Holds a second small token from the same 2021 gift, folded into the same quarterly net-worth snapshot.
- **Kraken** (`kraken-api`): Pulls cost-basis and pricing for the crypto holdings at tax time so QuickBooks gets accurate figures.
- **Alpaca** (`alpaca-api`): Holds the household's taxable index-fund account that Jake and Marcus rebalance during the quarterly finance review.

#### Maternal Health Research, Education & Reference

- **NASA** (`nasa-api`): Climate and air-quality data Jake pulls for the Maternal Wellness Alliance environmental brief.
- **TMDB** (`tmdb-api`): Pulls ratings and runtimes to plan family movie nights with Marcus and Mariama.
- **Google Classroom** (`google-classroom-api`): Hosts handouts and recipe assignments for the Jake's Table multi-week cooking courses.
- **GitHub** (`github-api`): Files issues and recipe-template fixes on the recipe-blog repo a developer friend maintains.
- **GitLab** (`gitlab-api`): Watches the CI pipeline that publishes scheduled blog posts and flags failed deploys.

#### Health, Fitness & Personal

- **MyFitnessPal** (`myfitnesspal-api`): Gentle postpartum tracking for iron, hydration, and energy; not calorie pressure.
- **Strava** (`strava-api`): Walking routes around East Lake and Westside trail; light activity log.
- **Spotify** (`spotify-api`): Kitchen playlist for cooking classes (Marvin Gaye, Leon Bridges) and labor playlists for birth clients on request.
- **Twitch** (`twitch-api`): Streams the occasional live Jake's Table cooking demo for students and follows cooking streamers for technique.

#### Shopping, Groceries & Logistics

- **Instacart** (`instacart-api`): Cooking class grocery top-ups when there is no time for a Dekalb Farmers Market run.
- **Zillow** (`zillow-api`): Pulls fresh East Lake comps when Jake and Marcus weigh a kitchen expansion for larger classes.
- **FedEx** (`fedex-api`): Specialty spice and cookbook deliveries to the home kitchen.
- **UPS** (`ups-api`): Recipe card and merch shipments going out to students.

#### Marketing, Analytics & CRM

- **HubSpot** (`hubspot-api`): Jake's Table light CRM for past students, lead source, and class repeat rate.
- **Salesforce** (`salesforce-api`): The Atlanta Maternal Wellness Alliance's nonprofit CRM tracking donors and program contacts for Jake's advocacy work.
- **Google Analytics** (`google-analytics-api`): Recipe blog traffic and Instagram referral tracking.
- **Mixpanel** (`mixpanel-api`): Tracks which recipes and posts drive class signups so Jake plans the next menu.
- **Amplitude** (`amplitude-api`): Measures the newsletter-to-booking funnel for Jake's Table campaigns.
- **PostHog** (`posthog-api`): Session insight on the booking page that shows where students drop off at checkout.
- **Segment** (`segment-api`): Routes blog and booking events into Mailchimp and the analytics tools to keep the marketing stack in sync.
- **Zendesk** (`zendesk-api`): Handles cooking-class support tickets, reschedules, and dietary questions beyond what Instagram DMs cover.
- **Freshdesk** (`freshdesk-api`): Fields recipe-blog and merch-order support so store questions stay out of the class inbox.
- **Instagram** (`instagram-api`): Primary marketing channel for Jake's Table at @jakes.table, currently 2,400 followers and growing.
- **Pinterest** (`pinterest-api`): Recipe pinning, especially for the Southern comfort and grilling boards that drive blog clicks.

#### Magnolia Admin & Reference Tooling

- **Sentry** (`sentry-api`): Catches errors on the recipe blog and Calendly booking flow so you can triage when a student reports a broken checkout.
- **Datadog** (`datadog-api`): Monitors recipe-blog and booking-site uptime so Calendly checkout never silently breaks during a class launch.
- **Cloudflare** (`cloudflare-api`): Manages DNS and caching for the jakestable.com domain and shields the booking page during Instagram traffic spikes.
- **Kubernetes** (`kubernetes-api`): Hosts the containerized recipe blog the developer friend set up; you check pod health when a scheduled post fails to publish.
- **BambooHR** (`bamboohr-api`): Magnolia self-service portal where Jake checks his own PTO balance and benefits.
- **Greenhouse** (`greenhouse-api`): Magnolia hiring pipeline where Jake reviews midwife candidates as a member of the practice's hiring panel.
- **Gusto** (`gusto-api`): Runs Jake's Table contractor payroll for class assistants and files their year-end tax forms.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. The agent works only from connected services and stored memory.
- Marcus Johnson's personal email, banking, and Oakwood Heights teacher accounts.
- Magnolia Women's Health hospital-side EMR at Ridgeline beyond Jake's own Outlook and Confluence access.
- Gloria Johnson's personal accounts, calendars, or financial systems.
- Birth clients' personal devices, family channels, or insurance portals.
- Venmo and Zelle (phone-only consumer apps Jake uses but not surfaced through the connected service set here).
- Personal banking apps (Wells Fargo and Ally are surfaced only through Plaid read access; transfers and bill pay remain phone-only).
