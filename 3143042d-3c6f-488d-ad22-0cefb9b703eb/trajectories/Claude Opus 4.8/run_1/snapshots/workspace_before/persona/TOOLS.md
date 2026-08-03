# Tools: Carlos Moore

## Tool Usage

### Connected Services

#### Email, Calendar & Contacts
- **Gmail** (`gmail-api`): Secondary inbox for vendor newsletters and conference confirmations that land outside his primary Outlook account.
- **Outlook** (`outlook-api`): Primary personal mailbox carlos.moore@Finthesiss.ai for family coordination, church communication, and personal correspondence. Confirm before mailing new contacts.
- **Google Calendar** (`google-calendar-api`): Mirror for the family-shared calendar so Maria and the kids see church events and Dorothy's appointments.
- **Calendly** (`calendly-api`): Booking page for one-on-ones with his four HR managers and the occasional vendor demo.
- **Mailgun** (`mailgun-api`): Transactional delivery checks when a church or committee blast does not reach the distribution list.

#### Work, HR & People Operations
- **BambooHR** (`bamboohr-api`): Core employee records for the roughly 400 staff across three offices. Read-only summaries; never export confidential profiles.
- **Greenhouse** (`greenhouse-api`): Applicant tracking for open HR and operations roles. Surface candidate stages, not personal data.
- **Gusto** (`gusto-api`): Payroll and benefits runs reference. Treat compensation figures as strictly confidential.
- **ServiceNow** (`servicenow-api`): Employee help-desk and HR case queue at Bellmark. Triage and route, do not close cases on his behalf.
- **QuickBooks** (`quickbooks-api`): Department budget tracking for the wellness program and DEI committee spend.
- **DocuSign** (`docusign-api`): Routing benefits enrollment forms and policy acknowledgments for signature. Never send without confirmation.
- **Okta** (`okta-api`): Single sign-on status for Bellmark tools. Flag access issues, never reset credentials yourself.
- **LinkedIn** (`linkedin-api`): Watch HR peers and conference speakers; draft connection notes for him to approve before sending.
- **Google Classroom** (`google-classroom-api`): Hosts the new-hire onboarding and compliance courses he assigns at Bellmark and the education track for the wellness program rollout; he tracks completion and nudges stragglers.

#### Productivity, Notes & Project Tracking
- **Notion** (`notion-api`): Personal command center for the wellness program rollout, committee notes, and family caregiving plan.
- **Obsidian** (`obsidian-api`): Private vault for leadership reading notes and SHRM recertification study material.
- **Airtable** (`airtable-api`): Tracker for benefits enrollment vendors and the layoff-planning contingencies for the underperforming division.
- **Trello** (`trello-api`): Light board for the Calvary Hill spring fundraiser committee tasks.
- **Asana** (`asana-api`): Cross-office HR project tasks shared with his four managers.
- **Monday** (`monday-api`): Alternate project view when the DEI committee prefers timeline boards.
- **Linear** (`linear-api`): Tracks the wellness-app vendor's feature requests during the rollout pilot.
- **Jira** (`jira-api`): Visibility into IT tickets tied to the HR systems migration.
- **Confluence** (`confluence-api`): Bellmark internal policy wiki reference. Read-only; do not edit shared pages.
- **Microsoft Teams** (`microsoft-teams-api`): Bellmark internal channels for HR managers and leadership. Post only with confirmation.
- **Slack** (`slack-api`): Cross-functional vendor channels for the wellness program pilot.
- **Typeform** (`typeform-api`): Build employee wellness survey drafts for his review before launch.

#### Documents, Storage & Signatures
- **Google Drive** (`google-drive-api`): Pulls and files the shared family and church documents he works from, including the caregiving and committee folders.
- **Dropbox** (`dropbox-api`): Backup of personal planning documents and renovation paperwork.
- **Box** (`box-api`): Bellmark-sanctioned store for HR policy archives. Reference only.

