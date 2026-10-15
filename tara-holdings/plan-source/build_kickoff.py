"""Build the kick-off presentation (16:9 HTML deck) for Tara Holding from the project plan data.

Usage (from tara-holdings/):  python3 plan-source/build_kickoff.py
Output: tara-kickoff-presentation.html  (arrow keys / click to navigate; prints one slide per 16:9 page)
"""
import json, html, re, datetime as dt
from itertools import groupby

D = json.load(open('plan-source/plan-data.json', encoding='utf-8'))
e = html.escape
OUT = 'tara-kickoff-presentation.html'
slides = []


def d(s):
    return dt.date.fromisoformat(s)


def fmt(s, e_=None):
    a = d(s)
    if not e_ or e_ == s:
        return f"{a.day} {a.strftime('%b')}"
    b = d(e_)
    return f"{a.day}–{b.day} {b.strftime('%b')}" if a.month == b.month else f"{a.day} {a.strftime('%b')} – {b.day} {b.strftime('%b')}"


def slide(body, tone='paper', num=None, title=None, kicker=None, cls=''):
    head = ''
    if title:
        n = f'<span class="cn">{num:02d}</span>' if num else ''
        k = f'<p class="kicker">{kicker}</p>' if kicker else ''
        head = f'<header class="sh">{n}<div><h2>{title}</h2>{k}</div></header>'
    slides.append(f'<section class="slide {tone} {cls}">{head}{body}</section>')


CHECK = '<svg class="ic" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'

# ---------------- 1. Cover ----------------
slide('''
<div class="cover">
  <div class="brandrow">
    <span class="plate"><img src="taraholding_logo.jpeg" alt="Tara Holding"></span>
    <span class="brandname">Tara Holding</span>
    <span class="x">with</span>
    <span class="plate wide"><img src="code-ox-logo.svg" alt="Code-ox Technologies"></span>
  </div>
  <div class="cover-main">
    <p class="cover-pre">Project kick-off, Thursday 15 October 2026</p>
    <h1>Odoo 19 Upgrade &amp; Urban&nbsp;Eats Implementation</h1>
  </div>
  <div class="span">
    <div class="pt"><span class="big">15 Oct 2026</span><span class="lbl">Work starts today</span></div>
    <div class="rail"><i></i></div>
    <div class="pt end"><span class="big gold">1 Jan 2027</span><span class="lbl">Every outlet live on Odoo POS</span></div>
  </div>
  <p class="cover-foot">Prepared by Code-ox Technologies, Odoo Silver Partner. Purchase Order TH P00008.</p>
</div>''', 'night', cls='is-cover')

# ---------------- 2. Agenda ----------------
agenda = ['Why we are here today', 'What we are delivering', 'The road to 1 January', 'Phases, timeline and milestones',
          'The first two weeks', 'Our team and how to reach us', 'How we work together', 'What we need from Tara Holding',
          'Decisions, risks and go-live', 'Next steps']
items = ''.join(f'<li><span class="an">{i + 1:02d}</span><span>{e(a)}</span></li>' for i, a in enumerate(agenda))
slide(f'<ol class="agenda">{items}</ol>', 'paper', None, 'Today’s agenda')

# ---------------- 3. Purpose ----------------
slide('''
<div class="purpose">
  <p class="lead-serif">The goal: Tara Holding upgraded to Odoo 19 and Urban Eats running on Odoo from 1 January 2027, on a platform your own team can run with confidence.</p>
  <div class="obj">
    <div><h3>Start the project</h3><p>Officially begin the work, with the agreement signed and the advance invoiced.</p></div>
    <div><h3>Align on the plan</h3><p>Walk through the phases, dates and milestones so both teams share one picture.</p></div>
    <div><h3>Confirm who does what</h3><p>Name the people, owners and escalation path on both sides.</p></div>
    <div><h3>Agree the first inputs</h3><p>Access, information and decisions Tara Holding provides in the first two weeks.</p></div>
  </div>
</div>''', 'green', 1, 'Why we are here today')

