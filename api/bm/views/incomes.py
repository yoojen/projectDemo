from flask import request
from api.bm.views import bm_views
from models.engine import *
from flask import jsonify
from models import *

"""
This module creates view for users in the db
All routes for user belongs here
"""


@bm_views.route('/incomes', methods=['GET', 'POST'], strict_slashes=False)
def incomes():
    """returns all objects from db"""
    data = []
    print(request.method)
    if (request.method == 'POST'):
        name = request.form['name']
        amount = request.form['amount']
        category = request.form['category']
        type = request.form['type']
        desc = request.form['desc']
        data.append(name)
        data.append(desc)
        data.append(int(amount))
        data.append(1)
        data.append(int(category))
        if type == "incomes":
            Income(data[0], data[1], data[2], data[3], data[4]).save()
            return jsonify(message="data recorded successfully")
        else:
            return jsonify(message="failed")
    return jsonify(get_object(Income))


@bm_views.route('/incomes/<string:name>',  strict_slashes=False)
def income_byName(name):
    """return expense based on ID"""
    data = get_object(Income)
    for exp in data:
        dbName = exp.get('name').lower()
        if name in dbName:
            return jsonify([exp])
    return jsonify(error="not found")


@bm_views.route('/incomes/<int:income_id>',  strict_slashes=False)
def income_byId(income_id):
    """return expense based on ID"""
    return jsonify(get_objectByID(Income, income_id))


@bm_views.route('/incomes/total')
def total_incomes():
    """returns total amount spent"""
    sum = 0
    income_list = get_total(Income, "income")
    for inc in income_list:
        for values in inc.values():
            sum = sum + int(values)
    return jsonify(income_list, {"total incomes": sum})


@bm_views.route('/incomes/categories')
def incomes_categories():
    """returns category that is spent"""
    res = categoriesOfExpenses(Income, "income")
    return jsonify(res)


@bm_views.route('/incomes/category/<int:category_id>', strict_slashes=False)
def incomeMatchingCategoryId(category_id):
    """returns income which match the category id"""
    Obj = getObjMatchingCategoryId(Income, category_id)
    return jsonify(Obj)


@bm_views.route('/incomes/<int:income_id>/category')
def incomes_category(income_id):
    earned = find_exp_category(Income, income_id)
    if type(earned) is not list:
        return jsonify({str(earned.name): [{"category": str(earned.revenue.type)}]})
    return jsonify({"null": "yes"})


@bm_views.route('/incomes/amt_gt/<int:amount>')
def get_income_amt_gt(amount):
    all_items = amount_gt(Income, amount, "income")
    return jsonify(all_items)


@bm_views.route('/incomes/amt_lt/<int:amount>')
def get_income_amt_lt(amount):
    all_items = amount_lt(Income, amount, "income")
    return jsonify(all_items)


@bm_views.route('/incomes/date/<string:date_range_1>/<string:date_range_2>')
def filter_income_by_date(date_range_1, date_range_2):
    data = filter_obj_byDate(Income, date_range_1, date_range_2)
    return jsonify(data)
