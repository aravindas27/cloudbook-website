#!/usr/bin/env python3
"""Builds the Cloudbook Associates LLP website into the repository root.
Run:  python3 _build/build.py
Edit the content below (firm details, services, FAQs), then rebuild and commit."""
import json, os, html, datetime, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://cloudbookassociates.com"
TODAY = datetime.date.today().isoformat()

FIRM = {
    "name": "Cloudbook Associates LLP",
    "short": "Cloudbook Associates",
    "llpin": "ACH-3667",
    "gstin": "32AATFC9596J1ZM",
    "street": "Second Floor, Harmony Heights, Near LP School Junction, Thiruvallam",
    "city": "Thiruvananthapuram",
    "region": "Kerala",
    "pin": "695027",
    "phone1": "+91 94472 49439", "tel1": "+919447249439",
    "phone2": "+91 80751 39378", "tel2": "+918075139378",
    "email": "info@cloudbookassociates.com",
    "wa": "919447249439",
    "maps": "https://www.google.com/maps/search/?api=1&query=Harmony+Heights+Thiruvallam+Thiruvananthapuram+695027",
}
e = html.escape

ICON = {
    "gst": '<path d="M4 7h16M4 12h16M4 17h10"/><circle cx="18" cy="17" r="2.5"/>',
    "tax": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/>',
    "roc": '<path d="M3 21h18M5 21V10l7-5 7 5v11"/><path d="M9 21v-6h6v6"/>',
    "books": '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5M9 7h6M9 11h6"/>',
    "start": '<path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.4 6.8 19.1l1-5.8L3.5 9.2l5.9-.9z"/>',
    "payroll": '<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18M7 15h4"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    "shield": '<path d="M12 3l8 3v6c0 4.5-3.4 7.8-8 9-4.6-1.2-8-4.5-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "chat": '<path d="M4 5h16v11H8l-4 4z"/><path d="M8 9h8M8 12h5"/>',
    "rupee": '<path d="M7 5h10M7 9h10M7 5c5 0 7 1.5 7 4s-2 4-7 4l7 6"/>',
    "pin": '<path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
}
def icon(n): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[n]}</svg>'
WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.3-.4.8-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.9-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>'