# ---------------- 4. Scope ----------------
part2 = ['Urban Eats as one company, with Brand, Branch and Channel reporting', 'Main Warehouse, Central Kitchen and outlet stock',
         'Products, recipes and central kitchen production', 'Restaurant POS and Kitchen Display per branch and brand',
         'Delivery platforms through UrbanPiper (Option B)', 'Settlement and platform reconciliation',
         'Paymob, Tabby, Tamara and POS terminals', 'ZATCA Phase 2', 'WhatsApp, loyalty and promotions',
         'Foodics exit with a full data archive']
p2 = ''.join(f'<li>{e(x)}</li>' for x in part2)
slide(f'''
<div class="scope">
  <div class="p1">
    <p class="tag">Part 1</p>
    <h3>Odoo 18 to 19 upgrade</h3>
    <p>All six companies move to Odoo 19 in the same database, with history intact.</p>
    <ul class="ticks"><li>{CHECK}Assessment and module-by-module register</li><li>{CHECK}Upgrade validated on staging first</li><li>{CHECK}Finance sign-off for each company</li><li>{CHECK}Production upgraded outside working hours</li></ul>
  </div>
  <div class="p2">
    <p class="tag">Part 2</p>
    <h3>Urban Eats / MYLK on Odoo 19</h3>
    <ul class="cols">{p2}</ul>
    <p class="note">Included after go-live: two weeks of hypercare, the Foodics archive, source and documentation handover, and support until 30 June 2027.</p>
  </div>
</div>''', 'paper', 2, 'What we are delivering')

# ---------------- 5. Road to go-live ----------------
road = [('15 Oct', 'Kick-off', 'Today'), ('29 Oct', 'SRS signed', 'Upgrade signed off on staging'),
        ('6–7 Nov', 'Production upgrade', 'Six companies on Odoo 19'), ('1 Dec', 'UAT environment', 'Committed date'),
        ('24 Dec', 'UAT accepted', 'Code freeze starts'), ('1 Jan', 'Go-live', 'Committed date'),
        ('30 Jun', 'Support ends', 'Six months under SLA')]
nodes = ''.join(f'<div class="node{" key" if t in ("UAT environment", "Go-live") else ""}"><i></i><span class="dt">{e(a)}</span><span class="nm">{e(t)}</span><span class="sb">{e(s)}</span></div>' for a, t, s in road)
slide(f'<div class="road"><div class="line"></div>{nodes}</div><p class="foot-note">The two committed dates hold if access, inputs and UAT feedback arrive on time and the delivery platforms approve their connections.</p>',
      'night', 3, 'The road to 1 January')

# ---------------- 6. Phases ----------------
ph_text = ['Agreement and access, requirement workshops, staging upgrade, finance sign-off and the production upgrade.',
           'Foundation, central kitchen, POS and Kitchen Display, platforms, payments, ZATCA, data loads and internal testing.',
           'Two UAT cycles, role-based training, cutover rehearsal and UAT acceptance.',
           'Production deployment, Go / No-Go, cutover night on 31 December and go-live on 1 January.',
           'Weekend cover, two weeks of hypercare, handover on 14 January, then support to 30 June 2027.']
phs = ''.join(f'<div class="phase"><span class="pn">{i + 1}</span><h3>{e(p["n"])}</h3><p class="pd">{e(fmt(p["s"], p["e"]))}</p><p>{e(ph_text[i])}</p></div>'
              for i, p in enumerate(D['phases']))
slide(f'<div class="phases">{phs}</div>', 'paper', 4, 'Five phases')

