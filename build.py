#!/usr/bin/env python3
# Generator voor brouwersmode.nl - onafhankelijke gids over herenkleding, pasvorm en stoffen.
import os, json, html, hashlib
def _ver(p):
    try: return hashlib.md5(open(os.path.join(os.path.dirname(__file__),p),'rb').read()).hexdigest()[:8]
    except Exception: return "1"
BASE="https://brouwersmode.nl"; SITE="Brouwers Mode"; EMAIL="info@brouwersmode.nl"
AUTEUR="Thomas Brouwers"; AUTEUR_ROL="Moderedacteur"
SRC=os.path.dirname(__file__); OUT=os.path.join(SRC,"site"); CSS_VER=_ver("assets/css/style.css")
def esc(s): return html.escape(str(s), quote=True)
DISC="Maten en pasvormen verschillen per merk en per land. De aanwijzingen hier zijn richtlijnen; passen blijft de enige manier om zeker te weten of iets goed zit."

IC={
 "check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
 "arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "doc":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"/><path d="M6 6v13a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V6"/><path d="M9 6V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2"/></svg>',
 "scale":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3l3 2 3-2 4 2c1 .5 1.5 1.4 1.5 2.4V20a1 1 0 0 1-1 1H4.5a1 1 0 0 1-1-1V7.4C3.5 6.4 4 5.5 5 5z"/><path d="M9 3l3 4 3-4"/></svg>',
 "clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/></svg>',
 "book":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h7a3 3 0 0 1 3 3v13a2.5 2.5 0 0 0-2.5-2.5H4z"/><path d="M20 4h-3a3 3 0 0 0-3 3v13a2.5 2.5 0 0 1 2.5-2.5H20z"/></svg>',
 "menu":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>',
}
NAV=[("Home","/"),("Onderwerpen","/onderwerpen/"),("Gidsen","/gidsen/"),("Nieuws","/nieuws/"),("Over","/over/"),("Contact","/contact/")]

def head(t,d,path,ld=None):
    can=BASE+path
    j="".join('<script type="application/ld+json">'+json.dumps(b,ensure_ascii=False)+'</script>' for b in (ld or []))
    nav="".join(f'<a class="navlink" href="{h}">{esc(l)}</a>' for l,h in NAV)
    return f"""<!DOCTYPE html>
<html lang="nl"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t)}</title><meta name="description" content="{esc(d)}">
<link rel="canonical" href="{can}">
<meta property="og:type" content="website"><meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{esc(SITE)}"><meta property="og:title" content="{esc(t)}">
<meta property="og:description" content="{esc(d)}"><meta property="og:url" content="{can}">
<meta name="theme-color" content="#2A2724">
<link rel="icon" href="/assets/icons/logo-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v={CSS_VER}">
{j}</head><body>
<header class="site-head"><nav class="nav" id="nav">
  <a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>Brouwers Mode</b><span>Modegids</span></span></a>
  {nav}
  <button class="menu-toggle" aria-label="Menu" onclick="document.getElementById('nav').classList.toggle('open')">{IC['menu']}</button>
</nav></header>
"""

def footer():
    return f"""<footer class="foot"><div class="wrap"><div class="cols">
  <div><a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>Brouwers Mode</b><span style="color:#94897B">Modegids</span></span></a>
    <p class="note">Brouwers Mode is een onafhankelijke gids over herenkleding: pasvorm, stoffen, onderhoud en de opbouw van een garderobe. Het platform verkoopt geen kleding en is geen winkel.</p></div>
  <div><h4>Kennis</h4><a href="/onderwerpen/">Onderwerpen</a><a href="/gidsen/">Gidsen</a><a href="/nieuws/">Nieuws</a><a href="/redactie/">Over de redactie</a></div>
  <div><h4>Informatie</h4><a href="/over/">Over dit platform</a><a href="/contact/">Contact</a><a href="/privacybeleid/">Privacybeleid</a><a href="/cookiebeleid/">Cookiebeleid</a></div>
</div><div class="foot-bottom"><span>&copy; 2026 {esc(SITE)}</span>
<span><a href="/contact/">Contact</a> &middot; <a href="/privacybeleid/">Privacy</a> &middot; <a href="/cookiebeleid/">Cookies</a></span></div></div></footer>
</body></html>"""

def crumb(i): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":k+1,"name":n,"item":BASE+u} for k,(n,u) in enumerate(i)]}
def crumbs_html(i):
    o=[f'<a href="{u}">{esc(n)}</a>' for n,u in i[:-1]]; o.append(f'<span>{esc(i[-1][0])}</span>')
    return '<div class="wrap"><nav class="crumbs">'+' / '.join(o)+'</nav></div>'
def write(path,c):
    f=os.path.join(OUT,"index.html") if path=="/" else os.path.join(OUT,path.strip("/"),"index.html")
    os.makedirs(os.path.dirname(f),exist_ok=True); open(f,"w",encoding="utf-8").write(c)
