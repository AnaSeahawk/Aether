# Cal.com

**Use the Cal.com MCP first** (claude.ai connector, connected 27 Nov 2026): event types, availability, bookings and cancellations all go through it. The browser is for anything it cannot do.

- **Sign-in:** Ana's own Chrome (Claude in Chrome). The built-in browser pane has no Cal.com or Google session.
- **Event types** live at `app.cal.com/links` (not /event-types). Seats are under the "Payments & Seats" tab.
- **Public page:** `cal.com/anaseahawk`. A slot can be opened straight into the booking form with `?date=YYYY-MM-DD&slot=<ISO UTC>&month=YYYY-MM`.
- **Cancel a booking:** `cal.com/booking/<uid>?cancel=true`; the reason is shared with the guests.
- **Test attendees:** Cal.com rejects addresses that can't receive mail (example.com/.org). Use plus-tags on Ana's Gmail only with her yes in chat.
- **Conflict checking** is account-wide. There is no per-event choice of calendars ("Consider only this booking link's bookings" needs an organization of 15+ members).
- **Finding (27 Nov 2026):** a booking on one event blocks that time on every other event of the same host. This is Cal.com's own check, not the Google calendars: with the booking written only to "Circles · Speaking Seats" (conflict check off), the listening event and the 60-minute event both lost the slot. So a speaking seat and a listening seat can't be two events on one account at the same time.
- **Check results** through Google Calendar (the GOA token): each test event writes to its own Circles calendar.
- **Isolated availability** (`useIsolatedAvailability`) is refused by the API with 403: "only available to organizations with at least 15 members" (checked 27 Nov 2026).
- **Two-seat answer (27 Nov 2026): a second host account works.** `cal.com/anaseahawk-circles` (display name Ana Seahawk; signed up under Ana's other Gmail, which stays out of this repo) holds the listening seats. Tested through the MCP: a speaking booking on `anaseahawk` left the listening slot on `anaseahawk-circles` fully open, and a listening booking left the speaking slot untouched. Test bookings cancelled.
- The MCP is signed in to the main account only. It can read availability and book or cancel on the second account (as a guest), but editing the second account's events goes through Chrome, where Ana signs in to it.
- **Second account must keep "Hide organizer's email" on every event**, or bookers see the private address. Its Google sign-up also brought in the private name, which was changed to Ana Seahawk.
- Cloudflare's human check fails in the built-in browser pane; sign-ups go in Chrome.
