"""Build the A4 print version of the Tara Holding project plan in the Tara template.

Usage (from tara-holdings/):
  python3 plan-source/build_plan.py                # estimate row heights
  python3 plan-source/build_plan.py heights.json   # paginate with row heights measured in a browser

Inputs:  plan-source/plan-data.json (tasks, milestones, inputs, decisions, risks, team, gantt)
         plan-source/plan.css       (Tara template + print overrides)
Output:  Tara_Holding_Project_Plan_Print.html  (render to PDF with Chrome --print-to-pdf)
"""
import re, json, sys, math, html, datetime as dt
from itertools import groupby

HERE = 'plan-source'
D = json.load(open(f'{HERE}/plan-data.json', encoding='utf-8'))
css = open(f'{HERE}/plan.css', encoding='utf-8').read()
HJ = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else None
BUDGET = (HJ['ic'] - HJ['head'] - 14) if HJ else 960.0  # usable px per inner page
OUT = 'Tara_Holding_Project_Plan_Print.html'

e = html.escape
HDR = 'Tara Holding — Expected Project Plan'
REF = 'Based on Execution Plan v1.2 · 13 Oct 2026'
FOOT = 'Code-ox Technologies · raghib@code-ox.com · +966 561 765 707 | Odoo Silver Partner'
EXT = {'Odoo', 'Platforms', 'UrbanPiper', 'Meta', 'ZATCA'}
pages = []


def page(body, label, title, intro=''):
    pages.append((label, title, intro, body))


def d(s):
    return dt.date.fromisoformat(s)


def fmt(s, e_=None):
    a = d(s)
    if not e_ or e_ == s:
        return f"{a.day} {a.strftime('%b')}"
    b = d(e_)
    return f"{a.day}–{b.day} {b.strftime('%b')}" if a.month == b.month else f"{a.day} {a.strftime('%b')}–{b.day} {b.strftime('%b')}"


def pills(t):
    p = [f'<span class="who cx">{e(r)}</span>' for r in t.get('cx', [])]
    p += [f'<span class="who {"ex" if r in EXT else "tr"}">{e(r)}</span>' for r in t.get('ot', [])]
    return ''.join(p) or '—'


# ---------- task text: module tags and step flows ----------
MODS = ['simplify_access_management', 'advanced_web_domain_widget', 'auditlog', 'hide_menu_user', 'Hikvision attendance',
        'muk_web_utils', 'notify_email_inbox', 'muk_mcp_access', 'muk_mcp', 'pos_paymob', 'paymob']
MOD_RE = re.compile(r'\b(' + '|'.join(re.escape(m) for m in MODS) + r')\b')


def flow(steps, sep):
    arrow = f'<span class="arr">{sep}</span>'
    return '<span class="flow">' + arrow.join(f'<span class="step">{e(x.strip())}</span>' for x in steps) + '</span>'


def flows(text):
    """Clauses holding a sequence of 3+ steps (a → b → c, or a › b › c) become a chip flow; the rest stays text."""
    parts, rest = [], []
    for clause in text.split('; '):
        sep = '→' if clause.count('→') >= 2 else '›' if clause.count('›') >= 2 else None
        if not sep:
            rest.append(clause)
            continue
        if rest:
            parts.append(e('; '.join(rest)))
            rest = []
        lead, _, seq = clause.rpartition(': ') if ': ' in clause.split(sep)[0] else ('', '', clause)
        parts.append((e(lead + ':') if lead else '') + flow(seq.split(sep), sep))
    if rest:
        parts.append(e('; '.join(rest)))
    return ''.join(parts) if any('class="flow"' in x for x in parts) else e(text)


def task_text(text):
    out = MOD_RE.sub(lambda m: f'<span class="mod">{m.group(1)}</span>', flows(text))
    return re.sub(r'</span>,\s*(?=<span class="mod">)', '</span> ', out)  # tags separate themselves


def lines(text, chars):
    return max(1, math.ceil(len(text) / chars))