# ---------------- 7. Gantt ----------------
weeks = [('2026-10-15', '2026-10-22'), ('2026-10-25', '2026-10-29'), ('2026-11-01', '2026-11-05'), ('2026-11-08', '2026-11-12'),
         ('2026-11-15', '2026-11-19'), ('2026-11-22', '2026-11-26'), ('2026-11-29', '2026-12-03'), ('2026-12-06', '2026-12-10'),
         ('2026-12-13', '2026-12-17'), ('2026-12-20', '2026-12-24'), ('2026-12-27', '2027-01-02'), ('2027-01-03', '2027-01-07'),
         ('2027-01-10', '2027-01-14')]


def wk(s):
    x = d(s)
    for i, (a, b) in enumerate(weeks):
        if x <= d(b) + dt.timedelta(days=2):
            return i
    return len(weeks) - 1


tone = {'kickoff': 'g4', 'req': 'g2', 'upg': 'g1', 'prod': 'g1', 'found': 'g1', 'recipes': 'g1', 'kitchen': 'g1', 'pos': 'g1',
        'deliv': 'g2', 'settle': 'g2', 'wlz': 'g1', 'foodics': 'g4', 'test': 'g3', 'uat': 'g3', 'train': 'g3', 'cutover': 'g1', 'hyper': 'g2'}
g = ['<div class="gh first" style="grid-row:1;grid-column:1">Workstream</div>'] + [f'<div class="gh{" hot" if i in (6, 10) else ""}" style="grid-row:1;grid-column:{i + 2}">W{i + 1}<small>{e(fmt(a, b))}</small></div>' for i, (a, b) in enumerate(weeks)]
for r, (key, name, s0, e0) in enumerate(D['gantt']['rows']):
    row = r + 2
    g.append(f'<div class="gl" style="grid-row:{row}">{e(name)}</div>')
    g.append(f'<div class="gbar {tone.get(key, "g1")}" style="grid-row:{row};grid-column:{wk(s0) + 2}/{wk(e0) + 3}"></div>')
for c in (6, 10):
    g.append(f'<div class="gcol" style="grid-column:{c + 2};grid-row:1/{len(D["gantt"]["rows"]) + 3}"></div>')
mrow = len(D['gantt']['rows']) + 2
g.append(f'<div class="gline" style="grid-row:{mrow};grid-column:1/-1"></div>')
g.append(f'<div class="gl ms" style="grid-row:{mrow}">Milestones</div>')
by = {}
for mid, date, *_ in D['gantt']['ms']:
    by.setdefault(wk(date), []).append(mid)
for c, ids in by.items():
    g.append(f'<div class="gm" style="grid-row:{mrow};grid-column:{c + 2}"><i></i><span>{e(" ".join(ids))}</span></div>')
legend = '<div class="legend"><span><i class="g1"></i>Build and go-live</span><span><i class="g2"></i>Design, integration and support</span><span><i class="g3"></i>Testing, UAT and training</span><span><i class="g4"></i>Mobilisation and data</span></div>'
slide(f'<div class="gantt">{"".join(g)}</div>{legend}', 'paper', 5, 'Timeline', 'Seventeen workstreams across thirteen weeks, 15 October 2026 to 14 January 2027.', cls='tight')

# ---------------- 8. Milestones ----------------
ms = D['ms']
half = (len(ms) + 1) // 2


def mrows(lst):
    return ''.join(f'<li class="{"hot" if m.get("hot") else ""}"><span class="mid">{e(m["id"])}</span><span class="md">{e(m["said"])}</span><span class="mn">{e(m["name"])}</span></li>' for m in lst)


slide(f'<div class="mlist"><ul>{mrows(ms[:half])}</ul><ul>{mrows(ms[half:])}</ul></div><p class="foot-note">Gold marks the two committed dates.</p>',
      'green', 6, 'Fifteen milestones')

