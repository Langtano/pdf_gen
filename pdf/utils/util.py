import math
from rest_framework.response import Response
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, TableStyle, Image, Paragraph
import datetime


def create_response(success: bool, status: int, data: object, message: object, code: int):

    status = 200
    if success:
        code = 200

    response = {
        'success': success,
        'code': code,
        'data': data,
        'message': message
    }

    return Response(response, status=status)


class PdfGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_pdf(ticket):
        try:
            w, h = letter
            wPadding = w - 100
            money_box_table_header = ["Transacción", "Cantidad", "Fecha", "Réditos", "Total"]

            # DEFINE PDF CONFIGURATIONS
            c = canvas.Canvas('{}.pdf'.format(ticket['report']), pagesize=letter)
            c.setTitle('MoneyBox {}'.format(ticket['report']))
            pdfmetrics.registerFont(
                TTFont('Lato', "fonts/Lato-Regular.ttf"),
            )
            pdfmetrics.registerFont(
                TTFont('Lato-Bold', "fonts/Lato-Bold.ttf"),
            )
            pdfmetrics.registerFont(
                TTFont('Montserrat', "fonts/Montserrat-Bold.ttf")
            )

            number_pages = (len(ticket['data'])) / 15
            table_data = ticket['data']

            for item in range(math.ceil(number_pages)):
                page_table_data = table_data[item*15 : (item*15)+15]
                page_table_data.insert(0, money_box_table_header)

                # TABLE CONFIGURATION
                table = Table(page_table_data)
                style = TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#000000')),
                    ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#FFFFFF')),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, -1), 'Lato'),
                    ('FONTSIZE', (0, 0), (-1, 0), 14),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12)
                ])
                row_number = len(page_table_data)
                for i in range(1, row_number):
                    if i % 2 == 0:
                        bc = HexColor('#DEDEDE')
                    else:
                        bc = HexColor('#FFFFFF')
                    ts = TableStyle([
                        ('BACKGROUND', (0, i), (-1, i), bc),
                        ('LINEBELOW', (0, i), (-1, i), 1, HexColor('#000000'))
                    ])
                    table.setStyle(ts)
                table.setStyle(style)
                table._argW[0] = wPadding / 5
                table._argW[1] = wPadding / 5
                table._argW[2] = wPadding / 5
                table._argW[3] = wPadding / 5
                table._argW[4] = wPadding / 5
                table.wrapOn(c, 0, 0)
                table.drawOn(c, x=50, y=462 - ((row_number - 1) * 18))

                # IMAGES
                Image("images/naica.png", width=150, height=150).drawOn(c, x=((wPadding / 4) * 3) + 50, y=(h / 4) * 3.1)
                Image("images/naicaClearLogo.png", width=wPadding, height=400).drawOn(c, x=50, y=196)
                Image("images/mblogo.png", width=150, height=30).drawOn(c, x=50, y=(h / 2) + 110)

                # HEADER
                formated_address = Helpers.split_long_string_fields_and_spacing(
                    long_string=ticket['address'], field1=25, field2=35, field3=35
                )
                c.setFont('Montserrat', 15)
                c.setFillColor(HexColor('#000000'))
                c.drawString(x=50, y=h - 50, text='Estado de Cuenta')
                c.drawString(x=50, y=h - 100, text=ticket['name'])
                c.drawString(x=250, y=h - 100, text='Usuario: {user}'.format(user=ticket['user']))
                c.setFont('Montserrat', 13)
                if item+1 == math.ceil(number_pages):
                    c.drawRightString(x=wPadding + 50, y=442 - ((row_number - 1) * 18),
                                  text='Total: {total}'.format(total=ticket['total']))
                c.setFillColor(HexColor('#0F682D'))
                c.drawRightString(x=wPadding + 50, y=(h / 2) + 120, text=ticket['goal'])
                c.setFont('Lato', 10)
                c.setFillColor(HexColor('#000000'))
                c.drawString(x=50, y=h - 65, text='Fecha: {date}'.format(date=Helpers.get_date()))
                c.drawString(x=50, y=h - 120, text='RFC: {rfc}'.format(rfc=ticket['rfc']))
                c.drawString(x=50, y=h - 135, text='Direccion: {address0}'.format(address0=formated_address[0]))
                c.drawString(x=50, y=h - 150, text=formated_address[1])
                c.drawString(x=50, y=h - 165, text=formated_address[2])
                c.drawString(x=250, y=h - 120, text='Moneda: {currency}'.format(currency=ticket['currency']))
                c.drawString(x=250, y=h - 135, text='Plan: {plan}'.format(plan=ticket['plan']))
                c.drawString(x=250, y=h - 150, text='Período: {period}'.format(period=ticket['period']))
                c.drawRightString(x=wPadding + 50, y=(h / 2) + 135, text='Objetivo de mi MoneyBox:')

                if item+1 == math.ceil(number_pages):
                    congrats_text_header = (
                        """
                            <strong>
                                ¡Felicidades!
                            </strong>
                        """
                    )
                    congrats_text = (
                        """
                            Hasta el día de hoy, tus aportaciones constantes y sin retiros
                            te hacen acreedor al <strong name="Lato-Bold">bono anual</strong> de <strong name="Lato-Bold">Naica.</strong> Podrás disponerlo
                            en el doceavo mes de aportación, el <b name="Lato-Bold">FECHA</b>

                        """
                    )
                    congrats_text_style_h = ParagraphStyle(
                        name='congrats',
                        alignment=TA_LEFT,
                        fontName='Lato-Bold',
                        fontSize=15
                    )
                    congrats_text_style_t = ParagraphStyle(
                        name='congrats',
                        alignment=TA_LEFT,
                        fontName='Lato',
                        fontSize=10
                    )
                    resp = Paragraph(congrats_text, style=congrats_text_style_t)
                    resp_h = Paragraph(congrats_text_header, style=congrats_text_style_h)
                    congrats_table = Table([[resp_h], [resp]])
                    congrats_table._argW[0] = wPadding / 2 + 20
                    congrats_table.wrapOn(c, 0, 0)
                    congrats_table.drawOn(c, x=50, y=370 - ((row_number - 1) * 18))

                c.drawCentredString(x=w / 2, y=50, text='XETER CORPORATION, S.C. DE A.P. DE R.L. DE C.V.')
                c.drawCentredString(x=w / 2, y=30,
                                    text='Domicilio fiscal: Lorem ipsum dolor sit amet, consectetur adipiscing elit')
                c.setFont('Lato', 5)
                c.drawRightString(x=w-50, y=30, text='Page: {}/{}'.format(item+1,math.ceil(number_pages)))
                c.showPage()


            # SAVES PDF FILE
            c.save()
            return {
                'success': True,
                'message': 'PDF CREADO'
            }
        except Exception as e:
            print(e)
            return {
                'success': False,
                'message': e
            }

    @staticmethod
    def generate_pdfTESTNOFUNCTIONAL(ticket):
        try:
            w, h = letter
            wPadding = w-100
            money_box_table_header = ["Transacción", "Cantidad", "Fecha", "Réditos", "Total"]

            # DEFINE PDF CONFIGURATIONS
            c = canvas.Canvas('{}.pdf'.format(ticket['report']), pagesize=letter)
            c.setTitle('MoneyBox {}'.format(ticket['report']))
            pdfmetrics.registerFont(
                TTFont('Lato', "fonts/Lato-Regular.ttf"),
            )
            pdfmetrics.registerFont(
                TTFont('Lato-Bold', "fonts/Lato-Bold.ttf"),
            )
            pdfmetrics.registerFont(
                TTFont('Montserrat', "fonts/Montserrat-Bold.ttf")
            )

            number_pages = (len(ticket['data']))/3

            ticket['data'].insert(0, money_box_table_header)
            # TABLE CONFIGURATION
            table = Table(ticket['data'])
            style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), HexColor('#000000')),
                ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#FFFFFF')),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, -1), 'Lato'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12)
            ])
            row_number = len(ticket['data'])
            for i in range(1, row_number):
                if i % 2 == 0:
                    bc = HexColor('#77B3C7')
                else:
                    bc = HexColor('#FFFFFF')
                ts = TableStyle([
                    ('BACKGROUND', (0, i), (-1, i), bc),
                    ('LINEBELOW', (0, i), (-1, i), 1, HexColor('#000000'))
                ])
                table.setStyle(ts)
            table.setStyle(style)
            table._argW[0] = wPadding/5
            table._argW[1] = wPadding/5
            table._argW[2] = wPadding/5
            table._argW[3] = wPadding/5
            table._argW[4] = wPadding/5
            table.wrapOn(c, 0, 0)
            table.drawOn(c, x=50, y=462-((row_number-1)*18))

            # IMAGES
            Image("images/naica.png", width=150, height=150).drawOn(c, x=((wPadding/4)*3)+50, y=(h/4)*3.1)
            Image("images/naicaClearLogo.png", width=wPadding, height=400).drawOn(c, x=50, y=196)
            Image("images/mblogo.png", width=150, height=30).drawOn(c, x=50, y=(h/2)+110)

            # HEADER
            formated_address = Helpers.split_long_string_fields_and_spacing(
                long_string=ticket['address'], field1=25, field2=35, field3=35
            )
            c.setFont('Montserrat', 15)
            c.setFillColor(HexColor('#000000'))
            c.drawString(x=50, y=h -50, text='Estado de Cuenta')
            c.drawString(x=50, y=h-100, text=ticket['name'])
            c.drawString(x=250, y=h-100, text='Usuario: {user}'.format(user=ticket['user']))
            c.setFont('Montserrat', 13)
            c.drawRightString(x=wPadding+50, y=442-((row_number-1)*18), text='Total: {total}'.format(total=ticket['total']))
            c.setFillColor(HexColor('#0F682D'))
            c.drawRightString(x=wPadding+50, y=(h/2)+120, text=ticket['goal'])
            c.setFont('Lato', 10)
            c.setFillColor(HexColor('#000000'))
            c.drawString(x=50, y=h-65, text='Fecha: {date}'.format(date=Helpers.get_date()))
            c.drawString(x=50, y=h-120, text='RFC: {rfc}'.format(rfc=ticket['rfc']))
            c.drawString(x=50, y=h-135, text='Direccion: {address0}'.format(address0=formated_address[0]))
            c.drawString(x=50, y=h-150, text=formated_address[1])
            c.drawString(x=50, y=h-165, text=formated_address[2])
            c.drawString(x=250, y=h-120, text='Moneda: {currency}'.format(currency=ticket['currency']))
            c.drawString(x=250, y=h-135, text='Plan: {plan}'.format(plan=ticket['plan']))
            c.drawString(x=250, y=h-150, text='Período: {period}'.format(period=ticket['period']))
            c.drawRightString(x=wPadding+50, y=(h/2)+135, text='Objetivo de mi MoneyBox:')

            congrats_text_header = (
                """
                    <strong>
                        ¡Felicidades!
                    </strong>
                """
            )
            congrats_text = (
                """
                    Hasta el día de hoy, tus aportaciones constantes y sin retiros
                    te hacen acreedor al <strong name="Lato-Bold">bono anual</strong> de <strong name="Lato-Bold">Naica.</strong> Podrás disponerlo
                    en el doceavo mes de aportación, el <b name="Lato-Bold">FECHA</b>

                """
            )
            congrats_text_style_h = ParagraphStyle(
                name='congrats',
                alignment=TA_LEFT,
                fontName='Lato-Bold',
                fontSize=15
            )
            congrats_text_style_t = ParagraphStyle(
                name='congrats',
                alignment=TA_LEFT,
                fontName='Lato',
                fontSize=10
            )
            resp = Paragraph(congrats_text, style=congrats_text_style_t)
            respH = Paragraph(congrats_text_header, style=congrats_text_style_h)
            congrats_table = Table([[respH],[resp]])
            congrats_table._argW[0] = wPadding / 2 + 20
            congrats_table.wrapOn(c, 0, 0)
            congrats_table.drawOn(c, x=50, y=370-((row_number-1)*18))

            c.drawCentredString(x=w/2, y=50, text='XETER CORPORATION, S.C. DE A.P. DE R.L. DE C.V.')
            c.drawCentredString(x=w/2, y=30, text='Domicilio fiscal: Lorem ipsum dolor sit amet, consectetur adipiscing elit')


            # SAVES PDF FILE
            c.save()
        except Exception as e:
            print(e)


