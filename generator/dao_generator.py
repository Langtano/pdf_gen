from pdf.utils.util import PdfGenerator


class GeneratePdfDao:
    def generate_pdf(self, ticket):
        result = PdfGenerator.generate_pdf(ticket=ticket)
        return result