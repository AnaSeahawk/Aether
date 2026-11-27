---
name: circle-booking
description: Open a Circle date for booking on Cal.com — a speaking seat on Ana's main account and a listening seat on her second account, made to feel like one booking. Use when Ana sets a date for a Circle, changes its seats or prices, or asks how Circle booking works.
---

# Skill — circle-booking

A Circle has two kinds of seat: a **speaking seat** (joins the conversation)
and a cheaper **listening seat** (present and receiving). On one Cal.com
account, a booking on one event blocks that hour on every other event of the
same host, so the two seats can't share a time there. The answer, tested on
27 Nov 2026: two accounts that look like one.

| Seat | Cal.com account | Reached by | Google calendar |
|---|---|---|---|
| Speaking | `cal.com/anaseahawk` (main) | the Cal.com MCP | Circles · Speaking Seats |
| Listening | `cal.com/anaseahawk-circles` (second) | Ana's Chrome, signed in to the second account | Circles · Listening Seats (to be shared with the second account) |

Both Circle calendars are excluded from conflict checking on the main account.
The second account's sign-in email is private: it carries a name Ana keeps out
of public view. Never write it into this repo or onto a page.

## Use the MCP first

The Cal.com MCP is signed in to the main account. It creates, edits, books and
cancels there, and it can read open times and book or cancel seats on the
second account. Editing the second account's events and settings goes through
Chrome (see `.claude/skills/browser-work/sites/cal.md`).

## Opening a Circle date

Get from Ana: the Circle, the date and hour (her time zone, America/Mexico_City
unless she says otherwise), the length (most Circles run two hours: 90 minutes,
then 30 minutes of open conversation), the price and the cap for each seat.

For each seat, make one event with the same title, words and length:

- **Title:** `<Circle name> · Speaking seat` and `<Circle name> · Listening seat`.
- **Slug:** `<circle-slug>-<yyyy-mm-dd>-speaking` and `…-listening`.
- **Seats on,** with Ana's cap; show the count of seats left; don't share
  attendee information between guests.
- **Hidden from the profile.** People arrive from the website, not the
  Cal.com profile.
- **One hour only:** a booking window of that one date (range type), and an
  availability schedule that opens only that hour, made as a date override.
- **Payment:** PayPal at that seat's price, paid on booking.
- **Same video link** in both, so speakers and listeners meet in one room.
  Ana chooses the room (Zoom or Google Meet); a fixed link is simplest.
- **Same thank-you:** set the success redirect of both to the Circle's page
  on anaseahawk.com, so every booker lands in the same place.
- **Second account only:** turn on *Hide organizer's email* on every event.

Then book nothing. Check both events through the MCP (`get_availability` for
each username and slug): the hour shows, with the full seat count.

## One booking, not two

The visitor never chooses an account. On the Circle's page on anaseahawk.com,
one "Take a seat" block shows the date once, then the two seats side by side:
the speaking and listening pictures already used on the site, a line each, the
price, and a button. Each button opens that seat's Cal.com page.

Keep the two Cal.com accounts looking the same: name **Ana Seahawk**, the same
photo, brand colour and bio. Confirmation emails then come from the same name.

## Still to set up (as of 27 Nov 2026)

- PayPal on the second account. Ana connects it herself (its keys are hers to
  enter), to the same PayPal account as the main one.
- Share Circles · Listening Seats with the second account, and connect its
  Google Calendar to write only there.
- The second account's photo and brand colour to match the main one.
- The first real date: Ana picks the Circle, the date, and the two prices.