class Helpers:
    def __init__(self):
        pass

    @staticmethod
    def get_date():
        today = datetime.date.today()
        today_format = today.strftime("%d/%m/%y")
        return today_format

    @staticmethod
    def split_long_string_fields_and_spacing(long_string, field1, field2, field3):
        new_split_string = {
            0: '',
            1: '',
            2: ''
        }
        lens = {
            0: field1,
            1: field2,
            2: field3,
        }
        max_length = field1 + field2 + field3
        counter = 0
        i = 0
        if len(long_string) < field1:
            new_split_string[counter] += long_string
            return new_split_string
        long_string = long_string[0: max_length]
        while i <= len(long_string):
            if long_string[i] != ' ':
                i += 1
                if i == len(long_string):
                    if len(new_split_string[counter]) + i <= lens[counter]:
                        new_split_string[counter] += long_string
                        return new_split_string
                    else:
                        counter += 1
                        new_split_string[counter] = ''
                        new_split_string[counter] += long_string
                        return new_split_string
            else:
                aux = long_string[0:i + 1]
                long_string = long_string[i + 1:]
                if len(new_split_string[counter]) + i <= lens[counter]:
                    new_split_string[counter] += aux
                    i = 0
                else:
                    counter += 1
                    new_split_string[counter] = ''
                    new_split_string[counter] += aux
                    i = 0
        return new_split_string