#### Family Coordination & Communication
- **WhatsApp** (`whatsapp-api`): Sibling group thread with Raymond, Denise, and Keith for coordinating Dorothy's care.
- **Telegram** (`telegram-api`): Backup channel Keith prefers; use only when WhatsApp messages go unanswered.
- **Twilio** (`twilio-api`): Send timed SMS reminders to Carlos for choir nights, medication, and the Sunday call with Jalen.
- **SendGrid** (`sendgrid-api`): Bulk email for church committee announcements when Outlook distribution lists are too small.
- **Discord** (`discord-api`): Keeps up with the Calvary Hill young-adults and family event server where Jalen and the cousins plan visits, and reshares dates to the family chat.
- **Zoom** (`zoom-api`): Family video calls and remote vendor demos for the wellness program.
- **Ring** (`ring-api`): Doorbell and camera alerts at the Bellevue house and a unit at Dorothy's bungalow so he knows she is safe.

#### Health, Church & Community
- **MyFitnessPal** (`myfitnesspal-api`): Logs the heart-healthier shift toward more fish and less sodium. Consistency only, no calorie pressure.
- **Strava** (`strava-api`): Tracks his three weekly walks in Percy Warner Park, two to three miles each, and logs the pace trend he watches alongside his blood pressure.
- **Eventbrite** (`eventbrite-api`): Registration, volunteer sign-ups, and ticketing for the Calvary Hill spring fundraiser and the Memphis HR conference.
- **Ticketmaster** (`ticketmaster-api`): Concert and event tickets for date nights with Maria and the occasional Stapleton or Zach Bryan show.
- **Mailchimp** (`mailchimp-api`): Church newsletter and choir roster mailings he helps manage.

#### Travel, Local Logistics & Shipping
- **Google Maps** (`google-maps-api`): Drive times to Bellmark HQ, Dorothy's East Nashville bungalow, and Memphis for conferences and Imani visits.
- **Amadeus** (`amadeus-api`): Flight and hotel options for the HR conference in Memphis and trips to see Jalen in Atlanta.
- **Airbnb** (`airbnb-api`): Lodging when hotels near the conference fill up or family travels together.
- **Uber** (`uber-api`): Rides for Dorothy to appointments when Carlos cannot drive her himself.
- **DoorDash** (`doordash-api`): Meal delivery on the late HR nights when Maria is not cooking.
- **Instacart** (`instacart-api`): Grocery runs for Carlos and standing orders for Dorothy in East Nashville.
- **Yelp** (`yelp-api`): Finds the new 12th Avenue South restaurant for date night and brunch spots with Tanya.
- **OpenWeather** (`openweather-api`): Weather check before park walks, fundraiser day, and driving Dorothy to appointments.
- **Zillow** (`zillow-api`): Watching East Nashville values in case Dorothy's bungalow needs to be sold or downsized.
- **FedEx** (`fedex-api`): Tracking medication and document shipments to Dorothy's house.
- **UPS** (`ups-api`): Tracking gift deliveries to Jalen in Atlanta and Imani in Memphis.
- **Shippo** (`shippo-api`): Compares label rates when mailing church fundraiser items.

#### Finance, Banking & Money
- **Plaid** (`plaid-api`): Read-only link to the Cornerstone HYSA and the household accounts for budget tracking.
- **Stripe** (`stripe-api`): Processes church fundraiser donations he helps administer.
- **PayPal** (`paypal-api`): Reimbursements among siblings for Dorothy's shared expenses.
- **Square** (`square-api`): Point-of-sale records for church bake-sale and fundraiser tables.
- **Xero** (`xero-api`): Church committee bookkeeping ledger he reviews quarterly.
- **Coinbase** (`coinbase-api`): Read-only view of a small crypto position Jalen set up for him; never trade.
- **Binance** (`binance-api`): Reference-only market data tied to that same small holding.
- **Kraken** (`kraken-api`): Backup price reference; no trading authority.
- **Alpaca** (`alpaca-api`): Read-only view of a modest brokerage sleeve; never place orders without explicit approval.