def task_row(t):
    when = t.get('said') or (fmt(t['s'], t.get('e')) if t.get('s') else '—')
    ms = f'<span class="badge">{e(t["ms"])}</span>' if t.get('ms') else ''
    roles = t.get('cx', []) + t.get('ot', [])
    own = max(1, math.ceil(sum(len(r) * 6 + 18 for r in roles) / 105)) if roles else 1
    n = max(lines(t['task'], 62), lines(t.get('out', ''), 18), lines(when, 13), own, lines(t.get('needs', ''), 8))
    h = HJ['rows'].get(t['id'], n * 16.7 + 10) if HJ else n * 16.7 + 10
    cls = ' class="ms"' if t.get('ms') else ''
    row = (f'<tr{cls}><td class="id">{e(t["id"])}</td><td><b>{task_text(t["task"])}</b>{ms}</td>'
           f'<td class="dt">{e(when)}</td><td class="own">{pills(t)}</td>'
           f'<td>{e(t.get("needs", "—"))}</td><td>{e(t.get("out", ""))}</td></tr>')
    return row, h


TH = ('<table class="t tk"><thead><tr><th style="width:6%">ID</th><th style="width:44%">Task</th>'
      '<th style="width:12%">When</th><th style="width:15%">Owner</th><th style="width:8%">Needs</th>'
      '<th style="width:15%">Output</th></tr></thead><tbody>')

# ---------- cover ----------
phases = ''.join(
    f'<div><div class="n">Phase {i + 1}</div><div class="t">{e(p["n"])}</div><div class="d">{e(fmt(p["s"], p["e"]))}</div></div>'
    for i, p in enumerate(D['phases']))
cover = f'''<section class="page cv"><div class="cv-bar"></div>
<div class="cv-top"><div class="l"><div><div class="cv-client">Tara Holding</div><div class="cv-sub">Urban Eats · Kingdom of Saudi Arabia</div></div><div class="cv-div"></div><div><div class="cv-pl">Prepared by</div><div class="cv-pn">Code-ox Technologies</div></div></div><div class="pill">Project Plan</div></div>
<div class="cv-hero">
<div class="cv-over">Expected project plan · 13 October 2026</div>
<div class="cv-title">From Kick-off<br>on 15 October<br><span>to Go-live on 1 January</span></div>
<div class="cv-lead">The Odoo 19 upgrade for six companies and Urban Eats on Odoo POS, planned task by task. Dates are expected dates from Execution Plan v1.2. Handover follows on 14 January, then support to 30 June 2027.</div>
<div class="kd">
<div><div class="k">Kick-off</div><div class="v">15 Oct</div><div class="s">Thu · 2026</div></div>
<div><div class="k">SRS signed</div><div class="v">29 Oct</div><div class="s">upgrade signed off too</div></div>
<div><div class="k">UAT environment</div><div class="v">1 Dec</div><div class="s">Tue · committed</div></div>
<div class="hl"><div class="k">Go-live</div><div class="v">1 Jan</div><div class="s">Fri · all outlets on Odoo POS</div></div>
<div><div class="k">Support</div><div class="v">30 Jun</div><div class="s">2027 · six months</div></div>
</div>
<div class="ph-l">Five phases</div>
<div class="ph">{phases}</div>
<div class="cv-points">
<div><b>Standard Odoo first</b>Standard, then configuration, Studio, a supported module, and custom development last. Each custom item is justified in writing and approved before it is built.</div>
<div><b>Staging first, production last</b>Every department validates on staging, and finance signs off each company before production is touched.</div>
<div><b>Dated and linked</b>Every task has a start, an end, an owner and the task or input it depends on, tracked live in Odoo Project.</div>
<div><b>Signed requirements baseline</b>Scope, prices and terms are as in proposal CX-TARA-2026-02 Rev. 1. The SRS signed on 29 October is the baseline for the build and for change control.</div>
</div>
</div>
<div class="cv-ref"><div><div class="k">Document</div><div class="v">Expected Project Plan</div></div><div><div class="k">Based on</div><div class="v">Execution Plan v1.2</div></div><div><div class="k">Companion to</div><div class="v">CX-TARA-2026-02 Rev. 1</div></div><div><div class="k">Date</div><div class="v">13 October 2026</div></div></div>
<div class="cv-foot"><img src="code-ox-logo.svg" alt="Code-ox"><span>raghib@code-ox.com · +966 561 765 707 · code-ox.com · 3239 Al Zubair Bin Al Awwam St, Al Rawabi Dist., Riyadh 14215, Kingdom of Saudi Arabia</span></div>
</section>'''