def blocks(bs):
    o=[]
    for b in bs:
        if b[0]=="p": o.append(f"<p>{esc(b[1])}</p>")
        elif b[0]=="h2": o.append(f"<h2>{esc(b[1])}</h2>")
        elif b[0]=="ul": o.append("<ul>"+"".join(f"<li>{esc(x)}</li>" for x in b[1])+"</ul>")
        elif b[0]=="callout": o.append(f'<div class="callout"><p>{esc(b[1])}</p></div>')
    return "".join(o)
def byline(): return f'<div class="byline"><img src="/assets/img/auteur.svg" alt="{esc(AUTEUR)}"><div class="who">{esc(AUTEUR)}<small>{esc(AUTEUR_ROL)}</small></div></div>'

ONDERWERPEN=[
 {"slug":"pak-en-pasvorm","naam":"Pak en pasvorm",
  "resume":"De schoudernaad bepaalt of een colbert past. Vrijwel al het andere is bij te laten maken.",
  "specs":[("Maatgevend","Schouder"),("Aanpasbaar","Mouw, taille, lengte"),("Sluiting","Onderste knoop open")],
  "secties":[("De schouder is het ijkpunt","Een colbert past wanneer de schouderlijn eindigt waar de schouder eindigt, zonder overhang en zonder dat de naad op de arm valt. Een schouder aanpassen betekent het jasje vrijwel volledig uit elkaar halen, wat zelden loont. Mouwen inkorten, de taille innemen en de lengte aanpassen zijn daarentegen gangbare ingrepen bij elke kleermaker."),
   ("Colbertlengte en revers","De klassieke maat voor de lengte is dat de zoom de knokkels raakt bij afhangende armen, met een marge van enkele centimeters afhankelijk van de gewenste stijl. De breedte van de revers volgt de breedte van de borst; smalle revers op een breed postuur oogt uit verhouding."),
   ("Broeklengte","De hoeveelheid stof die op de schoen rust bepaalt de uitstraling. Geen enkele break geeft een strakke lijn, een enkele vouw is de meest veilige keuze, en meer dan dat oogt al snel te ruim. De pijpbreedte bij de zoom bepaalt hoeveel break er ontstaat.")],
  "punten":["Schouder bepaalt of het jasje past","Mouw, taille en lengte zijn aanpasbaar","Onderste knoop blijft open","Broeklengte in overleg met de schoenkeuze"]},
 {"slug":"overhemden-en-boorden","naam":"Overhemden en boorden",
  "resume":"De boord bepaalt de uitstraling van een overhemd meer dan de stof, en moet passen bij het gezicht en de das.",
  "specs":[("Boord","Cutaway, kent, button-down"),("Maat","Halswijdte"),("Vuistregel","Een vinger ruimte")],
  "secties":[("Boordtypen en wanneer","Een cutaway boord heeft ver uiteenstaande punten en geeft ruimte aan een grotere dasknoop, wat goed werkt bij een smaller gezicht. Een kent of semi-spread is de meest veelzijdige keuze. Een button-down hoort bij een informelere setting en past minder goed bij een pak met een strakke snit."),
   ("De maat"," De halswijdte hoort zo te zijn dat er een vinger tussen boord en hals past. Te ruim zakt de boord weg onder de das, te strak vervormt de kraag zodra het hoofd draait. De mouwlengte eindigt op het polsbeen, zodat er bij een colbert ongeveer een centimeter zichtbaar blijft."),
   ("Weefsels","Popeline is glad en formeel, oxford grover en informeler, twill valt zwaarder en kreukt minder. Een fijne popeline onder een pak oogt netter dan een oxford, maar is ook doorschijnender en vraagt om een onderhemd bij lichte kleuren.")],
  "punten":["Boordtype bepaalt de uitstraling","Een vinger ruimte bij de hals","Mouw eindigt op het polsbeen","Popeline formeel, oxford informeel"]},
 {"slug":"stoffen","naam":"Stoffen en weefsels",
  "resume":"Wol, katoen en linnen gedragen zich totaal verschillend, en het gewicht per meter zegt meer dan het label.",
  "specs":[("Wol","Veerkrachtig"),("Linnen","Kreukt"),("Gewicht","Gram per meter")],
  "secties":[("Wol is niet één materiaal","Wol met een hoog Super-getal is fijner van draad en voelt zachter, maar is ook kwetsbaarder en kreukt sneller. Voor een pak dat dagelijks wordt gedragen, is een lager getal met een steviger draad vaak praktischer dan het duurste weefsel. Het gewicht, uitgedrukt in gram per meter, bepaalt hoe een pak valt en voor welk seizoen het geschikt is."),
   ("Linnen en katoen","Linnen ademt uitstekend en koelt, maar kreukt onvermijdelijk; dat hoort bij het materiaal en is geen gebrek. Katoen zit tussen beide in en is makkelijker in onderhoud. Mengsels met een klein aandeel elastaan geven bewegingsvrijheid, maar bemoeilijken vermaken en verkorten de levensduur."),
   ("Seizoen en gewicht","Een pak van rond de 250 gram is geschikt voor het grootste deel van het jaar in Nederland. Onder de 200 gram wordt het een zomerpak, boven de 320 gram een winterpak dat binnen te warm aanvoelt.")],
  "punten":["Hoger Super-getal is fijner maar kwetsbaarder","Gewicht bepaalt het seizoen","Linnen kreukt, dat hoort erbij","Elastaan bemoeilijkt vermaken"]},
 {"slug":"schoenen","naam":"Schoenen",
  "resume":"De constructie van de zool bepaalt of een schoen tien jaar meegaat of twee, ongeacht de prijs.",
  "specs":[("Constructie","Goodyear of gelijmd"),("Onderhoud","Spanners en poetsen"),("Rusten","Dag ertussen")],
  "secties":[("Goodyear en gelijmd","Bij een Goodyear-geranде constructie is de zool via een rand aan het bovenwerk genaaid en kan die meerdere keren worden vervangen. Een gelijmde zool is goedkoper en lichter, maar bij slijtage is vervangen zelden rendabel. Dat verschil bepaalt de werkelijke kosten per jaar meer dan de aanschafprijs."),
   ("Leest boven maat","Elke fabrikant werkt met een eigen leest, de vorm waaromheen de schoen wordt gebouwd. Dezelfde maat valt daardoor per merk anders. De breedte en de hoogte van de wreef zijn belangrijker voor het comfort dan de lengte alleen."),
   ("Onderhoud","Schoenspanners van cederhout nemen vocht op en houden de vorm, wat scheuren in het leer voorkomt. Een dag rust tussen twee draagbeurten laat het leer drogen. Poetsen voedt het leer en houdt het soepel; dat is onderhoud, geen cosmetica.")],
  "punten":["Genaaide zool is meerdere keren te vervangen","Leest verschilt per merk","Spanners na elke draagbeurt","Een dag rust tussen twee beurten"]},
 {"slug":"breigoed","naam":"Breigoed",
  "resume":"Merinowol, lamswol en kasjmier verschillen in warmte, prijs en gevoeligheid voor pilling.",
  "specs":[("Merino","Fijn, veelzijdig"),("Kasjmier","Warm, kwetsbaar"),("Onderhoud","Liggend drogen")],
  "secties":[("De soorten"," Merinowol is fijn van vezel, kriebelt nauwelijks en is het hele jaar bruikbaar. Lamswol is iets grover en steviger. Kasjmier is warmer bij hetzelfde gewicht en voelt zachter, maar de korte vezels maken het gevoeliger voor pilling en slijtage. Een mengsel combineert vaak het beste van twee."),
   ("Pilling hoort erbij","De kleine bolletjes die ontstaan op plekken met wrijving zijn geen teken van slechte kwaliteit, maar van losse vezeluiteinden. Met een truienkam of een scheerapparaatje voor textiel verdwijnen ze; na enkele keren neemt het af."),
   ("Wassen en drogen","Breigoed rekt uit onder eigen gewicht wanneer het nat hangt. Liggend drogen op een handdoek behoudt de vorm. Wassen op wolprogramma met een wolwasmiddel, of luchten in plaats van wassen, verlengt de levensduur aanzienlijk.")],
  "punten":["Merino is het meest veelzijdig","Kasjmier is warmer maar kwetsbaarder","Pilling is normaal en te verhelpen","Altijd liggend laten drogen"]},
 {"slug":"jassen","naam":"Jassen en outerwear",
  "resume":"Een jas gaat over een colbert heen, en dat stelt eisen aan de lengte en de ruimte in de schouder.",
  "specs":[("Lengte","Tot de knie"),("Ruimte","Over een colbert"),("Model","Chesterfield, trenchcoat")],
  "secties":[("Ruimte inplannen","Een jas die alleen over een trui past, valt af zodra er een colbert onder gaat. Passen met de dikste laag die eronder gedragen gaat worden, voorkomt dat de jas alleen bruikbaar is voor de helft van de situaties waarvoor die is gekocht."),
   ("Lengte en verhouding","Een klassieke overjas eindigt op of net onder de knie en bedekt daarmee een colbert volledig. Kortere modellen ogen moderner maar laten een colbert uitsteken, wat rommelig oogt. Bij informele jassen speelt dat minder."),
   ("Materiaal","Wol houdt warmte vast maar is niet waterdicht; een gabardine katoen of een technisch weefsel is geschikter bij regen. Een voering van zijde of viscose maakt aantrekken over een colbert aanzienlijk soepeler dan een ruwe voering.")],
  "punten":["Passen met de dikste onderlaag","Overjas bedekt het colbert volledig","Wol is warm maar niet waterdicht","Gladde voering maakt aantrekken makkelijk"]},
]
def onderwerp(s): return next(x for x in ONDERWERPEN if x["slug"]==s)