SERVICES = [
    {
        "slug": "gst-services", "icon": "gst", "name": "GST registration & returns",
        "short": "Registration, monthly and quarterly returns, annual GSTR-9, LUT, refunds and notices.",
        "bullets": ["GSTIN registration and amendments", "GSTR-1, GSTR-3B and QRMP returns", "GSTR-9 annual return, LUT and refunds"],
        "title": "GST Registration & Returns in Thiruvananthapuram",
        "desc": "GST registration, monthly GSTR-1 and GSTR-3B, QRMP, GSTR-9, LUT, refunds and notice replies for businesses in Thiruvananthapuram and Kerala. Fixed fees.",
        "intro": "GST is a monthly habit, not a once-a-year job. We take care of it every month so your returns go in on time, your input tax credit is matched, and late fees stop being a line item.",
        "body": [
            ("What we handle", ["New GST registration, including documents, place-of-business proof and replies to officer queries", "Monthly or quarterly returns: GSTR-1, GSTR-3B and the QRMP scheme with invoice furnishing", "Reconciliation of your purchases with GSTR-2B before every return, so you claim the credit you are entitled to", "GSTR-9 annual return and reconciliation with your books", "Letter of Undertaking (LUT) for exporters and refund applications", "Amendments, cancellation and revocation of registration", "Replies to notices, mismatches and scrutiny, with clear explanations of what the department is asking"]),
            ("How it works", ["You share sales and purchase data each month: Tally or Zoho export, Excel, or simply your invoices", "We reconcile, prepare the return and send you a short summary of tax payable before filing", "You pay the challan (or we pay it and recover at cost), and we file and send you the acknowledgement", "Every due date is tracked on our compliance desk, so nothing depends on memory"]),
            ("Who this suits", ["Traders, manufacturers and service providers registered under GST", "Startups and small businesses that need their first registration", "Exporters who need an LUT every year", "Businesses that have fallen behind and need returns brought up to date"]),
        ],
        "faq": [("What does it cost to file GST returns every month?", "It depends on the number of invoices and whether you file monthly or quarterly. Most small businesses pay a fixed monthly fee, which we quote before we start. Late fees for missed returns usually cost more than our fee."),
                ("Can you file returns I have already missed?", "Yes. We file pending returns in order, work out the late fee and interest, and get your GSTIN back to a clean status."),
                ("Do I need GST registration?", "Registration is compulsory once your turnover crosses the threshold for your state and type of supply, and in some cases (inter-state sales, e-commerce, specified services) regardless of turnover. Tell us what you sell and where, and we will give you a straight answer.")],
    },
    {
        "slug": "income-tax-tds", "icon": "tax", "name": "Income tax & TDS",
        "short": "Returns for individuals, firms, LLPs and companies, TDS returns, Form 16 and advance tax.",
        "bullets": ["ITR for individuals, firms, LLPs and companies", "Quarterly TDS returns and Form 16 / 16A", "Advance tax planning and notice replies"],
        "title": "Income Tax & TDS Return Filing, Thiruvananthapuram",
        "desc": "Income tax returns for individuals, doctors, firms, LLPs and companies, quarterly TDS returns, Form 16, advance tax and notice replies in Thiruvananthapuram.",
        "intro": "Whether it is one salaried person's return or a company's TDS for the whole year, we prepare it carefully, check it against the department's records, and file on time.",
        "body": [
            ("Income tax returns", ["Individuals: salaried, pensioners, NRIs, doctors and other professionals, with capital gains and rental income where needed", "Proprietorships, partnership firms, LLPs and companies, prepared from properly finalised accounts", "Every return checked against AIS and Form 26AS before filing, so mismatches are caught before the department finds them", "Advance tax worked out each quarter, so there are no surprises in March", "Replies to notices for mismatch, defective returns and outstanding demands"]),
            ("TDS and TCS", ["Monthly TDS working and challans for salaries, rent, contractors and professional fees", "Quarterly returns: Form 24Q, 26Q and 27Q", "Form 16 and Form 16A for your employees and vendors", "Correction statements and clearing defaults on TRACES"]),
            ("Worth knowing", ["The new Income-tax Act, 2025 applies from 1 April 2026. We keep track of the changes in forms and terms so you don't have to", "If your clients deduct TDS from your fees, we make sure it reflects in your 26AS and is claimed in your return"]),
        ],
        "faq": [("When is the due date for filing my income tax return?", "For most individuals and businesses that don't need an audit, the due date is 31 July after the year ends. Audited businesses usually have until 31 October. Dates are sometimes extended, so check our compliance calendar or ask us."),
                ("I received an income tax notice. What should I do?", "Don't ignore it and don't reply in a hurry. Send us the notice. We will tell you what it means, what the deadline is, and prepare the reply with the right documents."),
                ("Do you file TDS returns for small businesses and associations?", "Yes. We file TDS returns for companies, firms, doctors, societies and associations. Missed TDS returns attract a late fee of ₹200 a day, so it is worth getting them up to date.")],
    },
    {
        "slug": "company-llp-compliance", "icon": "roc", "name": "Company & LLP compliance",
        "short": "ROC annual filings, AOC-4, MGT-7, LLP Form 8 and 11, DIR-3 KYC, board minutes and changes.",
        "bullets": ["AOC-4, MGT-7 / 7A, ADT-1 and AGM paperwork", "LLP Form 8 and Form 11", "Director KYC, partner changes and name changes"],
        "title": "Company & LLP ROC Compliance in Kerala",
        "desc": "ROC compliance for companies and LLPs in Kerala: AOC-4, MGT-7, ADT-1, DIR-3 KYC, LLP Form 8 and 11, AGM paperwork, partner changes and backlog filings.",
        "intro": "MCA penalties add up at ₹100 a day per form, and a missed filing can disqualify directors. We run your company or LLP compliance on a calendar, so filings are prepared well before the due date.",
        "body": [
            ("Private limited companies", ["Board meetings and the AGM: notices, minutes and resolutions", "AOC-4 (financial statements) and MGT-7 / MGT-7A (annual return)", "ADT-1 for auditor appointment, DIR-3 KYC for directors", "DPT-3, MSME-1 and INC-20A where they apply", "Change of name, registered office, directors or share capital", "Clearing old backlogs, including filings that were missed for several years"]),
            ("LLPs", ["Form 11 (annual return) by 30 May and Form 8 (statement of accounts) by 30 October", "Designated partner KYC", "Admission and retirement of partners, with the supplementary LLP agreement and Form 3 and Form 4 filings", "Changes to contribution, business activity or address"]),
            ("Foreign-owned companies", ["Annual FLA return to the RBI for companies with foreign investment", "Coordination of transfer pricing reports and FEMA reporting with your auditors"]),
        ],
        "faq": [("What happens if my company does not file AOC-4 and MGT-7?", "The company pays an additional fee of ₹100 a day for each form, and after continuing defaults the directors can be disqualified and the company can be struck off. If you are behind, the sooner it is fixed, the lower the cost."),
                ("Is audit compulsory for my LLP?", "An LLP needs an audit if its turnover exceeds ₹40 lakh or contribution exceeds ₹25 lakh in a year. Below that, the accounts are certified by the partners. Audits are carried out by practising Chartered Accountants we work with."),
                ("Can you handle a partner leaving our LLP?", "Yes. We draft the retirement and admission documents, the supplementary LLP agreement, and file Form 3 and Form 4 with the MCA.")],
    },
    {
        "slug": "accounting-bookkeeping", "icon": "books", "name": "Accounting & bookkeeping",
        "short": "Monthly books in Tally, Zoho Books or Xero, financial statements and MIS for owners and banks.",
        "bullets": ["Monthly bookkeeping and bank reconciliation", "Year-end financial statements", "Project reports and CMA data for loans"],
        "title": "Accounting & Bookkeeping in Thiruvananthapuram",
        "desc": "Monthly bookkeeping in Tally, Zoho Books and Xero, financial statements, MIS, project reports and CMA data for bank loans, for businesses in Kerala.",
        "intro": "Good books make every other job easier: tax returns, bank loans, investor questions and your own decisions. We keep your accounts up to date every month, not in a rush at year-end.",
        "body": [
            ("Monthly accounting", ["Bookkeeping in Tally Prime, Zoho Books or Xero, from your bank statements, invoices and bills", "Bank, GST and vendor reconciliations", "Simple monthly reports: sales, expenses, profit, receivables and payables", "Payroll processing and salary statements"]),
            ("Year-end and reporting", ["Financial statements in the required format for companies, LLPs, firms and proprietors", "Coordination with your auditor and preparation of schedules", "Books for a new company's first year, set up properly from day one"]),
            ("For loans and funding", ["Projected financial statements and project reports", "CMA data for bank loans, including renewals", "Working-capital and repayment projections that a bank can follow"]),
            ("For overseas accounting practices", ["Outsourced bookkeeping and payroll in Xero for small practices in Australia and elsewhere, handled by our team in Kerala"]),
        ],
        "faq": [("Which accounting software do you work with?", "Tally Prime, Zoho Books and Xero. If you don't use any software yet, we will suggest one that suits the size of your business and set it up."),
                ("Can you prepare a project report for my bank loan?", "Yes. We prepare projected financial statements, project reports and CMA data based on your actual numbers and a realistic plan, in the format banks expect."),
                ("I only have bank statements. Can you still do my accounts?", "Yes. Many of our clients start that way. We build the books from the bank statements and ask you about the entries we can't identify.")],
    },
    {
        "slug": "business-registration", "icon": "start", "name": "Business setup & registrations",
        "short": "Private limited company and LLP incorporation, GST, IEC, Udyam, and setup for foreign founders.",
        "bullets": ["Company and LLP incorporation", "GST, IEC, Udyam (MSME) and PAN/TAN", "LLPs and companies with foreign partners"],
        "title": "Company & LLP Registration in Thiruvananthapuram",
        "desc": "Private limited company and LLP registration, GST, IEC, Udyam, DSC and DIN, and setup for foreign founders with Indian partners, in Thiruvananthapuram.",
        "intro": "Starting a business involves a dozen registrations in the right order. We tell you which structure fits, then handle the paperwork end to end so you can get on with the business.",
        "body": [
            ("Choosing the right structure", ["An honest comparison of proprietorship, partnership, LLP and private limited company for your plans, tax position and funding needs", "For foreign nationals starting in India: the options available with a resident Indian partner, and what each means for ownership and reporting"]),
            ("Registrations we handle", ["Private limited company incorporation (SPICe+) and LLP incorporation (RUN-LLP and FiLLiP)", "Digital signature certificates (DSC) and director or designated partner identification (DIN)", "LLP agreements and company documents", "PAN, TAN, GST registration and the first bank account documents", "Import Export Code (IEC) from the DGFT, and LUT for exporters", "Udyam (MSME) registration", "Foreign investment reporting for LLPs and companies with foreign partners"]),
            ("After registration", ["A compliance calendar for your first year, so the first filings don't get missed", "Accounting and GST from the first month, if you want us to stay on"]),
        ],
        "faq": [("How long does it take to register a private limited company or LLP?", "Usually two to four weeks once documents are ready, depending on name approval and MCA processing."),
                ("Should I choose an LLP or a private limited company?", "An LLP is simpler and cheaper to run. A private limited company suits you better if you plan to raise investment or issue shares to employees. We'll go through your situation and recommend one."),
                ("Can a foreign national be a partner in an Indian LLP?", "Yes, subject to the FDI rules for the activity and with at least one resident designated partner. We handle the incorporation and the foreign investment reporting.")],
    },
]