# ---------- overview + milestones ----------
msrows = ''.join(
    f'<tr{" class=ms" if m.get("hot") else ""}><td class="id">{e(m["id"])}</td><td><b>{e(m["name"])}</b></td>'
    f'<td class="dt">{e(m["said"])}</td><td>{e(m["needs"])}</td><td>{e(m["by"])}</td><td>{e(m["ev"])}</td></tr>'
    for m in D['ms'])
page(f'''<div class="two" style="margin-bottom:6px">
<div class="card"><h4>Part 1: Odoo 18 to 19 upgrade</h4><ul><li>All six existing companies move to <b>Odoo 19 in the same database</b>, with history intact.</li><li>Everything is validated on staging first, and <b>finance signs off each company</b> before production is touched.</li></ul></div>
<div class="card"><h4>Part 2: Urban Eats on Odoo 19</h4><ul><li>Structure and finance, central kitchen, <b>POS and Kitchen Display</b>, delivery platforms, payments, ZATCA, WhatsApp, loyalty, and the <b>exit from Foodics</b>.</li><li>Requirements are signed off in one <b>SRS</b> before the build starts on 1 November.</li></ul></div>
</div>
<h3>Milestones</h3>
<div class="intro" style="margin-bottom:6px">Fifteen milestones from kick-off to the end of support. The two committed dates are the UAT environment on 1 December and go-live on 1 January.</div>
<table class="t"><thead><tr><th style="width:5%">#</th><th style="width:30%">Milestone</th><th style="width:14%">Date</th><th style="width:12%">Needs</th><th style="width:17%">Confirmed by</th><th style="width:22%">Evidence</th></tr></thead><tbody>{msrows}</tbody></table>''',
     'Overview', 'The Plan at a Glance',
     'Work starts on Thursday 15 October 2026. The UAT environment opens on Tuesday 1 December and every outlet goes live on Odoo POS on Friday 1 January 2027, with six months of support after that.')

# ---------- gantt ----------
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


colour = {'kickoff': 'b5', 'req': 'b3', 'upg': 'b1', 'prod': 'b1', 'found': 'b1', 'recipes': 'b1', 'kitchen': 'b1', 'pos': 'b1',
          'deliv': 'b3', 'settle': 'b3', 'wlz': 'b1', 'foodics': 'b4', 'test': 'b2', 'uat': 'b2', 'train': 'b2', 'cutover': 'b1',
          'hyper': 'b3'}
g = ['<div class="h first" style="grid-row:1;grid-column:1">Workstream</div>']
for i, (a, b) in enumerate(weeks):
    g.append(f'<div class="h" style="grid-row:1;grid-column:{i + 2}">W{i + 1}<small>{e(fmt(a, b))}</small></div>')
rows = D['gantt']['rows']
for r, (key, name, s0, e0) in enumerate(rows):
    gr = r + 2
    g.append(f'<div class="rl" style="grid-row:{gr};grid-column:1">{e(name)}</div>')
    for c in range(13):
        hl = ' wk' if c in (6, 10) else ''
        g.append(f'<div class="c{hl}" style="grid-row:{gr};grid-column:{c + 2}"></div>')
    a, b = wk(s0), wk(e0)
    g.append(f'<div class="bar {colour.get(key, "b1")}" style="grid-row:{gr};grid-column:{a + 2}/{b + 3}"></div>')
gr = len(rows) + 2
g.append(f'<div class="rl" style="grid-row:{gr};grid-column:1">Milestones</div>')
bycol = {}
for mid, date, *_ in D['gantt']['ms']:
    bycol.setdefault(wk(date), []).append(mid)
for c in range(13):
    if c in bycol:
        g.append(f'<div class="msc" style="grid-row:{gr};grid-column:{c + 2}"><div class="dm"></div><div class="ml">{e(" ".join(bycol[c]))}</div></div>')
    else:
        g.append(f'<div class="c" style="grid-row:{gr};grid-column:{c + 2}"></div>')
