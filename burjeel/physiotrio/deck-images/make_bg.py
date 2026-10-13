"""Faint line-art slide backgrounds in PhysioTrio colours (transparent PNG, 1920x1080)."""
import math, sys
from PIL import Image, ImageDraw

OUT = sys.argv[1]
W, H, S = 1920, 1080, 2  # draw at 2x, downsample for anti-aliasing
PURPLE, GREEN = (136, 7, 114), (76, 175, 80)


def canvas():
    im = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    return im, ImageDraw.Draw(im)


def save(im, name):
    im.resize((W, H), Image.LANCZOS).save(f"{OUT}/{name}", optimize=True)


def bezier(p0, p1, p2, p3, n=240):
    pts = []
    for i in range(n + 1):
        t = i / n
        a, b, c, d = (1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t ** 2, t ** 3
        pts.append(((a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0]) * S,
                    (a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1]) * S))
    return pts


# 1. Curves: two loose parallel line pairs in opposite corners (like the hand-drawn curve sample)
im, d = canvas()
for off in (0, 70):
    d.line(bezier((1180 + off, -20), (1240 + off, 260), (1500, 300 + off), (1960, 280 + off)), fill=PURPLE + (34,), width=4 * S, joint="curve")
    d.line(bezier((-40, 640 + off), (260, 640 + off), (380 + off, 900), (400 + off, 1120)), fill=GREEN + (40,), width=4 * S, joint="curve")
save(im, "bg-curves.png")

# 2. Arcs: concentric rings from two off-canvas corners, fading toward the centre
im, d = canvas()
for (cx, cy), col in (((-120, -160), PURPLE), ((2040, 1240), GREEN)):
    for i, r in enumerate(range(140, 900, 22)):
        a = max(0, int(46 * (1 - i / 34)))
        d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S], outline=col + (a,), width=int(1.5 * S))
save(im, "bg-arcs.png")

# 3. Waves: a band of fine flowing lines along the bottom edge, fading upward
im, d = canvas()
for k in range(28):
    base = 1100 - k * 9
    a = max(0, int(52 * (1 - k / 28)))
    col = PURPLE if k % 2 else GREEN
    pts = [(x * S, (base - 70 * math.sin(x / 520 + k * 0.06) - 40 * math.sin(x / 230 + 1.3)) * S) for x in range(-20, W + 21, 8)]
    d.line(pts, fill=col + (a,), width=2 * S, joint="curve")
save(im, "bg-waves.png")
print("ok")
