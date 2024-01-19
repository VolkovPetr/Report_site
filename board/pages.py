from flask import Blueprint, render_template, abort, send_file, redirect, url_for
import os

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return redirect(url_for('pages.dir_listing'))

@bp.route('/files', defaults={'req_path': ''})
@bp.route('/files/<path:req_path>')
def dir_listing(req_path):
    BASE_DIR = f"{os.path.curdir}/board/users_data"
    print(BASE_DIR)

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = sorted(os.listdir(abs_path))
    return render_template('pages/files.html', files=files)
