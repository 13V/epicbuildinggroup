"""Builds tools/photos.json from the photo labels and exports the photographs as WebP.

Labels (kind, build stage, alt text, order) were made by looking at every photograph on
epicbuildinggroup.com.au; they live in tools/labels/*.json. Originals are not kept in this repo:
pass the folder that mirrors their site (the one that contains images/).
"""
import glob, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from projects import P, EXTRA, CHECKED  # noqa: E402
import re

MAX_GALLERY = 18
MAX_STAGE = 3  # photographs per build stage
MAX_SITE = 6  # site photographs where the stages have not been checked by hand


def tidy(alt):
    """Alt text describes what is seen; it should not guess at materials or quote stamps on the photo."""
    alt = re.sub(r"(sand)?stone-look", "stone", alt)
    alt = re.sub(r",? ?marked as (the )?before( photo)?", "", alt)
    return alt


def merge():
    labels = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "tools", "labels", "*.json"))):
        labels.update(json.load(open(f)))
    out = {}
    for p in P:
        L = labels[p["k"]]
        meta = {m["file"]: m for m in L["images"]}
        people = {f for f, m in meta.items() if m.get("people")}
        ok = lambda f: f in meta and f not in people and meta[f]["kind"] != "render"  # no identifiable people, no renders
        order = [f for f in L.get("order", []) if ok(f)][:MAX_GALLERY]
        stages, per = [], {}
        for f in L.get("stages", []):
            if not ok(f):
                continue
            s = meta[f].get("stage") or "site"
            if per.get(s, 0) < MAX_STAGE:
                per[s] = per.get(s, 0) + 1
                stages.append(f)
        pair = L.get("pair") if L.get("pair") and ok(L["pair"]["earlier"]) and ok(L["pair"]["finished"]) else None
        hero = L["hero"] if ok(L.get("hero", "")) else (order or stages)[0]
        C = CHECKED.get(p["slug"])
        if C:
            f_ = lambda n: f"{C['dir']}{n}.jpg"
            stages = [f_(n) for _, ns in C["stages"] for n in ns]
            for st, ns in C["stages"]:
                for n in ns:
                    meta[f_(n)]["stage"] = st
            if "order" in C:
                order = [f_(n) for n in C["order"]]
            if "hero" in C:
                hero = f_(C["hero"])
            if "pair" in C:
                pair = dict(earlier=f_(C["pair"][0]), finished=f_(C["pair"][1]), earlier_label=C["pair"][2])
        else:
            stages = [f for f in L.get("stages", []) if ok(f)][:MAX_SITE]
        files = []
        for f in [hero] + order + stages + ([pair["earlier"], pair["finished"]] if pair else []) + EXTRA.get(p["slug"], []):
            if f not in files:
                files.append(f)
        out[p["slug"]] = dict(src=p["k"], checked=bool(C), hero=hero, order=order, stages=stages, pair=pair, notes=L.get("notes", ""), files=files,
                              meta=[dict(alt=tidy(meta[f]["alt"]), kind=meta[f]["kind"], stage=meta[f].get("stage", ""), room=meta[f].get("room", "")) for f in files])
    return out


def export(mirror):
    from PIL import Image

    out = merge()
    for slug, ph in out.items():
        d = os.path.join(ROOT, "assets", "img", "projects", slug)
        os.makedirs(d, exist_ok=True)
        for old in os.listdir(d):
            os.remove(os.path.join(d, old))
        for i, f in enumerate(ph["files"]):
            im = Image.open(mirror + f).convert("RGB")
            if im.width > 1480:
                im = im.resize((1480, round(im.height * 1480 / im.width)), Image.LANCZOS)
            ph["meta"][i]["w"], ph["meta"][i]["h"] = im.size
            im.save(os.path.join(d, f"{i + 1:02d}.webp"), quality=76, method=6)
            s = im.resize((370, round(im.height * 370 / im.width)), Image.LANCZOS)
            s.save(os.path.join(d, f"{i + 1:02d}-s.webp"), quality=72, method=6)
    json.dump(out, open(os.path.join(ROOT, "tools", "photos.json"), "w"), indent=1)
    print("exported", sum(len(p["files"]) for p in out.values()), "photographs")