# ---------------- 9. First two weeks ----------------
first = [('Thu 15 Oct', 'Agreement signed, advance invoiced, kick-off held', 'Both teams'),
         ('Thu 15 Oct', 'Odoo.sh, staging and GitHub access', 'Tara IT'),
         ('Thu 15 Oct', 'Full production backup; staging branch created', 'Code-ox'),
         ('15–18 Oct', 'Staging copy upgraded to Odoo 19', 'Code-ox with Odoo'),
         ('15–22 Oct', 'Upgrade assessment and module register', 'Code-ox'),
         ('15–22 Oct', 'Foodics console and API access; data inventory', 'Tara IT, Code-ox'),
         ('18–21 Oct', 'Studio customisations and third-party modules checked', 'Code-ox'),
         ('18–26 Oct', 'Requirement workshops, two hours each', 'Both teams'),
         ('by 22 Oct', 'Joint Odoo and UrbanPiper meeting on platform coverage', 'Tara Holding'),
         ('21–27 Oct', 'Validation of every company and department on staging', 'Tara Finance, departments'),
         ('25–27 Oct', 'Software Requirements Specification prepared', 'Code-ox'),
         ('Thu 29 Oct', 'SRS signed; finance sign-off for each company', 'Tara Holding')]
rows = ''.join(f'<tr><td class="w">{e(a)}</td><td>{e(b)}</td><td class="{"tr" if "Tara" in c else ("both" if "Both" in c else "cx")}">{e(c)}</td></tr>' for a, b, c in first)
slide(f'<table class="tbl"><thead><tr><th style="width:15%">When</th><th>Task</th><th style="width:27%">Owner</th></tr></thead><tbody>{rows}</tbody></table>',
      'paper', 7, 'The first two weeks', '15 to 29 October: access, staging upgrade, workshops and the signed SRS.', cls='tight')

# ---------------- 10. Team ----------------
slide('''
<div class="team">
  <div class="org">
    <div class="person lead"><span class="role">Overall project handling</span><span class="name">Muhammed Thayif</span><span class="ttl">Co-founder, Code-ox</span></div>
    <div class="kids">
      <div class="col"><div class="person"><span class="role">Point of contact</span><span class="name">Raghib Ali Rafeeque</span><span class="ttl">Engagement Lead</span></div></div>
      <div class="col"><div class="person"><span class="role">Project Manager</span><span class="name">Shayar CV</span><span class="ttl">Runs delivery day to day</span></div>
        <div class="devs"><div class="person sm"><span class="name">Developer</span></div><div class="person sm"><span class="name">Developer</span></div><div class="person sm"><span class="name">Developer</span></div></div></div>
    </div>
  </div>
  <div class="client">
    <p class="tag">Tara Holding</p>
    <div class="cl"><span class="role">Project Owner</span><span class="name">Eng. AbdulRahman Al-Nouman</span></div>
    <div class="cl"><span class="role">Executive Sponsor</span><span class="name">Named at kick-off</span></div>
    <div class="cl"><span class="role">Area leads</span><span class="name sm">Finance (one validator per company), Procurement and Inventory, Central Kitchen, Operations and outlet managers, Marketing, IT</span></div>
  </div>
</div>''', 'paper', 8, 'Our team', 'One point of contact for Tara Holding, a project manager with three developers, and founder-level oversight.')

# ---------------- 11. Escalation ----------------
slide('''
<div class="esc">
  <div class="step s1"><span class="lv">Initial contact</span><span class="name">Raghib Ali Rafeeque</span><span class="ttl">Engagement Lead</span><span class="ct">raghib@code-ox.com<br>+966 561 765 707</span></div>
  <div class="step s2"><span class="lv">Escalation 1</span><span class="name">Shabeeb K</span><span class="ttl">Head of Operations</span><span class="ct">shabeeb.k@code-ox.com<br>+966 535 716 437</span></div>
  <div class="step s3"><span class="lv">Escalation 2</span><span class="name">Muhammed Thayif</span><span class="ttl">Co-founder</span><span class="ct">Final escalation</span></div>
</div>
<p class="foot-note">Start with Raghib for anything at all. If something needs more weight, it moves up one step at a time.</p>''',
      'night', 9, 'How to reach us')