GIDSEN=[
 {"slug":"garderobe-opbouwen","titel":"Een garderobe opbouwen die blijft werken","ic":"scale",
  "resume":"Een beperkt aantal stukken dat onderling combineert, levert meer combinaties op dan een volle kast.",
  "body":[("p","De kast van veel mensen bevat kleding die zelden wordt gedragen, niet omdat het lelijk is, maar omdat het nergens bij past. Combineerbaarheid is daarmee belangrijker dan aantal."),
   ("h2","Beginnen bij de onderkant"),("p","Een neutrale broek in marine of grijs combineert met vrijwel elk bovenstuk. Uitgesproken kleuren en patronen beperken het aantal combinaties, en horen daarom pas aan de beurt te komen wanneer de basis staat."),
   ("h2","Wat de basis vormt"),("ul",["Twee neutrale broeken die met alles combineren.","Drie tot vier overhemden in effen wit, lichtblauw en een gedempte tint.","Een colbert in een neutrale kleur en een middelzwaar gewicht.","Twee paar schoenen in verschillende formaliteit.","Een trui in merino die zowel onder een colbert als los werkt."]),
   ("h2","Kwaliteit waar het telt"),("p","Schoenen en outerwear worden het langst gebruikt en zijn het duurst om te vervangen. Daar loont investeren. Een basis-T-shirt of een overhemd dat elk jaar wordt vervangen, hoeft dat niveau niet te halen."),
   ("callout","De vraag bij elk nieuw stuk: met hoeveel dingen die al in de kast hangen, valt dit te combineren. Onder de drie is het meestal een aankoop die blijft hangen."),
   ("h2","Vermaken telt mee in de prijs"),("p","Confectiekleding is gemaakt voor een gemiddelde die niemand precies is. Vijftig euro aan vermaakwerk op een betaalbaar colbert levert doorgaans meer op dan hetzelfde bedrag extra aan aanschafprijs."),
   ("p",DISC)]},
 {"slug":"kleding-onderhouden","titel":"Kleding onderhouden: minder wassen, langer mooi","ic":"doc",
  "resume":"De wasmachine is de grootste oorzaak van slijtage. Luchten, borstelen en gericht behandelen doen vaak meer.",
  "body":[("p","Textiel slijt vooral tijdens het wassen, door mechanische beweging en warmte. Minder vaak wassen, met gerichte behandeling van vlekken, verlengt de levensduur van vrijwel elk kledingstuk."),
   ("h2","Wat niet elke keer in de was hoeft"),("p","Een colbert, een wollen trui of een broek die één dag is gedragen zonder te transpireren, heeft geen wasbeurt nodig. Een nacht luchten op een goede hanger herstelt de vorm en verwijdert geuren. Een kledingborstel haalt stof en oppervlakkig vuil eruit."),
   ("h2","Hangers en vouwen"),("ul",["Brede hangers voor colberts en jassen, zodat de schouder niet vervormt.","Breigoed opvouwen in plaats van hangen.","Broeken hangen aan de zoom of over een brede stang.","Kleding niet opgepropt bewaren, stof heeft ruimte nodig."]),
   ("h2","Wassen wanneer het moet"),("p","Op lage temperatuur, met een beperkt toerental en een vulling die niet te vol is. Binnenstebuiten wassen beperkt pilling en beschermt de buitenkant. Drogen in een droger verkort de levensduur van vrijwel alle natuurlijke vezels aanzienlijk."),
   ("h2","Stomen met mate"),("p","Chemisch reinigen is agressiever dan luchten en hoeft alleen bij zichtbare vervuiling of na een heel seizoen. Voor een pak is twee tot drie keer per jaar in de meeste gevallen voldoende."),
   ("p",DISC)]},
]

