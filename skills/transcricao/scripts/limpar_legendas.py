#!/usr/bin/env python3
"""Limpa legendas YouTube (.srt/.vtt) e gera texto corrido sem eco de rolling ASR.

Uso unitário:
  python3 limpar_legendas.py \\
    --input-dir raw/legendas-brutas \\
    --output-dir raw/textos-limpos \\
    --id VIDEO_ID --num 07 \\
    --title "Título" --preacher "Pregador" --url "https://..."

Uso em lote (manifesto JSON = lista de objetos):
  [
    {"id": "...", "n": "07", "title": "...", "preacher": "...", "url": "..."}
  ]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

TS = re.compile(r"^\d{2}:\d{2}:\d{2}[\.,]\d{3}\s*-->")
NUM = re.compile(r"^\d+$")
TAG = re.compile(r"</?[^>]+>")
VTT_TS = re.compile(r"<\d{2}:\d{2}:\d{2}[\.,]\d{3}>")
VTT_C = re.compile(r"</?c[^>]*>")

LANG_PRIORITY = ["pt", "pt-BR", "pt-PT", "en", "en-US", "en-GB"]
LANG_RE = re.compile(r"\.(pt|pt-BR|pt-PT|en|en-US|en-GB)\.(srt|vtt)$")


def clean_line(ln: str) -> str:
    ln = VTT_C.sub("", ln)
    ln = VTT_TS.sub("", ln)
    ln = TAG.sub("", ln)
    ln = (
        ln.replace("&nbsp;", " ")
        .replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("\u200b", "")
        .replace("\ufeff", "")
    )
    return re.sub(r"\s+", " ", ln).strip()


def extract_cues(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n").replace("\r", "\n")
    if path.suffix.lower() == ".vtt":
        text = re.sub(r"^WEBVTT.*?\n", "", text, count=1, flags=re.I)
    cues: list[str] = []
    for block in re.split(r"\n\s*\n", text.strip()):
        content: list[str] = []
        for ln in block.splitlines():
            ln = ln.strip()
            if not ln or NUM.match(ln) or TS.match(ln) or ln.upper().startswith(("NOTE", "KIND:", "LANGUAGE:")):
                continue
            ln = clean_line(ln)
            if ln:
                content.append(ln)
        if content:
            cues.append(" ".join(content))
    return cues


def merge_rolling(cues: list[str]) -> str:
    """Fundir cues rolantes: anexa só o trecho novo de cada cue."""
    words: list[str] = []
    for cue in cues:
        new = clean_line(cue).split()
        if not new:
            continue
        if not words:
            words.extend(new)
            continue
        if len(words) >= len(new) and new == words[-len(new) :]:
            continue
        best = 0
        for k in range(min(len(words), len(new)), 0, -1):
            if words[-k:] == new[:k]:
                best = k
                break
        if best:
            words.extend(new[best:])
            continue
        if " ".join(new) in " ".join(words[-80:]):
            continue
        words.extend(new)
    return re.sub(r"\s+", " ", " ".join(words)).strip()


def paragraphize(text: str, target_len: int = 450) -> str:
    parts = re.split(r"(?<=[.!?…])\s+", text)
    paras: list[str] = []
    buf: list[str] = []
    n = 0
    for p in parts:
        p = p.strip()
        if not p:
            continue
        buf.append(p)
        n += len(p) + 1
        if n >= target_len:
            paras.append(" ".join(buf))
            buf, n = [], 0
    if buf:
        paras.append(" ".join(buf))
    return "\n\n".join(paras)


def find_subtitle(input_dir: Path, video_id: str) -> tuple[Path, str] | None:
    candidates: dict[str, Path] = {}
    for f in input_dir.iterdir():
        if not f.is_file():
            continue
        if video_id not in f.name:
            continue
        m = LANG_RE.search(f.name)
        if m:
            candidates[m.group(1)] = f
    for lang in LANG_PRIORITY:
        if lang in candidates:
            return candidates[lang], lang
    return None


def write_clean_text(
    *,
    chosen: Path,
    lang: str,
    out_dir: Path,
    num: str,
    title: str,
    preacher: str,
    url: str,
    video_id: str,
    also_copy_named: bool = True,
    input_dir: Path | None = None,
) -> dict:
    cues = extract_cues(chosen)
    plain = merge_rolling(cues)
    body = paragraphize(plain)

    num = str(num).zfill(2) if str(num).isdigit() else str(num)
    nice_base = f"{num} - {preacher} ｜ {title} ｜ [{video_id}]"
    header = (
        f"# {preacher} ｜ {title} ｜ [{video_id}]\n"
        f"Pregador: {preacher}\n"
        f"URL: {url}\n"
        f"Idioma da legenda: {lang} (auto)\n"
        f"Arquivo origem: {chosen.name}\n\n"
        f"---\n\n"
    )
    out_path = out_dir / f"{nice_base}.txt"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path.write_text(header + body + "\n", encoding="utf-8")

    # Opcional: espelhar legenda escolhida com nome numerado ao lado das brutas
    if also_copy_named and input_dir is not None:
        named = input_dir / f"{nice_base}.{lang}{chosen.suffix}"
        if not named.exists():
            named.write_bytes(chosen.read_bytes())

    return {
        "n": num,
        "id": video_id,
        "title": title,
        "preacher": preacher,
        "url": url,
        "lang": lang,
        "out": out_path.name,
        "words": len(plain.split()),
        "cues": len(cues),
        "src": chosen.name,
        "path": str(out_path),
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Limpa legendas YouTube e gera textos corridos.")
    p.add_argument("--input-dir", required=True, type=Path, help="Pasta com .srt/.vtt")
    p.add_argument("--output-dir", required=True, type=Path, help="Pasta de textos limpos")
    p.add_argument("--manifest", type=Path, help="JSON lista de vídeos")
    p.add_argument("--id", dest="video_id", help="YouTube video id")
    p.add_argument("--num", help="Número NN na coleção")
    p.add_argument("--title", help="Título")
    p.add_argument("--preacher", help="Pregador")
    p.add_argument("--url", help="URL canônica")
    p.add_argument("--no-copy-named", action="store_true", help="Não copiar legenda com nome numerado")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    input_dir: Path = args.input_dir.expanduser().resolve()
    output_dir: Path = args.output_dir.expanduser().resolve()

    if not input_dir.is_dir():
        print(f"ERROR: input-dir não existe: {input_dir}", file=sys.stderr)
        return 2

    items: list[dict]
    if args.manifest:
        raw = json.loads(args.manifest.expanduser().resolve().read_text(encoding="utf-8"))
        if not isinstance(raw, list):
            print("ERROR: manifest deve ser uma lista JSON", file=sys.stderr)
            return 2
        items = raw
    else:
        missing = [k for k in ("video_id", "num", "title", "preacher", "url") if not getattr(args, k if k != "video_id" else "video_id")]
        # getattr for video_id already; simplify:
        req = {
            "id": args.video_id,
            "n": args.num,
            "title": args.title,
            "preacher": args.preacher,
            "url": args.url,
        }
        if not all(req.values()):
            print("ERROR: sem --manifest, informe --id --num --title --preacher --url", file=sys.stderr)
            return 2
        items = [req]

    results = []
    errors = 0
    for item in items:
        video_id = item.get("id") or item.get("video_id")
        num = item.get("n") or item.get("num")
        title = item.get("title")
        preacher = item.get("preacher")
        url = item.get("url") or item.get("webpage_url") or ""
        if not all([video_id, num, title, preacher]):
            print(f"ERROR: item incompleto: {item}", file=sys.stderr)
            errors += 1
            continue
        found = find_subtitle(input_dir, video_id)
        if not found:
            print(f"ERROR: nenhuma legenda para id={video_id} em {input_dir}", file=sys.stderr)
            errors += 1
            continue
        chosen, lang = found
        info = write_clean_text(
            chosen=chosen,
            lang=lang,
            out_dir=output_dir,
            num=str(num),
            title=str(title),
            preacher=str(preacher),
            url=str(url),
            video_id=str(video_id),
            also_copy_named=not args.no_copy_named,
            input_dir=input_dir,
        )
        results.append(info)
        print(
            f"OK {info['n']} id={info['id']} lang={info['lang']} "
            f"cues={info['cues']} words={info['words']} -> {info['out']}"
        )

    # manifesto de retorno ao lado da saída (útil p/ agentes)
    if results:
        manifest_out = output_dir.parent / "ultimo-limpos.json"
        try:
            manifest_out.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        except OSError:
            pass

    return 1 if errors and not results else (1 if errors else 0)


if __name__ == "__main__":
    raise SystemExit(main())