# ---------------- 12. How we work ----------------
cad = [c for c in D['team']['cadence'] if c[0] != 'Kick-off']
crow = ''.join(f'<div class="wk"><h3>{e(a)}</h3><p class="when">{e(b)}</p><p>{e(x)}</p></div>' for a, b, c, x in cad)
slide(f'''<div class="work">{crow}
<div class="wk wide"><h3>Requirements and changes</h3><p class="when">SRS signed 29 October</p><p>The signed SRS is the agreed scope. Every change is assessed for scope, cost and dates, approved in writing and recorded as a new SRS revision. Code freeze starts on 24 December.</p></div>
</div>''', 'green', 10, 'How we work together')

# ---------------- 13. Inputs ----------------
ins = [x for x in D['inputs'] if x['due'] <= '2026-10-29']
irows = ''.join(f'<tr><td class="w">{e(x["said"])}</td><td><b>{e(x["item"].replace("Platform merchant accounts (A) or UrbanPiper order (B)", "UrbanPiper order and platform merchant accounts").replace("Odoo.sh access, staging URL + admin login, GitHub read access; Code-ox on the subscription", "Odoo.sh, staging and GitHub access for Code-ox"))}</b></td><td>{e(x["owner"])}</td></tr>' for x in ins)
slide(f'<table class="tbl"><thead><tr><th style="width:15%">Due</th><th>Input from Tara Holding</th><th style="width:22%">Owner</th></tr></thead><tbody>{irows}</tbody></table>'
      , 'paper', 11, 'What we need first', f'Inputs due by 29 October. There are {len(D["inputs"])} in total, all listed in the Project Plan; a late input moves the tasks that depend on it.', cls='tight')

# ---------------- 14. Decisions ----------------
decs = sorted(D['decs'], key=lambda x: x['due'])
cols = ''
for due, grp in groupby(decs, key=lambda x: x['said']):
    lis = ''
    for x in grp:
        if x['id'] == 'D-01':
            lis += f'<li class="done">{CHECK}<span><b>{e(x["id"])}</b> Delivery layer confirmed: Option B, UrbanPiper</span></li>'
        else:
            item = re.sub(r' *\(.*?\)', '', x['item'])
            lis += f'<li><b>{e(x["id"])}</b> {e(item)}</li>'
    cols += f'<div class="dcol"><p class="dd">{e(due)}</p><ul>{lis}</ul></div>'
slide(f'<div class="decs">{cols}</div>', 'night', 12, 'Decisions calendar', 'Fifteen decisions, each due before the work that depends on it.', cls='tight')

# ---------------- 15. Risks ----------------
risks = [('Delivery platform coverage', 'Odoo’s UrbanPiper list does not include ToYou or The Chefz today. Coverage is confirmed in the joint meeting by 22 October; any platform not covered stays on its tablet or gets a direct connector.', 'Tara Holding and UrbanPiper'),
         ('Six companies validated in one week', 'Before-and-after reports are prepared in advance, so finance reviews only the differences.', 'Both teams'),
         ('Recipes rebuilt from the start', 'Foodics holds no recipes. Templates arrive on day one, recipe workshops run in weeks two and three, top sellers first.', 'Tara Holding'),
         ('Data Foodics cannot export', 'A gap report by 22 October, so the approach for anything missing is agreed early.', 'Code-ox'),
         ('Devices or network late', 'Specification on 29 October, devices on site by 19 November, pilot test from 24 to 26 November.', 'Tara Holding'),
         ('Late scope changes', 'Every change goes through change control against the signed SRS. Code freeze starts on 24 December.', 'Both teams')]
rk = ''.join(f'<div class="risk"><h3>{e(a)}</h3><p>{e(b)}</p><span class="own">{e(c)}</span></div>' for a, b, c in risks)
slide(f'<div class="risks">{rk}</div>', 'paper', 13, 'Risks we are watching', 'Reviewed every week, so nothing surprises either team.', cls='tight')