ARTIKELEN=[
 {"slug":"waarom-maten-verschillen","titel":"Waarom dezelfde maat per merk anders valt","cat":"Achtergrond","datum":"2026-07-19","datum_nl":"19 juli 2026","lees":4,
  "resume":"Er bestaat geen bindende norm voor confectiematen, en dat verklaart de verwarring bij online bestellen.",
  "body":[("p","Een maat 50 bij het ene merk past, bij het andere niet. Dat komt niet door onzorgvuldigheid maar door het ontbreken van een verplichte standaard."),
   ("h2","Elk merk zijn eigen blok"),("p","Fabrikanten werken met een eigen basispatroon, gebaseerd op een doelgroep en een gewenste snit. Een merk dat zich richt op een slanker postuur gebruikt andere verhoudingen dan een merk voor een breder publiek, ook bij dezelfde nominale maat."),
   ("h2","Vanity sizing"),("p","In de loop der jaren zijn maataanduidingen bij veel merken opgeschoven, waarbij hetzelfde nummer een ruimer kledingstuk aanduidt dan decennia geleden. Dat maakt vergelijken met oudere kleding onbetrouwbaar."),
   ("h2","Wat wel werkt"),("ul",["Meten in centimeters en die vergelijken met de maattabel van het merk.","Een goed passend kledingstuk opmeten en die maten aanhouden.","Bij twijfel het ruimere kiezen, omdat innemen makkelijker is dan uitleggen."]),
   ("p",DISC)]},
 {"slug":"kosten-per-draagbeurt","titel":"Kosten per draagbeurt: een nuttiger maatstaf dan de prijs","cat":"Praktijk","datum":"2026-07-06","datum_nl":"6 juli 2026","lees":3,
  "resume":"Een duur kledingstuk dat honderden keren wordt gedragen, is goedkoper dan een goedkoop stuk dat blijft hangen.",
  "body":[("p","De aanschafprijs zegt weinig over wat kleding uiteindelijk kost. De prijs gedeeld door het aantal draagbeurten geeft een bruikbaarder beeld."),
   ("h2","De rekensom"),("p","Een colbert van vierhonderd euro dat vijf jaar lang wekelijks wordt gedragen, komt uit op ongeveer anderhalve euro per keer. Een jasje van tachtig euro dat tien keer wordt gedragen en daarna niet meer past of uit vorm is, kost acht euro per keer."),
   ("h2","Waar het misgaat"),("p","De rekensom werkt alleen wanneer een duurder stuk daadwerkelijk vaker wordt gedragen. Een uitgesproken kleur of een sterk modegevoelige snit haalt dat aantal zelden, hoe goed het ook gemaakt is. Neutrale stukken in een klassieke snit halen die aantallen wel."),
   ("h2","Waar investeren loont"),("p","Schoenen, jassen en een neutraal colbert worden het vaakst gedragen en zijn het duurst om te vervangen. Daar is de kans op een lage prijs per draagbeurt het grootst."),
   ("p",DISC)]},
]

