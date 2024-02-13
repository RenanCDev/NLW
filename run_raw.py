import os
from flask import Flask as fk
from flask import request as rq
from flask import jsonify as jf
from barcode import Code128 as cd
from barcode.writer import ImageWriter as bw

os.system('clear')

app = fk(__name__)

@app.route('/create_tag', methods=["POST"])
def create_tag():
    body = rq.json
    product_code = body.get('product_code')

    tag = cd(product_code, writer=bw())
    path_from_tag = f'{tag}'
    tag.save(path_from_tag)

    return jf({ "tag path": path_from_tag})


if __name__=='__main__':
    app.run(host='0.0.0.0', port=3000)