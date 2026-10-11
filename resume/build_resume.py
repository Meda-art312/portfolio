"""Build the editable resume data into a searchable, linked, single-column PDF."""
import json
import sys
import reportlab
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'resume/content.json').read_text(encoding='utf-8'))
DEST = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'output/pdf/Mohamed-Medhat-Abdelfattah.pdf'
DEST.parent.mkdir(parents=True, exist_ok=True)
FONT_PATH = Path('C:/Windows/Fonts')
font_files = [('Resume', 'calibri.ttf'), ('ResumeBold', 'calibrib.ttf'), ('ResumeItalic', 'calibrii.ttf')]
if not (FONT_PATH / 'calibri.ttf').is_file():
    FONT_PATH = Path(reportlab.__file__).parent / 'fonts'
    font_files = [('Resume', 'Vera.ttf'), ('ResumeBold', 'VeraBd.ttf'), ('ResumeItalic', 'VeraIt.ttf')]
for name, filename in font_files:
    pdfmetrics.registerFont(TTFont(name, str(FONT_PATH / filename)))
pdfmetrics.registerFontFamily('Resume', normal='Resume', bold='ResumeBold', italic='ResumeItalic', boldItalic='ResumeBold')

INK = colors.HexColor('#172336')
MUTED = colors.HexColor('#435168')
BLUE = colors.HexColor('#2553d8')
RULE = colors.HexColor('#d9dfe9')
WIDTH = A4[0] - 92
styles = {
    'name': ParagraphStyle('name', fontName='ResumeBold', fontSize=23, leading=26, textColor=INK, spaceAfter=2),
    'title': ParagraphStyle('title', fontName='Resume', fontSize=10.5, leading=13, textColor=MUTED, spaceAfter=5),
    'contact': ParagraphStyle('contact', fontName='Resume', fontSize=9.2, leading=12, textColor=MUTED),
    'body': ParagraphStyle('body', fontName='Resume', fontSize=10.1, leading=12.3, textColor=INK),
    'heading': ParagraphStyle('heading', fontName='ResumeBold', fontSize=9.3, leading=11.5, textColor=BLUE, spaceBefore=8, spaceAfter=3),
    'role': ParagraphStyle('role', fontName='ResumeBold', fontSize=10.2, leading=12.5, textColor=INK),
    'date': ParagraphStyle('date', fontName='Resume', fontSize=9.2, leading=12.5, textColor=MUTED, alignment=TA_RIGHT),
    'sub': ParagraphStyle('sub', fontName='Resume', fontSize=9.6, leading=11.7, textColor=MUTED, spaceAfter=2),
    'bullet': ParagraphStyle('bullet', fontName='Resume', fontSize=10, leading=12, textColor=INK, leftIndent=9, firstLineIndent=0, bulletIndent=0, spaceAfter=1.5),
    'links': ParagraphStyle('links', fontName='Resume', fontSize=9.2, leading=12, textColor=BLUE, alignment=TA_RIGHT),
    'stack': ParagraphStyle('stack', fontName='ResumeItalic', fontSize=9.2, leading=11, textColor=MUTED, spaceAfter=1),
}

def p(text, style='body'):
    return Paragraph(text, styles[style])

def text(value):
    return escape(value)

def link(label, url):
    return f'<a href="{escape(url, {chr(34): "&quot;"})}" color="#2553d8">{text(label)}</a>'

def heading(label):
    return [p(text(label.upper()), 'heading'), HRFlowable(width='100%', thickness=.45, color=RULE, spaceAfter=5)]

def row(left, right, left_style='role', right_style='date', ratio=.75):
    t = Table([[p(left, left_style), p(right, right_style)]], colWidths=[WIDTH * ratio, WIDTH * (1-ratio)])
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    return t

def bullets(items):
    return [Paragraph(text(item), styles['bullet'], bulletText='-') for item in items]

story = [p(text(DATA['name']), 'name'), p(text(DATA['title']), 'title')]
story.append(p(link(DATA['email'], 'mailto:' + DATA['email']) + '  |  ' + text(DATA['phone']) + '  |  ' + link('Portfolio', DATA['portfolio']) + '  |  ' + link('LinkedIn', DATA['linkedin']) + '  |  ' + link('GitHub', DATA['github']), 'contact'))
story += heading('Summary')
story.append(p(text(DATA['summary'])))
story += heading('Technical skills')
for name, value in DATA['skills']:
    story.append(p(f'<b>{text(name)}:</b> {text(value)}'))
story += heading('Experience')
for i, role in enumerate(DATA['experience']):
    block = [row(text(role['company']), text(role['dates'])), p(text(role['role']) + ' | ' + text(role['type']), 'sub')]
    block += bullets(role['bullets'])
    if i < len(DATA['experience']) - 1:
        block.append(Spacer(1, 5))
    story.append(KeepTogether(block))
story += heading('Selected projects')
for i, project in enumerate(DATA['projects']):
    project_links = '  |  '.join(link(label, url) for label, url in project['links'])
    block = [row(text(project['name']), project_links, right_style='links', ratio=.80), p(text(project['stack']), 'stack')]
    block += bullets(project['bullets'])
    if i < len(DATA['projects']) - 1:
        block.append(Spacer(1, 4))
    story.append(KeepTogether(block))
story += heading('Education')
story.append(row('<b>' + text(DATA['education']['degree']) + '</b> | ' + text(DATA['education']['school']), text(DATA['education']['dates']), left_style='body'))
story.append(p(text(DATA['education']['detail']), 'sub'))
story += heading('Certification & languages')
story.append(p('<b>Course:</b> ' + text(DATA['certification']) + '<br/><b>Languages:</b> ' + text(DATA['languages'])))

doc = SimpleDocTemplate(str(DEST), pagesize=A4, topMargin=32, bottomMargin=30, leftMargin=40, rightMargin=40, title=DATA['name'] + ' - Software Engineer', author=DATA['name'], subject='Software engineering experience and selected projects', pageCompression=1)
doc.build(story)
print(DEST)