def tile(s):
    return f"""<a class="tile" href="/onderwerpen/{s['slug']}/"><h3>{esc(s['naam'])}</h3><p>{esc(s['resume'][:96].rsplit(' ',1)[0])}...</p></a>"""
def newscard(a):
    return f"""<article class="news"><span class="cat">{esc(a['cat'])}</span>
  <h3><a href="/nieuws/{a['slug']}/" style="color:inherit;text-decoration:none">{esc(a['titel'])}</a></h3>
  <p>{esc(a['resume'])}</p><div class="meta">{esc(a['datum_nl'])} &middot; {a['lees']} min lezen</div></article>"""

def p_home():
    ld=[{"@context":"https://schema.org","@type":"WebSite","@id":BASE+"/#w","url":BASE+"/","name":SITE,"inLanguage":"nl-NL",
         "description":"Onafhankelijke gids over herenkleding: pasvorm, stoffen, onderhoud en het opbouwen van een garderobe."},
        {"@context":"https://schema.org","@type":"Organization","@id":BASE+"/#o","name":SITE,"url":BASE+"/","email":EMAIL},crumb([("Home","/")])]
    gids="".join(f'<div class="card"><div class="ic">{IC[g["ic"]]}</div><h3><a href="/gidsen/{g["slug"]}/" style="color:inherit;text-decoration:none">{esc(g["titel"])}</a></h3><p>{esc(g["resume"])}</p></div>' for g in GIDSEN)
    h=head("Brouwers Mode | gids over herenkleding en pasvorm",
      "Onafhankelijke gids over herenkleding: pasvorm, stoffen, schoenen, breigoed en onderhoud, zonder merkvoorkeur en zonder verkoop.","/",ld)
    h+=f"""<section class="hero"><div class="wrap hero-inner">
  <div><span class="eyebrow">{IC['scale']}Kennisgids</span>
  <h1>Kleding die <em>past</em></h1>
  <p class="lead">Pasvorm, stoffen, schoenen en onderhoud: waaraan te zien is of iets goed zit, wat een materiaal doet en waar investeren loont. Onafhankelijk en zonder merkvoorkeur.</p>
  <div class="hero-actions"><a class="btn btn-plum" href="/onderwerpen/">Bekijk de onderwerpen {IC['arrow']}</a><a class="btn btn-ghost" href="/gidsen/">Naar de gidsen</a></div>
  <div class="hero-meta"><span>{IC['check']}6 onderwerpen</span><span>{IC['check']}Geen merkvoorkeur</span><span>{IC['check']}Geen winkel</span></div></div>
  <div class="hero-art"><img src="/assets/img/hero.svg" alt="Illustratie van kledingstukken aan een rek" width="480" height="340"></div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['doc']}Onderwerpen</span><h2>De onderwerpen die het meeste uitmaken</h2>
  <p class="lead">Per onderwerp waar het op aankomt, wat aanpasbaar is en waar het in de praktijk misgaat.</p></div>
  <div class="grid cols-3">{"".join(tile(s) for s in ONDERWERPEN)}</div></div></section>

<section class="section panel"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['book']}Gidsen</span><h2>Twee praktische gidsen</h2></div>
  <div class="grid cols-2">{gids}</div></div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['clock']}Nieuws</span><h2>Laatste artikelen</h2></div>
  <div class="grid cols-2">{"".join(newscard(a) for a in ARTIKELEN)}</div>
  <p style="margin-top:22px"><a class="more" href="/nieuws/">Alle artikelen {IC['arrow']}</a></p></div></section>

<section class="section tight"><div class="wrap"><div class="cta">
  <h2>Een onderwerp gemist?</h2><p>Deze gids groeit op basis van vragen die binnenkomen. Suggesties en correcties zijn welkom bij de redactie.</p>
  <a class="btn btn-gold" href="/contact/">Mail de redactie {IC['arrow']}</a></div></div></section>"""
    write("/",h+footer())

