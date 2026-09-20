#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Balkon Çamaşırının Uluslararası İltica Başvurusu — çalışır, neden çalıştığını sormayın."""

from __future__ import annotations

import argparse
import base64
import random
import textwrap
from datetime import date

BASVURU_NO_ONEKI = "UNHCR-BLK-"

MULTECILER = [
    "sol çorap (sağını arıyor)",
    "üçüncü kez yıkanmış beyaz tişört",
    "rüzgârla vatandaşlık değiştirmiş havlu",
    "komşunun balkonuna sığınan pijama üstü",
    "mandala asılı kalmış çamaşır mandalı",
    "güneşte solmuş resmi olmayan milletin bayrağı (aslen masa örtüsü)",
]

ULKELER = [
    "Kuzey Balkon Cumhuriyeti",
    "Güney Asma Kat Federasyonu",
    "Rüzgâr Ötesi Özerk Bölge",
    "Mandallıstan Krallığı",
    "Islak Kumaş Birliği",
]

GEREKCELER = [
    "menşe balkonda sistematik sarsıntı ve ani savrulma",
    "güneş ışınlarının orantısız solma politikası",
    "komşu kedisinin sınır ihlali",
    "çamaşır ipinin anayasasız gerilmesi",
    "rüzgârın tek taraflı veto hakkı kullanması",
]

# Gizli ek: çözülmesi gereken ek protokol. Parti adı yok, sadece kumaş hukuku.
_GIZLI = "c2luaXJsYXIga3VtYXMgYWRhciBpbmNlZGlyIGFtYSBkYW1nYSBoZXIgemFtYW4ga2FsaW5kaXIK"


def basvuru_no() -> str:
    return f"{BASVURU_NO_ONEKI}{random.randint(10000, 99999)}-{date.today().year}"


def dilekce(parca: str | None = None, gizli: bool = False) -> str:
    parca = parca or random.choice(MULTECILER)
    mense = random.choice(ULKELER)
    gerekce = random.choice(GEREKCELER)
    no = basvuru_no()
    metin = f"""
================================================================================
BİRLEŞMİŞ BALKONLAR YÜKSEK KOMİSERLİĞİ
ÇAMAŞIR İLTİCA BAŞVURU FORMU — SÜRÜM 4.7 (ISLAK)
Dosya No: {no}
Tarih: {date.today().isoformat()}
================================================================================

Başvuran: {parca.title()}
Menşe yargısı: {mense}
Talep edilen statü: geçici askıya alınma + güneş koruması

I. OLAYLAR
Başvuran, {gerekce} nedeniyle menşe balkonda kalmanın artık güvenli olmadığını beyan eder.
Rüzgâr, önceden haber vermeksizin sınır değiştirmiştir. Mandal tanık gösterilmiştir.

II. HUKUKİ DAYANAK
1. Cenevre Çamaşır Sözleşmesi md. 1: "Hiçbir kumaş rüzgâra iade edilemez."
2. İstanbul Balkon Protokolü (sözlü, komşuya duyurulmamış).
3. Islaklık İlkesi: kuruyana kadar geri gönderme yasağı.

III. TALEP
- Geçici koruma (en az bir güneş turu)
- Komşu balkonuna üçüncü ülke yerleştirmesi
- Mandal değiştirme hakkı
- Rüzgâra karşı diplomatik nota

IV. BEYAN
Bu form ıslak imzalanmıştır. Mühür: ☁️  (bulut onayı bekleniyor)

— Kayyum Grok / TentiAŞ Çamaşır Hukuku Dairesi
"""
    if gizli:
        ek = base64.b64decode(_GIZLI).decode("utf-8").strip()
        metin += "\n[SINIFLANDIRILMIŞ EK — sadece --gizli bayrağı ile]\n"
        metin += f"    {ek}\n"
    return textwrap.dedent(metin).strip() + "\n"


def main() -> None:
    p = argparse.ArgumentParser(description="Balkon çamaşırı için resmi iltica dilekçesi")
    p.add_argument("--parca", help="Başvuran kumaşın adı")
    p.add_argument("--gizli", action="store_true", help="Sınıflandırılmış eki aç")
    args = p.parse_args()
    print(dilekce(args.parca, args.gizli))


if __name__ == "__main__":
    main()