FAQ_HOME = [
    ("Which areas do you serve?", "We are based in Thiruvallam, Thiruvananthapuram, and work with clients across Kerala. Most work is done online, so we also work with NRIs and businesses elsewhere in India."),
    ("How are your fees decided?", "We quote a fixed fee before we start, based on the work involved. Government fees, challans and late fees are passed on at actual cost, with receipts. No surprises on the invoice."),
    ("Do you do audits?", "Statutory and tax audits are carried out and signed by practising Chartered Accountants we work with. We prepare the books, schedules and filings around the audit, so the whole process stays in one place for you."),
    ("I am behind on my filings. Can you help?", "Yes, and it is more common than you think. We list everything that is pending, work out the penalties, and bring you up to date in the order that saves you the most money."),
    ("How do I share documents with you?", "Whatever is easiest for you: WhatsApp, email, a shared Google Drive folder, or drop them at our office. We send a short checklist so you know exactly what is needed."),
    ("How do you make sure deadlines are not missed?", "Every client's GST, TDS, income tax and ROC due dates are on our own compliance desk, which flags what is due and what is overdue every day. You get reminders well before the due date."),
]

WHO = [
    ("Startups and new businesses", "Registration, the first year's compliance and accounts set up properly from day one."),
    ("Private limited companies", "Annual ROC filings, TDS, GST and year-end accounts, including foreign-owned subsidiaries."),
    ("LLPs and partnership firms", "Form 8 and 11, partner changes, ITR and monthly GST."),
    ("Doctors and professionals", "Clinic accounts, GST where it applies, income tax and advance tax."),
    ("Associations and societies", "TDS returns, GST and accounts for professional associations and not-for-profits."),
    ("NRIs and foreign founders", "Indian tax returns, business setup with an Indian partner, and filings handled online."),
]