def p_ond_index():
    path="/onderwerpen/"; c=[("Home","/"),("Onderwerpen",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Onderwerpen","inLanguage":"nl-NL"},
        {"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":s["naam"],"url":BASE+f"/onderwerpen/{s['slug']}/"} for i,s in enumerate(ONDERWERPEN)]},crumb(c)]
    h=head("Onderwerpen herenkleding | "+SITE,"Overzicht van onderwerpen rond herenkleding: pak en pasvorm, overhemden, stoffen, schoenen, breigoed en jassen.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['doc']}Overzicht</span>
  <h1>Onderwerpen</h1><p class="lead">Zes onderwerpen die samen bepalen of een garderobe werkt, van pasvorm tot materiaalkeuze.</p></div>
  <div class="grid cols-3">{"".join(tile(s) for s in ONDERWERPEN)}</div></div></section>"""
    write(path,h+footer())

def p_ond(s):
    path=f"/onderwerpen/{s['slug']}/"; c=[("Home","/"),("Onderwerpen","/onderwerpen/"),(s["naam"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":s["naam"],"description":s["resume"],
         "inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    sp="".join(f"<div><dt>{esc(l)}</dt><dd>{esc(v)}</dd></div>" for l,v in s["specs"])
    sec="".join(f"<h2>{esc(t)}</h2><p>{esc(p)}</p>" for t,p in s["secties"])
    pt="".join(f'<li>{IC["check"]}<span>{esc(x)}</span></li>' for x in s["punten"])
    anders=[x for x in ONDERWERPEN if x["slug"]!=s["slug"]][:3]
    h=head(f"{s['naam']} | uitgelegd | {SITE}", s["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section tight"><div class="wrap prose"><span class="eyebrow">{IC['scale']}Onderwerp</span>
  <h1>{esc(s['naam'])}</h1><p class="lead">{esc(s['resume'])}</p></div>
  <div class="wrap"><dl class="specs">{sp}</dl></div>
  <div class="wrap prose">{sec}<h2>Kort samengevat</h2><ul class="ticks" style="margin-bottom:16px">{pt}</ul>
  <p class="disc">{esc(DISC)}</p>{byline()}</div></section>
<section class="section panel"><div class="wrap"><div class="section-head"><h2>Andere onderwerpen</h2></div>
  <div class="grid cols-3">{"".join(tile(x) for x in anders)}</div></div></section>"""
    write(path,h+footer())

def p_gidsen():
    path="/gidsen/"; c=[("Home","/"),("Gidsen",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Gidsen","inLanguage":"nl-NL"},crumb(c)]
    cards="".join(f'<div class="card"><div class="ic">{IC[g["ic"]]}</div><h3><a href="/gidsen/{g["slug"]}/" style="color:inherit;text-decoration:none">{esc(g["titel"])}</a></h3><p>{esc(g["resume"])}</p><p style="margin-top:10px"><a class="more" href="/gidsen/{g["slug"]}/">Lees de gids {IC["arrow"]}</a></p></div>' for g in GIDSEN)
    h=head("Gidsen | garderobe en onderhoud | "+SITE,"Praktische gidsen over het opbouwen van een garderobe en over het onderhouden van kleding.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['book']}Gidsen</span>
  <h1>Gidsen</h1><p class="lead">Twee onderwerpen die losstaan van een enkel kledingstuk en het hele jaar spelen.</p></div>
  <div class="grid cols-2">{cards}</div></div></section>"""
    write(path,h+footer())

def p_gids(g):
    path=f"/gidsen/{g['slug']}/"; c=[("Home","/"),("Gidsen","/gidsen/"),(g["titel"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":g["titel"],"description":g["resume"],
         "inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    h=head(f"{g['titel']} | {SITE}", g["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC[g['ic']]}Gids</span>
  <h1>{esc(g['titel'])}</h1><p class="lead">{esc(g['resume'])}</p>{blocks(g['body'])}{byline()}</div></section>"""
    write(path,h+footer())

def p_nieuws():
    path="/nieuws/"; c=[("Home","/"),("Nieuws",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Nieuws","inLanguage":"nl-NL"},crumb(c)]
    h=head("Nieuws | artikelen over maten en kosten | "+SITE,"Achtergrondartikelen over confectiematen, kosten per draagbeurt en wat kleding werkelijk kost.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['clock']}Nieuws</span>
  <h1>Artikelen</h1><p class="lead">Achtergrond bij wat maten betekenen en waar geld aan uitgeven loont.</p></div>
  <div class="grid cols-2">{"".join(newscard(a) for a in ARTIKELEN)}</div></div></section>"""
    write(path,h+footer())

def p_art(a):
    path=f"/nieuws/{a['slug']}/"; c=[("Home","/"),("Nieuws","/nieuws/"),(a["titel"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":a["titel"],"description":a["resume"],
         "datePublished":a["datum"],"inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    h=head(f"{a['titel']} | {SITE}", a["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['clock']}{esc(a['cat'])}</span>
  <h1>{esc(a['titel'])}</h1><p class="meta" style="margin-bottom:22px">Door {esc(AUTEUR)} &middot; {esc(a['datum_nl'])} &middot; {a['lees']} min lezen</p>
  {blocks(a['body'])}{byline()}</div></section>
<section class="section panel"><div class="wrap"><div class="section-head"><h2>Meer lezen</h2></div>
  <div class="grid cols-2">{"".join(newscard(x) for x in ARTIKELEN if x['slug']!=a['slug'])}</div></div></section>"""
    write(path,h+footer())

def p_over():
    path="/over/"; c=[("Home","/"),("Over",path)]
    ld=[{"@context":"https://schema.org","@type":"AboutPage","@id":BASE+path,"url":BASE+path,"name":"Over","inLanguage":"nl-NL"},crumb(c)]
    h=head("Over Brouwers Mode | wat dit platform is | "+SITE,
      "Brouwers Mode is een onafhankelijke gids over herenkleding. Geen winkel, geen merkvoorkeur en geen samenwerking met fabrikanten.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['book']}Over het platform</span>
  <h1>Een gids, geen kledingzaak</h1>
  <p class="lead">Brouwers Mode legt uit waaraan te zien is of kleding past, wat een materiaal in de praktijk doet, en waar geld uitgeven werkelijk verschil maakt.</p>
  <h2>Waarom deze gids bestaat</h2>
  <p>Advies over kleding komt meestal van partijen die iets verkopen, waardoor lastig te scheiden is wat werkelijk uitmaakt en wat verkooppraat is. Deze gids beschrijft pasvorm en materiaal los van welk merk dan ook, zodat een keuze op eigen gronden gemaakt kan worden.</p>
  <div class="callout"><p><strong>Geen winkel.</strong> Dit platform verkoopt geen kleding, bemiddelt niet en heeft geen afspraken met merken of winkels. Overeenkomsten met namen van bestaande kledingzaken berusten niet op enige samenwerking of betrokkenheid.</p></div>
  <h2>Wat hier wel staat</h2>
  <p>Per onderwerp waar het op aankomt, wat een kleermaker kan aanpassen en waar het in de praktijk misgaat. Merknamen blijven achterwege, omdat collecties sneller wisselen dan de principes erachter.</p>
  <h2>Verschillen per persoon</h2>
  <p>Postuur, houding en voorkeur bepalen wat goed staat. De richtlijnen hier zijn vertrekpunten, geen regels. Passen blijft de enige manier om vast te stellen of iets werkt.</p>
  <p style="margin-top:16px"><a class="btn btn-plum" href="/redactie/">Over de redactie {IC['arrow']}</a> <a class="btn btn-ghost" href="/onderwerpen/">Naar de onderwerpen</a></p></div></section>"""
    write(path,h+footer())

def p_redactie():
    path="/redactie/"; c=[("Home","/"),("Over de redactie",path)]
    ld=[{"@context":"https://schema.org","@type":"Person","@id":BASE+"/#thomas","name":AUTEUR,"jobTitle":AUTEUR_ROL,"worksFor":{"@type":"Organization","name":SITE}},
        {"@context":"https://schema.org","@type":"ProfilePage","@id":BASE+path,"url":BASE+path,"name":"Over de redactie","inLanguage":"nl-NL"},crumb(c)]
    h=head(f"Over de redactie: {AUTEUR} | {SITE}", f"{AUTEUR} schrijft de onderwerpen en gidsen van Brouwers Mode.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="persona">
  <div class="persona-photo"><img src="/assets/img/auteur.svg" alt="Illustratie van {esc(AUTEUR)}"></div>
  <div><span class="eyebrow">{IC['scale']}De redactie</span><h1>{esc(AUTEUR)}</h1>
  <p class="lead">{esc(AUTEUR_ROL)}. Thomas schrijft de onderwerpen, de gidsen en de artikelen op deze site.</p></div></div></div></section>
<section class="section panel"><div class="wrap prose">
  <h2>Van de paskamer naar de redactie</h2>
  <p>Thomas werkte jaren in een herenmodezaak en later bij een kleermakerij, waar zichtbaar werd hoeveel een paar centimeter uitmaakt en hoe vaak dure kleding slecht zit terwijl betaalbare kleding na vermaken uitstekend valt.</p>
  <h2>Principes boven merken</h2>
  <p>Op deze site staan geen merknamen en geen aanbevelingen voor specifieke winkels. Wat er wel staat is waaraan kwaliteit en pasvorm te herkennen zijn, zodat een aanbod daaraan getoetst kan worden.</p>
  <h2>Een getekend portret</h2>
  <p>De illustratie op deze pagina is een tekening, geen foto.</p>
  <h2>Contact</h2>
  <p>Correcties en suggesties komen binnen via <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></section>"""
    write(path,h+footer())

def p_contact():
    path="/contact/"; c=[("Home","/"),("Contact",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"ContactPage","@id":BASE+path,"url":BASE+path,"name":"Contact","inLanguage":"nl-NL"}]
    h=head("Contact | "+SITE,"Vraag, correctie of suggestie voor Brouwers Mode? Een e-mail komt rechtstreeks bij de redactie binnen.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['mail']}Contact</span>
  <h1>Contact met de redactie</h1>
  <p class="lead">Deze site heeft geen contactformulier. Een e-mail komt rechtstreeks bij de redactie binnen.</p>
  <div class="callout"><p><strong>E-mailadres</strong></p><p style="margin:.3em 0"><a href="mailto:{EMAIL}" style="font-size:1.1rem;font-weight:600">{EMAIL}</a></p></div>
  <h2>Waar de redactie iets mee kan</h2>
  <ul><li>Een correctie op een beschrijving, met onderbouwing.</li><li>Een onderwerp dat nog ontbreekt in de gids.</li><li>Praktijkervaring die iets aanvult of tegenspreekt.</li></ul>
  <h2>Waar niet</h2>
  <p>Dit platform verkoopt niets en bemiddelt niet bij aankoop of retour. Voor persoonlijk pasadvies zijn een herenmodezaak of een kleermaker de aangewezen partijen.</p></div></section>"""
    write(path,h+footer())

def legal(path,titel,bs):
    c=[("Home","/"),(titel,path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":titel,"inLanguage":"nl-NL"}]
    h=head(f"{titel} | {SITE}", f"{titel} van {SITE}.",path,ld)+crumbs_html(c)
    h+=f'<section class="section"><div class="wrap prose"><h1>{esc(titel)}</h1>{"".join(bs)}</div></section>'
    write(path,h+footer())

def p_legal():
    legal("/privacybeleid/","Privacybeleid",[
      "<p>Brouwers Mode is een redactioneel platform en verwerkt zo min mogelijk persoonsgegevens.</p>",
      "<h2>Welke gegevens</h2><p>De site bevat geen contactformulier. Wie per e-mail contact opneemt, deelt uitsluitend wat in dat bericht staat, en dat wordt alleen gebruikt om te antwoorden.</p>",
      "<h2>Statistieken</h2><p>Als bezoekcijfers worden bijgehouden, gebeurt dat zo privacyvriendelijk mogelijk en zonder verkoop aan derden.</p>",
      "<h2>Bewaartermijn</h2><p>E-mails worden niet langer bewaard dan nodig is voor de afhandeling.</p>",
      f"<h2>Vragen</h2><p>Vragen over privacy kunnen naar {EMAIL}.</p>"])
    legal("/cookiebeleid/","Cookiebeleid",[
      "<p>Deze site gebruikt zo min mogelijk cookies en plaatst geen advertentiecookies.</p>",
      "<h2>Functioneel</h2><p>Alleen cookies die nodig zijn voor het functioneren van de pagina's kunnen worden geplaatst.</p>",
      "<h2>Lettertypen</h2><p>De lettertypen worden geladen via een externe dienst, wat bij het tonen van een pagina een verzoek naar die dienst met zich meebrengt.</p>",
      f"<h2>Vragen</h2><p>Vragen over cookies kunnen naar {EMAIL}.</p>"])

def p_404():
    h=head("Pagina niet gevonden | "+SITE,"De opgevraagde pagina bestaat niet.","/404.html",None)
    h+=f"""<section class="section"><div class="wrap prose" style="text-align:center">
  <span class="eyebrow" style="justify-content:center">404</span><h1>Deze pagina bestaat niet</h1>
  <p class="lead">De link is mogelijk verouderd. Het overzicht van onderwerpen is een goed vertrekpunt.</p>
  <p><a class="btn btn-plum" href="/">Naar de homepage {IC['arrow']}</a> <a class="btn btn-ghost" href="/onderwerpen/">Alle onderwerpen</a></p></div></section>"""
    open(os.path.join(OUT,"404.html"),"w",encoding="utf-8").write(h+footer())

def extras():
    u=["/","/over/","/redactie/","/onderwerpen/","/gidsen/","/nieuws/","/contact/","/privacybeleid/","/cookiebeleid/"]
    u+=[f"/onderwerpen/{s['slug']}/" for s in ONDERWERPEN]+[f"/gidsen/{g['slug']}/" for g in GIDSEN]+[f"/nieuws/{a['slug']}/" for a in ARTIKELEN]
    open(os.path.join(OUT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}{x}</loc></url>\n" for x in u)+"</urlset>\n")
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(OUT,"_headers"),"w").write("/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    open(os.path.join(OUT,"_redirects"),"w").write(f"https://www.brouwersmode.nl/* {BASE}/:splat 301!\n")

def main():
    import shutil
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT,exist_ok=True)
    shutil.copytree(os.path.join(SRC,"assets"), os.path.join(OUT,"assets"))
    p_home(); p_over(); p_redactie(); p_ond_index()
    for s in ONDERWERPEN: p_ond(s)
    p_gidsen()
    for g in GIDSEN: p_gids(g)
    p_nieuws()
    for a in ARTIKELEN: p_art(a)
    p_contact(); p_legal(); p_404(); extras()
    print("Build klaar in", OUT)

if __name__=="__main__": main()
