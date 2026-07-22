# NADEC — Social Media Presence

Source: `/en/social-media`
Full structured data: `12-json-data/social-media.json`

## Platforms confirmed present
| Platform | Handle |
|---|---|
| Facebook | facebook.com/nadec.com.sa |
| Instagram | instagram.com/nadecfoods/ |
| LinkedIn | linkedin.com/company/nadecfoods/ |
| X (Twitter) | twitter.com/nadecfoods |
| YouTube | youtube.com/user/NadecKSA/videos |
| TikTok | tiktok.com/@nadecfood |
| Snapchat | snapchat.com/add/nadecfoods |

Seven platforms is a broad footprint, consistent with a large FMCG consumer brand targeting the Saudi market (TikTok and Snapchat presence in particular reflects an intentional youth/mobile-first content strategy, not just legacy Facebook/Twitter maintenance).

## What could and couldn't be verified
- Follower counts, posting frequency, engagement rates, and content strategy details are **not shown on the NADEC website itself** — the `/en/social-media` page is a link/embed hub, not an analytics dashboard. Determining these would require visiting each platform directly, which is out of scope for a website-content crawl and was not done in this pass.
- The page embeds a **live Twitter/X feed widget**, which is the one platform where the site itself signals ongoing active use (the widget would show blank/stale if the account were dormant, and the embed choice implies X is treated as a primary real-time channel).
- Brand handle naming is inconsistent across platforms: `nadecfoods` (Instagram, LinkedIn, X, Snapchat) vs `nadec.com.sa` (Facebook) vs `NadecKSA` (YouTube) vs `nadecfood` (TikTok, singular). This fragmentation is a minor brand-consistency issue worth flagging.

## Recommendation flag
A social-media analytics pull (via each platform's public page or a tool like Social Blade / Meta Business Suite if client-side access is available) should be a discovery-phase task if the RFP scope includes social/content strategy — this knowledge base intentionally does not fabricate follower/engagement numbers that aren't published on-site.