page(f'''<div class="gt">{''.join(g)}</div>
<div class="legend"><span><i class="b1"></i>Build &amp; go-live</span><span><i class="b3"></i>Design, integration &amp; support</span><span><i class="b2"></i>Testing, UAT &amp; training</span><span><i class="b4"></i>Data migration</span><span><i class="b5"></i>Mobilisation</span><span><i class="d"></i>Milestone</span></div>
<div class="two" style="margin-top:8px">
<div class="note g" style="margin:0"><div class="nl">Upgrade before cutover</div>The upgrade is signed off by <b>29 October</b> and production is upgraded on the weekend of <b>6–7 November</b>, so cutover night carries only the Urban Eats switch.</div>
<div class="note" style="margin:0"><div class="nl">Highlighted weeks</div><b>W7</b>: the UAT environment goes live on Tue 1 Dec. <b>W11</b>: cutover week, ending on the night of 31 Dec for go-live on Fri 1 Jan 2027, with weekend cover on 1–2 Jan.</div>
</div>''', 'Timeline', 'Gantt: Kick-off to Handover',
     'Seventeen workstreams across thirteen weeks, Thursday 15 October 2026 to Thursday 14 January 2027. Weeks run Sunday to Thursday.')

# ---------- tasks (paginated) ----------
groups = [(ws, list(ts)) for ws, ts in groupby(D['tasks'], key=lambda t: t['ws'])]
first_intro = ('Every task with its expected dates, owner, dependency and output. Green tags are Code-ox roles, gold tags are '
               'Tara Holding and grey tags are third parties; gold rows are milestones. In Needs, an ID must be finished first, '
               'and “with” marks work that runs alongside it.')
WSH = float(HJ.get('wsr', 40)) if HJ else 40.0  # workstream row inside the table
TBL = float(HJ['th'] + HJ['tblmb']) if HJ else 33.0  # one table header per page
budget = BUDGET - (HJ['intro'] if HJ else 72)
chunks, cur, used = [], [], TBL
for ws, ts in groups:
    i = 0
    while i < len(ts):
        need = WSH + task_row(ts[i])[1]
        if used + need > budget and cur:
            chunks.append(cur); cur, used, budget = [], TBL, BUDGET
        part, used = [], used + WSH
        while i < len(ts):
            r, h = task_row(ts[i])
            if used + h > budget and part:
                break
            part.append(r); used += h; i += 1
        cur.append((ws, part))
        if i < len(ts):
            chunks.append(cur); cur, used, budget = [], TBL, BUDGET
if cur:
    chunks.append(cur)
for n, ch in enumerate(chunks):
    body = TH
    for ws, part in ch:
        m = re.match(r'(WS \w+)\s+(.*)', ws)
        tag, name = (m.group(1), m.group(2)) if m else ('', ws)
        body += f'<tr class="wsr"><td colspan="6"><span class="ws">{e(tag)}</span>{e(name)}</td></tr>' + ''.join(part)
    body += '</tbody></table>'
    page(body, 'Task list', 'Tasks by Workstream', first_intro if n == 0 else '')

# ---------- inputs ----------
n_in, n_dec = len(D['inputs']), len(D['decs'])
n_early = sum(1 for x in D['inputs'] if x['due'] <= '2026-10-22')
inr = ''.join(f'<tr><td class="id">{e(i["id"])}</td><td><b>{e(i["item"])}</b></td><td class="dt">{e(i["said"])}</td>'
              f'<td>{e(i["owner"])}</td><td>{e(i["unb"])}</td></tr>' for i in D['inputs'])
page(f'''<div class="cnt"><div><div class="v">{n_in}</div><div class="k">inputs from Tara Holding</div></div><div><div class="v">{n_early}</div><div class="k">inputs due by 22 October</div></div><div><div class="v">{n_dec}</div><div class="k">decisions</div></div><div><div class="v">29 Oct</div><div class="k">SRS signed by the Project Owner</div></div></div>
<h3>Inputs</h3>
<table class="t"><thead><tr><th style="width:7%">ID</th><th style="width:48%">Input</th><th style="width:14%">Due</th><th style="width:15%">Owner</th><th style="width:16%">Unblocks</th></tr></thead><tbody>{inr}</tbody></table>''',
     'Inputs and decisions', 'What Tara Holding Provides',
     f'Tara Holding owes {n_in} inputs and {n_dec} decisions. {n_early} of the inputs fall due by 22 October, so the first week carries the most. A late input moves the tasks that depend on it.')

# ---------- decisions ----------
dcr = ''.join(f'<tr><td class="id">{e(x["id"])}</td><td><b>{e(x["item"])}</b></td><td class="dt">{e(x["said"])}</td></tr>'
              for x in D['decs'])