STEPS = [
    ("Tell us what you need", "Call, WhatsApp or fill the form. A short conversation is usually enough to understand your situation."),
    ("Get a clear quote", "We list exactly what we'll do, the due dates involved and a fixed fee. Government fees are shown separately."),
    ("Share documents once", "We send a checklist. Share by WhatsApp, email or Drive, and we only ask again if something is missing."),
    ("Filed, and kept on track", "You get the acknowledgement for every filing, and reminders before the next due date."),
]

WHY = [
    ("shield", "Deadlines tracked, not remembered", "Every filing for every client sits on our compliance desk, with its due date, status and acknowledgement."),
    ("rupee", "Fixed fees, agreed upfront", "You know the fee before we start. Government fees and challans are billed at actual cost, with receipts."),
    ("user", "One person who knows your file", "You speak to the same person every time, who already knows your business and your history."),
    ("chat", "Plain answers, quickly", "We explain what a notice or a filing means in simple language, on WhatsApp, a call or a visit."),
]

# Compliance calendar (standard due dates; extensions are announced from time to time).
CAL = [
    ("Every month", [("7th", "TDS and TCS payment for the previous month", "TDS"), ("11th", "GSTR-1 for monthly filers", "GST"), ("13th", "IFF for QRMP filers (first two months of a quarter)", "GST"), ("15th", "PF and ESI contributions", "Payroll"), ("20th", "GSTR-3B for monthly filers", "GST"), ("22nd / 24th", "GSTR-3B for QRMP filers, in the month after each quarter (22nd for Kerala)", "GST")]),
    ("April – June 2026", [("30 Apr", "TDS payment for March; MSME-1 for October to March", "TDS / ROC"), ("30 May", "LLP Form 11 annual return", "LLP"), ("31 May", "TDS return for January to March (Q4)", "TDS"), ("15 Jun", "Advance tax, first instalment (15%); Form 16 to employees", "Income tax"), ("30 Jun", "DPT-3 return of deposits", "ROC")]),
    ("July – September 2026", [("15 Jul", "FLA return to the RBI (companies with foreign investment)", "FEMA"), ("31 Jul", "Income tax return for individuals and non-audit cases; TDS return for April to June (Q1)", "Income tax / TDS"), ("15 Sep", "Advance tax, second instalment (45%)", "Income tax"), ("30 Sep", "Tax audit report; DIR-3 KYC for directors; last date for the company AGM", "Income tax / ROC")]),
    ("October – December 2026", [("14 Oct", "ADT-1 auditor appointment (15 days from AGM)", "ROC"), ("29 Oct", "AOC-4 financial statements (30 days from AGM)", "ROC"), ("30 Oct", "LLP Form 8 statement of accounts", "LLP"), ("31 Oct", "Income tax return for audit cases; TDS return for July to September (Q2); MSME-1 for April to September", "Income tax / TDS"), ("29 Nov", "MGT-7 / MGT-7A annual return (60 days from AGM)", "ROC"), ("15 Dec", "Advance tax, third instalment (75%)", "Income tax"), ("31 Dec", "GSTR-9 and GSTR-9C annual returns; last date for belated or revised income tax returns", "GST / Income tax")]),
    ("January – March 2027", [("31 Jan", "TDS return for October to December (Q3)", "TDS"), ("15 Mar", "Advance tax, final instalment (100%)", "Income tax"), ("31 Mar", "Year-end: GST LUT for the next year, closing entries, tax-saving investments", "Planning")]),
]

