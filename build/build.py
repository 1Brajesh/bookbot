"""Rebuild index.html from build/books.json + covers.json + build/template.html. Run from repo root: python3 build/build.py"""
import json
D=json.load(open("build/books.json"));C=json.load(open("covers.json"))
j=lambda o:json.dumps(o,ensure_ascii=False).replace("</","<\\/")
open("index.html","w").write(open("build/template.html").read().replace("__DATA__",j(D)).replace("__COVERS__",j({k:v for k,v in C.items() if v})))
