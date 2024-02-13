from barcode import Code128 as cd
from barcode.writer import ImageWriter as iw

class BarcodeHandler:
    def create_barcode(self, product_code: str) -> str:
        tag = cd(product_code, writer=iw())
        path_from_tag = f'{tag}'
        tag.save(path_from_tag)

        return path_from_tag