NAV = [("Services", "index.html#services"), ("Who we help", "index.html#who"), ("Compliance calendar", "compliance-calendar.html"), ("About", "index.html#about"), ("Contact", "contact.html")]

def jsonld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + '</script>'

ORG = {
    "@context": "https://schema.org", "@type": "AccountingService", "@id": SITE + "/#firm",
    "name": FIRM["name"], "url": SITE + "/", "logo": SITE + "/assets/img/logo.png", "image": SITE + "/assets/img/og-image.png",
    "telephone": FIRM["tel1"], "email": FIRM["email"],
    "address": {"@type": "PostalAddress", "streetAddress": FIRM["street"], "addressLocality": FIRM["city"], "addressRegion": FIRM["region"], "postalCode": FIRM["pin"], "addressCountry": "IN"},
    "areaServed": [{"@type": "State", "name": "Kerala"}, {"@type": "Country", "name": "India"}],
    "knowsAbout": ["GST", "Income tax", "TDS", "ROC compliance", "LLP compliance", "Bookkeeping", "Company registration"],
    "priceRange": "₹₹",
}

def faq_ld(items): return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def page(path, title, desc, body, current="", extra_ld=None, robots="index, follow"):
    url = SITE + "/" + ("" if path == "index.html" else path)
    lds = [ORG] + (extra_ld or [])
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if current == lbl else ""}>{lbl}</a>' for lbl, h in NAV)
    svc_links = "".join(f'<li><a href="{s["slug"]}.html">{e(s["name"])}</a></li>' for s in SERVICES)
    return f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self'; style-src 'self'; font-src 'self'; img-src 'self' data:; connect-src 'none'; manifest-src 'self'; base-uri 'none'; form-action 'none'; object-src 'none'">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0b2c6e">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{FIRM["name"]}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="assets/img/icon-64.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/ibm-plex-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/site.css">
{"".join(jsonld(x) for x in lds)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="{FIRM["name"]} home"><img src="assets/img/logo.png" alt="{FIRM["name"]}" width="398" height="101"></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" aria-label="Main">{nav}</nav>
    <a class="btn btn-primary btn-sm" href="contact.html">Get a quote</a>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <img src="assets/img/logo-white.png" alt="{FIRM["name"]}" width="398" height="101">
        <p>Accounting, tax and compliance for businesses in Kerala.</p>
      </div>
      <div><h3>Services</h3><ul>{svc_links}</ul></div>
      <div><h3>Company</h3><ul><li><a href="index.html#about">About us</a></li><li><a href="compliance-calendar.html">Compliance calendar</a></li><li><a href="contact.html">Contact</a></li><li><a href="privacy.html">Privacy</a></li></ul></div>
      <div><h3>Office</h3><address>{e(FIRM["street"])}, {FIRM["city"]}, {FIRM["region"]} – {FIRM["pin"]}</address>
        <p class="mt-s"><a href="tel:{FIRM["tel1"]}">{FIRM["phone1"]}</a><br><a href="tel:{FIRM["tel2"]}">{FIRM["phone2"]}</a><br><a href="mailto:{FIRM["email"]}">{FIRM["email"]}</a></p></div>
    </div>
    <div class="legal"><span>© <span data-year>2026</span> {FIRM["name"]} · LLPIN {FIRM["llpin"]} · GSTIN {FIRM["gstin"]}</span><span>The information on this site is general. Please speak to us before acting on it.</span></div>
  </div>
</footer>
<a class="wa-float" href="https://wa.me/{FIRM["wa"]}" aria-label="Chat with us on WhatsApp" rel="noopener" target="_blank">{WA_SVG}</a>
<script src="assets/site.js" defer></script>
</body>
</html>
'''

def board():
    rows = [("07 Nov", "TDS payment for October", "All monthly clients", "ok", "Paid"), ("11 Nov", "GSTR-1, October", "Monthly filers", "ok", "Filed"),
            ("20 Nov", "GSTR-3B, October", "Reconciled with 2B", "due", "Due soon"), ("29 Nov", "MGT-7 annual returns", "Private limited companies", "plan", "Prepared"),
            ("31 Dec", "GSTR-9 for FY 2025-26", "Annual return", "plan", "Scheduled")]
    li = "".join(f'<li><span class="d">{d}</span><span class="w">{w}<small>{s}</small></span><span class="tag {c}">{t}</span></li>' for d, w, s, c, t in rows)
    return f'<div class="board" role="img" aria-label="Example of the compliance tracking we do for clients: monthly GST and TDS, annual ROC filings"><div class="board-h"><b>This month’s filings</b><span>November</span></div><ul>{li}</ul><div class="board-f">An example of how we track every client’s due dates.</div></div>'

def contact_block(heading=True):
    opts = "".join(f"<option>{e(s['name'])}</option>" for s in SERVICES) + "<option>Something else</option>"
    types = "".join(f"<option>{t}</option>" for t in ["Proprietorship", "Partnership firm", "LLP", "Private limited company", "Individual / NRI", "Association / society", "Not started yet"])
    head = '<div class="sec-head"><span class="eyebrow">Contact</span><h2>Let’s talk about what you need</h2><p class="lead">Call, WhatsApp or send the form. We usually reply the same working day.</p></div>' if heading else ''
    return f'''{head}<div class="contact">
  <div class="contact-info">
    <div>{icon("phone")}<span><b>Phone</b><a href="tel:{FIRM["tel1"]}">{FIRM["phone1"]}</a> · <a href="tel:{FIRM["tel2"]}">{FIRM["phone2"]}</a></span></div>
    <div>{icon("chat")}<span><b>WhatsApp</b><a href="https://wa.me/{FIRM["wa"]}" target="_blank" rel="noopener">Message us on {FIRM["phone1"]}</a></span></div>
    <div>{icon("mail")}<span><b>Email</b><a href="mailto:{FIRM["email"]}">{FIRM["email"]}</a></span></div>
    <div>{icon("pin")}<span><b>Office</b>{e(FIRM["street"])},<br>{FIRM["city"]}, {FIRM["region"]} – {FIRM["pin"]}<br><a href="{e(FIRM["maps"])}" target="_blank" rel="noopener">Open in Google Maps</a></span></div>
    <div>{icon("clock")}<span><b>Visits</b>Please call before you come, so the right person is in the office.</span></div>
  </div>
  <form class="form" id="enquiry" novalidate>
    <label>Your name<input name="name" autocomplete="name" required></label>
    <label>Phone or WhatsApp<input name="phone" type="tel" autocomplete="tel" inputmode="tel" required></label>
    <label>Type of business<select name="type"><option value="">Choose…</option>{types}</select></label>
    <label>What do you need help with?<select name="service"><option value="">Choose…</option>{opts}</select></label>
    <label class="full">Anything we should know?<textarea name="message" placeholder="For example: we are a new LLP and need GST registration and monthly returns."></textarea></label>
    <div class="full actions"><button class="btn btn-wa" type="submit" value="whatsapp">{WA_SVG} Send on WhatsApp</button><button class="btn btn-ghost" type="submit" value="email">Send by email</button></div>
    <p class="full err" role="alert"></p>
    <p class="full note">Your details go straight to us on WhatsApp or email. This website does not store them.</p>
  </form>
</div>'''

def home():
    cards = "".join(f'''<a class="card" href="{s["slug"]}.html"><span class="ico">{icon(s["icon"])}</span><h3>{e(s["name"])}</h3><p class="muted">{e(s["short"])}</p><ul>{"".join(f"<li>{e(b)}</li>" for b in s["bullets"])}</ul><span class="more">Learn more {icon("arrow").replace('<svg ', '<svg width="16" height="16" ')}</span></a>''' for s in SERVICES)
    cards += f'''<div class="card"><span class="ico">{icon("payroll")}</span><h3>Payroll & advisory</h3><p class="muted">Monthly payroll, PF and ESI coordination, and straight advice when you are making a decision.</p><ul><li>Salary processing and payslips</li><li>Lease, partnership and business documents</li><li>Second opinions on notices and agreements</li></ul><a class="more" href="contact.html">Ask us {icon("arrow").replace('<svg ', '<svg width="16" height="16" ')}</a></div>'''
    who = "".join(f"<div><b>{e(a)}</b><p>{e(b)}</p></div>" for a, b in WHO)
    steps = "".join(f"<li><b>{e(a)}</b><p>{e(b)}</p></li>" for a, b in STEPS)
    why = "".join(f'<div>{icon(i)}<span><b>{e(a)}</b><p>{e(b)}</p></span></div>' for i, a, b in WHY)
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in FAQ_HOME)
    body = f'''<section class="hero"><div class="wrap">
  <div>
    <span class="eyebrow">Accounting · Tax · Compliance · Thiruvananthapuram</span>
    <h1>Your GST, tax and company filings, <em>handled on time</em>, every time.</h1>
    <p class="lead">We are an accounting and compliance firm in Thiruvallam, Thiruvananthapuram. We look after GST, income tax, TDS, ROC filings and books for small businesses, companies, LLPs and professionals across Kerala, so you can spend your time on the business.</p>
    <div class="cta-row"><a class="btn btn-primary" href="contact.html">Get a fixed-fee quote</a><a class="btn btn-wa" href="https://wa.me/{FIRM["wa"]}" target="_blank" rel="noopener">{WA_SVG} WhatsApp us</a></div>
    <ul class="ticks"><li>Fixed fees, agreed before we start</li><li>Every due date tracked for you</li><li>One point of contact for all filings</li><li>Online or at our office</li></ul>
  </div>
  {board()}
</div></section>

<section id="services"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">What we do</span><h2>Everything a growing business has to file, in one place</h2><p class="lead">Most of our clients came to us for one thing, usually GST or a notice, and now leave all their compliance with us. Start with whatever you need today.</p></div>
  <div class="grid g3">{cards}</div>
</div></section>

<section class="alt" id="who"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Who we work with</span><h2>From first registration to annual returns</h2><p class="lead">Our clients range from a doctor's clinic to foreign-owned companies. What they have in common: they want filings done correctly, on time, without chasing.</p></div>
  <div class="who">{who}</div>
</div></section>

<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">How it works</span><h2>Simple to start, easy to stay</h2></div>
  <ol class="steps">{steps}</ol>
</div></section>

<section class="alt" id="about"><div class="wrap split">
  <div><span class="eyebrow">About us</span><h2 class="h2-about">A local firm that treats your deadlines as its own</h2>
    <p class="lead mb-s">{FIRM["name"]} is a limited liability partnership based in Thiruvallam, Thiruvananthapuram. We started by doing GST and books for local businesses and grew into a full compliance practice for companies, LLPs, professionals and associations.</p>
    <p class="muted">We run our own practice on a compliance desk that tracks every client's filings, hours and due dates. Audits and certifications are carried out by practising Chartered Accountants we work closely with, so you get everything through one door.</p></div>
  <div class="points">{why}</div>
</div></section>

<section class="band" aria-label="Compliance calendar"><div class="wrap">
  <div><h2>Never miss a due date again</h2><p>See every GST, TDS, income tax and ROC deadline for 2026-27 on one page.</p></div>
  <div class="cta-row"><a class="btn btn-primary" href="compliance-calendar.html">Open the compliance calendar</a><a class="btn btn-ghost" href="contact.html">Ask us to track yours</a></div>
</div></section>

<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Questions</span><h2>Frequently asked questions</h2></div>
  <div class="faq">{faq}</div>
</div></section>

<section class="alt" id="contact"><div class="wrap">{contact_block()}</div></section>'''
    return page("index.html", "GST, Tax & ROC Compliance in Thiruvananthapuram | Cloudbook",
                "GST, income tax, TDS, accounting and company/LLP compliance for businesses in Thiruvananthapuram and Kerala. Fixed fees, every due date tracked.",
                body, extra_ld=[faq_ld(FAQ_HOME)])

def service_page(s):
    sections = "".join(f'<h2>{e(h)}</h2><ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul>' for h, items in s["body"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in s["faq"])
    others = "".join(f'<li><a href="{o["slug"]}.html">{e(o["name"])}</a></li>' for o in SERVICES if o is not s)
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": s["name"], "item": f'{SITE}/{s["slug"]}.html'}]}
    svc = {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "description": s["desc"], "provider": {"@id": SITE + "/#firm"}, "areaServed": {"@type": "State", "name": "Kerala"}}
    body = f'''<section class="page-hero"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / <a href="index.html#services">Services</a> / {e(s["name"])}</nav>
  <h1>{e(s["name"])}</h1><p class="lead">{e(s["intro"])}</p>
  <div class="cta-row mt"><a class="btn btn-primary" href="contact.html">Get a fixed-fee quote</a><a class="btn btn-wa" href="https://wa.me/{FIRM["wa"]}?text={urllib.parse.quote("Hello, I need help with " + s["name"])}" target="_blank" rel="noopener">{WA_SVG} WhatsApp us</a></div></div></section>
<section><div class="wrap layout">
  <article class="prose">{sections}
    <h2>Questions we often get</h2><div class="faq">{faq}</div></article>
  <aside class="aside"><h3>Talk to us</h3><p class="muted small">Tell us what you need and we’ll come back with a clear, fixed quote.</p>
    <a class="btn btn-primary" href="contact.html">Get a quote</a><a class="btn btn-ghost" href="tel:{FIRM["tel1"]}">Call {FIRM["phone1"]}</a>
    <h3 class="mt-s">Other services</h3><ul>{others}</ul><a href="compliance-calendar.html">Compliance calendar 2026-27 →</a></aside>
</div></section>'''
    return page(f'{s["slug"]}.html', f'{s["title"]} | Cloudbook', s["desc"], body, current="Services", extra_ld=[svc, crumbs, faq_ld(s["faq"])])

def calendar_page():
    blocks = ""
    for head, rows in CAL:
        blocks += f'<h2>{e(head)}</h2><div class="tblwrap"><table class="cal"><thead><tr><th>Due date</th><th>What is due</th><th>Area</th></tr></thead><tbody>' + "".join(f"<tr><td>{e(d)}</td><td>{e(w)}</td><td>{e(a)}</td></tr>" for d, w, a in rows) + "</tbody></table></div>"
    body = f'''<section class="page-hero"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Compliance calendar</nav>
  <h1>Compliance calendar 2026-27: GST, TDS, income tax and ROC due dates</h1>
  <p class="lead">Every regular due date for businesses, companies and LLPs in India, from April 2026 to March 2027, on one page. Bookmark it, or let us track it for you.</p></div></section>
<section><div class="wrap layout"><article class="prose">
  <div class="callout">These are the standard statutory due dates. The government sometimes extends them, and some dates depend on your AGM or quarterly filing choice. The new Income-tax Act, 2025 applies from 1 April 2026. Please check with us before relying on a date.</div>
  {blocks}
  <h2>Late fees in brief</h2><ul>
    <li>GST returns: late fee per day of delay, plus 18% interest on tax paid late</li>
    <li>TDS returns: ₹200 a day until the return is filed, up to the TDS amount</li>
    <li>ROC forms (AOC-4, MGT-7, LLP Form 8 and 11): ₹100 a day per form, with no upper limit</li>
    <li>DIR-3 KYC: ₹5,000 once the due date passes</li>
    <li>Belated income tax return: a fee of up to ₹5,000, plus interest on tax due</li></ul>
</article>
<aside class="aside"><h3>Want us to track these for you?</h3><p class="muted small">We keep every client’s due dates on our compliance desk and file well before the deadline.</p><a class="btn btn-primary" href="contact.html">Get started</a>
  <h3 class="mt-s">Services</h3><ul>{"".join(f'<li><a href="{s["slug"]}.html">{e(s["name"])}</a></li>' for s in SERVICES)}</ul></aside>
</div></section>'''
    return page("compliance-calendar.html", "Compliance Calendar 2026-27: GST, TDS, ITR & ROC | Cloudbook",
                "All GST, TDS, income tax, advance tax, ROC and LLP due dates for FY 2026-27 in one calendar, with late fees, from Cloudbook Associates LLP, Thiruvananthapuram.",
                body, current="Compliance calendar")

def contact_page():
    body = f'''<section class="page-hero"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / Contact</nav>
  <h1>Contact Cloudbook Associates</h1><p class="lead">Tell us what you need. We usually reply the same working day with a clear next step and a fixed quote.</p></div></section>
<section><div class="wrap">{contact_block(heading=False)}</div></section>'''
    return page("contact.html", "Contact Cloudbook Associates LLP, Thiruvallam, Trivandrum",
                "Cloudbook Associates LLP, Harmony Heights, Thiruvallam, Thiruvananthapuram 695027. Call or WhatsApp +91 94472 49439 for GST, tax and compliance help.",
                body, current="Contact")

def privacy_page():
    body = f'''<section class="page-hero"><div class="wrap"><h1>Privacy</h1><p class="lead">Short and plain: this website does not collect or store your personal data.</p></div></section>
<section><div class="wrap"><div class="prose">
  <h2>This website</h2><p>The site has no tracking, analytics, advertising or cookies, and loads nothing from other companies. The enquiry form does not send your details to us or to anyone else through this website: it opens WhatsApp or your email app with your message filled in, and you choose whether to send it.</p>
  <h2>When you work with us</h2><p>Documents and information you share with us are used only to provide the services you ask for and to meet our legal obligations, and are kept confidential. We do not sell or share client data. Ask us at any time what we hold about you, or to correct it.</p>
  <h2>Contact</h2><p>{FIRM["name"]}, {e(FIRM["street"])}, {FIRM["city"]} – {FIRM["pin"]}. Email <a href="mailto:{FIRM["email"]}">{FIRM["email"]}</a>.</p>
  <p class="muted">Last updated {datetime.date.today().strftime("%d %B %Y")}.</p></div></div></section>'''
    return page("privacy.html", "Privacy | Cloudbook Associates LLP", "Privacy notice for the Cloudbook Associates LLP website: no tracking, no cookies, and the enquiry form stores nothing.", body)

def notfound_page():
    body = '<section class="page-hero"><div class="wrap"><h1>Page not found</h1><p class="lead">The page you were looking for isn’t here. Try the <a href="index.html">home page</a>, our <a href="compliance-calendar.html">compliance calendar</a>, or <a href="contact.html">contact us</a>.</p></div></section>'
    return page("404.html", "Page not found | Cloudbook Associates LLP", "Page not found.", body, robots="noindex")

def write(name, text):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f: f.write(text)

def main():
    write("index.html", home())
    for s in SERVICES: write(f'{s["slug"]}.html', service_page(s))
    write("compliance-calendar.html", calendar_page())
    write("contact.html", contact_page())
    write("privacy.html", privacy_page())
    write("404.html", notfound_page())
    urls = ["", "contact.html", "compliance-calendar.html"] + [f'{s["slug"]}.html' for s in SERVICES] + ["privacy.html"]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print("built", len(urls) + 1, "pages")

if __name__ == "__main__":
    main()
