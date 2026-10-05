# Sara — AIKA live voice demo for Madeline (Vapi)

A single-page, talk-to-it demo of Madeline's AI collector, built on the Vapi Web SDK.
You play the customer; "Sara" verifies you, discusses the balance and writes the
outcome to the CRM panel through her own tool calls.

## Run it (2 minutes)

1. Get your **public key**: Vapi dashboard → Organization settings → API Keys → *Public key*.
   (Never put the private key in the page.)
2. Serve this folder over http (the browser needs a secure context for the microphone):
   ```bash
   cd aika-live-demo
   npx serve .          # or: python3 -m http.server 8080
   ```
   Open http://localhost:3000 (or :8080).
3. Pick a sample customer → **Start call**. The page ships with Madeline's public key and the saved assistant
   `Sara — Madeline Collections` (ID `684fb868-a207-469a-b993-13238147921d`) as defaults; change them in ⚙︎.

`code-ox-logo.svg` sits next to `index.html`; the folder is self-contained and can be dropped on any static host.

## Two ways to run the assistant

| Mode | When | How |
|---|---|---|
| **Inline** | Quick demos, iterating on the prompt | Leave *Assistant ID* empty. The page sends the full Sara configuration with each call (`vapi.start(assistantObject)`). Edit `systemPrompt()` / `TOOLS` in `index.html`. |
| **Saved assistant (default)** | Client-facing, phone numbers, analytics in the dashboard | ⚙︎ → *Copy create-assistant cURL* → run it with `VAPI_PRIVATE_KEY` set → paste the returned `id` into *Assistant ID*. The page then passes the customer record as `variableValues`. |

`assistant.sara.json` in this folder is the same template, ready to `POST https://api.vapi.ai/assistant`.

## What Sara does

- Speaks first (Arabic or English depending on the customer's file), discloses recording.
- Verifies identity (last 4 of ID) **before** mentioning the client, product or balance.
- Detects language/dialect from the reply; Saudi colloquial by default, switches to English on request.
- Offers options in order: pay now by link → promise to pay within 14 days → up to 3 instalments. No waivers.
- Handles every scenario from the discovery document: agreed to pay, callback, refusal, dispute, wrong number, asks for a human, distress → escalate.
- Calls three client-side tools the page renders live:
  - `record_call_outcome` → status / sub-status / PTP / reason
  - `send_payment_link` → payment link chip
  - `escalate_to_human` → agent screen-pop card
  then `endCall`.

## Providers (change in ⚙︎)

- **Transcriber**: ElevenLabs Scribe v2 realtime (auto AR/EN) with OpenAI `gpt-4o-transcribe` fallback. Alternatives: OpenAI, Gladia Solaria (explicit ar+en code-switching), Deepgram Nova-3 multi.
- **Voice**: Vapi v2 `Layla` (default) / `Savannah` / `Elliot` with `language: auto` (Vapi retired Hana, Neha, Lily, Kylie, Cole, Harry, Paige, Spencer); ElevenLabs `sarah` on turbo v2.5; or any ElevenLabs Arabic voice ID on multilingual v2 — the best option for Najdi delivery.
- **Model**: OpenAI gpt-4o (default), gpt-4.1, gpt-4o-mini.

All of these use Vapi's built-in provider keys; nothing else to configure for the demo.

## Production notes (not in the demo)

- Real CRM read/write happens server-side: Vapi → your webhook (`serverUrl`) → CRM REST API. The demo updates the panel in the browser only.
- `analysisPlan` in the saved template produces a 3-line summary and structured data (status, sub_status, promised_amount, …) after every call for the CRM write-back.
- Outbound phone calls need a Saudi number on a SIP trunk connected to Vapi; calling hours, retry rules and attempt limits live in the campaign layer, not in the assistant.
- Live transfer to a human agent uses Vapi's `transferCall` tool with your contact-centre number or SIP URI; the demo simulates it with a screen-pop.
