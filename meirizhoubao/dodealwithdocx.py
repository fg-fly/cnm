#coding=utf-8
import os
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn #中文
from docx.shared import Inches
from docx.shared import RGBColor
from docx.shared import Pt


# reload(sys)  # reload 才能调用 setdefaultencoding 方法
# sys.setdefaultencoding('utf-8')
document = Document('sunday.docx')
table_target = document.tables[0].columns
table_target[1].cells[1].text = u'ok'

document.save('sunday.docx')