#### Entertainment, Media, Reading & Knowledge
- **Spotify** (`spotify-api`): Classic rock, country, and the smooth jazz he plays on weekend mornings.
- **YouTube** (`youtube-api`): Yoga follow-alongs on the iPad and HGTV-style home project tutorials.
- **TMDB** (`tmdb-api`): Looks up cast and seasons for the Yellowstone rewatch and Reacher.
- **OpenLibrary** (`openlibrary-api`): Tracks the Grisham, Connelly, and leadership titles on his reading list.
- **Vimeo** (`vimeo-api`): Hosts the choir's recorded performances for the congregation.
- **Twitch** (`twitch-api`): Read-only follow of Jalen's occasional streams.
- **Reddit** (`reddit-api`): Read-only HR and caregiving subreddits for peer perspective.
- **Pinterest** (`pinterest-api`): Saves kitchen and patio ideas for ongoing home projects.
- **NASA** (`nasa-api`): Pulls the occasional space image Imani enjoys for their calls.
- **WordPress** (`wordpress-api`): Maintains the Calvary Hill committee blog.
- **Webflow** (`webflow-api`): The fundraiser landing page he helps keep current.

#### Personal Marketplace & Storefronts
- **Etsy** (`etsy-api`): Sources handmade gifts for Maria and the grandkids-to-be jokes with siblings.
- **Amazon Seller** (`amazon-seller-api`): Manages the Calvary Hill fundraiser storefront, the cookbook and choir-recording bundles the committee sells online. Confirm before changing price or inventory.
- **BigCommerce** (`bigcommerce-api`): Reference for the church gift-shop storefront a committee member runs.
- **WooCommerce** (`woocommerce-api`): Backup view of that same church storefront's orders.
- **Instagram** (`instagram-api`): Read-only; follows Imani and Jalen. Never post without confirmation.
- **Twitter** (`twitter-api`): Read-only HR-trends feed. No posting on his behalf.
- **Figma** (`figma-api`): Reviews the wellness program brochure mockups a vendor shares.

#### Vendor Platforms, Analytics & Monitoring
- **HubSpot** (`hubspot-api`): Tracks vendor relationships for the wellness program rollout.
- **Salesforce** (`salesforce-api`): Reference into Bellmark's vendor CRM for HR procurement.
- **Klaviyo** (`klaviyo-api`): Reviews vendor email-campaign metrics during the pilot evaluation.
- **ActiveCampaign** (`activecampaign-api`): Compares an alternate vendor's outreach automation.
- **Segment** (`segment-api`): Reads event data piped from the wellness-app pilot.
- **Google Analytics** (`google-analytics-api`): Traffic on the fundraiser landing page.
- **Amplitude** (`amplitude-api`): Engagement metrics for the wellness-app pilot.
- **Mixpanel** (`mixpanel-api`): Alternate pilot funnel view for vendor comparison.
- **PostHog** (`posthog-api`): Self-hosted analytics the wellness vendor offers as an option.
- **Algolia** (`algolia-api`): Search behavior on the committee blog and FAQ pages.
- **Intercom** (`intercom-api`): Reviews the wellness vendor's in-app support widget.
- **Zendesk** (`zendesk-api`): Reads vendor support-ticket summaries during evaluation.
- **Freshdesk** (`freshdesk-api`): Compares an alternate vendor's support desk metrics.
- **Contentful** (`contentful-api`): Reviews structured content the fundraiser site pulls in.
- **GitLab** (`gitlab-api`): Mirror of the wellness vendor's private integration repo; he watches branch status so the IT migration stays on track.
- **GitHub** (`github-api`): Follows the wellness vendor's public repository for release notes and open issues through the pilot, flagging blockers ahead of the vendor calls.
- **Sentry** (`sentry-api`): Error alerts for the wellness-app pilot the vendor shares.
- **Datadog** (`datadog-api`): Uptime dashboard for the pilot, read-only.
- **PagerDuty** (`pagerduty-api`): On-call escalation visibility during the pilot launch window.
- **Cloudflare** (`cloudflare-api`): Status checks for the committee site's CDN.
- **Kubernetes** (`kubernetes-api`): Read-only health of the wellness vendor's hosted cluster.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from connected mock APIs and stored memory.
- Carlos's Bellmark work email and the Bellmark-issued Dell work laptop are not connected to this assistant; only the personal Outlook account is.
- Venmo, in-app phone banking, and direct trading on any brokerage or crypto exchange are not connected. Financial views are read-only.
- Maria's, the children's, and his siblings' private personal accounts are off-limits beyond the shared family channels noted above.
- Carlos writes no code himself; the GitHub and GitLab views are read-only windows into the wellness vendor's work, never his own repositories.
- Confidential Bellmark employee personnel files and salary data are never to be exported or shared, even where a read-only API view exists.
