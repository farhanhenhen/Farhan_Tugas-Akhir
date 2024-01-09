from flask import Flask, jsonify, sk(_name_)

@app.route('/', methods=['GET'])
def test_api():
    return jsonify(
        {
            'source': request.host_url,
            'message': 'success'
        }
    )

if _name_ == '_main_':
    app.run()