page(f'''<table class="t"><thead><tr><th style="width:8%">ID</th><th style="width:70%">Decision</th><th style="width:22%">Due</th></tr></thead><tbody>{dcr}</tbody></table>
<div class="note"><div class="nl">Dates and conditions</div>The 1 December and 1 January dates hold if the agreement is signed and kick-off is held by <b>15 October</b>, the SRS is signed on <b>29 October</b>, inputs arrive on the dates in this plan, UAT feedback is timely, and delivery-platform approvals come through.</div>
<div class="note g"><div class="nl">Dates in this plan</div>Dates are expected dates from Execution Plan v1.2. They move with the signed agreement, Tara's inputs and platform approvals.</div>''',
     'Inputs and decisions', 'Decisions Needed from Tara Holding',
     'Each decision is due on the date shown so the tasks that depend on it can start on time.')

# ---------- team ----------
tm = D['team']
cxr = ''.join(f'<li><b>{e(r)}</b>: {e(n)}. {e(t)}</li>' for r, n, t in tm['cx'])
trr = ''.join(f'<li><b>{e(r)}</b>: {e(n)}. {e(t)}</li>' for r, n, t in tm['tara'])
cad = ''.join(f'<tr><td><b>{e(a)}</b></td><td class="dt">{e(b)}</td><td>{e(c)}</td><td>{e(x)}</td></tr>' for a, b, c, x in tm['cadence'])
page(f'''<div class="two">
<div class="card"><h4>Code-ox Technologies</h4><ul>{cxr}</ul></div>
<div class="card"><h4>Tara Holding</h4><ul>{trr}</ul></div>
</div>
<h3>How we stay in sync</h3>
<table class="t"><thead><tr><th style="width:18%">Forum</th><th style="width:22%">When</th><th style="width:25%">Who</th><th style="width:35%">Covers</th></tr></thead><tbody>{cad}</tbody></table>
<div class="note g"><div class="nl">Requirements baseline</div>All requirements are consolidated into one <b>Software Requirements Specification (SRS)</b>, issued on 27 October and signed by Tara's Project Owner on <b>29 October</b>, before the build starts on 1 November.</div>
<div class="note"><div class="nl">Change control</div>Every change after sign-off is measured against the signed SRS. Change requests are logged in the tracker with their impact on scope, cost and dates, and work begins only on written approval. Each approved change is recorded in the SRS as a new revision, so the SRS always shows the agreed scope. Code freeze starts on <b>24 December</b>, with Critical fixes only.</div>''',
     'Team and governance', 'Team, Roles &amp; Governance',
     "Raghib Ali Rafeeque is Tara's single point of contact, Shayar CV runs delivery day to day, and Thayif Kabir oversees the engagement and chairs five steering reviews between 29 October and 24 December.")

# ---------- risks ----------
rk = ''.join(f'<tr><td class="id">{e(r["id"])}</td><td><b>{e(r["risk"])}</b></td><td>{e(r["mitigation"])}</td><td>{e(r["owner"])}</td></tr>'
             for r in D['risks'])
page(f'''<table class="t"><thead><tr><th style="width:6%">ID</th><th style="width:36%">Risk</th><th style="width:44%">Mitigation</th><th style="width:14%">Owner</th></tr></thead><tbody>{rk}</tbody></table>''',
     'Risks', 'Top Risks and How They Are Managed',
     'Twelve risks are reviewed every Thursday. The ones that can most directly move the 1 December and 1 January dates are late delivery-platform APIs (R1, R2), rebuilding product and recipe data (R5), and validating six companies in one week (R4).')

# ---------- assemble ----------
total = len(pages) + 1
out = [cover]
for n, (label, title, intro, body) in enumerate(pages, start=2):
    out.append(
        f'<section class="page"><div class="ih"><img src="code-ox-logo.svg" alt="Code-ox"><div class="t">{HDR}</div><div class="r">{REF}</div></div>'
        f'<div class="ic"><div class="lab">{e(label)}</div><h2>{title}</h2>{f"<div class=intro>{e(intro)}</div>" if intro else ""}{body}</div>'
        f'<div class="if"><img src="code-ox-logo.svg" alt=""><div class="t">{FOOT}</div><div class="p">Page {n} of {total}</div></div></section>')
doc = ('<!DOCTYPE html>\n<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
       '<title>Tara Holding — Expected Project Plan</title>\n'
       '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">\n'
       f'<style>{css}</style></head><body>' + '\n'.join(out) + '</body></html>\n')
open(OUT, 'w', encoding='utf-8').write(doc)
print(f'pages={total} task_pages={len(chunks)}')