# ---------------- 16. Go-live ----------------
gl = [('29 Dec', 'Go / No-Go', 'Checklist signed by both sides'), ('31 Dec', 'Cutover night', 'Final Foodics export and stock count'),
      ('1 Jan', 'Go-live', 'Every outlet on Odoo POS'), ('1–2 Jan', 'Weekend cover', 'Code-ox team on call'),
      ('3–14 Jan', 'Hypercare', 'Two weeks of close support'), ('14 Jan', 'Handover', 'Source code and documents')]
gls = ''.join(f'<div class="gs"><span class="n">{i + 1}</span><span class="dt">{e(a)}</span><h3>{e(b)}</h3><p>{e(c)}</p></div>' for i, (a, b, c) in enumerate(gl))
slide(f'''<div class="golive">{gls}</div>
<div class="sla">
  <div><span class="pr">Critical</span><span>Response in 1 hour, 7 days a week</span><span>Fix in 4 hours</span></div>
  <div><span class="pr">High</span><span>Response in 4 hours</span><span>Fix in 1 business day</span></div>
  <div><span class="pr">Normal</span><span>Response in 1 business day</span><span>Fix in 3 business days</span></div>
</div>
<p class="foot-note">From 1 January all outlets use Odoo POS only. Foodics stays read-only until the archive is verified. Support runs until 30 June 2027.</p>''',
      'green', 14, 'Go-live and support')

# ---------------- 17. Next steps ----------------
nxt = [('Today', 'Agreement signed and kick-off held', 'Both teams'), ('Today', 'Odoo.sh, staging and GitHub access granted', 'Tara IT'),
       ('Today', 'Executive sponsor, project owner and key users named', 'Tara Holding'), ('15–18 Oct', 'Backup and staging upgrade to Odoo 19', 'Code-ox'),
       ('From 18 Oct', 'Requirement workshops begin', 'Both teams'), ('By 22 Oct', 'Questionnaires, Foodics items, outlet list and merchant accounts', 'Tara Holding'),
       ('29 Oct', 'SRS signed; upgrade signed off on staging', 'Tara Holding')]
ns = ''.join(f'<li><span class="an">{i + 1:02d}</span><span class="nw">{e(a)}</span><span class="nt">{e(b)}</span><span class="no">{e(c)}</span></li>' for i, (a, b, c) in enumerate(nxt))
slide(f'<ol class="next">{ns}</ol>', 'paper', 15, 'Next steps')

# ---------------- 18. Close ----------------
slide('''
<div class="close">
  <p class="cover-pre">Thank you</p>
  <h1>Let’s begin.</h1>
  <p class="lead-serif">Questions, now or at any point: Raghib is your first call.</p>
  <div class="contacts">
    <div><span class="name">Raghib Ali Rafeeque</span><span>Engagement Lead</span><span>raghib@code-ox.com</span><span>+966 561 765 707</span></div>
    <div><span class="name">Shabeeb K</span><span>Head of Operations</span><span>shabeeb.k@code-ox.com</span><span>+966 535 716 437</span></div>
  </div>
  <div class="brandrow end"><span class="plate"><img src="taraholding_logo.jpeg" alt="Tara Holding"></span><span class="plate wide"><img src="code-ox-logo.svg" alt="Code-ox Technologies"></span></div>
</div>''', 'night', cls='is-cover')

CSS = open('plan-source/kickoff.css', encoding='utf-8').read()
JS = open('plan-source/kickoff.js', encoding='utf-8').read()
total = len(slides)
body = '\n'.join(s.replace('</section>', f'<span class="pg">{i + 1:02d} / {total:02d}</span></section>', 1) for i, s in enumerate(slides))
doc = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Project Kick-off — Tara Holding × Code-ox</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="stage"><div class="deck">{body}</div></div>
<div class="hud"><div class="bar"><i></i></div></div>
<script>{JS}</script>
</body></html>
'''
open(OUT, 'w', encoding='utf-8').write(doc)
print('slides', total)
